

shinyServer(function(input,output,session){
  
  
  RV <- reactiveValues()
  
  
  #### Reactive Elements #####
  
  # stats_model <- reactive({
  # 
  #     html_values <- pasiva_model_stats()
  #     
  #     return(html_values)
  #   
  # })
  # 
  # stats_model_Active <- reactive({
  #   
  #   html_values <- activa_model_stats()
  #   
  #   return(html_values)
  #   
  # })
  
  
  
  #### Observe Events ####
  
  
  observeEvent(list(input$menu,input$fecha_summary),{
    if(input$menu=="summary"){

       RV$filtered_df <- df_joined%>%
         filter(FECHA>=input$fecha_summary[1] & FECHA<=input$fecha_summary[2])
    }
    else if(input$menu=="predictor"){
      RV$stats_model <- pasiva_model_stats()
      
      RV$stats_model_Active <- activa_model_stats()
      
      
      RV$all_data <- as.data.frame(read_excel("./data_modelo/master.xlsx"))
    }
    
  })
  
  
  
  observeEvent(input$button_adder,{
    showModal(
      modalDialog(
        title=h3(paste("Add New Actual Data for Model")),
        fluidRow(
          column(
            width=6, 
            selectInput(
              "type_insert",
              "Tipo Información: ",
              choices=c("Tasa Activa","Tasa Pasiva","Ambos"), 
              selected="Ambos"
            )
        )
      ),
      fluidRow(
        column(
          width = 6,
          fileInput("file_button","Choose xlsx file",accept=c(".xlsx"))
        )
        
        
      ),easyClose = TRUE,
      footer=tagList(actionButton("insert_data","Insert"),
                     actionButton("cerrar2","Cerrar"))
      
    )
    
    )
  })
  
  observeEvent(input$cerrar2,{
    removeModal()
  })
  
  observeEvent(input$insert_data,{
    insert_type <- input$type_insert
    file_uploaded <- input$file_button
    file.rename(file_uploaded$datapath,
                paste(file_uploaded$datapath, ".xlsx", sep=""))
    data_file <- read_excel(paste(file_uploaded$datapath, ".xlsx", sep=""), 1)
    
    if(insert_type=="Tasa Activa" && ncol(data_file)==2){
      
      data_file <- as.data.frame(data_file)
      
      
      names(data_file) <- c("FECHA","ACTIVA")
      
      
      
      
      
      new_df <- smartbind(df_real, data_file)
      
      new_df[is.na(new_df)] <- 0
      
      
      
      new_df$FECHA <- as.Date(new_df$FECHA)
      
      my_workbook <- createWorkbook()
      addWorksheet(wb=my_workbook,sheetName = "Sheet1")
      writeData(my_workbook,sheet=1,new_df,startCol = 1,startRow = 1,keepNA = FALSE)
      
      saveWorkbook(my_workbook,"./data_modelo/master.xlsx",overwrite=TRUE)
      
      
      main()
      
      RV$stats_model <- pasiva_model_stats()
      
      RV$stats_model_Active <- activa_model_stats()
      
      RV$all_data <- as.data.frame(read_excel("./data_modelo/master.xlsx"))
      
      showModal(modalDialog("DATA UPDATED!"))
      
    }
    else if(insert_type=="Tasa Pasiva" && ncol(data_file)==2){
      
      data_file <- as.data.frame(data_file)
      
      
      names(data_file) <- c("FECHA","PASIVA")
      
      
      
      
      
      new_df <- smartbind(df_real, data_file)
      
      new_df[is.na(new_df)] <- 0
      
      
      
      new_df$FECHA <- as.Date(new_df$FECHA)
      
      my_workbook <- createWorkbook()
      addWorksheet(wb=my_workbook,sheetName = "Sheet1")
      writeData(my_workbook,sheet=1,new_df,startCol = 1,startRow = 1,keepNA = FALSE)
      
      saveWorkbook(my_workbook,"./data_modelo/master.xlsx",overwrite=TRUE)
      
      
      main()
      
      RV$stats_model <- pasiva_model_stats()
      
      RV$stats_model_Active <- activa_model_stats()
      
      RV$all_data <- as.data.frame(read_excel("./data_modelo/master.xlsx"))
      
      showModal(modalDialog("DATA UPDATED!"))
      
      
      
      
    }
    else if(insert_type=="Ambos" && ncol(data_file)==3){
      
      
      data_file <- as.data.frame(data_file)
      
      
      names(data_file) <- c("FECHA","ACTIVA","PASIVA")
      
      
      
      
      
      new_df <- smartbind(df_real, data_file)
      
      new_df[is.na(new_df)] <- 0
      
      
      
      new_df$FECHA <- as.Date(new_df$FECHA)
      
      my_workbook <- createWorkbook()
      addWorksheet(wb=my_workbook,sheetName = "Sheet1")
      writeData(my_workbook,sheet=1,new_df,startCol = 1,startRow = 1,keepNA = FALSE)
      
      saveWorkbook(my_workbook,"./data_modelo/master.xlsx",overwrite=TRUE)
      
      
      main()
      
      RV$stats_model <- pasiva_model_stats()
      
      RV$stats_model_Active <- activa_model_stats()
      
      RV$all_data <- as.data.frame(read_excel("./data_modelo/master.xlsx"))

      showModal(modalDialog("DATA UPDATED!"))
      
    }
    else{
      showModal(modalDialog("WRONG FORMAT"))
    }
    
    
  })
  
  
  
  
  #### GRAPHS####
  output$activa_graph <- renderHighchart({
    data <- df_activa
    
    data_graph <- RV$filtered_df
  
    
    highchart()%>%
      hc_chart(animation=TRUE)%>%
      hc_xAxis(categories=as.Date(df_joined$FECHA))%>%
      
      hc_add_series(data=data_graph$FORECAST_ACTIVA,type="line",name="Forecast Interes Activo",color="red")%>%
    hc_add_series(data=data_graph$ACTIVA_REAL[data_graph$ACTIVA_REAL>0],type="line",name="Real Interes Activo",color="black")
    
    
  })
  
  
  output$pasiva_graph <- renderHighchart({
    data <- df_pasiva
    
    data_graph <- RV$filtered_df
    
    
    highchart()%>%
      hc_chart(animation=TRUE)%>%
      hc_xAxis(categories=as.Date(df_joined$FECHA))%>%
      
      hc_add_series(data=data_graph$FORECAST_PASIVA,type="line",name="Forecast Interes Pasivo",color="blue")%>%
      hc_add_series(data=data_graph$PASIVA_REAL[data_graph$PASIVA_REAL>0],type="line",name="Real Interes Pasivo",color="black")
    
    
  })
  
  
  ###REACTABLE####
  output$activa_tabla <- renderReactable({
    data <-  RV$filtered_df%>%
      select(FECHA, ACTIVA_REAL, FORECAST_ACTIVA)
    
    reactable(
      data,resizable=TRUE, defaultPageSize = nrow(data), onClick="expand",highlight=TRUE, 
      theme=reactableTheme(
        headerStyle = list(background="#2171B5",color="white")
      ),
      columns=list(
        ACTIVA_REAL=colDef(name="Tasa Activa Real", cel=function(value,index){
          args <- list(prettyNum(round(value,2),big.mark=","))
        }
          
          ),
        FORECAST_ACTIVA=colDef(name="Tasa Activa Proyectada", cel=function(value,index){
          args <- list(prettyNum(round(value,2),big.mark=","))
        }
        
        )
      )
    )
      
  
    
    
  })
  
  output$pasiva_tabla <- renderReactable({
    data <-  RV$filtered_df%>%
      select(FECHA, PASIVA_REAL, FORECAST_PASIVA)
    
    reactable(
      data,resizable=TRUE, defaultPageSize = nrow(data), onClick="expand",highlight=TRUE, 
      theme=reactableTheme(
        headerStyle = list(background="#2171B5",color="white")
      ),
      columns=list(
        PASIVA_REAL=colDef(name="Tasa Pasiva Real", cel=function(value,index){
          args <- list(prettyNum(round(value,2),big.mark=","))
        }
        
        ),
        FORECAST_PASIVA=colDef(name="Tasa Pasiva Proyectada", cel=function(value,index){
          args <- list(prettyNum(round(value,2),big.mark=","))
        }
        
        )
      )
    )
    
    
  })
  
  
  output$stats_activa_table <- renderReactable({
    
    data <- RV$stats_model
    
    
    #data <- RV$stats_model
    
    reactable(data, defaultPageSize = nrow(data), onClick="expand",highlight=TRUE, 
              theme=reactableTheme(
                headerStyle = list(background="#2171B5",color="white")
              ))
    
  })
  
  
  
  output$stats_pasiva_table <- renderReactable({
    
    data <- RV$stats_model_Active 
    
    
    
    reactable(data, showPageSizeOptions = TRUE, onClick="expand",highlight=TRUE, 
              theme=reactableTheme(
                headerStyle = list(background="#2171B5",color="white")
              ))
    
  })
  
  #RV$all_data
  
  
  
  output$real_table <- renderReactable({
    
    data <- RV$all_data
    
    
    
    reactable(data, showPageSizeOptions = TRUE, onClick="expand",highlight=TRUE, 
              theme=reactableTheme(
                headerStyle = list(background="#2171B5",color="white")
              ))
    
  })
  
  ### Text Output####
  output$activa_real_date <- renderText({
    date_data <- max(df_real$FECHA[df_real$ACTIVA>0])
    
    
    paste0("Latest Data: ",format(date_data,'%d-%m-%Y'))
    
  })
  
  output$pasiva_real_date <- renderText({
    date_data <- max(df_real$FECHA[df_real$PASIVA>0])
    
    
    paste0("Latest Data: ",format(date_data,'%d-%m-%Y'))
    
  })
  
  
  
  

  
  
})