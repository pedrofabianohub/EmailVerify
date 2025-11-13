from flask import Flask, request, jsonify
import time
from services.classifier import classify_email
from services.ai_response import generate_response
from utils.file_processor import process_uploaded_file
from config.settings import GEMINI_API_KEY

app = Flask(__name__)

@app.route('/api/classify', methods=['POST'])
def classify():
    """Endpoint principal de classificação com IA"""
    start_time = time.time()
    data = request.get_json()
    text = data.get('text', '').strip()
    
    if not text:
        return jsonify({'error': 'Texto não fornecido'}), 400
    
    # Classificação usando algoritmo híbrido
    category, confidence = classify_email(text)
    
    # Geração de resposta com IA ou fallback
    response = generate_response(category, confidence, text)
    
    processing_time = round(time.time() - start_time, 3)
    
    return jsonify({
        'category': category,
        'confidence': confidence,
        'response': response,
        'processing_time': processing_time,
        'ai_powered': bool(GEMINI_API_KEY)
    })

@app.route('/api/upload', methods=['POST'])
def upload_file():
    """Upload e processamento de arquivos"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'Nenhum arquivo enviado'}), 400
        
        file = request.files['file']
        result = process_uploaded_file(file)
        
        # Classificar texto extraído
        category, confidence = classify_email(result['text'])
        result.update({
            'category': category,
            'confidence': confidence
        })
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/analyze', methods=['POST'])
def analyze():
    """Análise detalhada sem resposta IA"""
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        
        if not text:
            return jsonify({'error': 'Texto não fornecido'}), 400
        
        category, confidence = classify_email(text)
        
        return jsonify({
            'category': category,
            'confidence': confidence,
            'word_count': len(text.split()),
            'char_count': len(text),
            'original_text': text
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Status da API"""
    return jsonify({
        'status': 'ok',
        'mode': 'ai_classification' if GEMINI_API_KEY else 'nlp_classification',
        'api_key_suffix': GEMINI_API_KEY[-8:] if GEMINI_API_KEY else 'none'
    })

if __name__ == '__main__':
    print("🚀 Classificador de Emails rodando...")
    print(f"🤖 IA Gemini: {'Ativada' if GEMINI_API_KEY else 'Desativada (usando fallback)'}")
    if GEMINI_API_KEY:
        print(f"🔑 API Key: ...{GEMINI_API_KEY[-8:]}")
    app.run(host='0.0.0.0', port=5000, debug=True)