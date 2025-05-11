"""
Módulo para análise de sentimento e processamento de texto
"""
import re
from collections import Counter
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


def get_most_common_words(texts, n=10):
    """
    Identifica as palavras mais comuns em um conjunto de textos
    
    Args:
        texts (list): Lista de textos para análise
        n (int, optional): Número de palavras para retornar
        
    Returns:
        list: Lista de tuplas (palavra, frequência) ordenadas por frequência
    """
    # Combinar stopwords de diferentes idiomas
    stop_words = STOPWORDS['english'].union(STOPWORDS['portuguese'])

    words = []

    for text in texts:
        if not text or pd.isna(text):
            continue

        # Tokenizar e filtrar palavras
        tokens = simple_tokenize(text)
        filtered_tokens = [word for word in tokens
                           if word.isalpha() and word.lower() not in stop_words and len(word) > 2]
        words.extend(filtered_tokens)

    # Contar frequências
    word_counts = Counter(words)
    return word_counts.most_common(n)
