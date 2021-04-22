from xgboost.sklearn import XGBClassifier
from .TimelessModel import TimelessModel

class XGB(TimelessModel):
    def __init__(self, learning_rate=0.2, max_delta_step=0, max_depth=20, n_estimators=200, gamma=0, alpha=0, reg_lambda=1, colsample_bylevel=0.75, colsample_bytree=1, colsample_bynode=1, subsample=1, scale_pos_weight=1):
        self.model = XGBClassifier(
            verbosity=0,
            use_label_encoder=False,
            learning_rate=learning_rate,
            max_delta_step=max_delta_step,
            max_depth=max_depth,
            n_estimators=n_estimators,
            gamma=gamma,
            alpha=alpha,
            reg_lambda=reg_lambda,
            colsample_bylevel=colsample_bylevel,
            colsample_bytree=colsample_bytree,
            colsample_bynode=colsample_bynode,
            subsample=subsample,
            scale_pos_weight=scale_pos_weight
        )

