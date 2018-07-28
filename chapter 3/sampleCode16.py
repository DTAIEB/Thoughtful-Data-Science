[[RepoAnalysis]]
@route(analyse_type="*")
@templateArgs
def do_analyse_type(self, analyse_type):
    fn = [analysis_fn for a_type,analysis_fn in analyses if a_type == analyse_type]
    if len(fn) == 0:
        return "No loader function found for {{analyse_type}}"
    vis_info = fn[0](self._analyse_repo_owner, self._analyse_repo_name)
    self.pdf = vis_info["pdf"]
    chart_options = {"handlerId":"dataframe"} if self.show_stats else vis_info["chart_options"]
    return """
    <div pd_entity="get_pdf()" pd_render_onload>
        <pd_options>{{chart_options | tojson}}</pd_options>
    </div>
    """
