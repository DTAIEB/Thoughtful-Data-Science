@PixieApp
class GitHubTracking(RepoAnalysis):
    @route()
    def main_screen(self):
        <<Code omitted here>>

    @route(query="*")
    @templateArgs
    def do_search(self, query):
        <<Code omitted here>>

    @route(page="*")
    @templateArgs
    def do_retrieve_page(self, page):
        <<Code omitted here>>

app = GitHubTracking()
app.run()
