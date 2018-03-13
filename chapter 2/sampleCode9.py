#import the pixieapp decorators
from pixiedust.display.app import *

#Load the cars dataframe into the Notebook
cars = pixiedust.sampleData(1)

@PixieApp   #decorator for making the class a PixieApp
class HelloWorldApp():
    @route()  #decorator for making a method a route (no arguments means default route)
    def main_screen(self):
        return """
        <button type="submit" pd_options="show_chart=true" pd_target="chart">Show Chart</button> 
        <!--Placeholder div to display the chart-->
        <div id="chart"></div>
        """
    
    @route(show_chart="true")
    def chart(self):
        #Return a div bound to the cars dataframe using the pd_entity attribute
        #pd_entity can refer a class variable or a global variable scoped to the notebook
        return """
        <div pd_render_onload pd_entity="cars">
            <pd_options>
                {
                  "title": "Average Mileage by Horsepower",
                  "aggregation": "AVG",
                  "clusterby": "origin",
                  "handlerId": "barChart",
                  "valueFields": "mpg",
                  "rendererId": "bokeh",
                  "keyFields": "horsepower"
                }
            </pd_options>
        </div>
        """

#Instantiate the application and run it
app = HelloWorldApp()
app.run()
