""" Module for keypad """
import time
from GPIOSimulator_v5 import *
GPIO = GPIOSimulator()

class Keypad:
    """ Class for the keypad """

    def setup(self):
        """ initialize the row pins as outputs and the column pins as inputs """
        GPIO.setup(PIN_KEYPAD_ROW_0, GPIO.OUT)
        GPIO.setup(PIN_KEYPAD_ROW_1, GPIO.OUT)
        GPIO.setup(PIN_KEYPAD_ROW_2, GPIO.OUT)
        GPIO.setup(PIN_KEYPAD_ROW_3, GPIO.OUT)

        GPIO.setup(PIN_KEYPAD_COL_0, GPIO.IN, state=GPIO.LOW)
        GPIO.setup(PIN_KEYPAD_COL_1, GPIO.IN, state=GPIO.LOW)
        GPIO.setup(PIN_KEYPAD_COL_2, GPIO.IN, state=GPIO.LOW)

    def do_polling(self):
        """ Use nested loops to determine the key currently being pressed on the keypad """
        start_time = time.time()

        # If keypad is pressed, these values represent the row and column of the key
        pressed_key_row = None
        pressed_key_col = None

        # Iterate through every row to see if a key has been pressed
        for row in range(4):
            GPIO.output(keypad_row_pins[row], GPIO.HIGH)

            # Iterate through every column to see if a key has been pressed
            for column in range(3):
                if GPIO.input(keypad_col_pins[column]) == GPIO.HIGH:

                    # A loop is created to measure the amount of time the key is pressed
                    while GPIO.input(keypad_col_pins[column]) == GPIO.HIGH:
                        continue
                    # A key has been pressed
                    # What row and column is set
                    pressed_key_row = keypad_row_pins[row]
                    pressed_key_col = keypad_col_pins[column]

            GPIO.output(keypad_row_pins[row], GPIO.LOW)

        duration = time.time() - start_time

        return pressed_key_row, pressed_key_col, duration

    def get_next_signal(self):
        """ This is the main interface between the agent and the keypad. It should initiate
        repeated calls to do_polling until a key press is detected """

        while True:
            # If do_polling returns values, this means a key has been pressed
            # This breaks the loop
            signal = self.do_polling()

            # Key has to be pushed for longer than 0.5 seconds
            if None not in signal and signal[2] > 0.5:
                print(signal)
                return signal
            time.sleep(0.2)


if __name__ == '__main__':
    # Tests keypad by getting next signal
    keypad = Keypad()
    keypad.setup()
    keypad.get_next_signal()
