from sklearn.ensemble import RandomForestClassifier
from .TimelessModel import TimelessModel


class RF(TimelessModel):
    def __init__(self, criterion='entropy', class_weight=None, max_depth=100, max_features='sqrt', min_samples_leaf=1, min_samples_split=2, n_estimators=150):
        self.model = RandomForestClassifier(
            criterion=criterion,
            class_weight=class_weight,
            max_depth=max_depth,
            max_features=max_features,
            min_samples_leaf=min_samples_leaf,
            min_samples_split=min_samples_split,
            n_estimators=n_estimators
        )
