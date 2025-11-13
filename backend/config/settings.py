import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configurações da aplicação
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Configurações de upload
ALLOWED_EXTENSIONS = ['.txt', '.pdf']
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB