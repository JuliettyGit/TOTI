import pymorphy2
from nltk import WordNetLemmatizer
from tokenization import tokenization_with_nltk, tokenization_with_pymorphy

lemmatizer = WordNetLemmatizer()
morph = pymorphy2.MorphAnalyzer()


def lemmatization_with_nltk(text_to_analise):
    lems = []
    for word in tokenization_with_nltk(text_to_analise):
        lems.append(lemmatizer.lemmatize(word))
    print("Lems from NLTK: ", lems)


def lemmatization_with_pymorphy(text_to_analise):
    lems = []
    for word in tokenization_with_pymorphy(text_to_analise):
        lems.append(morph.parse(word)[0].normal_form)
    print("Lems from pymorphy: ", lems)
