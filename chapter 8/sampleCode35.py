@route()
    @BaseSubApp.add_ticker_selection_markup([])
    def main_screen(self):
        return """
<div class="page-header text-center">
  <h2>1. Data Exploration to test for Stationarity
    <button class="btn btn-default" pd_script="self.toggle_differencing()" pd_refresh>
    {%if this.differencing%}Remove differencing{%else%}Add differencing{%endif%}
    </button>
    <button class="btn btn-default" pd_options="do_forecast=true">
        Continue to Forecast
    </button>
  </h2>
</div>

<div class="row" style="min-height:300px">
  <div class="col-sm-10" id="chart{{prefix}}" pd_render_onload pd_options="show_chart=Adj. Close">
  </div>
</div>

<div class="row" style="min-height:300px">
    <div class="col-sm-6">
        <div class="page-header text-center">
            <h3>Auto-correlation Function</h3>
        </div>
        <div id="chart_acf{{prefix}}" pd_render_onload pd_options="show_acf=true">
        </div>
    </div>
    <div class="col-sm-6">
      <div class="page-header text-center">
         <h3>Partial Auto-correlation Function</h3>
      </div>
      <div id="chart_pacf{{prefix}}" pd_render_onload pd_options="show_pacf=true">
      </div>
    </div>
</div>
        """
