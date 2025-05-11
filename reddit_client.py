"""
Cliente para interagir com a API do Reddit
"""
import praw
import pandas as pd
import streamlit as st
from sentiment_analyzer import analyze_sentiment, clean_text


def fetch_reddit_data(keyword, client_id, client_secret, user_agent, 
                    subreddit=None, limit=30, time_filter="week"):
    """
    Busca posts do Reddit com base em uma palavra-chave e parâmetros definidos
    
    Args:
        keyword (str): Termo de busca
        client_id (str): ID do cliente da API Reddit
        client_secret (str): Secret do cliente da API Reddit
        user_agent (str): User agent para API do Reddit
        subreddit (str, optional): Subreddit específico para busca
        limit (int, optional): Número máximo de posts
        time_filter (str, optional): Filtro de tempo (day, week, month, year, all)
        
    Returns:
        pandas.DataFrame: DataFrame com os dados coletados
    """
    try:
        # Inicializar Reddit API
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )

        # Definir a busca
        query = keyword
        if subreddit:
            posts = reddit.subreddit(subreddit).search(query, limit=limit, time_filter=time_filter)
        else:
            posts = reddit.subreddit("all").search(query, limit=limit, time_filter=time_filter)

        # Coletar dados
        data = []
        with st.spinner(f"Buscando posts sobre '{keyword}'..."):
            for post in posts:
                title = post.title
                selftext = post.selftext if hasattr(post, 'selftext') else ""
                score = post.score
                num_comments = post.num_comments
                created_utc = post.created_utc
                url = post.url
                subreddit_name = post.subreddit.display_name

                combined_text = f"{title} {selftext}"
                sentiment_score, sentiment_label = analyze_sentiment(combined_text)

                data.append({
                    "title": title,
                    "selftext": selftext,
                    "score": score,
                    "num_comments": num_comments,
                    "created_utc": pd.to_datetime(created_utc, unit='s'),
                    "url": url,
                    "subreddit": subreddit_name,
                    "sentiment_score": sentiment_score,
                    "sentiment": sentiment_label,
                    "cleaned_text": clean_text(combined_text)
                })

        return pd.DataFrame(data)

    except Exception as e:
        st.error(f"Erro ao buscar dados do Reddit: {str(e)}")
        if "401" in str(e):
            st.error("Erro de autenticação. Verifique suas credenciais da API.")
        return pd.DataFrame()
