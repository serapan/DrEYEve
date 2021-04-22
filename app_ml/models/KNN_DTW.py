from tslearn.neighbors import KNeighborsTimeSeriesClassifier
from .TimeModel import TimeModel


class KNN_DTW(TimeModel):
    def __init__(self, n_neighbors=5, weights='uniform', metric='dtw'):
        self.model = KNeighborsTimeSeriesClassifier(
            n_neighbors=n_neighbors,
            weights=weights,
            metric=metric,
            n_jobs=-1
        )
