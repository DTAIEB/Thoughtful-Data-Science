[[USFlightsAnalysis]]
@route(org_airport="*", dest_airport="*")
def compute_path_screen(self, org_airport, dest_airport):
    return """
<div class="container-fluid">
    <div class="form-group col-sm-2" style="padding-right:10px;">
        <div><strong>Centrality Indices</strong></div>
        {% for centrality in this.centrality_indices.keys() %}
        <div class="rendererOpt checkbox checkbox-primary">
            <input type="checkbox" pd_refresh="flight_map{{prefix}}" 
                pd_script="self.compute_toggle_centrality_layer('{{org_airport}}', '{{dest_airport}}', '{{centrality}}')">
            <label>{{centrality}}</label>
        </div>      
        {%endfor%}
    </div>
    <div class="form-group col-sm-10">
        <h1 class="rendererOpt">Select a centrality index to show the shortest flight path
        </h1>
        <div id="flight_map{{prefix}}" pd_entity="self.airports_centrality" pd_render_onload>
            <pd_options>
            {
              "keyFields": "LATITUDE,LONGITUDE",
              "valueFields": "AIRPORT,DEGREE,PAGE_RANK,ELAPSED_TIME,CLOSENESS",
              "custombasecolorsecondary": "#fffb00",
              "colorrampname": "Light to Dark Red",
              "handlerId": "mapView",
              "quantiles": "0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0",
              "kind": "choropleth",
              "rowCount": "1000",
              "numbins": "5",
              "mapboxtoken": "pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4M29iazA2Z2gycXA4N2pmbDZmangifQ.-g_vE53SD2WrJ6tFX7QHmA",
              "custombasecolor": "#ffffff"
            }
            </pd_options>
        </div>
    </div>
</div>
"""
