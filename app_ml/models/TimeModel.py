from imblearn.under_sampling import RandomUnderSampler
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score
from tslearn.utils import to_time_series_dataset
from collections import Counter
from pprint import pprint
import numpy as np

class TimeModel():
    def __init__(self):
        self.model = None
    
    def split_train_test(self, data, labels, sampling_strategy=0.3):
        scaler = StandardScaler()
        sampler = RandomUnderSampler(sampling_strategy=sampling_strategy)
        # new_data, new_labels = sampler.fit_resample(data, labels['drivingStyleEncoded'])
        # x_train, x_test, y_train, y_test = train_test_split(
            # new_data['sequence'], new_labels, test_size=0.3, train_size=0.7, random_state=42)
        x_train, x_test, y_train, y_test = train_test_split(
            data['sequence'], labels['drivingStyleEncoded'], test_size=0.3, train_size=0.7, random_state=42)
        x_train = x_train.reset_index(drop=True)
        y_train = y_train.reset_index(drop=True)
        x_test = x_test.reset_index(drop=True)
        y_test = y_test.reset_index(drop=True)
        x_train = x_train.apply(scaler.fit_transform)
        x_test = x_test.apply(scaler.fit_transform)
        x_train = to_time_series_dataset(x_train)
        y_train = np.asarray(y_train)
        x_test = to_time_series_dataset(x_test)
        y_test = np.asarray(y_test)
        train_count = Counter(y_train)
        test_count = Counter(y_test)
        pprint(y_train)
        print('Train Set:')
        print('\tEvenPaceStyle: {0}'.format(train_count.get(1)))
        print('\tAggressiveStyle: {0}'.format(train_count.get(0)))
        print('Test Set:')
        print('\tEvenPaceStyle: {0}'.format(test_count.get(1)))
        print('\tAggressiveStyle: {0}\n'.format(test_count.get(0)))
        return x_train, y_train, x_test, y_test
    
    def preprocess_test(self, x_test, y_test):
        scaler = StandardScaler()
        x_test = x_test.reset_index(drop=True)
        y_test = y_test.reset_index(drop=True)
        x_test = x_test.apply(scaler.fit_transform)
        x_test = to_time_series_dataset(x_test)
        y_test = np.asarray(y_test)
        return x_test, y_test

    def train(self, x_train, y_train):
        self.model.fit(x_train, y_train)

    def test(self, x_test, y_test):
        predictions = self.model.predict(x_test)
        conf_matrix = confusion_matrix(predictions, y_test)
        accuracy = accuracy_score(y_test, predictions)
        roc_auc = roc_auc_score(y_test, predictions)
        print('Accuracy: {0}'.format(accuracy))
        print('Roc Auc: {0}'.format(roc_auc))
        pprint(conf_matrix)