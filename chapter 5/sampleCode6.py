@abstractmethod
def doGetNextData(self):
    """Return the next batch of data from the underlying stream. 
    Accepted return values are:
    1. (x,y): tuple of list/numpy arrays representing the x and y axis
    2. pandas dataframe
    3. y: list/numpy array representing the y axis. In this case, the x axis is automatically created
    4. pandas serie: similar to #3
    5. json
    6. geojson
    7. url with supported payload (json/geojson)
    """
    Pass
