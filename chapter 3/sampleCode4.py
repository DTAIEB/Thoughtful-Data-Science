from pixiedust.display.app import *

@PixieApp
class GitHubTracking():
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
          <input id="query{{prefix}}" type="text" class="form-control" placeholder="Search projects on GitHub">
          <span class="input-group-btn">
            <button class="btn btn-default" type="button">Submit Query</button>
          </span>
        </div>
    </div>
</div>   
"""
    
app = GitHubTracking()
app.run()
