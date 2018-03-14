@route(topic="*",streampreview="*",schemaX="*")
    def showChart(self, schemaX):
        self.schemaX = schemaX
        self.avgChannelData = self.streamingData.getStreamingChannel(self.computeAverages)
        return """
<div class="well" style="text-align:center">
    <div style="font-size:x-large">Real-time chart for {{this.schemaX}}(average).</div>
</div>
…
<div pd_refresh_rate="1000" pd_entity="avgChannelData"></div>
        """
