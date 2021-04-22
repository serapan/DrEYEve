from tslearn.svm import TimeSeriesSVC
from .TimeModel import TimeModel


class SVM_DTW(TimeModel):
    def __init__(self, C=100, kernel='gak', gamma='auto', class_weight='balanced', tol=0.01, decision_function_shape='ovo'):
        self.model = TimeSeriesSVC(
            C=C,
            kernel=kernel,
            gamma=gamma,
            class_weight=class_weight,
            cache_size=2000.0,
            tol=tol,
            decision_function_shape=decision_function_shape,
            n_jobs=-1
        )
