""" Module for the led board """
import time
from GPIOSimulator_v5 import *
GPIO = GPIOSimulator()


class Led_board:
    """ Class for the led board """

    def light_nth_led(self, n):
        """ Takes in argument n, lights up nth LED """

        if n == 0:
            GPIO.setup(PIN_CHARLIEPLEXING_0, GPIO.OUT)
            GPIO.setup(PIN_CHARLIEPLEXING_1, GPIO.OUT)
            GPIO.setup(PIN_CHARLIEPLEXING_2, GPIO.IN)

            GPIO.output(PIN_CHARLIEPLEXING_0, GPIO.HIGH)
            GPIO.output(PIN_CHARLIEPLEXING_1, GPIO.LOW)
        elif n == 1:
            GPIO.setup(PIN_CHARLIEPLEXING_0, GPIO.OUT)
            GPIO.setup(PIN_CHARLIEPLEXING_1, GPIO.OUT)
            GPIO.setup(PIN_CHARLIEPLEXING_2, GPIO.IN)

            GPIO.output(PIN_CHARLIEPLEXING_0, GPIO.LOW)
            GPIO.output(PIN_CHARLIEPLEXING_1, GPIO.HIGH)
        elif n == 2:
            GPIO.setup(PIN_CHARLIEPLEXING_0, GPIO.IN)
            GPIO.setup(PIN_CHARLIEPLEXING_1, GPIO.OUT)
            GPIO.setup(PIN_CHARLIEPLEXING_2, GPIO.OUT)

            GPIO.output(PIN_CHARLIEPLEXING_1, GPIO.HIGH)
            GPIO.output(PIN_CHARLIEPLEXING_2, GPIO.LOW)
        elif n == 3:
            GPIO.setup(PIN_CHARLIEPLEXING_0, GPIO.IN)
            GPIO.setup(PIN_CHARLIEPLEXING_1, GPIO.OUT)
            GPIO.setup(PIN_CHARLIEPLEXING_2, GPIO.OUT)

            GPIO.output(PIN_CHARLIEPLEXING_1, GPIO.LOW)
            GPIO.output(PIN_CHARLIEPLEXING_2, GPIO.HIGH)
        elif n == 4:
            GPIO.setup(PIN_CHARLIEPLEXING_0, GPIO.OUT)
            GPIO.setup(PIN_CHARLIEPLEXING_1, GPIO.IN)
            GPIO.setup(PIN_CHARLIEPLEXING_2, GPIO.OUT)

            GPIO.output(PIN_CHARLIEPLEXING_0, GPIO.HIGH)
            GPIO.output(PIN_CHARLIEPLEXING_2, GPIO.LOW)
        elif n == 5:
            GPIO.setup(PIN_CHARLIEPLEXING_0, GPIO.OUT)
            GPIO.setup(PIN_CHARLIEPLEXING_1, GPIO.IN)
            GPIO.setup(PIN_CHARLIEPLEXING_2, GPIO.OUT)

            GPIO.output(PIN_CHARLIEPLEXING_0, GPIO.LOW)
            GPIO.output(PIN_CHARLIEPLEXING_2, GPIO.HIGH)
        else:
            raise Exception
        GPIO.show_leds_states()

        self.reset_led()

    def reset_led(self):
        """ All led lights turn off """
        GPIO.setup(PIN_CHARLIEPLEXING_0, GPIO.OUT)
        GPIO.setup(PIN_CHARLIEPLEXING_1, GPIO.OUT)
        GPIO.setup(PIN_CHARLIEPLEXING_2, GPIO.IN)

        GPIO.output(PIN_CHARLIEPLEXING_0, GPIO.LOW)
        GPIO.output(PIN_CHARLIEPLEXING_1, GPIO.LOW)

        GPIO.setup(PIN_CHARLIEPLEXING_0, GPIO.IN)
        GPIO.setup(PIN_CHARLIEPLEXING_1, GPIO.OUT)
        GPIO.setup(PIN_CHARLIEPLEXING_2, GPIO.OUT)

        GPIO.output(PIN_CHARLIEPLEXING_1, GPIO.LOW)
        GPIO.output(PIN_CHARLIEPLEXING_2, GPIO.LOW)

        GPIO.setup(PIN_CHARLIEPLEXING_0, GPIO.OUT)
        GPIO.setup(PIN_CHARLIEPLEXING_1, GPIO.IN)
        GPIO.setup(PIN_CHARLIEPLEXING_2, GPIO.OUT)

        GPIO.output(PIN_CHARLIEPLEXING_0, GPIO.LOW)
        GPIO.output(PIN_CHARLIEPLEXING_2, GPIO.LOW)

    def light_led(self):
        """ Turn on one of the 6 LEDs by making the appropriate combination of input
        and output declarations, and then making the appropriate HIGH / LOW settings on the
        output pins"""
        GPIO.setup(PIN_CHARLIEPLEXING_0, GPIO.OUT)
        GPIO.setup(PIN_CHARLIEPLEXING_1, GPIO.OUT)
        GPIO.setup(PIN_CHARLIEPLEXING_2, GPIO.IN)
        GPIO.output(PIN_CHARLIEPLEXING_0, GPIO.HIGH)
        GPIO.output(PIN_CHARLIEPLEXING_1, GPIO.LOW)
        GPIO.show_leds_states()

    def flash_all_leds(self, k):
        """ Flash all 6 LEDs on and off for k seconds, where k is an argument of the method """

        start_time = time.time()

        while time.time() - start_time < k:

            # 0
            GPIO.setup(PIN_CHARLIEPLEXING_0, GPIO.OUT)
            GPIO.setup(PIN_CHARLIEPLEXING_1, GPIO.OUT)
            GPIO.setup(PIN_CHARLIEPLEXING_2, GPIO.IN)

            GPIO.output(PIN_CHARLIEPLEXING_0, GPIO.HIGH)
            GPIO.output(PIN_CHARLIEPLEXING_1, GPIO.LOW)

            # 1
            GPIO.setup(PIN_CHARLIEPLEXING_0, GPIO.OUT)
            GPIO.setup(PIN_CHARLIEPLEXING_1, GPIO.OUT)
            GPIO.setup(PIN_CHARLIEPLEXING_2, GPIO.IN)

            GPIO.output(PIN_CHARLIEPLEXING_0, GPIO.LOW)
            GPIO.output(PIN_CHARLIEPLEXING_1, GPIO.HIGH)

            # 2
            GPIO.setup(PIN_CHARLIEPLEXING_0, GPIO.IN)
            GPIO.setup(PIN_CHARLIEPLEXING_1, GPIO.OUT)
            GPIO.setup(PIN_CHARLIEPLEXING_2, GPIO.OUT)

            GPIO.output(PIN_CHARLIEPLEXING_1, GPIO.HIGH)
            GPIO.output(PIN_CHARLIEPLEXING_2, GPIO.LOW)

            # 3
            GPIO.setup(PIN_CHARLIEPLEXING_0, GPIO.IN)
            GPIO.setup(PIN_CHARLIEPLEXING_1, GPIO.OUT)
            GPIO.setup(PIN_CHARLIEPLEXING_2, GPIO.OUT)

            GPIO.output(PIN_CHARLIEPLEXING_1, GPIO.LOW)
            GPIO.output(PIN_CHARLIEPLEXING_2, GPIO.HIGH)

            # 4
            GPIO.setup(PIN_CHARLIEPLEXING_0, GPIO.OUT)
            GPIO.setup(PIN_CHARLIEPLEXING_1, GPIO.IN)
            GPIO.setup(PIN_CHARLIEPLEXING_2, GPIO.OUT)

            GPIO.output(PIN_CHARLIEPLEXING_0, GPIO.HIGH)
            GPIO.output(PIN_CHARLIEPLEXING_2, GPIO.LOW)

            # 5
            GPIO.setup(PIN_CHARLIEPLEXING_0, GPIO.OUT)
            GPIO.setup(PIN_CHARLIEPLEXING_1, GPIO.IN)
            GPIO.setup(PIN_CHARLIEPLEXING_2, GPIO.OUT)

            GPIO.output(PIN_CHARLIEPLEXING_0, GPIO.LOW)
            GPIO.output(PIN_CHARLIEPLEXING_2, GPIO.HIGH)

            GPIO.show_leds_states()

            self.reset_led()

    def twinkle_all_leds(self, k):
        """ Turn all LEDs on and off in sequence for k seconds, where k is an argument of
        the method """
        self.flash_all_leds(k)
        start_time = time.time()
        while time.time() - start_time < k:
            GPIO.show_leds_states()

    # Need methods for lighting patterns associated with powering up and down the system


if __name__ == '__main__':
    led_board = Led_board()
    led_board.twinkle_all_leds(1)
