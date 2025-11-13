import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import RSLPStemmer
from unidecode import unidecode
import string

# Configurar NLTK
def setup_nltk():
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')

    try:
        nltk.data.find('tokenizers/punkt_tab')
    except LookupError:
        nltk.download('punkt_tab')
        
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        nltk.download('stopwords')

    try:
        nltk.data.find('stemmers/rslp')
    except LookupError:
        nltk.download('rslp')

# Inicializar componentes NLP
setup_nltk()
stop_words = set(stopwords.words('portuguese'))
stemmer = RSLPStemmer()

def preprocess_text(text):
    """Aplica técnicas de NLP para pré-processar o texto"""
    # Converter para minúsculas
    text = text.lower()
    
    # Remover acentos
    text = unidecode(text)
    
    # Remover pontuação
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenização
    tokens = word_tokenize(text, language='portuguese')
    
    # Remover stop words e palavras muito curtas
    tokens = [token for token in tokens if token not in stop_words and len(token) > 2]
    
    # Stemming
    tokens = [stemmer.stem(token) for token in tokens]
    
    return tokens