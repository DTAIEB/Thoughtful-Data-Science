[[StockExplorer]]
@route(explore="*")
@templateArgs
def stock_explore_screen(self):
    tabs = [("Explore","StockExploreSubApp"), ("Moving Average", "MovingAverageSubApp"),
            ("ACF and PACF", "AutoCorrelationSubApp")]
    return """
<style>    
    .btn:active, .btn.active {
        background-color:aliceblue;
    }
</style>
<div class="page-header">
  <h1>Stock Explorer PixieApp</h1>
</div>
<div class="container-fluid">
    <div class="row">
        <div class="btn-group-vertical btn-group-toggle col-sm-2" data-toggle="buttons">
            {%for title, subapp in tabs%}
            <label class="btn btn-secondary {%if loop.first%}active{%endif%}"
                pd_options="show_analytic={{subapp}}"
                pd_target="analytic_screen{{prefix}}">
                <input type="radio" {%if loop.first%}checked{%endif%}> 
                    {{title}}
            </label>
            {%endfor%}
        </div>
        <div id="analytic_screen{{prefix}}" class="col-sm-10">
        </div>
    </div>
"""
