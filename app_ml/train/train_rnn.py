from app_ml.functionalities.preprocessing_mongo import read_from_mongo_as_dataframe
from app_ml.functionalities.constants import SAVED_MODEL_PATH
from app_ml.models.RNN import RNN
import pymongo

def main():
    cars_db = pymongo.MongoClient('mongodb://localhost:27017')['cars']
    data, labels = read_from_mongo_as_dataframe(cars_db)
    rnn_model = RNN(data.iloc[0][0].shape, 2)
    x_train, y_train, x_test, y_test = rnn_model.split_train_test(data, labels)
    rnn_model.train(x_train, y_train)
    rnn_model.test(x_test, y_test)
    rnn_model.model.save(SAVED_MODEL_PATH)
    
if __name__ == '__main__':
    main()