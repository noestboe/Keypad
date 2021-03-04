""" Module for keypad """


class Keypad:
    """ Class for the keypad """

    def setup(self):
        """ initialize the row pins as outputs and the column pins as inputs """

    def do_polling(self):
        """ Use nested loops to determine the key currently being pressed on the keypad """

    def get_next_signal(self):
        """ This is the main interface between the agent and the keypad. It should initiate
        repeated calls to do_polling until a key press is detected """