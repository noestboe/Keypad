""" Module for finite state machine """
from inspect import isfunction
from kpc import KPC
from keypad import Keypad


class Rule:
    """ A rule will have the current state1, the next state state2, the signal and
    the action that will be performed when changing state """

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
        self.agent = KPC()
        self.signal = None

    def make_rules(self):
        # Rules to login
        self.add_rule(Rule('S-INIT', 'S-READ', all_signals, KPC.reset_passcode_entry))
        self.add_rule(Rule('S-READ', 'S-READ', all_digits, KPC.append_digit))
        self.add_rule(Rule('S-READ', 'S-VERIFY', '*', KPC.verify_login))
        self.add_rule(Rule('S-READ', 'S-INIT', all_signals, KPC.reset_agent))
        self.add_rule(Rule('S-VERIFY', 'S-ACTIVE', 'Y', KPC.activated))
        self.add_rule(Rule('S-VERIFY', 'S-INIT', all_signals, KPC.reset_agent))

        # Rules to change password
        self.add_rule(Rule(active, 'S-READ-2', '*', KPC.change_passcode_entry))
        self.add_rule(Rule('S-READ-2', 'S-READ-2', all_digits, KPC.append_digit))
        self.add_rule(Rule('S-READ-2', 'S-READ-3', '*', KPC.cache_password))
        self.add_rule(Rule('S-READ-2', 'S-ACTIVE', all_signals, KPC.stop_new_password))
        self.add_rule(Rule('S-READ-3', 'S-READ-3', all_digits, KPC.append_digit))
        self.add_rule(Rule('S-READ-3', 'S-ACTIVE', '*', KPC.validate_passcode_change))
        self.add_rule(Rule('S-READ-3', 'S-ACTIVE', all_signals, KPC.stop_new_password))

        # Rules to manipulate lights
        self.add_rule(Rule(active, 'S-LED', led_symbols, KPC.select_led))
        self.add_rule(Rule('S-LED', 'S-TIME', '*', KPC.reset_duration))
        self.add_rule(Rule('S-TIME', 'S-TIME', all_digits, KPC.append_duration_digit))
        self.add_rule(Rule('S-TIME', 'S-ACTIVE', '*', KPC.light_one_led))

        # Rules to logout
        self.add_rule(Rule('S-ACTIVE', 'S-ACTIVE-2', '#', KPC.begin_logout))
        self.add_rule(Rule('S-ACTIVE-2', 'S-FINISH', '#', KPC.confirm_logout))
        self.add_rule(Rule('S-FINISH', 'S-READ', all_signals, KPC.reset_passcode_entry))

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
            if not is_match:
                return
        else:
            is_match &= rule.signal == self.signal
            if not is_match:
                return

        if isfunction(rule.state1):
            is_match = rule.state1(self.state)
        else:
            is_match &= self.state == rule.state1
        return is_match

    def fire(self, rule):
        """ use the consequent of a rule to A) set the next state of the FSM, and B) call the
        appropriate agent action method. """
        self.state = rule.state2
        rule.action(self.agent, self.signal)

    def loop(self):

        self.make_rules()
        self.agent.keypad = Keypad()
        self.agent.keypad.setup()
        self.state = 'S-INIT'
        self.agent.read_password_from_file()

        while self.state is not None:
            try:
                self.get_next_signal()
                self.run()
            except KeyboardInterrupt:
                pass


def all_signals(*_):
    """ Check if it is a signal"""
    return True


def led_symbols(signal):
    return 48 <= ord(signal) < 48 + 5


def all_digits(signal):
    """ Check if it is digits """
    return 48 <= ord(signal) <= 57


def active(state):
    return state in ('S-ACTIVE', 'S-ACTIVE-2')


if __name__ == '__main__':
    fsm = FSM()
    fsm.loop()
