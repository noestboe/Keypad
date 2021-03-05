"""" Module for the defining the rules """

from kpc import KPC


def all_signals(signal):
    """ Check if """
    return True


def all_digits(signal):
    """ Check if it is digits """
    return 48 <= ord(signal) <= 57


RULES = [
    # Rules for login
    ('S-INIT', 'S-READ', all_signals, KPC.init_password),  # INIT
    ('S-READ', 'S-READ', all_digits, KPC.append_digit),  # ADD DIGIT
    ('S-READ', 'S-VERIFY', '*', KPC.verify_login),  # VERIFY PASSWORD
    ('S-READ', 'S-INIT', all_signals, KPC.reset_agent),  # GO BACK TO INIT IF IT GETS A SYMBOL
    ('S-VERIFY', 'S-ACTIVE', 'Y', KPC.activated),  # PASSWORD IS ACCEPTED
    ('S-VERIFY', 'S-INIT', all_signals, KPC.reset_agent),  # GO BACK TO INIT IF PASSWORD IS NOT ACCEPTED
    # Rules for
]

