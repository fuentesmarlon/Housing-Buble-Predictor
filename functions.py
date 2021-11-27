from math import sqrt
from multiprocessing import cpu_count
from multiprocessing import Pool
from joblib import Parallel
from joblib import delayed
from warnings import catch_warnings
from warnings import filterwarnings
from sklearn.metrics import mean_squared_error
import pandas as pd 
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Mean Squared Error
def measure_rmse(actual, predicted):
    return mean_squared_error(actual, predicted)

# Particion del dataset (n_test = cantidad de periodos)
def train_test_split(data, n_test):
    return data[:-n_test], data[-n_test:]

# Pronóstico SARIMA
def sarima_forecast(history, config):
    order, sorder, trend = config
    model = SARIMAX(history, order = order, seasonal_order = sorder, trend = trend, enforce_stationarity = False, enforce_invertibilty = False)
    model_fit = model.fit(disp = False)
    yhat = model_fit.predict(len(history), len(history))
    return yhat[0]

# Validaicón
def walk_forward_validation(data, n_test, cfg):
    predictions = list()
    train, test = train_test_split(data, n_test)
    history = [x for x in train]
    for i in range(len(test)):
        yhat = sarima_forecast(history, cfg)
        predictions.append(yhat)
        history.append(test[i])
    error = 84*measure_rmse(test, predictions)
    average = sum(test)/len(test)
    average_sum = 0
    for i in test:
        average_sum += (average-i)**2
    return error/average_sum

# Scoring
def score_model(data, n_test, cfg, debug = False):
    result = None 
    key = str(cfg)
    if debug:
        result = walk_forward_validation(data, n_test, cfg)
    else:
        try:
            with catch_warnings():
                filterwarnings("ignore")
                result = walk_forward_validation(data, n_test, cfg)
        except:
            error = None
    if result is not None:
        print(' > Model[%s] %.3f' % (key,result))
    return (key,result)

# Configuraciones GridSearch
def grid_search(data, cfg_list, n_test, parallel = True):
    scores = None
    if parallel:
        executor = Parallel(n_jobs = cpu_count(), backend = 'multiprocessing')
        tasks = (delayed(score_model)(data, n_test, cfg) for cfg in cfg_list)
        scores = executor(tasks)
        print(scores)
    else:
        scores = [score_model(data, n_test, cfg) for cfg in cfg_list]
    scores = [r for r in scores if r[1] != None]
    scores.sort(key = lambda tup: tup[1])
    print(scores)
    return scores

# Parametros SARIMA 
def sarima_configs(seasonal = [0]):
    models = list()
    p_params = [0,1,2]
    d_params = [1]
    q_params = [0,1,2]
    t_params = ['t']
    P_params = [0,1,2]
    D_params = [0,1]
    Q_params = [0,1,2]
    m_params = seasonal
    for p in p_params:
        for d in d_params:
            for q in q_params:
                for t in t_params:
                    for P in P_params:
                        for D in D_params:
                            for Q in Q_params:
                                for m in m_params:
                                    cfg = [(p,d,q),(P,D,Q,m),t]
                                    models.append(cfg)
    return models

model=sarima_configs()
print(model)