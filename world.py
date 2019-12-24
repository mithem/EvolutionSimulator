import math


class World:
    def __init__(self, name="MyWorld", initial_food=100):
        self.__name__ = name
        self.creatures = {}
        self.food_count = initial_food
        self.initial_food = initial_food

    def act(self, iteration):
        self.update_food_count(iteration=iteration,
                               callback=self.f_base)

    def update_food_count(self, callback, iteration):
        self.food_count = callback(iteration, self.initial_food)

    def f_base(self, x_not_needed=0, base_not_needed=0):
        return self.initial_food

    def f_linear(self, x, base):
        return x * base * 0.01

    def f_sqrt(self, x, base_not_needed=0):
        return math.sqrt(x) * 100

    def f_fraction(self, x, base_not_needed=0):
        return (1 / (x + 1)) * 10000

    def f_negative_parabola(self, x, base):
        return -0.0008 * (x**2) + base

    def f_fourth_grade(self, x, base):
        return (x**4 - (x**2 * 10000)) / 100000
