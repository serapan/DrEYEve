from sklearn.neighbors import KNeighborsClassifier
from .TimelessModel import TimelessModel


class KNN(TimelessModel):
    def __init__(self, n_neighbors=5, p=1, weights='distance'):
        self.model = KNeighborsClassifier(
            algorithm='auto',
            n_neighbors=n_neighbors,
            p=p,
            weights=weights
        )
