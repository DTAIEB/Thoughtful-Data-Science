@route(predictor="*")
@templateArgs
def prepare_training(self, predictor):
        #select only numerical columns
        self.dataset = self.pixieapp_entity.dropna(axis=1).select_dtypes(
            include=['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        )
        #Compute the number of classed by counting the groups
        self.num_classes = self.dataset.groupby(predictor).size().shape[0]
        #Create the train and test feature and labels
        self.train_x=self.dataset.sample(frac=0.8)
        self.full_train = self.train_x.copy()
        self.train_y = self.train_x.pop(predictor)
        self.test_x=self.dataset.drop(self.train_x.index)
        self.full_test = self.test_x.copy()
        self.test_y=self.test_x.pop(predictor)
        
        bar_chart_options = {
          "rowCount": "100",
          "keyFields": predictor,
          "handlerId": "barChart",
          "noChartCache": "true"
        }
        
        return """
<div class="container" style="margin-top:20px">
    <div class="row">
        <div class="col-sm-5">
            <h3><center>Train set class distribution</center></h3>
            <div pd_entity="full_train" pd_render_onload>
                <pd_options>{{bar_chart_options|tojson}}</pd_options>
            </div>
        </div>
        <div class="col-sm-5">
            <h3><center>Test set class distribution</center></h3>
            <div pd_entity="full_test" pd_render_onload>
                <pd_options>{{bar_chart_options|tojson}}</pd_options>
            </div>
        </div>
    </div>
</div>

<div style="text-align:center">
    <button class="btn btn-default" type="submit" pd_options="do_training=true">
        Start Training
    </button>
</div>
"""
