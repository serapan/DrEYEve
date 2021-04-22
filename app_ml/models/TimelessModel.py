from imblearn.under_sampling import RandomUnderSampler
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score
from collections import Counter
from pprint import pprint

class TimelessModel():
    def __init__(self):
        self.model = None
    
    def split_train_test(self, data, labels, sampling_strategy=0.42):
        scaler = StandardScaler()
        sampler = RandomUnderSampler(sampling_strategy=sampling_strategy)
        x_train, x_test, y_train, y_test = train_test_split(
            data, labels['drivingStyleEncoded'], test_size=0.3, train_size=0.7, random_state=42)
        x_train = scaler.fit_transform(x_train)
        x_test = scaler.fit_transform(x_test)
        x_train, y_train = sampler.fit_resample(x_train, y_train)
        train_count = Counter(y_train)
        test_count = Counter(y_test)
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