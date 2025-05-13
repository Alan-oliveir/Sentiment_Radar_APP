// Script para detectar o tema atual (claro/escuro)
const detectTheme = () => {
    const bodyEl = window.parent.document.body;
    const isDarkTheme = bodyEl.classList.contains('dark');
    const htmlEl = document.querySelector('html');
    
    if (isDarkTheme) {
        htmlEl.classList.remove('light-mode');
        htmlEl.classList.add('dark-mode');
    } else {
        htmlEl.classList.remove('dark-mode');
        htmlEl.classList.add('light-mode');
    }
};

// Executar detecção de tema inicial
window.addEventListener('DOMContentLoaded', () => {
    // Pequeno atraso para garantir que o DOM esteja completamente carregado
    setTimeout(() => {
        detectTheme();
        
        // Criar um observador para detectar mudanças no tema
        try {
            const observer = new MutationObserver(() => {
                detectTheme();
            });
            
            // Observe o documento para mudanças na classe que indica o tema
            if (window.parent && window.parent.document && window.parent.document.body) {
                observer.observe(window.parent.document.body, { 
                    attributes: true, 
                    attributeFilter: ['class'] 
                });
            }
        } catch (e) {
            console.log("Erro ao configurar o observador de tema:", e);
        }
    }, 500);
});

// Tentar aplicar o tema novamente quando a página estiver completamente carregada
window.addEventListener('load', () => {
    detectTheme();
});
