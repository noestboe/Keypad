""" Module for the keypad controller """


class KPC:
    """ Class for the keypad controller. It will need following variables:
    A keypad instance,
    An LED Board instance,
    The complete pathname to the file holding the KPC 's password,
    the override_signal
    """

    def __init__(self):
        self.keypad = None
        self.led_board = None
        self.path = "password.txt"
        self.override_signal = None
        self.input_password = None
        self.actual_password = None
        self.cache = None

    def read_password_from_file(self):
        """ Gets the password that is stored in a file """
        file = open(self.path)
        data = file.readline().rstrip('\n')
        self.actual_password = data
        file.close()

    def get_next_signal(self):
        """ Return the override_signal, if it is non-blank; otherwise query the keypad
        for the next pressed key """

    def flash_leds(self):
        """ Call the LED Board and request the flashing of all LEDs """

    def twinkle_leds(self):
        """" Call the LED Board and request the twinkling of all LEDs """

    def exit_action(self):
        """ Call the LED Board to initiate the 'power down' lighting sequence """

    # Actions that will be performed depending on the state which
    # is determined by the FSM's rules

    # A1
    def reset_passcode_entry(self, *_):
        """ Clear the passcode-buffer and initiate a 'power up' lighting sequence on the LED
         Board. """
        self.input_password = ""

    # A2
    def append_digit(self, digit):
        """ will append the digit, ignores other parameters """
        self.input_password += digit

    # A3
    def verify_login(self, *_):
        """ Check that the password just entered via the keypad matches that in the password file.
        Store the result (Y or N) in the override_signal. Also, this should call the LED Board
        to initiate the appropriate lighting pattern for login success or failure. """
        password_is_equal = self.actual_password == self.input_password
        if password_is_equal:
            print('password verified')
            self.override_signal = 'Y'
        else:
            print('password is not verified')
            self.override_signal = 'N'
        self.input_password = ""
        return self.override_signal

    # A4
    def reset_agent(self, *_):
        """ Reset the password """
        print("you selected the wrong password")
        self.input_password = ""

    # A5
    def activated(self, *_):
        """ Let the user know that they are activated """
        print("activated")

    # A6
    def stop_new_password(self):
        """ This is called when a symbol is not a number in the new password """
        print('Stopping the password entry because it is not a number')
        self.input_password = ""

    # A7
    def cache_password(self):
        """ this is called when the user is done with the input of the password for the
        for the first time"""
        self.cache = self.input_password
        self.input_password = ""

    # A8
    def validate_passcode_change(self):
        """" Check that the new password is legal. If so, write the new password in the password file.
        A legal password should be at least 4 digits long and should contain no symbols other than the
        digits 0-9. As in verify_login, this should use the LED Board to signal success or failure in
        changing the password. """


    # Actions for the LED
    def select_led(self):
        """ Will select the led """

    def reset_duration(self):
        """ Rest the duration time """

    def append_duration_digit(self):
        """ Will append the duration digit to the time """

    def light_one_led(self):
        """" Using values stored in the Lid and Ldur slots, call the LED Board and request that LED
        # Lid be turned on for Ldur seconds """


def test_read():
    kpc = KPC()
    kpc.read_password_from_file()
    print(kpc.actual_password)


if __name__ == '__main__':
    test_read()
