[[AirlinesApp]]
 @route(delay_org_airport="*",airline_code="*", airline_name="*")
    @templateArgs
    def delay_airline_screen(self, delay_org_airport, airline_code, airline_name):
        mask = (flights["AIRLINE"] == airline_code)
        if delay_org_airport == "true":
            mask = mask & (flights["ORIGIN_AIRPORT"] == self.org_airport)
        average_delay = round(flights[mask]["ARRIVAL_DELAY"].mean(), 2)
        return """
{%if delay_org_airport == "true" %}
<h4>Delay chart for all flights out of {{this.org_airport}}</h4>
{%else%}
<h4>Delay chart for all flights</h4>
{%endif%}
<h4 style="margin-top:5px">Average delay: {{average_delay}} minutes</h4>
<div pd_render_onload pd_entity="compute_delay_airline_df('{{airline_code}}', '{{delay_org_airport}}')">
    <pd_options>
    {
      "keyFields": "DATE",
      "handlerId": "lineChart",
      "valueFields": "ARRIVAL_DELAY",
      "noChartCache": "true"
    }
    </pd_options>
</div>
        """
