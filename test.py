""" Module for tests """
from fsm import FSM
from kpc import KPC


def test_run():
    fsm3 = FSM()
    fsm3.agent = KPC()
    fsm3.state = 'S-VERIFY'
    fsm3.signal = '3'
    fsm3.make_rules()
    fsm3.run()


def test_fire():
    fsm2 = FSM()
    fsm2.state = 'S-READ'
    fsm2.make_rules()
    a_rule = fsm2.rules[2]
    fsm2.agent = KPC()
    fsm2.fire(a_rule)


def test_match():
    fsm1 = FSM()
    fsm1.state = 'S-READ'
    fsm1.signal = '4'
    fsm1.make_rules()

    for j in fsm1.rules:
        print(fsm1.match(j))


if __name__ == '__main__':
    """ Testing method """
    # test_match()
    # test_fire()
    # test_run()
    # test change
