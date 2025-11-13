# 🚀 Deploy no Vercel

## Pré-requisitos
1. Conta no [Vercel](https://vercel.com)
2. Repositório no GitHub/GitLab
3. Chave da API do Gemini

## Passos para Deploy

### 1. Push para o GitHub
```bash
# Se ainda não tem repositório remoto
git remote add origin https://github.com/SEU_USUARIO/classificador-emails.git
git push -u origin main

# Se já tem repositório
git push origin main
```

### 2. Conectar no Vercel
1. Acesse [vercel.com](https://vercel.com)
2. Clique em "New Project"
3. Conecte seu repositório GitHub
4. Selecione o projeto "classificador-emails"

### 3. Configurar Variáveis de Ambiente
No painel do Vercel:
1. Vá em "Settings" > "Environment Variables"
2. Adicione:
   - **Nome**: `GEMINI_API_KEY`
   - **Valor**: Sua chave da API do Gemini
   - **Environments**: Production, Preview, Development

### 4. Deploy
1. Clique em "Deploy"
2. Aguarde o build completar
3. Acesse a URL gerada

## Estrutura para Vercel
```
/
├── api/index.py          # Backend Flask
├── frontend/             # Frontend estático
├── backend/              # Código fonte (não deployado)
├── vercel.json          # Configuração do Vercel
├── requirements.txt     # Dependências Python
└── .vercelignore       # Arquivos ignorados
```

## URLs de Acesso
- **Frontend**: https://seu-projeto.vercel.app
- **API**: https://seu-projeto.vercel.app/api/health

## Troubleshooting
- Se der erro de import: verificar se todos os arquivos estão na estrutura correta
- Se a API não funcionar: verificar se a variável `GEMINI_API_KEY` está configurada
- Para logs: acessar "Functions" no painel do Vercel