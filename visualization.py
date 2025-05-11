"""
Funções para visualização e geração de gráficos
"""
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from wordcloud import WordCloud
import streamlit as st
from sentiment_analyzer import STOPWORDS


def generate_wordcloud(texts, sentiment=None, sentiments=None):
    """
    Gera uma nuvem de palavras a partir de textos
    
    Args:
        texts (list): Lista de textos
        sentiment (str, optional): Sentimento específico para filtrar
        sentiments (list, optional): Lista de sentimentos correspondente aos textos
        
    Returns:
        WordCloud: Objeto WordCloud ou None se não houver dados suficientes
    """
    # Combinar stopwords de diferentes idiomas
    stop_words = STOPWORDS['english'].union(STOPWORDS['portuguese'])

    # Filtrar por sentimento se especificado
    if sentiment and sentiments:
        filtered_texts = " ".join([text for text, sent in zip(texts, sentiments) if sent == sentiment])
    else:
        filtered_texts = " ".join(texts)

    if not filtered_texts.strip():
        return None

    # Criar nuvem de palavras
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        stopwords=stop_words,
        min_font_size=10,
        max_words=100,
        colormap='viridis'
    ).generate(filtered_texts)

    return wordcloud


def display_sentiment_distribution(df):
    """
    Exibe gráfico de distribuição de sentimentos
    
    Args:
        df (pandas.DataFrame): DataFrame com coluna 'sentiment'
    """
    st.subheader("Distribuição de Sentimentos")
    sentiment_counts = df['sentiment'].value_counts()

    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ['#2ecc71', '#f39c12', '#e74c3c']  # Verde, Amarelo, Vermelho

    # Garantir que todas as categorias estejam presentes
    all_sentiments = {'Positivo': 0, 'Neutro': 0, 'Negativo': 0}
    for sentiment, count in sentiment_counts.items():
        all_sentiments[sentiment] = count

    sentiment_series = pd.Series(all_sentiments)
    ax = sns.barplot(x=sentiment_series.index, y=sentiment_series.values, palette=colors)

    # Adicionar rótulos de valor
    for i, v in enumerate(sentiment_series.values):
        ax.text(i, v + 0.1, str(v), ha='center')

    plt.title("Distribuição dos Sentimentos")
    plt.xlabel("Sentimento")
    plt.ylabel("Número de Posts")
    st.pyplot(fig)


def display_wordcloud_tabs(df):
    """
    Exibe tabs com nuvens de palavras para diferentes sentimentos
    
    Args:
        df (pandas.DataFrame): DataFrame com colunas 'cleaned_text' e 'sentiment'
    """
    st.subheader("Nuvem de Palavras")

    # Tabs para diferentes nuvens de palavras
    tab1, tab2, tab3, tab4 = st.tabs(["Todos", "Positivos", "Neutros", "Negativos"])

    with tab1:
        wordcloud = generate_wordcloud(df['cleaned_text'])
        if wordcloud:
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis('off')
            st.pyplot(fig)
        else:
            st.info("Sem dados suficientes para gerar a nuvem de palavras.")

    with tab2:
        positive_texts = df[df['sentiment'] == 'Positivo']['cleaned_text']
        if not positive_texts.empty:
            wordcloud = generate_wordcloud(positive_texts)
            if wordcloud:
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.imshow(wordcloud, interpolation='bilinear')
                ax.axis('off')
                st.pyplot(fig)
            else:
                st.info("Sem dados suficientes para gerar a nuvem de palavras.")
        else:
            st.info("Nenhum post com sentimento positivo encontrado.")

    with tab3:
        neutral_texts = df[df['sentiment'] == 'Neutro']['cleaned_text']
        if not neutral_texts.empty:
            wordcloud = generate_wordcloud(neutral_texts)
            if wordcloud:
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.imshow(wordcloud, interpolation='bilinear')
                ax.axis('off')
                st.pyplot(fig)
            else:
                st.info("Sem dados suficientes para gerar a nuvem de palavras.")
        else:
            st.info("Nenhum post com sentimento neutro encontrado.")

    with tab4:
        negative_texts = df[df['sentiment'] == 'Negativo']['cleaned_text']
        if not negative_texts.empty:
            wordcloud = generate_wordcloud(negative_texts)
            if wordcloud:
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.imshow(wordcloud, interpolation='bilinear')
                ax.axis('off')
                st.pyplot(fig)
            else:
                st.info("Sem dados suficientes para gerar a nuvem de palavras.")
        else:
            st.info("Nenhum post com sentimento negativo encontrado.")


def display_common_words(df):
    """
    Exibe as palavras mais comuns em forma de tabela e gráfico
    
    Args:
        df (pandas.DataFrame): DataFrame com coluna 'cleaned_text'
    """
    from sentiment_analyzer import get_most_common_words
    
    st.subheader("Termos mais frequentes")

    # Exibir palavras comuns em uma tabela
    common_words = get_most_common_words(df['cleaned_text'], n=15)
    if common_words:
        word_df = pd.DataFrame(common_words, columns=['Palavra', 'Frequência'])

        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(word_df, use_container_width=True)

        with col2:
            # Gráfico horizontal de barras para palavras frequentes
            fig, ax = plt.subplots(figsize=(10, 8))
            sns.barplot(y=[word for word, _ in common_words],
                        x=[count for _, count in common_words],
                        palette='viridis')
            plt.title("Palavras mais frequentes")
            plt.xlabel("Frequência")
            plt.ylabel("Palavra")
            st.pyplot(fig)


def display_posts(df):
    """
    Exibe lista de posts com detalhes e opção de filtro
    
    Args:
        df (pandas.DataFrame): DataFrame com os posts
    """
    st.subheader("Posts Analisados")

    # Filtro para a lista de posts
    sentiment_filter = st.selectbox("Filtrar por sentimento:",
                                  ["Todos", "Positivo", "Neutro", "Negativo"])

    # Aplicar filtro
    if sentiment_filter != "Todos":
        filtered_df = df[df['sentiment'] == sentiment_filter]
    else:
        filtered_df = df

    # Exibir posts
    for i, row in filtered_df.iterrows():
        with st.expander(f"{row['title']} ({row['sentiment']})", expanded=False):
            col1, col2 = st.columns([3, 1])

            with col1:
                st.markdown(f"**Subreddit:** r/{row['subreddit']}")

                if row['selftext']:
                    st.markdown("**Conteúdo:**")
                    st.text(row['selftext'][:500] + ('...' if len(row['selftext']) > 500 else ''))

                st.markdown(f"**Score de Sentimento:** {row['sentiment_score']:.3f}")

            with col2:
                st.markdown(f"**Votos:** {row['score']}")
                st.markdown(f"**Comentários:** {row['num_comments']}")
                st.markdown(f"**Data:** {row['created_utc'].strftime('%d/%m/%Y')}")
                st.markdown(f"[Link para o post]({row['url']})")
