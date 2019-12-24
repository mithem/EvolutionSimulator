import random


class Creature:
    def __init__(self, name, replication_chance=0, death_chance=0, species="Creature", speed=1):
        self.__name__ = name
        self.__replication_chance__ = replication_chance
        self.__death_chance__ = death_chance
        self.__species__ = species
        self.__speed__ = speed
        self.reset_energy()

    def act(self):
        if random.random() <= self.__replication_chance__:
            return "spawn_new_" + self.__species__
        if random.random() <= self.__death_chance__:
            return "die"
        if random.random() * 10 <= self.__speed__:
            return "eat"
        self.__energy__ -= 1
        if self.__energy__ < 1:
            return "die"

    def reset_energy(self):
        self.__energy__ = 100


class Cat(Creature):
    def __init__(self, name=random.getrandbits(10), replication_chance=0.1, death_chance=0.09, speed=1):
        Creature.__init__(self, name=name, replication_chance=replication_chance,
                          death_chance=death_chance, species="cat", speed=speed)
