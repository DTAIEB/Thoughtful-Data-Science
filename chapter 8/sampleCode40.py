@route(p_order="*",d_order="*",q_order="*")
def build_arima_model_screen(self, p_order, d_order, q_order):
    #Build the arima model
    self.train_set = self.parent_pixieapp.get_active_df()[:-14]
    self.test_set = self.parent_pixieapp.get_active_df()[-14:]
    self.arima_model = ARIMA(
        self.train_set['Adj. Close'], dates=self.train_set['Date'], 
        order=(int(p_order),int(d_order),int(q_order))
    ).fit(disp=0)
    self.residuals = self.arima_model.resid.describe().to_frame().reset_index()
    return """
<div class="page-header text-center">
    <h3>ARIMA Model succesfully created</h3>
<div>
<div class="row">
    <div class="col-sm-10 col-sm-offset-3">
        <div pd_render_onload pd_options="plot_predict=true">
        </div>
        <h3>Predicted values against the train set</h3>
    </div>
</div>
<div class="row">
    <div pd_render_onload pd_entity="residuals">
        <pd_options>
        {
          "handlerId": "tableView",
          "table_noschema": "true",
          "table_nosearch": "true",
          "table_nocount": "true"
        }
        </pd_options>
    </div>
    <h3><center>Residual errors statistics</center></h3> 
<div>
        """
