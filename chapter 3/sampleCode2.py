@route(state1="*", state2="*")
def my_method(self, state1, state2):
    return "<div>State1 is {{state1}}. State2 is {{state2}}</div>"
