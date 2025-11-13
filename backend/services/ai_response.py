import google.generativeai as genai
from config.settings import GEMINI_API_KEY

def generate_response(category, confidence, email_text):
    """Gera resposta usando IA com prompt detalhado"""
    
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-2.0-flash')
    
    if category == "produtivo":
        prompt = f"""Você é um assistente de RH profissional e empático. Responda este email sobre trabalho/carreira:

EMAIL RECEBIDO:
"{email_text}"

INSTRUÇÕES DETALHADAS:
1. Use o nome da pessoa se estiver mencionado no email
2. Seja caloroso e acolhedor, mas mantenha profissionalismo
3. Reconheça especificamente o que a pessoa está pedindo (vaga, informação, dúvida, etc.)
4. Mencione que a equipe de RH/recrutamento irá analisar e dar retorno
5. Use linguagem natural do português brasileiro
6. Máximo 2 frases, tom positivo e encorajador
7. Se houver dados pessoais (telefone, email), reconheça sem repetir

RESPOSTA PROFISSIONAL:"""
    else:
        prompt = f"""Você é um assistente cordial e genuíno. Responda este email pessoal/social:

EMAIL RECEBIDO:
"{email_text}"

INSTRUÇÕES DETALHADAS:
1. Use o nome da pessoa se estiver mencionado no email
2. Seja caloroso, genuíno e humano
3. Reconheça o conteúdo da mensagem (parabéns, agradecimento, etc.)
4. Responda de forma apropriada ao contexto (aniversário, conquista, etc.)
5. Use linguagem natural e afetuosa do português brasileiro
6. Máximo 2 frases, tom caloroso e pessoal
7. Demonstre apreciação genuína pela mensagem

RESPOSTA CORDIAL:"""
    
    response = model.generate_content(prompt)
    
    if not response or not response.text:
        raise Exception("Falha na geração de resposta pela IA")
        
    return response.text.strip()