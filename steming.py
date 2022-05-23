from tokenization import tokenization_with_nltk, tokenization_with_pymorphy
from nltk.stem import PorterStemmer


porter = PorterStemmer()


def stems_with_nltk(text_to_analise):
    stems = []
    for word in tokenization_with_nltk(text_to_analise):
        stems.append(porter.stem(word))
    print("Stems from NLTK: ", stems)


def stems_with_pymorphy(text_to_analise):
    stems = []
    for word in tokenization_with_pymorphy(text_to_analise):
        stems.append(porter.stem(word))
    print("Stems from pymorphy: ", stems)
