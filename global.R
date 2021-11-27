library(reactable)
library(highcharter)
library(shinyjs)
library(readxl)
library(sqldf)
library(dplyr)
library(reticulate)
library(gtools)
library(openxlsx)


source_python("main.py")

main()

#use_python("C:/Users/Marlon/AppData/Local/Programs/Python/Python37",required=TRUE)



df_real <- as.data.frame(read_excel("./data_modelo/master.xlsx"))




df_activa <- as.data.frame(read_excel("./forecast_result/activa.xlsx"))

df_pasiva <- as.data.frame(read_excel("./forecast_result/pasiva.xlsx"))

df_joined <- sqldf("
                  select fecha FECHA, sum(activa) ACTIVA_REAL, sum(pasiva) PASIVA_REAL, sum(activa_forecast) FORECAST_ACTIVA, sum(pasiva_forecast) FORECAST_PASIVA
                  from (
                   select a.FECHA, a.ACTIVA, a.PASIVA, 0 activa_forecast,0 pasiva_forecast
                   from df_real a 
                   UNION ALL 
                   SELECT FECHA, 0,0, B.ACTIVA,0
                   FROM  df_activa b 
                   union all
                   select FECHA, 0,0,0,c.PASIVA
                   from df_pasiva c
                  )
                  group by fecha
                   
                   ")


