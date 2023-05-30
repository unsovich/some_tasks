class Component:
    def __init__(self, name):
        self.name = name

    def display(self):
        raise NotImplementedError()


class Home(Component):
    def __init__(self, name):
        super().__init__(name)
        self.guest = None
        self.kitchen = None

    def display(self):
        print(f"Home: {self.name}")


class Guest(Component):
    def __init__(self, name):
        super().__init__(name)
        self.kitchen = None
        self.main_dish = None
        self.additional_dish = None

    def display(self):
        print(f"Guest: {self.name}")

    def choose_main_dish(self, dish):
        self.main_dish = dish

    def choose_additional_dish(self, dish):
        self.additional_dish = dish


class Kitchen(Component):
    def __init__(self, name, cuisine):
        super().__init__(name)
        self.cuisine = cuisine

    def display(self):
        print(f"Kitchen: {self.name}")


class Cuisine(Component):
    def __init__(self, name):
        super().__init__(name)
        self.chef = None
        self.equipment = None

    def display(self):
        print(f"Cuisine: {self.name}")


class ItalianCuisine(Cuisine):
    def __init__(self):
        super().__init__("Italian")
        self.chef = Chef("Italian Chef")
        self.equipment = Equipment("Italian Equipment")

    def prepare_dish(self, guest):
        print(f"Italian Cuisine is preparing main dish: {guest.main_dish}")
        if guest.additional_dish:
            print(f"Italian Cuisine is preparing additional dish: {guest.additional_dish}")


class MexicanCuisine(Cuisine):
    def __init__(self):
        super().__init__("Mexican")
        self.chef = Chef("Mexican Chef")
        self.equipment = Equipment("Mexican Equipment")

    def prepare_dish(self, guest):
        print(f"Mexican Cuisine is preparing main dish: {guest.main_dish}")
        if guest.additional_dish:
            print(f"Mexican Cuisine is preparing additional dish: {guest.additional_dish}")


class Chef(Component):
    def __init__(self, name):
        super().__init__(name)

    def display(self):
        print(f"Chef: {self.name}")


class Equipment(Component):
    def __init__(self, name):
        super().__init__(name)

    def display(self):
        print(f"Equipment: {self.name}")


home = Home("My Home")
guest = Guest("John")
kitchen = Kitchen("Kitchen", None)
italian_cuisine = ItalianCuisine()
mexican_cuisine = MexicanCuisine()

home.guest = guest
home.kitchen = kitchen
guest.kitchen = kitchen
kitchen.cuisine = italian_cuisine

guest.choose_main_dish("Pizza")
guest.choose_additional_dish("Garlic Bread")

# Приготовление блюд
kitchen.cuisine.prepare_dish(guest)

# Вывод информации
home.display()
guest.display()
kitchen.display()
kitchen.cuisine.display()
kitchen.cuisine.chef.display()
kitchen.cuisine.equipment.display()
