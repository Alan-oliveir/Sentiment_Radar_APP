# 📊 Sentiment Radar – Análise de Sentimentos em Tempo Real com Python, Streamlit e Reddit

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sentimentradarapp-6rusrx3rigukjgvsygesud.streamlit.app/)

**Sentiment Radar** é uma aplicação web interativa que permite descobrir o que as pessoas realmente pensam sobre produtos, serviços ou marcas, analisando postagens do Reddit em tempo real.

## 📚 Sumário

- [Funcionalidades](#-funcionalidades)
- [Demo Online](#-demo-online)
- [Screenshots](#-screenshots)
- [Instalação Rápida](#-instalação-rápida)
- [Como Usar](#-como-usar)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Contribuições](#-contribuições)
- [Licença](#-licença)
- [Contato](#-contato)
- [Autor](#-autor)

## 🌟 Funcionalidades

- **Análise em Tempo Real**: Busca e analisa posts recentes do Reddit
- **Processamento de Linguagem Natural**: Identifica sentimentos positivos, neutros e negativos
- **Visualizações Interativas**: 
  - Gráficos de distribuição de sentimentos
  - Nuvens de palavras com os termos mais frequentes
  - Lista de posts analisados com sentimento estimado
- **Exportação de Dados**: Baixe os resultados para análise posterior

## 🚀 Demo Online

Experimente agora mesmo! Acesse a aplicação através do link abaixo:  
[https://sentimentradarapp-6rusrx3rigukjgvsygesud.streamlit.app/](https://sentimentradarapp-6rusrx3rigukjgvsygesud.streamlit.app/)

## 📸 Screenshots

![Screenshot da Aplicação](https://github.com/Alan-oliveir/Sentiment_Radar_APP/blob/master/images/screenshot.png)

## 🛠️ Instalação Rápida

```bash
# Clonar o repositório
git clone https://github.com/Alan-oliveir/Sentiment_Radar_APP.git
cd sentiment_radar_app

# Instalar dependências
pip install -r requirements.txt

# Executar a aplicação
streamlit run app.py
```

> ⚠️ **Importante**: Você precisará de credenciais da API do Reddit para usar todas as funcionalidades.  
> Crie suas credenciais em: https://www.reddit.com/prefs/apps  
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

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)  
Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📞 Contato

Se você tiver dúvidas ou sugestões, abra uma issue no GitHub ou entre em contato com o desenvolvedor.   

---

## 👤 Autor

Desenvolvido por **Alan de Oliveira Gonçalves**. Sinta-se à vontade para contribuir e melhorar este projeto!  
[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Alan-oliveir)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alan-ogoncalves)
