""" Module for keypad """
from GPIOSimulator_v5 import *
GPIO = GPIOSimulator()

class Keypad:

    """ Class for the keypad """
    def __init__(self):
        self.rows = keypad_row_pins
        self.cols = keypad_col_pins
        self.key_symbols = {
            (self.rows[0], self.cols[0]): '1',
            (self.rows[0], self.cols[1]): '2',
            (self.rows[0], self.cols[2]): '3',
            (self.rows[1], self.cols[0]): '4',
            (self.rows[1], self.cols[1]): '5',
            (self.rows[1], self.cols[2]): '6',
            (self.rows[2], self.cols[0]): '7',
            (self.rows[2], self.cols[1]): '8',
            (self.rows[2], self.cols[2]): '9',
            (self.rows[3], self.cols[0]): '0',
            (self.rows[3], self.cols[1]): '*',
            (self.rows[3], self.cols[2]): '#'
        }


    def setup(self):
        """ initialize the row pins as outputs and the column pins as inputs """

        for rp in self.rows:
            GPIO.setup(rp, GPIO.OUT)
        for cp in self.cols:
            GPIO.setup(cp, GPIO.IN, state=GPIO.LOW)

    def do_polling(self):
        """ Use nested loops to determine the key currently being pressed on the keypad """

    def get_next_signal(self):
        """ This is the main interface between the agent and the keypad. It should initiate
        repeated calls to do_polling until a key press is detected """


if __name__ == '__main__':
    keypad = Keypad()

