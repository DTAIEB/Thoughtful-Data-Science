[[BaseSubApp]]
def add_ticker_selection_markup(refresh_ids):
        def deco(fn):
            def wrap(self, *args, **kwargs):
                return """
<div class="row" style="text-align:center">
    <div class="btn-group btn-group-toggle" style="border-bottom:2px solid #eeeeee" data-toggle="buttons">
        {%for ticker, state in this.parent_pixieapp.tickers.items()%}
        <label class="btn btn-secondary {%if this.parent_pixieapp.active_ticker == ticker%}active{%endif%}"
            pd_refresh=\"""" + ",".join(refresh_ids) + """\" pd_script="self.set_active_ticker('{{ticker}}')">
            <input type="radio" {%if this.parent_pixieapp.active_ticker == ticker%}checked{%endif%}> 
                {{ticker}}
        </label>
        {%endfor%}
    </div>
</div>
                """ + fn(self, *args, **kwargs)
            return wrap
        return deco
    
    def set_active_ticker(self, ticker):
        self.parent_pixieapp.set_active_ticker(ticker)
