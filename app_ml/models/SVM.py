from sklearn.svm import SVC
from .TimelessModel import TimelessModel


class SVM(TimelessModel):
    def __init__(self, C=100, decision_function_shape='ovo', gamma='auto', kernel='rbf', tol=0.01):
        super().__init__()
        self.model = SVC(
            C=C,
            cache_size=2000,
            decision_function_shape=decision_function_shape,
            gamma=gamma,
            kernel=kernel,
            tol=tol
        )
