# 📧 Classificador de Emails com IA

Sistema para classificar emails como **produtivos** ou **improdutivos** com interface Vue.js e respostas automáticas geradas por IA.

## 🚀 Como Rodar

### 1. Configurar API do Gemini
```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite o arquivo .env e adicione sua chave do Gemini
GEMINI_API_KEY=sua_chave_real_aqui
```

### 2. Executar com Docker
```bash
docker-compose up --build
```

Acesse: http://localhost:3000

## 🔧 Arquitetura

- **Backend**: Flask (Python) - API de classificação + IA
- **Frontend**: Vue.js 3 + TailwindCSS - Interface moderna
- **Classificação**: BART (Hugging Face) - Análise semântica avançada
- **Respostas**: Google Gemini - Respostas personalizadas e humanizadas
- **Deploy**: Docker + Docker Compose

## 📊 API Endpoints

### `/classify` - Classificação Principal com IA
```json
POST /api/classify
{
  "text": "Olá, meu nome é Pedro e estou interessado em trabalhar na empresa"
}

Response:
{
  "category": "produtivo",
  "confidence": 0.65,
  "response": "Oi Pedro! Fico super feliz em saber do seu interesse em trabalhar conosco. Te envio por email as informações sobre as vagas abertas!",
  "processing_time": 1.2,
  "ai_powered": true
}
```

### `/health` - Status da API
```json
GET /api/health
{
  "status": "ok",
  "mode": "ai_classification"
}
```

## 🤖 Recursos da IA

- **Respostas Personalizadas**: Reconhece nomes e gera respostas contextualizadas
- **Tom Humanizado**: Linguagem natural e empática
- **Detecção de Conteúdo**: Lida adequadamente com linguagem inapropriada
- **Fallback Seguro**: Respostas padrão em caso de erro na API

## 🎯 Algoritmo de Classificação

1. **IA BART**: Modelo facebook/bart-large-mnli do Hugging Face para classificação zero-shot
2. **Análise Semântica**: Compreende o contexto e significado do texto
3. **Score de Confiança**: Probabilidade gerada pelo modelo neural
4. **Fallback Seguro**: Sistema de palavras-chave em caso de erro na IA
5. **Geração de Resposta**: IA Gemini cria resposta personalizada baseada no conteúdo

## 📁 Estrutura

```
/backend          # API Flask + Integração Gemini
/frontend         # Interface Vue.js
/data            # Dados de exemplo
.env.example     # Configuração da API
docker-compose.yml
```

## 🔑 Configuração da API Gemini

1. Acesse: https://makersuite.google.com/app/apikey
2. Crie uma nova chave de API
3. Adicione no arquivo `.env`:
```bash
GEMINI_API_KEY=sua_chave_aqui
```