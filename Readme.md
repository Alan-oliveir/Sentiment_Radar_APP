# 📊 Sentiment Radar - Analisador de Sentimentos em Redes Sociais

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sentimentradarapp-6rusrx3rigukjgvsygesud.streamlit.app/)


**Sentiment Radar** é uma aplicação web interativa que permite descobrir o que as pessoas realmente pensam sobre produtos, serviços ou marcas, analisando postagens do Reddit em tempo real.

## 🌟 Funcionalidades

- **Análise em Tempo Real**: Busca e analisa posts recentes do Reddit
- **Processamento de Linguagem Natural**: Identifica sentimentos positivos, neutros e negativos
- **Visualizações Interativas**: 
  - Gráficos de distribuição de sentimentos
  - Nuvens de palavras com os termos mais frequentes
  - Lista de posts analisados com sentimento estimado
- **Exportação de Dados**: Baixe os resultados para análise posterior

## 🚀 Demo Online

Experimente agora mesmo! Acesse a aplicação através do link:
[https://sentimentradarapp-6rusrx3rigukjgvsygesud.streamlit.app/](https://sentimentradarapp-6rusrx3rigukjgvsygesud.streamlit.app/)

## 📸 Screenshots

![Screenshot da Aplicação](https://via.placeholder.com/400x300?text=Dashboard)

## 🛠️ Instalação Rápida

```bash
# Clonar o repositório
git clone https://github.com/seu-usuario/analisador-sentimentos-reddit.git
cd analisador-sentimentos-reddit

# Instalar dependências
pip install -r requirements.txt

# Executar a aplicação
streamlit run app.py
```

> ⚠️ **Importante**: Você precisará de credenciais da API do Reddit para usar todas as funcionalidades.
> Para instruções detalhadas, consulte [CONFIG.md](CONFIG.md).

## 🧩 Como Usar

1. Insira suas credenciais da API do Reddit
2. Digite uma palavra-chave para pesquisa (ex: "iPhone", "Tesla", "ChatGPT")
3. Opcionalmente, especifique um subreddit específico
4. Ajuste os parâmetros de busca conforme necessário
5. Clique em "Analisar Sentimentos"
6. Explore as visualizações e insights gerados

## 🔧 Tecnologias Utilizadas

- **Python** – linguagem principal
- **Streamlit** – interface web interativa
- **PRAW** (Python Reddit API Wrapper) – coleta de dados do Reddit
- **TextBlob** – análise de sentimento
- **Matplotlib / WordCloud** – visualizações gráficas



## 📂 Estrutura do Projeto

```plaintext
sentiment_radar_app/
├── app.py                 # Aplicação principal
├── reddit_client.py       # Integração com API do Reddit
├── sentiment_analyzer.py  # Análise de sentimento
├── visualization.py       # Componentes visuais
├── resource_manager.py    # Gerenciador de recursos
├── static/                # Recursos estáticos
│   ├── styles.css         # Estilos da aplicação
│   └── theme_detector.js  # Detecção de tema
├── requirements.txt       # Dependências
├── .gitignore             # Ignorar arquivos desnecessários
├── LICENSE                # Licença do projeto
├── README.md              # Este arquivo
└── CONFIG.md              # Guia de configuração
```


## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:

1. 🍴 Fazer um fork do projeto
2. 🔄 Criar um branch para sua feature (`git checkout -b feature/incrivel`)
3. 💾 Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. 📤 Push para o branch (`git push origin feature/incrivel`)
5. 🔁 Abra um Pull Request

## 📜 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📞 Contato

Se você tiver dúvidas ou sugestões, abra uma issue no GitHub ou entre em contato com os desenvolvedores.

---
Desenvolvido por Alan de Oliveira. Sinta-se à vontade para contribuir e melhorar este projeto!
