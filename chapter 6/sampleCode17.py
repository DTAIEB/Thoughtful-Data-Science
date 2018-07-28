[[ScoreImageApp]]
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
        <div class="col-sm-3"></div>
        <div class="input-group col-sm-6">
          <input id="url{{prefix}}" type="text" class="form-control"
              value="https://www.flickr.com/search/?text=cats"
              placeholder="Enter a url that contains images">
          <span class="input-group-btn">
            <button class="btn btn-default" type="button" pd_options="image_url=$val(url{{prefix}})">Go</button>
          </span>
        </div>
    </div>
</div>        
"""
