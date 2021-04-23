import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow_addons as tfa
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.metrics import AUC
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from imblearn.under_sampling import RandomUnderSampler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, roc_auc_score
from collections import Counter
from pprint import pprint
import numpy as np


class LayerNormalizationLSTM():

    # input_size = data.iloc[0][0].shape, output_size = 2

    def __init__(self, input_size, output_size, optimizer= Adam(learning_rate=0.001)):
        self.model = keras.Sequential()
        # peep_cell = keras.experimental.PeepholeLSTMCell(128)
        ln_cell = tfa.rnn.LayerNormLSTMCell(128)
        self.model.add(
            layers.RNN(
                ln_cell,
                return_sequences=True,
                input_shape=input_size,
            )
        )
        # peep_cell = keras.experimental.PeepholeLSTMCell(64)
        ln_cell = tfa.rnn.LayerNormLSTMCell(64)
        self.model.add(layers.RNN(ln_cell, return_sequences=True))
        # peep_cell = keras.experimental.PeepholeLSTMCell(32)
        ln_cell = tfa.rnn.LayerNormLSTMCell(64)
        self.model.add(layers.RNN(ln_cell, return_sequences=False))
        self.model.add(layers.Dense(output_size, activation='softmax'))
        self.model.compile(
            optimizer=optimizer,
            loss='binary_crossentropy',
            metrics=['accuracy', AUC()]
        )

    def split_train_test(self, data, labels, sampling_strategy=0.15):
        scaler = MinMaxScaler(feature_range=(-1, 1))
        sampler = RandomUnderSampler(sampling_strategy=sampling_strategy)
        # new_data, new_labels = sampler.fit_resample(data, labels['drivingStyleEncoded'])
        # x_train, x_test, y_train, y_test = train_test_split(
        #     new_data['sequence'], new_labels, test_size=0.3, train_size=0.7, random_state=42)
        x_train, x_test, y_train, y_test = train_test_split(
            data['sequence'], labels['drivingStyleEncoded'], test_size=0.3, train_size=0.7, random_state=42)
        x_train = x_train.apply(scaler.fit_transform)
        x_test = x_test.apply(scaler.fit_transform)
        train_count = Counter(y_train)
        test_count = Counter(y_test)
        y_train = to_categorical(y_train)
        y_test = to_categorical(y_test)
        x_train = np.asarray(list(x_train))
        x_test = np.asarray(list(x_test))
        y_train = np.asarray(y_train)
        print('Train Set:')
        print('\tEvenPaceStyle: {0}'.format(train_count.get(1)))
        print('\tAggressiveStyle: {0}'.format(train_count.get(0)))
        print('Test Set:')
        print('\tEvenPaceStyle: {0}'.format(test_count.get(1)))
        print('\tAggressiveStyle: {0}\n'.format(test_count.get(0)))
        return x_train, y_train, x_test, y_test

    def preprocess_test(self, x_test, y_test):
        scaler = MinMaxScaler(feature_range=(-1, 1))
        x_test = x_test.apply(scaler.fit_transform)
        y_test = to_categorical(y_test)
        x_test = np.asarray(list(x_test))
        return x_test, y_test

    def train(self, x_train, y_train, epochs=50, batch_size=10):
        # self.model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, verbose=0)
        self.model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size)

    def test(self, x_test, y_test):
        predictions = self.model.predict(x_test)
        results_expected = np.argmax(y_test, axis=1)
        results_actual = np.argmax(predictions, axis=1)
        combined = list(zip(results_expected, results_actual))
        combined_equal = [x for x in combined if x[0] == x[1]]
        combined_diff = [x for x in combined if x[0] != x[1]]
        roc_auc = roc_auc_score(y_test.argmax(axis=1), predictions.argmax(axis=1))
        conf_matrix = confusion_matrix(predictions.argmax(axis=1), y_test.argmax(axis=1))
        print('Total: {0}, Equal: {1}, Diff: {2}, Accuracy: {3}'.format(len(combined), len(combined_equal), len(combined_diff), len(combined_equal)/len(combined)))
        print('Roc Auc: {0}'.format(roc_auc))
        pprint(conf_matrix)