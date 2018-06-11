[[AirlinesApp]]
 @route()
    def main_screen(self):
        return """
<div class="container-fluid">
    {%for airline_code, airline_name in this.airlines%}
    <div class="row" style="max-e">
        <h1 style="color:red">{{airline_name}}</h1>
        <div class="col-sm-6">
            <div pd_render_onload pd_options="delay_org_airport=true;airline_code={{airline_code}};airline_name={{airline_name}}"></div>
        </div>
        <div class="col-sm-6">
            <div pd_render_onload pd_options="delay_org_airport=false;airline_code={{airline_code}};airline_name={{airline_name}}"></div>
        </div>
    </div>
    {%endfor%}
</div>
        """
