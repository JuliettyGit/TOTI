from nltk import word_tokenize
from pymorphy2.tokenizers import simple_word_tokenize
from spacy.lang.en import English


nlp = English()


def tokenization_with_nltk(text_to_tokenize):
    tokens = word_tokenize(text_to_tokenize)
    return tokens


def tokenization_with_spacy(text_to_tokenize):
    tokens = []
    text = nlp(text_to_tokenize)
    for token in text:
        tokens.append(token.text)
    return tokens


def tokenization_with_pymorphy(text_to_tokenize):
    tokens = simple_word_tokenize(text_to_tokenize)
    return tokens

