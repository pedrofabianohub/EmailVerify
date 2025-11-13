from typing import Tuple
import google.generativeai as genai
from config.settings import GEMINI_API_KEY
from utils.nlp_processor import preprocess_text

# Configurar Gemini
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-pro')

def classify_email(text: str) -> Tuple[str, float]:
    """Classifica email usando NLP + Gemini para casos ambíguos"""
    
    try:
        # 1. Análise NLP com tokens processados
        nlp_result = analyze_with_nlp(text)
        
        # 2. Se NLP tem certeza, retorna direto
        if nlp_result['confidence'] > 0.8:
            return nlp_result['category'], nlp_result['confidence']
        
        # 3. Casos ambíguos: usar Gemini
        if GEMINI_API_KEY:
            return classify_with_gemini(text)
        else:
            return nlp_result['category'], nlp_result['confidence']
            
    except Exception as e:
        print(f"Erro na classificação: {e}")
        return fallback_classification(text)

def analyze_with_nlp(text: str) -> dict:
    """Análise usando NLP processado para casos óbvios"""
    
    # Processar texto com NLP existente
    tokens = preprocess_text(text)
    text_lower = text.lower()
    
    # Stems PRODUTIVOS (requer ação/resposta)
    productive_stems = {
        'precis': 2.0, 'necessit': 2.0, 'solicit': 2.0, 'gostar': 2.0,
        'duvid': 2.5, 'pergunt': 2.5, 'quest': 2.5, 'problem': 2.5,
        'suport': 3.0, 'ajud': 3.0, 'assist': 3.0,
        'atualiz': 2.0, 'status': 2.0, 'andam': 2.0,
        'reuni': 2.5, 'meeting': 2.5, 'agend': 2.5,
        'urgent': 1.5, 'import': 1.5, 'prior': 1.5
    }
    
    # Stems IMPRODUTIVOS (não requer ação)
    unproductive_stems = {
        'parab': -2.5, 'felicit': -2.5, 'congratul': -2.5,
        'obrig': -2.0, 'agradec': -2.0, 'gratid': -2.0,
        'inform': -1.5, 'comunic': -1.5, 'avis': -1.5,
        'newslett': -2.0, 'bolet': -2.0,
        'promoc': -2.5, 'descont': -2.5, 'ofert': -2.5
    }
    
    score = 0.0
    
    # Calcular score com tokens processados
    for token in tokens:
        for stem, weight in productive_stems.items():
            if stem in token:
                score += weight
                
        for stem, weight in unproductive_stems.items():
            if stem in token:
                score += weight
    
    # Bônus para perguntas
    if '?' in text: score += 1.0
    
    # Determinar categoria e confiança
    if score >= 2.0:
        return {'category': 'produtivo', 'confidence': 0.85}
    elif score <= -2.0:
        return {'category': 'improdutivo', 'confidence': 0.85}
    else:
        # Caso ambíguo
        category = 'produtivo' if score > 0 else 'improdutivo'
        return {'category': category, 'confidence': 0.6}

def classify_with_gemini(text: str) -> Tuple[str, float]:
    """Usa Gemini para casos ambíguos"""
    
    prompt = f"""Classifique este email como PRODUTIVO ou IMPRODUTIVO:

PRODUTIVO: Emails que requerem ação ou resposta (solicitações, dúvidas, suporte, atualizações)
IMPRODUTIVO: Emails que não necessitam ação imediata (felicitações, agradecimentos, informativos)

Email: "{text}"

Responda apenas: PRODUTIVO ou IMPRODUTIVO"""
    
    try:
        response = model.generate_content(prompt)
        result = response.text.strip().upper()
        
        if 'PRODUTIVO' in result:
            return 'produtivo', 0.9
        else:
            return 'improdutivo', 0.9
            
    except Exception as e:
        print(f"Erro no Gemini: {e}")
        return fallback_classification(text)

def fallback_classification(text: str) -> Tuple[str, float]:
    """Classificação de fallback em caso de erro na IA"""
    text_lower = text.lower()
    
    # Palavras-chave básicas para fallback
    productive_keywords = ['trabalho', 'vaga', 'emprego', 'reunião', 'projeto', 'empresa']
    spam_keywords = ['grátis', 'promoção', 'clique aqui', 'urgente']
    
    productive_count = sum(1 for word in productive_keywords if word in text_lower)
    spam_count = sum(1 for word in spam_keywords if word in text_lower)
    
    if productive_count > spam_count:
        return "produtivo", 0.6
    else:
        return "improdutivo", 0.6