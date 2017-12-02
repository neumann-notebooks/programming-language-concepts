class Transition(object):
    """Transition docstring."""
    def __init__(self, target, condition):
        self.target = target
        self.condition = condition
    def get_state(self):
        return self.target
    def isValid(self, value):
        return self.condition(value)

class State(object):
    """State docstring."""
    def __init__(self, name):
        self.name = name
        self.transitions = []
    def add_transition(self, target, condition):
        self.transitions.append(Transition(target, condition))
    def decide(self, value):
        for t in self.transitions:
            if t.isValid(value):
                return t.get_state()
        return self
    def __str__(self):
        return self.name

class FSM(object):
    """FSM docstring."""
    def __init__(self):
        self.state = None
        self.states = {}
    def add_state(self, name):
        if name not in self.states:
            self.states[name] = State(name)
    def set_state(self, name):
        if name not in self.states:
            raise Exception("State does not exist: "+name)
        self.state = self.states[name]
    def add_rule(self, state, target, condition):
        self.add_state(state)
        self.add_state(target)
        self.states[state].add_transition(self.states[target], condition)
    def add_char_rule(self, state, target, char):
        self.add_rule(state, target, lambda c: c == char)
    def decide(self, value):
        self.state = self.state.decide(value)

fsm = FSM()
fsm.add_char_rule("unknown", "add_op", '+')
fsm.add_char_rule("unknown", "lt_op", '<')
fsm.add_char_rule("lt_op", "lte_op", '=')
fsm.set_state("unknown")
print("current state:",fsm.state)
fsm.decide('<')
print("current state:",fsm.state)
fsm.decide('=')
print("current state:",fsm.state)
