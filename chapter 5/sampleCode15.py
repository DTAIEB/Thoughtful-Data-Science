from pixiedust.display.display import *
import pandas
@PixiedustDisplay()
class SimpleDisplayMeta(DisplayHandlerMeta):
    @addId
    def getMenuInfo(self,entity,dataHandler):
        if type(entity) is pandas.core.frame.DataFrame:
            return [
               {"categoryId": "Table", "title": "Simple Table", "icon": "fa-table", "id": "simpleTest"}
            ]
        return []
    def newDisplayHandler(self,options,entity):
        return SimpleDisplay(options,entity)
