[[USFlightsAnalysis]]
def setup(self):
   self.centrality_indices = OrderedDict([
      ("ELAPSED_TIME","rgba(256,0,0,0.65)"), 
      ("DEGREE", "rgba(0,256,0,0.65)"), 
      ("PAGE_RANK", "rgba(0,0,256,0.65)"),
      ("CLOSENESS", "rgba(128,0,128,0.65)")
  ])
