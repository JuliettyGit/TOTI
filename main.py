from lemmatization import lemmatization_with_nltk, lemmatization_with_pymorphy
from steming import stems_with_nltk, stems_with_pymorphy
from texts import text1, text2
from tokenization import tokenization_with_nltk, tokenization_with_pymorphy, tokenization_with_spacy


def get_tokens(text_to_analise):
    print("NLTK tokens: ", tokenization_with_nltk(text_to_analise))
    print("spaCy tokens: ", tokenization_with_spacy(text_to_analise))
    print("pymorphy tokens: ", tokenization_with_pymorphy(text_to_analise))


def get_stems(text_to_analise):
    stems_with_nltk(text_to_analise)
    stems_with_pymorphy(text_to_analise)


def get_lems(text_to_analise):
    lemmatization_with_nltk(text_to_analise)
    lemmatization_with_pymorphy(text_to_analise)


if __name__ == '__main__':
    print("First text (language: ukrainian): \n", text1)
    print("Text tokenization:", get_tokens(text1))
    print("Stems:", get_stems(text1))
    print("Lems:", get_lems(text1))

    print("\nSecond text (language: english): \n", text2)
    print("Text tokenization:", get_tokens(text2))
    print("Stems:", get_stems(text2))
    print("Lems:", get_lems(text2))
