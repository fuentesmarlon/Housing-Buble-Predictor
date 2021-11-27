import warnings
import itertools
import numpy as np 
import matplotlib.pyplot as plt 

import pandas as pd
import statsmodels.api as sm

warnings.filterwarnings("ignore")






df=pd.read_excel("data_home_post.xlsx")


y=df.set_index(['Fecha'])
#y.plot(figsize=(19,4))
#plt.show()
print(df.info())

#descompositional
from pylab import rcParams

p = d = q = range(0, 2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]



#100 010112
#000 10012
#001 01112
##mas cercano 001 10012
##nada mal 111 01012

mod = sm.tsa.statespace.SARIMAX(y,
                                order=(1, 1,1),
                                seasonal_order=(0, 1, 0, 31),
                                enforce_stationarity=False,
                                enforce_invertibility=False)    
results = mod.fit()
print(results.summary().tables[1])
#results.plot_diagnostics(figsize=(18, 8))
#plt.show()

"""pred=results.get_prediction(start=pd.to_datetime('2020-06-01'),dynamic=False)

pred_ci=pred.conf_int()
ax=y['2019':].plot(label='observed')
pred.predicted_mean.plot(ax=ax,label='One-step ahead Forecast',alpha=.7,figsize=(14,6))

ax.fill_between(pred_ci.index,pred_ci.iloc[:, 0],pred_ci.iloc[:, 1],color='k',alpha=.2)
ax.set_xlabel('Date')
ax.set_ylabel('Retail_sold')
plt.legend()
plt.show()

"""
pred_uc=results.get_forecast(steps=31)
pred_ci=pred_uc.conf_int()
ax=y.plot(label='observed',figsize=(14,4))
pred_uc.predicted_mean.plot(ax=ax,label='Forecast')
ax.fill_between(pred_ci.index,pred_ci.iloc[:,0],pred_ci.iloc[:,1],color='k',alpha=.25)

ax.set_xlabel('Date')
ax.set_ylabel('Sales')
plt.legend()
plt.show()
##---quitar estos
forecast=pred_uc.predicted_mean
print(forecast.head(30))
forecast.to_excel("./Forecast/forecast_home.xlsx")

#forecast=pred.predicted_mean
#print(forecast.head())
#forecast.to_excel("./forecast.xlsx")"""