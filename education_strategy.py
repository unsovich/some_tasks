class Strategy:
    def calculate_price(self):
        pass


class Fixed(Strategy):
    def calculate_price(self):
        total_cost = round(120 * 100 * 0.85)  # Стоимость курса с учетом скидки 15%
        return total_cost


class Hourly(Strategy):
    def calculate_price(self):
        total_cost = 120 * 100  # Стоимость курса (120 часов по 100 руб.)
        return total_cost


class Lesson:
    pass


class Lecture(Lesson):
    pass


class Seminar(Lesson):
    pass


fixed_strategy = Fixed()
hourly_strategy = Hourly()

fixed_price = fixed_strategy.calculate_price()
hourly_price = hourly_strategy.calculate_price()

print("Стоимость курса при фиксированной оплате:", fixed_price)
print("Стоимость курса при почасовой оплате:", hourly_price)
