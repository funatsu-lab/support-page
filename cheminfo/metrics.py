import numpy as np
import pandas as pd

__all__ = ['t2_score', 'q_value']

def t2_score(data, model):
    "T2値の計算モジュール"
    assert type(data)==pd.DataFrame or type(data)==np.ndarray, "input must be pandas.DataFrame or np.array"
    explained_std_ = np.sqrt(model.best_estimator_.x_scores_.var(axis=0))
    scores_whiten = model.transform(data) / explained_std_
    return (scores_whiten ** 2.).sum(axis=1)

def q_value(data, model):
    "Q値の計算モジュール"
    assert type(data)==pd.DataFrame or type(data)==np.ndarray, "input must be pandas.DataFrame or np.array"
    x_reproduced_ = model.transform(data) \
              @ model.best_estimator_.x_loadings_.T \
              * model.best_estimator_.x_std_ + model.best_estimator_.x_mean_
    return ((data - x_reproduced_)**2.).sum(axis=1)
