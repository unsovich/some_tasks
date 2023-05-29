"""
Юнит:
— лучник - урон 1
— пушка - урон 5

Каждый юнит может сделать
def perform_damage()
   return 1 (для лучника)
   return 5 (для пушки)

Мы хотим сделать класс Армия
— сумма своих частей (юнитов)
— армия ведет себя как один юнит (наследуется или реализует интерфейс юнит)
— армия может состоять из армий

def perform_damage()
   считает суммарный урон и его возвращает
   return суммарный_урон
"""


class Unit:
    def __init__(self, damage):  # атрибут урон
        self._damage = damage

    def make_damage(self):  # сила урона
        return self._damage


class Archer(Unit):
    def __init__(self):
        super().__init__(damage=1)


class Cannon(Unit):
    def __init__(self):
        super().__init__(damage=5)


class Army(Unit):
    def __init__(self):
        self._units = []  # список юнитов
        super().__init__(damage=0)

    def add_unit(self, unit: Unit):
        self._units.append(unit)  # добавление юнитов в армию

    def remove_unit(self, unit: Unit):
        self._units = [u for u in self._units if u != unit]

    def print_units(self):
        for u in self._units:
            print(f"{u.__class__.__name__} makes {u.make_damage()} damage")

    def make_damage(self):
        total_damage = sum(unit.make_damage() for unit in self._units)  # суммирует урон юнита
        return total_damage

if __name__ == "__main__":
    archer = Archer()
    cannon = Cannon()
    other = Unit(damage=100)


    army1 = Army()
    army1.add_unit(archer)
    army1.add_unit(cannon)
    army1.add_unit(other)
    print("===============")
    print(f"Army1 damage={army1.make_damage()}")
    army1.print_units()

    army2 = Army()
    army2.add_unit(archer)
    army2.add_unit(cannon)
    army2.add_unit(army1)
    print("===============")
    print(f"Army2 damage={army2.make_damage()}")
    army2.print_units()


