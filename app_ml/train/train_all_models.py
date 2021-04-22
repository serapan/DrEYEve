from app_ml.models.KNN import KNN
from app_ml.models.SVM import SVM
from app_ml.models.RF import RF
from app_ml.models.XGB import XGB
from app_ml.models.MLP import MLP
from app_ml.models.KNN_DTW import KNN_DTW
from app_ml.models.SVM_DTW import SVM_DTW
from app_ml.models.LS import LS
from app_ml.models.RNN import RNN
from app_ml.models.ESN import ESN
from app_ml.functionalities.preprocessing import create_dataset, create_test_set
from app_ml.functionalities.constants import FILES, WINDOW
import time

def test_files(model, window):
    for file in FILES:
        x_test, y_test = create_test_set(file=file, window_size=window)
        x_test, y_test = model.preprocess_test(x_test, y_test)
        print('---------------------------------------- {0} ----------------------------------------'.format(file))
        model.test(x_test, y_test)
        print('------------------------------------------------------------------------------------------------')

def do_it(name, model, data, labels, window):
    print('======================================================== {0} ========================================================\n'.format(name))
    x_train, y_train, x_test, y_test = model.split_train_test(data, labels)
    model.train(x_train, y_train)
    print('---------------------------------------- {0} ----------------------------------------'.format('train/test'))
    start_time = time.time()
    model.test(x_test, y_test)
    response_time = time.time() - start_time
    print('------------------------------------------------------------------------------------------------')
    test_files(model, window)
    num_of_preds = y_test.shape[0]
    throughput = num_of_preds / response_time
    print('Response Time: {0}'.format(response_time))
    print('Predictions/sec: {0}'.format(throughput))
    print('=======================================================================================================================\n')

def main():
    data_simple, labels_simple = create_dataset()
    data_time, labels_time = create_dataset(WINDOW)
    models_simple = {}
    models_time = {}
    # models_simple['KNN'] = KNN()
    # models_simple['SVM'] = SVM()
    # models_simple['RF'] = RF()
    # models_simple['XGB'] = XGB()
    # models_simple['MLP'] = MLP(data_simple.shape[1], 2)
    # models_time['KNN_DTW'] = KNN_DTW()
    # models_time['SVM_DTW'] = SVM_DTW()
    # models_time['LS'] = LS()
    # models_time['RNN'] = RNN(data_time.iloc[0][0].shape, 2)
    models_time['ESN'] = ESN(data_time.iloc[0][0].shape[1], 2)
    for name, model in models_simple.items():
        do_it(name, model, data_simple, labels_simple, 1)
    for name, model in models_time.items():
        do_it(name, model, data_time, labels_time, WINDOW)

if __name__ == '__main__':
    main()