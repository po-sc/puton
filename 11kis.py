class MealyError(Exception):
    pass


class MealyStateMachine:
    def __init__(self):
        self.current_state = -1

    def stall(self):
        if self.current_state in [-1, 8]:
            self.current_state = 0
        elif self.current_state in [0, 6, 11]:
            self.current_state = 2
        elif self.current_state in [2, 4]:
            self.current_state = 3
        elif self.current_state in [1, 3]:
            self.current_state = 6
        elif self.current_state == 5:
            self.current_state = 7
        elif self.current_state == 7:
            self.current_state = 9
        elif self.current_state == 9:
            self.current_state = 10
        else:
            raise MealyError("stall")
        return self.current_state

    def visit(self):
        if self.current_state in [-1, 8]:
            self.current_state = 1
        elif self.current_state in [2, 4]:
            self.current_state = 4
        elif self.current_state in [1, 3]:
            self.current_state = 5
        elif self.current_state == 5:
            self.current_state = 8
        elif self.current_state == 10:
            self.current_state = 11
        else:
            raise MealyError("visit")
        return self.current_state


def main():
    return MealyStateMachine()


def raises(func, error):
    output = None
    try:
        output = func()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    o = main()
    assert o.visit() == 1
    assert o.stall() == 6
    assert o.stall() == 2
    assert o.stall() == 3
    assert o.visit() == 5
    assert o.stall() == 7
    assert o.stall() == 9
    assert o.stall() == 10
    assert o.visit() == 11
    assert o.stall() == 2
    assert o.visit() == 4
    assert o.visit() == 4
    assert o.stall() == 3
    assert o.visit() == 5
    assert o.visit() == 8
    assert o.stall() == 0
    o = main()
    assert o.visit() == 1
    assert o.visit() == 5
    assert o.stall() == 7
    assert o.stall() == 9
    assert o.stall() == 10
    raises(lambda: o.stall(), MealyError)
    assert o.visit() == 11
    assert o.stall() == 2
    assert o.stall() == 3
    assert o.visit() == 5
    assert o.visit() == 8
    assert o.stall() == 0
    assert o.stall() == 2
    assert o.visit() == 4
    assert o.stall() == 3
    assert o.stall() == 6
    o = main()
    assert o.visit() == 1
    assert o.visit() == 5
    assert o.visit() == 8
    assert o.visit() == 1
    assert o.stall() == 6
    raises(lambda: o.visit(), MealyError)


test()
