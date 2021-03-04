""" Module for finite state machine """


class FSM:
    """" Class for the FSM """

    def add_rule(self):
        """ Add a new rule to the end of the FSM 's rule list """

    def get_next_signal(self):
        """" Query the agent for the next signal """

    def run(self):
        """ Begin in the FSM 's default initial state and then repeatedly call get_next_signal and
        run the rules on by one until reaching the final state"""

    def match(self):
        """ Check whether the rule condition is fulfilled """

    def fire(self):
        """ use the consequent of a rule to A) set the next state of the FSM, and B) call the
        appropriate agent action method. """