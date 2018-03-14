def newDisplayHandler(self, options, entity):
    if self.streamingDisplay is None:
        self.streamingDisplay = LineChartStreamingDisplay(options, entity)
    else:
        self.streamingDisplay.options = options
    return self.streamingDisplay
