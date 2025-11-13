import google.generativeai as genai
from config.settings import GEMINI_API_KEY

def generate_response(category, confidence, email_text):
    """Gera resposta profissional usando IA Gemini"""
    
    if not GEMINI_API_KEY:
        return "Agradecemos seu contato. Nossa equipe analisará sua mensagem."
    
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-2.0-flash')
        
        if category == "produtivo":
            prompt = f"""Você é um assistente de RH profissional. Responda este email sobre trabalho de forma empática e profissional:

"{email_text}"

INSTRUÇÕES:
- Use o nome da pessoa se houver no email
- Se houver palavrões ou linguagem inapropriada, ignore completamente e responda educadamente
- Se houver dados pessoais (telefone, email), reconheça sem repetir os dados
- Mencione que a equipe analisará ou entrará em contato
- Máximo 2 frases em português brasileiro
- Tom caloroso mas profissional

"""
        else:
            prompt = f"""Você é um assistente profissional. Responda este email de forma educada:

"{email_text}"

INSTRUÇÕES:
- Use o nome da pessoa se houver no email
- Se houver palavrões ou linguagem inapropriada, ignore completamente e responda educadamente
- Se houver dados pessoais, reconheça sem repetir os dados
- Agradeça o contato de forma genuína
- Máximo 2 frases em português brasileiro
- Tom cordial e respeitoso

"""
        
        response = model.generate_content(prompt)
        return response.text.strip()
    
    except Exception:
        # Fallback profissional
        if category == "produtivo":
            return "Agradecemos seu interesse em trabalhar conosco. Nossa equipe de recrutamento analisará sua solicitação."
        else:
            return "Agradecemos seu contato. Ficamos felizes em saber de você."