
# server.R

library(shiny)

function(input, output) {
  output$hist <- renderPlot({
    hist(rnorm(input$num))
  })
}
