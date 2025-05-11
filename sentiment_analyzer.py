"""
Módulo para análise de sentimento e processamento de texto
"""
import re

import pandas as pd
from textblob import TextBlob

# Lista básica de stopwords personalizada
STOPWORDS = {
    'english': {'a', 'an', 'the', 'and', 'or', 'but', 'if', 'because', 'as', 'what', 'when', 'where',
                'how', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do',
                'does', 'did', 'to', 'at', 'in', 'on', 'by', 'for', 'with', 'about', 'from', 'of',
                'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me',
                'him', 'her', 'us', 'them', 'my', 'your', 'his', 'its', 'our', 'their', 'mine', 'yours',
                'hers', 'ours', 'theirs', 'not', 'no', 'nor', 'can', 'will', 'should', 'would', 'could',
                'may', 'might', 'must', 'shall'},
    'portuguese': {'a', 'o', 'e', 'é', 'de', 'da', 'do', 'das', 'dos', 'em', 'no', 'na', 'nos', 'nas',
                   'um', 'uma', 'uns', 'umas', 'que', 'quem', 'qual', 'quais', 'cujo', 'cuja', 'cujos',
                   'cujas', 'este', 'esta', 'estes', 'estas', 'esse', 'essa', 'esses', 'essas', 'aquele',
                   'aquela', 'aqueles', 'aquelas', 'ele', 'ela', 'nós', 'vocês', 'eles', 'elas', 'seu',
                   'sua', 'seus', 'suas', 'meu', 'minha', 'meus', 'minhas', 'nosso', 'nossa', 'nossos',
                   'nossas', 'com', 'por', 'para', 'sem', 'sob', 'entre', 'até', 'desde', 'após', 'ante',
                   'perante', 'como', 'quando', 'onde', 'porque', 'pois'}
}


def analyze_sentiment(text):
    """
    Analisa o sentimento de um texto
    
    Args:
        text (str): Texto para análise
        
    Returns:
        tuple: (score, label) onde score é um valor entre -1 e 1, e label é "Positivo", "Neutro" ou "Negativo"
    """
    if not text or pd.isna(text):
        return 0, "Neutro"

    analysis = TextBlob(text)
    score = analysis.sentiment.polarity

    if score < -0.1:
        return score, "Negativo"
    elif score > 0.1:
        return score, "Positivo"
    else:
        return score, "Neutro"


def clean_text(text):
    """
    Limpa e normaliza o texto para análise
    
    Args:
        text (str): Texto para limpar
        
    Returns:
        str: Texto limpo
    """
    if not text or pd.isna(text):
        return ""

    # Converter para minúsculas
    text = text.lower()
    # Remover URLs
    text = re.sub(r'http\S+', '', text)
    # Remover caracteres especiais e números
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Remover espaços extras
    text = re.sub(r'\s+', ' ', text).strip()

    return text


def simple_tokenize(text):
    """
    Tokeniza um texto em palavras individuais
    
    Args:
        text (str): Texto para tokenizar
        
    Returns:
        list: Lista de tokens (palavras)
    """
    # Remover pontuação
    text = re.sub(r'[^\w\s]', '', text)
    # Retornar palavras
    return text.lower().split()


def get_common_words_by_sentiment(texts, sentiments, n=20):
    """
        Conta as palavras mais comuns e associa o sentimento dominante a cada uma delas.

        Args:
            texts (list): Lista de textos limpos
            sentiments (list): Lista de rótulos de sentimento correspondentes
            n (int): Número de palavras a retornar

        Returns:
            list: Lista de tuplas (palavra, frequência total, sentimento dominante)
        """
    from collections import defaultdict

    stop_words = STOPWORDS['english'].union(STOPWORDS['portuguese'])
    word_sentiment_counts = defaultdict(lambda: {'Positivo': 0, 'Neutro': 0, 'Negativo': 0})

    for text, sentiment in zip(texts, sentiments):
        tokens = simple_tokenize(text)
        filtered_tokens = [word for word in tokens if word.isalpha() and word not in stop_words and len(word) > 2]
        for token in filtered_tokens:
            word_sentiment_counts[token][sentiment] += 1

    # Montar lista com sentimento dominante
    result = []
    for word, counts in word_sentiment_counts.items():
        total = sum(counts.values())
        dominant_sentiment = max(counts, key=counts.get)
        result.append((word, total, dominant_sentiment))

    # Retornar os top N mais frequentes
    result.sort(key=lambda x: x[1], reverse=True)
    return result[:n]
