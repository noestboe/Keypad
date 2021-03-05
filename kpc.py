""" Module for the keypad controller """


class KPC:
    """ Class for the keypad controller. It will need following variables:
    A keypad instance,
    An LED Board instance,
    The complete pathname to the file holding the KPC 's password,
    the override_signal
    """

    def reset_passcode_entry(self):
        """ Clear the passcode-buffer and initiate a 'power up' lighting sequence on the LED
         Board. """

    def get_next_signal(self):
        """ Return the override_signal, if it is non-blank; otherwise query the keypad
        for the next pressed key """


    def light_one_led(self):
        """" Using values stored in the Lid and Ldur slots, call the LED Board and request that LED
        # Lid be turned on for Ldur seconds """

    def flash_leds(self):
        """ Call the LED Board and request the flashing of all LEDs """

    def twinkle_leds(self):
        """" Call the LED Board and request the twinkling of all LEDs """

    def exit_action(self):
        """ Call the LED Board to initiate the 'power down' lighting sequence """


    # Actions that will be performed depending of the FSM's rules

    def init_password(self, *_):
        """ Will begin the new password """
        print("init password")

    def append_digit(self, *_):
        """ will append the digit, ignores other parameters """
        print("append digit")

    def verify_login(self, *_):
        """ Check that the password just entered via the keypad matches that in the password file.
        Store the result (Y or N) in the override_signal. Also, this should call the LED Board
        to initiate the appropriate lighting pattern for login success or failure. """
        print("verify login")

    def reset_agent(self, *_):
        """ Reset the password """
        print("reset agent")

    def activated(self, *_):
        """ Let the user know that they are activated """
        print("activated")

    def new_password(self):
        """ Initialize the new password """

    def cache_password(self):
        """ this is called when the user is done with the input of the password for the
        for the first time"""

    def stop_new_password(self):
        """ This is called when a symbol is not a number in the new password """

    def reset_password(self):
        """" This is called when """

    def validate_passcode_change(self):
        """" Check that the new password is legal. If so, write the new password in the password file.
        A legal password should be at least 4 digits long and should contain no symbols other than the
        digits 0-9. As in verify_login, this should use the LED Board to signal success or failure in
        changing the password. """

