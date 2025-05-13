# Analisador de Sentimentos em Redes Sociais

Uma aplicação web interativa desenvolvida em Python com Streamlit, que permite ao usuário pesquisar a percepção pública sobre produtos, serviços ou marcas com base em postagens extraídas do Reddit.

## Funcionalidades

- Busca em tempo real por palavras-chave no Reddit
- Coleta de títulos e conteúdo de posts relacionados
- Análise de sentimento usando técnicas de NLP
- Visualizações interativas:
  - Gráficos de distribuição de sentimentos
  - Nuvens de palavras com os termos mais frequentes
  - Lista dos posts analisados com sentimento estimado

## Pré-requisitos

- Python 3.8 ou superior
- Conta de desenvolvedor do Reddit para obter credenciais de API

## Configuração

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/analisador-sentimentos-reddit.git
cd analisador-sentimentos-reddit
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Obter credenciais do Reddit

1. Acesse [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
2. Faça login na sua conta do Reddit
3. Clique em "Create App" ou "Create Another App"
4. Preencha os seguintes campos:
   - **Name**: SentimentAnalyzer (ou outro nome de sua escolha)
   - **App Type**: Script
   - **Description**: Aplicação para análise de sentimentos do Reddit
   - **About URL**: (pode deixar em branco)
   - **Redirect URI**: http://localhost:8501
5. Clique em "Create App"
6. Anote o **Client ID** (aparece abaixo do nome da aplicação) e o **Client Secret**

## Executando a aplicação

```bash
streamlit run app.py
```

Acesse a aplicação em seu navegador: http://localhost:8501

## Estrutura do projeto

```
project/
├── app.py                 # Arquivo principal da aplicação
├── reddit_client.py       # Funções para interagir com API do Reddit
├── sentiment_analyzer.py  # Análise de sentimento e processamento de texto
├── visualization.py       # Funções para gráficos e visualização
├── resource_manager.py    # Gerenciador de recursos CSS/JS
├── requirements.txt       # Dependências do projeto
├── README.md              # Documentação do projeto
├── LICENSE                # Licença do projeto
└── static/                # Diretório de recursos estáticos
    ├── styles.css         # Estilos CSS da aplicação
    └── theme_detector.js  # Script de detecção de tema
```

## Deploy

A aplicação foi implantada na plataforma Streamlit Cloud, permitindo acesso fácil e rápido sem necessidade de instalação local.
Acesse a aplicação através do seguinte link:
https://sentimentradarapp-6rusrx3rigukjgvsygesud.streamlit.app/

## Como usar

1. Insira suas credenciais da API do Reddit no painel lateral
2. Digite uma palavra-chave para pesquisa (ex: "iPhone", "Tesla", "ChatGPT")
3. Opcionalmente, especifique um subreddit para limitar a busca
4. Ajuste os parâmetros adicionais conforme necessário
5. Clique em "Analisar Sentimentos"
6. Explore as visualizações e resultados gerados
7. Baixe os dados como CSV se desejar

## Tecnologias utilizadas

- **Python** – linguagem principal
- **Streamlit** – interface web interativa
- **PRAW** (Python Reddit API Wrapper) – coleta de dados do Reddit
- **TextBlob** – análise de sentimento
- **NLTK** - processamento de linguagem natural
- **Matplotlib / Seaborn / WordCloud** – visualizações gráficas

## Segurança

- As credenciais da API do Reddit são utilizadas apenas durante a sessão ativa
- Nenhum dado é armazenado permanentemente
- A aplicação roda localmente no seu computador

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.
