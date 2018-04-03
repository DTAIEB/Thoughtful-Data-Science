from pixiedust.display.app import *
@PixieApp
class SimpleClassificationDNN():
    @route()
    def main_screen(self):
        return """
<h1 style="margin:40px">
    <center>The classificiation model will be trained on all the numeric columns of the dataset</center>
</h1>
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
          <select id="cols{{prefix}}" style="width:100%;height:30px" pd_options="predictor=$val(cols{{prefix}})">
              <option value="0">Select a predictor column</option>
              {%for col in this.pixieapp_entity.columns.values.tolist()%}
              <option value="{{col}}">{{col}}</option>
              {%endfor%}
          </select>
        </div>
    </div>
</div>     
        """
