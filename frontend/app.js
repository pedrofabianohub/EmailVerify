const { createApp } = Vue;

createApp({
    data() {
        return {
            emailText: '',
            result: null,
            loading: false,
            status: 'Online',
            uploading: false,
            examples: emailExamples
        }
    },
    methods: {
        async classifyEmail() {
            if (!this.emailText.trim()) return;
            
            this.loading = true;
            this.result = null;
            
            try {
                const response = await fetch('/api/classify', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        text: this.emailText
                    })
                });
                
                if (!response.ok) {
                    throw new Error('Erro na classificação');
                }
                
                this.result = await response.json();
            } catch (error) {
                console.error('Erro:', error);
                this.result = {
                    category: 'erro',
                    confidence: 0,
                    response: error.message,
                    processing_time: 0,
                    ai_powered: false
                };
            } finally {
                this.loading = false;
            }
        },
        
        clearResults() {
            this.result = null;
        },
        
        getCategoryClass(category) {
            const classes = {
                'produtivo': 'bg-green-100 text-green-800 border border-green-200',
                'improdutivo': 'bg-yellow-100 text-yellow-800 border border-yellow-200',
                'erro': 'bg-red-100 text-red-800 border border-red-200'
            };
            return classes[category] || classes['improdutivo'];
        },
        
        getCategoryIcon(category) {
            const icons = {
                'produtivo': 'fas fa-chart-line',
                'improdutivo': 'fas fa-calendar-times',
                'erro': 'fas fa-exclamation-triangle'
            };
            return icons[category] || icons['improdutivo'];
        },
        
        getCategoryLabel(category) {
            const labels = {
                'produtivo': 'Email Produtivo',
                'improdutivo': 'Email Improdutivo',
                'erro': 'Erro na Análise'
            };
            return labels[category] || labels['improdutivo'];
        },
        
        getConfidenceColor(confidence) {
            if (confidence >= 0.8) return 'bg-green-500';
            if (confidence >= 0.6) return 'bg-yellow-500';
            return 'bg-red-500';
        },
        
        copyResponse() {
            navigator.clipboard.writeText(this.result.response);
        },
        
        async handleFileUpload(event) {
            const file = event.target.files[0];
            if (!file) return;
            
            this.uploading = true;
            this.clearResults();
            
            try {
                const formData = new FormData();
                formData.append('file', file);
                
                const response = await fetch('/api/upload', {
                    method: 'POST',
                    body: formData
                });
                
                if (!response.ok) {
                    const error = await response.json();
                    throw new Error(error.error || 'Erro no upload');
                }
                
                const data = await response.json();
                this.emailText = data.text;
                
                // Mostrar notificação de sucesso
                console.log(`Arquivo ${data.filename} carregado com sucesso!`);
                
            } catch (error) {
                console.error('Erro no upload:', error);
                alert('Erro ao carregar arquivo: ' + error.message);
            } finally {
                this.uploading = false;
                // Limpar input
                event.target.value = '';
            }
        },
        

    },
    
    async mounted() {
        // Verificar status da API
        try {
            const response = await fetch('/api/health');
            if (response.ok) {
                this.status = 'Online';
            } else {
                this.status = 'Offline';
            }
        } catch (error) {
            this.status = 'Offline';
        }
    }
}).mount('#app');