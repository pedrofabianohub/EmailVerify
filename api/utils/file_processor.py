import PyPDF2
import io
import os
from config.settings import ALLOWED_EXTENSIONS

def extract_text_from_pdf(file_content):
    """Extrai texto de arquivo PDF"""
    try:
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_content))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        raise Exception(f"Erro ao ler PDF: {str(e)}")

def process_uploaded_file(file):
    """Processa arquivo enviado e extrai texto"""
    if not file or file.filename == '':
        raise Exception('Nenhum arquivo selecionado')
    
    # Verificar extensão do arquivo
    file_ext = os.path.splitext(file.filename)[1].lower()
    
    if file_ext not in ALLOWED_EXTENSIONS:
        raise Exception('Formato não suportado. Use .txt ou .pdf')
    
    # Ler conteúdo do arquivo
    file_content = file.read()
    
    if file_ext == '.pdf':
        text = extract_text_from_pdf(file_content)
    else:  # .txt
        text = file_content.decode('utf-8')
    
    if not text.strip():
        raise Exception('Arquivo vazio ou não foi possível extrair texto')
    
    return {
        'text': text,
        'filename': file.filename,
        'file_type': file_ext,
        'char_count': len(text)
    }