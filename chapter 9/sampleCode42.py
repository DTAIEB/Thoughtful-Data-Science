[[PredictDelayApp]] 
@route()
    def main_screen(self):
        return """
<div class="container-fluid">
    <div class="row">
        <div class="col-sm-6">
            <div class="rendererOpt" style="font-weight:bold">
                Select a flight segment:
            </div>
            <div>
                <select id="segment{{prefix}}" pd_refresh="prediction_graph{{prefix}}">
                    <option value="" selected></option>
                    {%for start, end in this.paths %}
                    <option value="{{start}}:{{end}}">{{start}} -> {{end}}</option>
                    {%endfor%}
                </select>
            </div>
        </div>
        <div class="col-sm-6">
            <div class="rendererOpt" style="font-weight:bold">
                Select an airline:
            </div>
            <div>
                <select id="airline{{prefix}}" pd_refresh="prediction_graph{{prefix}}">
                    <option value="" selected></option>
                    {%for airline_code, airline_name in this.airlines%}
                    <option value="{{airline_code}}">{{airline_name}}</option>
                    {%endfor%}
                </select>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-sm-12">
            <div id="prediction_graph{{prefix}}" 
                pd_options="flight_segment=$val(segment{{prefix}});airline=$val(airline{{prefix}})">
            </div>
        </div>
    </div>
</div>
        """
