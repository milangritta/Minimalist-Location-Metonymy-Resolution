import codecs
import random
import re
import cPickle
from keras.callbacks import ModelCheckpoint
import numpy as np
from keras.engine import Merge
from keras.layers import Embedding, TimeDistributed, Flatten
from keras.layers.core import Dense, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential
np.random.seed(133)
random.seed(133)
#  --------------------------------------------------------------------------------------------------------------------
dimensionality = 50  # No need to adjust, unless you want to experiment with custom embeddings
seq_length = 5  # Adjust to 5 for PreWin and 5, 10, 50 for baseline results
print("Dimensionality:", dimensionality)
print("Sequence Length: 2 times ", seq_length)
regex = re.compile(r"[+-.]?\d+[-.,\d+:]*(th|st|nd|rd)?")
# Remember to choose the CORRECT file names below otherwise you will see bad things happen :-)

# neg = cPickle.load(open("pickle/semeval_metonymic_train.pkl")) + cPickle.load(open("pickle/semeval_mixed_train.pkl"))
# pos = cPickle.load(open("pickle/semeval_literal_train.pkl"))

neg = cPickle.load(open("pickle/relocar_metonymic_train.pkl"))
pos = cPickle.load(open("pickle/relocar_literal_train.pkl"))
    
A = []
dep_labels = {u"<u>"}
for coll in [neg, pos]:
    for l in coll:
        A.append(l)
        dep_labels.update(set(l[1][-seq_length:] + l[3][:seq_length]))
random.shuffle(A)
X_L, D_L, X_R, D_R, Y = [], [], [], [], []
for a in A:
    X_L.append(a[0][-seq_length:])
    D_L.append(a[1][-seq_length:])
    X_R.append(a[2][:seq_length])
    D_R.append(a[3][:seq_length])
    Y.append(a[4])

print('No of training examples: ', len(X_L))
cPickle.dump(dep_labels, open("pickle/dep_labels.pkl", "w"))
dep_labels = cPickle.load(open("pickle/dep_labels.pkl"))
#  --------------------------------------------------------------------------------------------------------------------
vocabulary = {u"<u>", u"0.0"}
vocab_limit = 100000
print('Vocabulary Size: ', vocab_limit)
print("Building sequences...")

count = 0
vectors_glove = {u'<u>': np.ones(dimensionality)}
# Please supply your own embeddings, see README.md for details
for line in codecs.open("/Users/milangritta/PycharmProjects/Keras/archive/data/glove.txt", encoding="utf-8"):
    tokens = line.split()
    vocabulary.add(tokens[0])
    vectors_glove[tokens[0]] = [float(x) for x in tokens[1:]]
    count += 1
    if count >= vocab_limit:
        break

vectors_glove[u"0.0"] = np.zeros(dimensionality)
word_to_index = dict([(w, i) for i, w in enumerate(vocabulary)])
dep_to_index = dict([(w, i) for i, w in enumerate(dep_labels)])

for x_l, x_r, d_l, d_r in zip(X_L, X_R, D_L, D_R):
    for i, w in enumerate(x_l):
        if w != u"0.0":
            w = regex.sub(u"1", w)
        if w in word_to_index:
            x_l[i] = word_to_index[w]
        else:
            x_l[i] = word_to_index[u"<u>"]
    for i, w in enumerate(x_r):
        if w != u"0.0":
            w = regex.sub(u"1", w)
        if w in word_to_index:
            x_r[i] = word_to_index[w]
        else:
            x_r[i] = word_to_index[u"<u>"]
    for i, w in enumerate(d_l):
        arr = np.zeros(len(dep_labels))
        if w in dep_to_index:
            arr[dep_to_index[w]] = 1
        else:
            arr[dep_to_index[u"<u>"]] = 1
        d_l[i] = arr
    for i, w in enumerate(d_r):
        arr = np.zeros(len(dep_labels))
        if w in dep_to_index:
            arr[dep_to_index[w]] = 1
        else:
            arr[dep_to_index[u"<u>"]] = 1
        d_r[i] = arr

X_L = np.asarray(X_L)
X_R = np.asarray(X_R)
D_L = np.asarray(D_L)
D_R = np.asarray(D_R)
Y = np.asarray(Y)

weights = np.zeros((len(vocabulary), dimensionality))
for w in vocabulary:
    if w in vectors_glove:
        weights[word_to_index[w]] = vectors_glove[w]
weights = np.array([weights])

print(u"Done...")
#  --------------------------------------------------------------------------------------------------------------------
print(u'Building model...')
model_left = Sequential()
model_left.add(Embedding(len(vocabulary), dimensionality, input_length=seq_length, weights=weights))
model_left.add(LSTM(output_dim=15))
model_left.add(Dropout(0.2))

dep_left = Sequential()
dep_left.add(TimeDistributed(Dense(output_dim=15), input_shape=(seq_length, len(dep_labels))))
dep_left.add(Dropout(0.2))
dep_left.add(Flatten())

model_right = Sequential()
model_right.add(Embedding(len(vocabulary), dimensionality, input_length=seq_length, weights=weights))
model_right.add(LSTM(output_dim=15, go_backwards=True))
model_right.add(Dropout(0.2))

dep_right = Sequential()
dep_right.add(TimeDistributed(Dense(output_dim=15), input_shape=(seq_length, len(dep_labels))))
dep_right.add(Dropout(0.2))
dep_right.add(Flatten())

merged_model = Sequential()
merged_model.add(Merge([model_left, dep_left, model_right, dep_right], mode='concat', concat_axis=1))
merged_model.add(Dense(10))
merged_model.add(Dense(1, activation='sigmoid'))
merged_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(u"Done...")
#  --------------------------------------------------------------------------------------------------------------------
checkpoint = ModelCheckpoint(filepath="./weights/lstm.hdf5", verbose=0)
merged_model.fit([X_L, D_L, X_R, D_R], Y, batch_size=16, nb_epoch=5, callbacks=[checkpoint], verbose=1)
#  --------------------------------------------------------------------------------------------------------------------
