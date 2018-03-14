from pixiedust.display.app import *
@PixieApp
class DisplayCars():
    @route()
    def main_screen(self):
        return """
        <div>
            <label>Column to search</label>
            <input id="column{{prefix}}" value="name">
            <label>Query</label>
            <input id="search{{prefix}}">
            <button type="submit" pd_options="col=$val(column{{prefix}});query=$val(search{{prefix}})"
                pd_target="target{{prefix}}">
                Search
            </button>
        </div>
        <div id="target{{prefix}}"></div>
        """
    @route(col="*", query="*")
    def display_screen(self, col, query):
        self.pdf = cars.loc[cars[col].str.contains(query)]
        return """
        <div pd_render_onload pd_entity="pdf">
            <pd_options>
            {
              "handlerId": "tableView",
              "table_noschema": "true",
              "table_nosearch": "true",
              "table_nocount": "true"
            }
            </pd_options>
        </div>
        """
app = DisplayCars()
app.run()
