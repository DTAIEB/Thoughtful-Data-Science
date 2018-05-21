@route(do_forecast="true")
    @BaseSubApp.add_ticker_selection_markup([])
    def do_forecast_screen(self):
        return """
<div class="page-header text-center">
    <h2>2. Build Arima model
        <button class="btn btn-default" pd_options="do_diagnose=true">
            Diagnose Model
        </button>
    </h2>
</div>
<div class="row" id="forecast{{prefix}}">
    <div style="font-weight:bold">Enter the p,d,q order for the ARIMA model you want to build</div>

    <div class="form-group" style="margin-left: 20px">
        <label class="control-label">Enter the p order for the AR model:</label>
        <input type="text" class="form-control" id="p_order{{prefix}}" value="1" style="width: 100px;margin-left:10px">

        <label class="control-label">Enter the d order for the Integrated step:</label>
        <input type="text" class="form-control" id="d_order{{prefix}}" value="1" style="width: 100px;margin-left:10px">

        <label class="control-label">Enter the q order for the MA model:</label>
        <input type="text" class="form-control" id="q_order{{prefix}}" value="1" style="width: 100px;margin-left:10px">
    </div>

    <center>
        <button class="btn btn-default" pd_target="forecast{{prefix}}"
            pd_options="p_order=$val(p_order{{prefix}});d_order=$val(p_order{{prefix}});q_order=$val(p_order{{prefix}})">
        Go
        </button>
    </center>
</div>
"""
