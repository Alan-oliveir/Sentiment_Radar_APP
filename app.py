"""
Aplicativo Streamlit para análise de sentimentos em posts do Reddit
"""
import os
import time

import streamlit as st

# Importações de módulos locais
from reddit_client import fetch_reddit_data
from visualization import (
    display_wordcloud_tabs,
    display_common_words,
    display_posts,
    display_sentiment_distribution
)

# Configuração da página
st.set_page_config(
    page_title="Sentiment Radar App",
    page_icon="📊",
    layout="wide"
)


# Função para carregar arquivo CSS ou JS
def load_file_content(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    return ""


# Carrega estilos CSS e scripts JS de arquivos externos
css_content = load_file_content("static/styles.css")
js_content = load_file_content("static/theme_detector.js")

# Aplica CSS
st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

# Aplica JavaScript
st.markdown(f"<script>{js_content}</script>", unsafe_allow_html=True)

# Título principal
st.title("📊 Analisador de Sentimentos em Redes Sociais")
st.subheader("Extraindo percepções públicas do Reddit")
st.markdown("---")  # Linha separadora

# Sidebar para configurações
st.sidebar.header("Configurações")

# Autenticação Reddit
st.sidebar.subheader("Credenciais da API Reddit")
client_id = st.sidebar.text_input("Client ID", type="password")
client_secret = st.sidebar.text_input("Client Secret", type="password")
user_agent = st.sidebar.text_input("User Agent", placeholder="app_name")

# Parâmetros da busca
st.sidebar.subheader("Parâmetros da Pesquisa")
keyword = st.sidebar.text_input("Palavra-chave para busca:", placeholder="Ex: iPhone, Tesla, ChatGPT")
subreddit = st.sidebar.text_input("Subreddit específico (opcional):", placeholder="Ex: technology, apple")
limit_posts = st.sidebar.slider("Número de posts a analisar:", min_value=10, max_value=100, value=30)
time_filter = st.sidebar.selectbox("Período de tempo:",
                                   ["day", "week", "month", "year", "all"],
                                   index=1)


def display_results(df):
    """
    Exibe os resultados completos da análise

    Args:
        df (pandas.DataFrame): DataFrame com os dados coletados
    """
    if df.empty:
        return

    # Resumo dos dados
    st.subheader("Resumo da Análise")

    # Métricas em caixas coloridas
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total de Posts", len(df))
    with col2:
        st.metric("Posts Positivos", len(df[df['sentiment'] == 'Positivo']))
    with col3:
        st.metric("Posts Neutros", len(df[df['sentiment'] == 'Neutro']))
    with col4:
        st.metric("Posts Negativos", len(df[df['sentiment'] == 'Negativo']))

    # Tabs para visualizações detalhadas
    tab1, tab2, tab3, tab4 = st.tabs(
        ["Distribuição de Sentimentos", "Nuvens de Palavras", "Termos Frequentes", "Posts"])

    with tab1:
        display_sentiment_distribution(df)

    with tab2:
        display_wordcloud_tabs(df)

    with tab3:
        display_common_words(df)

    with tab4:
        display_posts(df)


def main():
    """Função principal do aplicativo"""
    # Placeholder para exibir mensagens de aviso ou instruções
    info_placeholder = st.empty()

    # Verificar se as credenciais foram fornecidas
    if not client_id or not client_secret:
        info_placeholder.info("""
        👋 **Bem-vindo ao Analisador de Sentimentos do Reddit!**

        Para começar, insira suas credenciais da API do Reddit no painel lateral.

        📝 **Como obter as credenciais:**
        1. Acesse [reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
        2. Faça login na sua conta Reddit
        3. Crie um novo aplicativo do tipo "script"
        4. Copie o Client ID e Client Secret gerados

        Suas credenciais não são armazenadas e são usadas apenas durante esta sessão.
        """)
        return

    # Verificar se a palavra-chave foi fornecida
    if not keyword:
        info_placeholder.info("Digite uma palavra-chave no painel lateral para iniciar a análise.")
        return

    # Limpar o placeholder
    info_placeholder.empty()

    # Botão para iniciar a análise
    if st.sidebar.button("Analisar Sentimentos", use_container_width=True):
        with st.spinner("Buscando e analisando posts do Reddit..."):
            # Buscar dados
            df = fetch_reddit_data(
                keyword,
                client_id=client_id,
                client_secret=client_secret,
                user_agent=user_agent,
                subreddit=subreddit,
                limit=limit_posts,
                time_filter=time_filter
            )

            if not df.empty:
                # Exibir resultados
                display_results(df)

                # Opção para baixar CSV
                st.download_button(
                    label="Baixar dados como CSV",
                    data=df.to_csv(index=False).encode('utf-8'),
                    file_name=f"reddit_sentiment_{keyword}_{time.strftime('%Y%m%d_%H%M%S')}.csv",
                    mime='text/csv',
                )
            else:
                st.warning("Nenhum resultado encontrado. Tente outra palavra-chave ou ajuste os parâmetros.")


if __name__ == "__main__":
    main()
