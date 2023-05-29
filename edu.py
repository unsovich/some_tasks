
class Strategy:
    def get_cost(self, lesson):
        raise NotImplemented("Method must be implementer in derived class")


class HoursStrategy(Strategy):
    def get_cost(self, lesson):
        return 100 + lesson.base_price

class FixedStrategy(Strategy):
    def get_cost(self, lesson):
        return 500 + lesson.base_price


class Lesson:
    _strat: Strategy = None
    base_price = 0

    def __init__(self, strat: Strategy):
        self._strat = strat

    def get_cost(self):
        return self._strat.get_cost(self)

class Lection(Lesson):
    def __init__(self, strat: Strategy):
        self.base_price = 111
        super().__init__(strat)

class Seminar(Lesson):
    def __init__(self, strat: Strategy):
        self.base_price = 222
        super().__init__(strat)


if __name__ == "__main__":
    st1 = HoursStrategy()
    st2 = FixedStrategy()

    lesson1 = Lection(st1)
    lesson2 = Seminar(st2)
    lesson3 = Lection(st2)
    lesson4 = Seminar(st1)

    print(lesson1.get_cost())
    print(lesson2.get_cost())
    print(lesson3.get_cost())
    print(lesson4.get_cost())