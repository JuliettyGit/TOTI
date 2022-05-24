from nltk import word_tokenize
from pymorphy2.tokenizers import simple_word_tokenize
from spacy.lang.en import English
import string

nlp = English()


def text_creator(text_to_filter):
    new_text = text_to_filter.translate(str.maketrans('', '', string.punctuation))
    return new_text


def tokenization_with_nltk(text_to_tokenize):
    text = text_creator(text_to_tokenize)
    tokens = word_tokenize(text)
    return tokens


def tokenization_with_spacy(text_to_tokenize):
    text = text_creator(text_to_tokenize)
    tokens = []
    text = nlp(text)
    for token in text:
        tokens.append(token.text)
    return tokens


def tokenization_with_pymorphy(text_to_tokenize):
    text = text_creator(text_to_tokenize)
    tokens = simple_word_tokenize(text)
    return tokens

