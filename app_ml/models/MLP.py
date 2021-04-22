import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.metrics import AUC
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import BorderlineSMOTE
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, roc_auc_score
from collections import Counter
from pprint import pprint
import numpy as np


class MLP():

    # input_size = data.shape[1], output_size = 2

    def __init__(self, input_size, output_size, optimizer=Adam(learning_rate=0.001)):
        self.model = keras.Sequential()
        self.model.add(layers.InputLayer(input_shape=input_size))
        self.model.add(layers.Dense(256, activation='relu'))
        self.model.add(layers.Dense(128, activation='relu'))
        self.model.add(layers.Dense(64, activation='relu'))
        self.model.add(layers.Dense(output_size, activation='softmax'))
        self.model.compile(
            optimizer=optimizer,
            loss='binary_crossentropy',
            metrics=['accuracy', AUC()]
        )

    def split_train_test(self, data, labels, undersampling_strategy=0.15, oversampling_strategy=0.6):
        scaler = StandardScaler()
        undersampler = RandomUnderSampler(sampling_strategy=undersampling_strategy)
        oversampler = BorderlineSMOTE(sampling_strategy=oversampling_strategy)
        x_train, x_test, y_train, y_test = train_test_split(
            data, labels['drivingStyleEncoded'], test_size=0.3, train_size=0.7, random_state=42)
        x_train = scaler.fit_transform(x_train)
        x_test = scaler.fit_transform(x_test)
        x_train, y_train = undersampler.fit_resample(x_train, y_train)
        x_train, y_train = oversampler.fit_resample(x_train, y_train)
        train_count = Counter(y_train)
        test_count = Counter(y_test)
        y_train = to_categorical(y_train)
        y_test = to_categorical(y_test)
        print('Train Set:')
        print('\tEvenPaceStyle: {0}'.format(train_count.get(1)))
        print('\tAggressiveStyle: {0}'.format(train_count.get(0)))
        print('Test Set:')
        print('\tEvenPaceStyle: {0}'.format(test_count.get(1)))
        print('\tAggressiveStyle: {0}\n'.format(test_count.get(0)))
        return x_train, y_train, x_test, y_test
    
    def preprocess_test(self, x_test, y_test):
        scaler = StandardScaler()
        x_test = scaler.fit_transform(x_test)
        y_test = to_categorical(y_test)
        return x_test, y_test

    def train(self, x_train, y_train, epochs=60, batch_size=10):
        self.model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, verbose=0)

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
