# Guia de Configuração do Sentiment Radar

Este guia contém instruções para configurar e executar a aplicação de análise de sentimentos em redes sociais.

---

## Requisitos do Sistema

- Python 3.8 ou superior
- Pip (gerenciador de pacotes)
- Conta de desenvolvedor do Reddit
- Acesso à internet

---

## Obtendo Credenciais da API do Reddit

1. Acesse [reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
2. Faça login e clique em **Create App**
3. Escolha o tipo **script**
4. Preencha os campos necessários:
   - Name: SentimentRadar
   - Redirect URI: `http://localhost:8501`
5. Anote seu **Client ID** e **Client Secret**

!!! warning
    Nunca compartilhe suas credenciais nem as publique em repositórios públicos.

---

## Configuração do Ambiente

### 1. Criar ambiente virtual

```bash
# Windows
python -m venv venv
venv\Scriptsctivate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## Executando a Aplicação

```bash
streamlit run app.py
```

Se não abrir automaticamente, acesse: [http://localhost:8501](http://localhost:8501)

---

## Deploy no Streamlit Cloud

1. Fork este repositório no GitHub
2. Acesse [streamlit.io/cloud](https://streamlit.io/cloud)
3. Faça login com sua conta GitHub
4. Clique em **New App**, selecione o repositório e clique em **Deploy**

---

## Ajustes de Parâmetros

### Limiar de sentimentos (`sentiment_analyzer.py`)

```python
if score < -0.1:
    return score, "Negativo"
elif score > 0.1:
    return score, "Positivo"
else:
    return score, "Neutro"
```

### Personalizar a nuvem de palavras (`visualization.py`)

```python
wordcloud = WordCloud(
    width=600,
    height=300,
    background_color='white',
    stopwords=stop_words,
    max_words=100,
    colormap='viridis'
).generate(filtered_texts)
```

---

## Solução de Problemas

- Verifique conexão com a internet
- Confirme as credenciais da API
- Verifique se o subreddit existe e é público
- Reduza a quantidade de posts para melhorar performance

---

## Modo Debug

```bash
streamlit run app.py --logger.level=debug
```

---

## Recursos Adicionais

- [Documentação do PRAW](https://praw.readthedocs.io/)
- [Guia do Streamlit](https://docs.streamlit.io/)
- [TextBlob Docs](https://textblob.readthedocs.io/)

---

## Próximos Passos

- Suporte a outras redes sociais (YouTube, Twitter)
- Análise de tópicos (LDA)
- Análise de emoções
- Autenticação de usuários

---

## Contato

Em caso de dúvidas ou sugestões, abra uma issue ou entre em contato.

---

## Autor

Desenvolvido por **Alan de Oliveira Gonçalves**  
[GitHub](https://github.com/Alan-oliveir) | [LinkedIn](https://www.linkedin.com/in/alan-ogoncalves)
