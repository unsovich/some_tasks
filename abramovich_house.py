from abc import ABC, abstractmethod


# Абстрактный базовый класс для компонентов дома
class HouseComponent(ABC):
    @abstractmethod
    def prepare(self):
        pass


class Guest(HouseComponent):
    def __init__(self):
        self.kitchen = None

    def set_kitchen(self, kitchen):
        self.kitchen = kitchen

    def prepare(self):
        print("Guest choose of kitchen...")
        if self.kitchen:
            self.kitchen.prepare()


class Kitchen(HouseComponent):
    def __init__(self, chef, equipment):
        self.chef = chef
        self.equipment = equipment

    def prepare(self):
        print("Preparing the kitchen...")
        self.chef.prepare()
        self.equipment.prepare()


class Chef(HouseComponent):
    def prepare(self):
        print("Preparing the chef...")


class Equipment(HouseComponent):
    def prepare(self):
        print("Preparing the equipment...")


class Dish(HouseComponent):
    def __init__(self, name, kitchen):
        self.name = name
        self.kitchen = kitchen
        self.additional_dish = None

    def add_additional_dish(self, additional_dish):
        self.additional_dish = additional_dish

    def prepare(self):
        print(f"Preparing dish: {self.name} from {self.kitchen} kitchen...")
        if self.additional_dish:
            self.additional_dish.prepare()


class Menu(HouseComponent):
    def __init__(self, name):
        self.name = name
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def prepare(self):
        print(f"Preparing menu: {self.name}")
        for dish in self.dishes:
            dish.prepare()


italian_kitchen = Kitchen(chef=Chef(), equipment=Equipment())
mexican_kitchen = Kitchen(chef=Chef(), equipment=Equipment())

Guest = Guest()
Guest.set_kitchen(italian_kitchen)

menu = Menu("Guest Menu")

pizza = Dish("Pizza", "Italian")
additional_dish = Dish("Additional Dish", "Italian")
pizza.add_additional_dish(additional_dish)

menu.add_dish(pizza)

Guest.prepare()
menu.prepare()
