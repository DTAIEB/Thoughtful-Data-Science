[[USFlightsAnalysis]]
from pixiedust.display.app import *
from pixiedust.apps.mapboxBase import MapboxBase
from collections import OrderedDict

@PixieApp
class USFlightsAnalysis(MapboxBase):
    …
    @route()
    def main_screen(self):
        return """
<style>
    div.outer-wrapper {
        display: table;width:100%;height:300px;
    }
    div.inner-wrapper {
        display: table-cell;vertical-align: middle;height: 100%;width: 100%;
    }
</style>
<div class="outer-wrapper">
    <div class="inner-wrapper">
        <div class="col-sm-6">
            <div class="rendererOpt" style="font-weight:bold">
Select origin airport:
            </div>
            <div>
                <select id="origin_airport{{prefix}}" pd_refresh="origin_graph{{prefix}}">
                    <option value="" selected></option>
                    {%for code, airport in this.get_airports() %}
                    <option value="{{code}}">{{code}} - {{airport}}</option>
                    {%endfor%}
                </select>
            </div>
            <div id="origin_graph{{prefix}}" pd_options="visualize_graph=$val(origin_airport{{prefix}})"></div>
        </div>
        <div class="input-group col-sm-6">
            <div class="rendererOpt" style="font-weight:bold">
Select destination airport:
  </div>
            <div>
                <select id="destination_airport{{prefix}}" pd_refresh="destination_graph{{prefix}}">
                    <option value="" selected></option>
                    {%for code, airport in this.get_airports() %}
                    <option value="{{code}}">{{code}} - {{airport}}</option>
                    {%endfor%}
                </select>
            </div>
            <div id="destination_graph{{prefix}}" 
                pd_options="visualize_graph=$val(destination_airport{{prefix}})">
            </div>
        </div>
    </div>
</div>
<div style="text-align:center">
    <button class="btn btn-default" type="button" 
        pd_options="org_airport=$val(origin_airport{{prefix}});dest_airport=$val(destination_airport{{prefix}})">
        <pd_script type="preRun">
            if ($("#origin_airport{{prefix}}").val() == "" || $("#destination_airport{{prefix}}").val() == ""){
                alert("Please select an origin and destination airport");
                return false;
            }
            return true;
        </pd_script>
        Analyze
    </button>
</div>
"""

def get_airports(self):
   return [tuple(l) for l in airports_centrality[["IATA_CODE", "AIRPORT"]].values.tolist()]
