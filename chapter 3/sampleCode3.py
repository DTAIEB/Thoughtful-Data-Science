@route()
@templateArgs
def main_screen(self):
    var1 = self.compute_something()
    var2 = self.compute_something_else()
    return "<div>var1 is {{var1}}. var2 is {{var2}}</div>"
