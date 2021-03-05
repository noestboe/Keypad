""" Module for finite state machine """
from inspect import isfunction
from kpc import KPC


class Rule:
    def __init__(self, state1, state2, signal, action):
        self.state1 = state1
        self.state2 = state2
        self.signal = signal
        self.action = action


class FSM:
    """" Class for the FSM """
    def __init__(self):
        self.rules = []
        self.state = None
        self.agent = None
        self.signal = None

    def make_rules(self):
        # Rules to login
        self.add_rule(Rule('S-INIT', 'S-READ', all_signals, KPC.init_password))
        self.add_rule(Rule('S-READ', 'S-READ', all_digits, KPC.append_digit))
        self.add_rule(Rule('S-READ', 'S-VERIFY', '*', KPC.verify_login))
        self.add_rule(Rule('S-READ', 'S-INIT', all_signals, KPC.reset_agent))
        self.add_rule(Rule('S-VERIFY', 'S-ACTIVE', 'Y', KPC.activated))
        self.add_rule(Rule('S-VERIFY', 'S-INIT', all_signals, KPC.reset_agent))

    def add_rule(self, rule):
        """ Add new rules to the end of the FSM 's rule list """
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
        if isfunction(rule.signal):
            is_match &= rule.signal(self.signal)
        else:
            is_match &= rule.signal == self.signal

        is_match &= self.state == rule.state1
        return is_match

    def fire(self, rule):
        """ use the consequent of a rule to A) set the next state of the FSM, and B) call the
        appropriate agent action method. """
        self.state = rule.state2
        rule.action(self.agent, self.signal)

    def loop(self):

        self.make_rules()

        self.agent = KPC()
        self.state = 'S-INIT'

        while self.state is not None:
            try:
                self.get_next_signal()
                self.run()
            except KeyboardInterrupt:
                pass


def all_signals(signal):
    """ Check if it si a signal"""
    return True


def all_digits(signal):
    """ Check if it is digits """
    return 48 <= ord(signal) <= 57
