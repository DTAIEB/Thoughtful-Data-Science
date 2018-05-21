    def compute_test_set_predictions(self):
        return compute_test_set_predictions(self.train_set, self.test_set)

    @route(do_diagnose="true")
    @BaseSubApp.add_ticker_selection_markup([])
    def do_diagnose_screen(self):
        return """
<div class="page-header text-center"><h2>3. Diagnose the model against the test set</h2></div>
<div class="row">
    <div class="col-sm-10 center" pd_render_onload pd_entity="compute_test_set_predictions()">
        <pd_options>
        {
          "keyFields": "Date",
          "valueFields": "forecast,test",
          "handlerId": "lineChart",
          "rendererId": "bokeh",
          "noChartCache": "true"          
        }
        </pd_options>
    </div>
</div>
"""
