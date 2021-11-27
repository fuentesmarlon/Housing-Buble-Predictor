library(shiny)
library(shinydashboard)
library(shinyWidgets)
library(shinycssloaders)


shinyUI(
  dashboardPage(
    skin="green",
    dashboardHeader(
      #Title Name when Collapsed
      title = tagList(
        tags$span(
          class = "logo-mini", "HB"
        ),
        tags$span(
          class = "logo-lg", "GT Housing Bubble"
        )
      )
    ),
    dashboardSidebar(
      sidebarMenu(
        id="menu",
        menuItem("summary",tabName = "summary",icon=icon("book")),
        menuItem("Predictor",tabName="predictor",icon=icon("brain"))
      )
      
    ),
    dashboardBody(
      tabItems(
        tabItem(
          
          #### Summary ####
          tabName="summary",
          
          #Housing Title 
          fluidRow(
            column(
              width=12, 
              strong(h3("Predictor Summary"))
            )
          ),
          fluidRow(
           column(
             width=12, 
             dateRangeInput(
               "fecha_summary",
               label="Range",
               start=as.Date(max(df_joined$FECHA))-365,
               end=as.Date(max(df_joined$FECHA)),
               separator=' to ',
               format='dd-mm-yyyy',
               startview='month'
             )
             
           )
          ),
          
          # Chart
          fluidRow(
            column(
              width=12, 
              tabsetPanel(
                tabPanel(
                  "Trend",
                  fluidRow(
                    column(
                      width=12,
                      box(
                        width=12, 
                        status="primary", 
                        title="Forecast Tasa Activa",
                        collapsible = FALSE, 
                        solidHeader = TRUE, 
                        highchartOutput("activa_graph")
                      )
                      
                    )
                    
                  
                    
                  ),
                  fluidRow(
                    column(
                      width=12,
                      box(
                        width=12, 
                        status="primary", 
                        title="Forecast Tasa Pasiva",
                        collapsible = FALSE, 
                        solidHeader = TRUE, 
                        highchartOutput("pasiva_graph")
                      )
                      
                    )
                    
                    
                    
                  )
                  
                ),
                tabPanel(
                  "Data Detail",
                  fluidRow(
                    column(
                      width=12,
                      box(
                        width=12, 
                        status="primary", 
                        title="Forecast Tasa Activa",
                        collapsible = FALSE, 
                        solidHeader = TRUE, 
                        reactableOutput("activa_tabla")
                      )
                      
                    )
                    
                  ),
                  fluidRow(
                    
                    column(
                      width=12,
                      box(
                        width=12, 
                        status="primary", 
                        title="Forecast Tasa Activa",
                        collapsible = FALSE, 
                        solidHeader = TRUE, 
                        reactableOutput("pasiva_tabla")
                      )
                      
                    )
                    
                  )
                )
              )
            )
            
            
          )
        ),
        
        #### PREDICTOR ####
        tabItem(
          tabName = "predictor",
          fluidRow(
            column(
              width=12, 
              strong(h3("Forecast Stats"))
            )
          ),
          fluidRow(
            column(
              width=12, 
              box(
                width=12, 
                status="primary", 
                title="Model Summary",
                collapsible = FALSE, 
                solidHeader = TRUE, 
                #htmlOutput("test")
                h3("Modelo Tasa Activa"),
                strong(textOutput("activa_real_date")),
                withSpinner( reactableOutput("stats_activa_table")),
                h3("Modelo Tasa Pasiva"),
                strong(textOutput("pasiva_real_date")),
                withSpinner(reactableOutput("stats_pasiva_table"))
              )
            )
          ),
          fluidRow(
            column(
              width=12, 
              strong(h3("Forecast Tuner"))
            )
          ),
          fluidRow(
            column(
              width=12, 
              box(
                title="New Actual Data",
                status="primary",
                width=12, 
                solidHeader = TRUE, 
                
                fluidRow(
                  column(
                    width=12, 
                    actionButton("button_adder","Add New Data",icon=icon("file-upload"))
                  )
                ),
                fluidRow(
                  column(
                    width=12, 
                    br(),
                    reactableOutput("real_table")
                  )
                )
              )
            )
          )
        )
      ),
      tags$script(HTML("$('body').addClass('sidebar-mini');"))
    )
  )
)