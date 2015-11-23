# ui.R
require("jsonlite")
require("RCurl")
require(ggplot2)
require(dplyr)
library(shiny)

navbarPage(
  title = "DV_SProject1",
  tabPanel(title= "Scatterplot",
           sidebarPanel(
             actionButton(inputId = "clicks1", label = "Click me")
           ),
           mainPanel(plotOutput("scatterplot"))
           ),
  tabPanel(title= "Barchart",
           sidebarPanel(
             actionButton(inputId="clicks2", label = "Click me")
           ),
           mainPanel(plotOutput("barchart"))
  ),
  tabPanel(title= "Crosstab",
           sidebarPanel(
             sliderInput("KPI1", "KPI_Low_Max_value:",
                         min = .1, max = .25, value = .25),
             sliderInput("KPI2", "KPI_Medium_Max_value:",
                         min = .25, max = 1, value = 1),
             
             actionButton(inputId="clicks3", label = "Click me")
           ),
           mainPanel(plotOutput("crosstab"))
           )
           )
#))
#fluidPage(
#  sliderInput(inputId = "num",
#              label="Choose a number",
#              value = 25, min = 1, max = 100),
#  plotOutput("scatterplot")
#)
