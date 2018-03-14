@PixieApp
class RepoAnalysis():
    @route(analyse_repo_owner="*", analyse_repo_name="*")
    @templateArgs
    def do_analyse_repo(self, analyse_repo_owner, analyse_repo_name):
        self._analyse_repo_owner = analyse_repo_owner
        self._analyse_repo_name = analyse_repo_name
        return """
<div class="container-fluid">
    <div class="dropdown center-block col-sm-2">
      <button class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown">
          Select Repo Data Set
          <span class="caret"></span>
      </button>
      <ul class="dropdown-menu" style="list-style:none;margin:0px;padding:0px">
          {%for analysis,_ in this.analyses%}
            <li>
                <a href="#" pd_options="analyse_type={{analysis}}" pd_target="analyse_vis{{prefix}}"
                    style="text-decoration: none;background-color:transparent">
                    {{analysis}}
                </a>
            </li>
          {%endfor%}
      </ul>
    </div> 
    <div id="analyse_vis{{prefix}}" class="col-sm-10"></div>
</div>
"""
