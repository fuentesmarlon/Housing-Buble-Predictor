import warnings
import itertools
import numpy as np 
import pandas as pd
import statsmodels.api as sm
from datetime import datetime, timedelta



warnings.filterwarnings("ignore")



#y_activa=df_activa.set_index(['FECHA'])





def y_maker(df_data,type_df):
    
    if (type_df==1):
        df=pd.read_excel(df_data)
        the_df=df[['FECHA','PASIVA']]
    elif (type_df==2):
        df=pd.read_excel(df_data)
        the_df=df[['FECHA','ACTIVA']]
    

    y_result=the_df.set_index(['FECHA'])

    return y_result

def season_pdq():
    p=d=q=range(0,2)

    pdq=list(itertools.product(p, d, q))


    seasonal_pdq=[(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

    return seasonal_pdq
    
def model_gen(y_index, p,d,q,season_type,P,D,Q):
    if(season_type==1):
        mod= sm.tsa.statespace.SARIMAX(y_index, order=(p,d,q),seasonal_order=(P,D,Q,52),enforce_stationarity=False, enforce_invertibility=False)
        return mod
    elif(season_type==2):
        mod= sm.tsa.statespace.SARIMAX(y_index, order=(p,d,q),seasonal_order=(P,D,Q,30),enforce_stationarity=False, enforce_invertibility=False)
        return mod


def forecaster(mod,steps_taken):
    results=mod.fit()
    pred_uc=results.get_forecast(steps=steps_taken)
    forecast=pred_uc.predicted_mean
    return forecast







#building forecast excel 


def forecast_to_df(forecast,name,df_overwrite):

    

    forecast_values =np.array(forecast.values.tolist())

    value_insert=[]
    row_forecast=[]

    max_value=df_overwrite["FECHA"].max()

    next_date=max_value+timedelta(7)

    for i in forecast_values:
        #row_date=datetime.strftime(next_date,'%Y-%m-%d')
        row_forecast.append(next_date)
        row_forecast.append(i)
        next_date=next_date+timedelta(7)
        value_insert.append(row_forecast)
        row_forecast=[]


    for i in value_insert:
        df_overwrite.loc[len(df_overwrite)]=i

    df_overwrite.to_excel("./forecast_result/"+str(name)+".xlsx",index=False)








