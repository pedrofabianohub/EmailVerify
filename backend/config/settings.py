import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configurações da aplicação
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Debug: mostrar parte da chave para verificar mudanças
if GEMINI_API_KEY:
    print(f"🔑 API Key: ...{GEMINI_API_KEY[-8:]}")
else:
    print("❌ Nenhuma API Key encontrada")

# Configurações de upload
ALLOWED_EXTENSIONS = ['.txt', '.pdf']
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB