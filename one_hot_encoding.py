from lemmatization import lemmatization_with_pymorphy
from texts import text2
from numpy import array
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

data = lemmatization_with_pymorphy(text2)
values = array(data[10:30])


def print_lemms():
    print("Lemms:", values)


def integer_encode():
    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(values)
    return integer_encoded


def binary_encode(integer_encoded):
    onehot_encoder = OneHotEncoder(sparse=False)
    integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
    print(onehot_encoded)
