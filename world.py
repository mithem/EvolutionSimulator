import math


class World:
    def __init__(self, name="MyWorld", initial_food=100):
        self.__name__ = name
        self.creatures = []
        self.food_count = initial_food
        self.initial_food = initial_food

    def act(self, iteration):
        self.update_food_count(iteration=iteration,
                               callback=self.fourth_grade_function)

    def update_food_count(self, callback, iteration):
        self.food_count = callback(iteration, self.initial_food)

    def linear_function(self, x, base):
        return x * base * 0.01

    def sqrt_function(self, x, base_not_needed=0):
        return math.sqrt(x) * 100

    def fraction(self, x, base_not_needed=0):
        return (1 / (x + 1)) * 10000

    def fourth_grade_function(self, x, base):
        return -0.0008 * (x**2) + 1000
