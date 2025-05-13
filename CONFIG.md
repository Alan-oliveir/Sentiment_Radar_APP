# 🔧 CONFIG.md – Guia de Configuração do Sentiment Radar

Este documento contém instruções detalhadas para configurar e executar o SentimentRadar, nossa aplicação de análise de sentimentos em redes sociais.

## 📚 Sumário

- [Requisitos do Sistema](#-requisitos-do-sistema)
- [Obtendo Credenciais da API do Reddit](#-obtendo-credenciais-da-api-do-reddit)
- [Configuração do Ambiente](#-configuração-do-ambiente)
- [Executando a Aplicação](#️-executando-a-aplicação)
- [Deploy no Streamlit Cloud](#-configuração-para-deploy)
- [Ajustes de Parâmetros](#️-ajustando-parâmetros)
- [Solução de Problemas](#️-solução-de-problemas)
- [Modo Debug](#-usando-o-modo-debug)
- [Recursos Adicionais](#-recursos-adicionais)
- [Próximos Passos](#-próximos-passos)
- [Contato e Suporte](#-contato-e-suporte)
- [Autor](#-autor)

## 📋 Requisitos do Sistema

- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)
- Acesso à internet (para coleta de dados e instalação de dependências)
- Conta de desenvolvedor do Reddit (para obter as credenciais da API)

## 🔑 Obtendo Credenciais da API do Reddit

### 1. Criar uma conta de desenvolvedor

1. Acesse [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
2. Faça login na sua conta do Reddit (ou crie uma se não tiver)
3. Clique em "Create App" ou "Create Another App"
4. Preencha os seguintes campos:
   - **Name**: SentimentRadar (ou outro nome de sua escolha)
   - **App Type**: Script
   - **Description**: Aplicação para análise de sentimentos do Reddit
   - **About URL**: (pode deixar em branco)
   - **Redirect URI**: http://localhost:8501
5. Clique em "Create App"
6. Anote o **Client ID** (aparece abaixo do nome da aplicação) e o **Client Secret**

### 2. Segurança das credenciais

- **NUNCA compartilhe** seu Client ID e Client Secret
- **NÃO inclua** estas informações em repositórios públicos

## 🛠️ Configuração do Ambiente

### 1. Criar um ambiente virtual (recomendado)

```bash
# No Windows
python -m venv venv
venv\Scripts\activate

# No macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar as dependências

```bash
pip install -r requirements.txt
```

Isso instalará todas as bibliotecas necessárias, incluindo:
- streamlit
- praw (Python Reddit API Wrapper)
- pandas
- textblob
- wordcloud
- matplotlib
- numpy

## ▶️ Executando a Aplicação

1. Com o ambiente virtual ativado, execute:

```bash
streamlit run app.py
```

2. A aplicação será aberta automaticamente no seu navegador padrão
3. Se não abrir, acesse: `http://localhost:8501`

## 🔄 Configuração para Deploy

### Deploy no Streamlit Cloud

1. Faça o fork deste repositório para sua conta GitHub
2. Acesse [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Faça login com sua conta GitHub
4. Clique em "New app" e selecione o repositório
5. Clique em "Deploy"

## ⚙️ Ajustando Parâmetros

### Ajustando os limiares de sentimento

Para modificar a sensibilidade da análise de sentimento, altere os valores limiares na função `analyze_sentiment` no arquivo `sentiment_analyzer.py`:

```python
# Exemplo para tornar a análise mais sensível a sentimentos positivos/negativos
 if score < -0.1:
     return score, "Negativo"
 elif score > 0.1:
     return score, "Positivo"
 else:
     return score, "Neutro"
```

### Personalizando a nuvem de palavras

Modifique os parâmetros da nuvem de palavras no arquivo `visualization.py`:

```python
 wordcloud = WordCloud(
     width=600,
     height=300,
     background_color='white',
     stopwords=stop_words,
     min_font_size=10,
     max_words=100,
     colormap='viridis'
 ).generate(filtered_texts)
```

## ⚠️ Solução de Problemas

### Erro na coleta de posts do Reddit

Se você encontrar erros ao coletar posts, verifique:
- Sua conexão com a internet
- Se as credenciais do Reddit estão corretas
- Se há restrições de API impostas pelo Reddit
- Se o subreddit especificado existe e é público

### Lentidão no processamento

Para conjuntos muito grandes de dados, o processamento pode ser lento. Considere:
- Reduzir o número de posts coletados
- Limitar a busca a subreddits específicos

## 🔍 Usando o Modo Debug

Para diagnosticar problemas:

```bash
streamlit run app.py --logger.level=debug
```

## 📚 Recursos Adicionais

- [Documentação do PRAW](https://praw.readthedocs.io/)
- [Guia do Streamlit](https://docs.streamlit.io/)
- [Tutorial de NLP com TextBlob](https://textblob.readthedocs.io/)
- [Regras de API do Reddit](https://github.com/reddit-archive/reddit/wiki/API)

## 🚀 Próximos Passos

Para estender essa aplicação, considere:

1. Adicionar suporte a outras redes sociais (como Twitter ou Instagram)
2. Implementar análise de tópicos com LDA (Latent Dirichlet Allocation)
3. Implementar análise de emoções mais detalhada
4. Adicionar autenticação para proteger a aplicação

## 📞 Contato e Suporte

Agradeço por usar o SentimentRadar! Espero que você aproveite a análise de sentimentos em redes sociais.
Para dúvidas ou problemas, abra uma issue no repositório do projeto ou entre em contato com o desenvolvedor.

---

## 👤 Autor

Desenvolvido por **Alan de Oliveira Gonçalves**. Sinta-se à vontade para contribuir e melhorar este projeto!  
[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Alan-oliveir)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alan-ogoncalves)
