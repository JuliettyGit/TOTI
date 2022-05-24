from lemmatization import lemmatization_with_nltk, lemmatization_with_pymorphy
from steming import stems_with_nltk, stems_with_pymorphy
from stop_words_finder import find_stopwords_with_nltk, find_ukrainian_stopwords
from texts import text1, text2
from tokenization import tokenization_with_nltk, tokenization_with_pymorphy, tokenization_with_spacy, text_creator

if __name__ == '__main__':
    print("First text (language: ukrainian): \n", text1)
    print("Text tokenization:", )
    print("NLTK tokens: ", tokenization_with_nltk(text1))
    print("spaCy tokens: ", tokenization_with_spacy(text1))
    print("pymorphy tokens: ", tokenization_with_pymorphy(text1))
    print("Stems: \n", stems_with_nltk(text1), "\n", stems_with_pymorphy(text1))
    print("Lems: \n", lemmatization_with_nltk(text1), "\n", lemmatization_with_pymorphy(text1))
    print("Stopwords: \n", find_ukrainian_stopwords(text1))

    print("\nSecond text (language: english): \n", text2)
    print("Text tokenization:", )
    print("NLTK tokens: ", tokenization_with_nltk(text2))
    print("spaCy tokens: ", tokenization_with_spacy(text2))
    print("pymorphy tokens: ", tokenization_with_pymorphy(text2))
    print("Stems: \n", stems_with_nltk(text2), "\n", stems_with_pymorphy(text2))
    print("Lems: \n", lemmatization_with_nltk(text2), "\n", lemmatization_with_pymorphy(text2))
    print("Stopwords: \n", find_stopwords_with_nltk(text2))
