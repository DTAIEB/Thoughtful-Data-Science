[[USFlightsAnalysis]]
@route(org_airport="*", dest_airport="*")
def analyze_route(self, org_airport, dest_airport):
    return """
<div pd_app="RouteAnalysisApp" 
    pd_options="org_airport={{org_airport}};dest_airport={{dest_airport}}" 
    pd_render_onload>
</div>
    """
