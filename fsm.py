""" Module for finite state machine """
from inspect import isfunction
from rules import RULES
from kpc import KPC


class FSM:
    """" Class for the FSM """
    def __init__(self):
        self.rules = []
        self.state = None
        self.agent = None
        self.signal = None

    def add_rule(self, rule):
        """ Add a new rule to the end of the FSM 's rule list """
        self.rules.append(rule)

    def get_next_signal(self):
        """" Query the agent for the next signal """
        self.signal = self.agent.get_next_signal()

    def run(self):
        """ Begin in the FSM 's default initial state and then repeatedly call get_next_signal and
        run the rules on by one until reaching the final state"""
        for rule in self.rules:
            if self.match(rule):
                self.fire(rule)
                return
        self.state = None

    def match(self, rule):
        """ Check whether the rule condition is fulfilled """
        is_match = True
        rule_signal = rule[2]
        if isfunction(rule_signal):
            is_match &= rule_signal(self.signal)
        else:
            is_match &= rule_signal == self.signal

        rule_state = rule[0]
        is_match &= self.state == rule_state
        return is_match

    def fire(self, rule):
        """ use the consequent of a rule to A) set the next state of the FSM, and B) call the
        appropriate agent action method. """
        self.state = rule[1]
        rule_action = rule[3]
        rule_action(self.agent, self.signal)


    def loop(self):

        for rule in RULES:
            self.add_rule(rule)

        self.agent = KPC()
        self.state = 'S-INIT'

        while self.state is not None:
            try:
                self.get_next_signal()
                self.run()
            except KeyboardInterrupt:
                pass


def test_match():
    fsm1 = FSM()
    fsm1.state = 'S-READ'
    fsm1.signal = '4'
    for k in RULES:
        fsm1.add_rule(k)

    for j in fsm1.rules:
        print(fsm1.match(j))


if __name__ == '__main__':
    test_match()
