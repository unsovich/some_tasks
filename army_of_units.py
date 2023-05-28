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
        self.damage = damage

    def make_damage(self):  # сила урона
        return self.damage


class Army:
    def __init__(self):
        self.units = []  # список юнитов

    def add_unit(self, unit):
        self.units.append(unit)  # добавление юнитов в армию

    def make_damage(self):
        total_damage = sum(unit.make_damage() for unit in self.units)  # суммирует урон юнита
        return total_damage


archer = Unit(1)
cannon = Unit(5)

army1 = Army()
army1.add_unit(archer)
army1.add_unit(cannon)

army2 = Army()
army2.add_unit(archer)
army2.add_unit(cannon)

army3 = Army()
army3.add_unit(archer)
army3.add_unit(cannon)


def maximum_damage(armies):  # суммарный урон от армии
    max_dmg = 0
    for army in armies:
        max_dmg += army.make_damage()
    return max_dmg


armies = [army1, army2, army3]
max_damage = maximum_damage(armies)
print("Максимальный урон от армий:", max_damage)
