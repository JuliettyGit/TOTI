from nltk.corpus import stopwords

from texts import stop_words
from tokenization import tokenization_with_nltk, tokenization_with_pymorphy, text_creator


def find_stopwords_with_nltk(text_to_analise):
    stop_words = set(stopwords.words('english'))
    words = tokenization_with_nltk(text_to_analise)
    words_filtered = []
    new_text = []
    for w in words:
        if w not in stop_words:
            new_text.append(w)
        if w in stop_words:
            words_filtered.append(w)

    return "English text without stopwords from NLTK: ", new_text, "Removed words: ", words_filtered


def find_ukrainian_stopwords(text_to_analise):
    stopwords = text_creator(stop_words)
    words = tokenization_with_pymorphy(text_to_analise)
    words_filtered = []
    new_text = []
    for w in words:
        if w not in stopwords:
            new_text.append(w)
        if w in stopwords:
            words_filtered.append(w)

    return "Ukrainian text without stopwords: ", new_text, "Removed words: ", words_filtered
