from predictor import *



def main():

    df=pd.read_excel("./data_modelo/master.xlsx")
    print(df.head())

    df_activa=df[['FECHA','ACTIVA']]
    df_pasiva=df[['FECHA','PASIVA']]

    df_pasiva=df_pasiva.loc[df_pasiva['PASIVA']>0]
    df_activa=df_activa.loc[df_activa['ACTIVA']>0]

    y_pasiva=y_maker("./data_modelo/master.xlsx",1)
    y_activa=y_maker("./data_modelo/master.xlsx",2)



    seasonal_pdq=season_pdq()


    mod_pasiva=model_gen(y_pasiva,1,1,1,1,0,1,0)
    mod_activa=model_gen(y_activa,1,1,1,1,0,1,0)
    results=mod_pasiva.fit()


    forecast_activa=forecaster(mod_activa,31)
    forecast_pasiva=forecaster(mod_pasiva,31)

    forecast_to_df(forecast_activa, "activa",df_activa)
    forecast_to_df(forecast_pasiva, "pasiva",df_pasiva)


#def get_model_stats():

def pasiva_model_stats():
    df=pd.read_excel("./data_modelo/master.xlsx")
    print(df.head())

    #df_activa=df[['FECHA','ACTIVA']]
    df_pasiva=df[['FECHA','PASIVA']]


    y_pasiva=y_maker("./data_modelo/master.xlsx",1)
    #y_activa=y_maker("./data_modelo/master.xlsx",2)



    seasonal_pdq=season_pdq()


    mod_pasiva=model_gen(y_pasiva,1,1,1,1,0,1,0)
#    mod_activa=model_gen(y_activa,1,1,1,1,0,1,0)
    result_pasiva=mod_pasiva.fit()
    summary=result_pasiva.summary()
    results_as_html=summary.tables[1].as_html()
    
    summary_frame=pd.read_html(results_as_html, header=0, index_col=0)[0]

    return summary_frame

def activa_model_stats():
    df=pd.read_excel("./data_modelo/master.xlsx")
    print(df.head())

    df_activa=df[['FECHA','ACTIVA']]
    #df_pasiva=df[['FECHA','PASIVA']]


    #y_pasiva=y_maker("./data_modelo/master.xlsx",1)
    y_activa=y_maker("./data_modelo/master.xlsx",2)



    seasonal_pdq=season_pdq()


    #mod_pasiva=model_gen(y_pasiva,1,1,1,1,0,1,0)
    mod_activa=model_gen(y_activa,1,1,1,1,0,1,0)
    result_activa=mod_activa.fit()
    summary=result_activa.summary()
    results_as_html=summary.tables[1].as_html()
    
    summary_frame=pd.read_html(results_as_html, header=0, index_col=0)[0]

    return summary_frame


