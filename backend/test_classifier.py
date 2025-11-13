#!/usr/bin/env python3
"""
Script de teste para o classificador com IA BART
"""

from services.classifier import classify_email

def test_classification():
    """Testa a classificação com exemplos"""
    
    test_cases = [
        {
            "text": "Olá, gostaria de saber sobre vagas de desenvolvedor Python na empresa",
            "expected": "produtivo"
        },
        {
            "text": "PROMOÇÃO IMPERDÍVEL! Clique aqui e ganhe 50% de desconto GRÁTIS!!!",
            "expected": "improdutivo"
        },
        {
            "text": "Boa tarde, podemos agendar uma reunião para discutir o projeto?",
            "expected": "produtivo"
        },
        {
            "text": "Spam spam spam ofertas limitadas clique urgente",
            "expected": "improdutivo"
        }
    ]
    
    print("🧪 Testando Classificador com IA BART\n")
    
    for i, case in enumerate(test_cases, 1):
        print(f"Teste {i}:")
        print(f"Texto: {case['text']}")
        
        try:
            category, confidence = classify_email(case['text'])
            print(f"Resultado: {category} (confiança: {confidence:.2f})")
            print(f"Esperado: {case['expected']}")
            
            status = "✅ PASSOU" if category == case['expected'] else "❌ FALHOU"
            print(f"Status: {status}\n")
            
        except Exception as e:
            print(f"❌ ERRO: {e}\n")

if __name__ == "__main__":
    test_classification()