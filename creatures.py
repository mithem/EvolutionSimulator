import random


class Creature:
    def __init__(self, name, replication_chance=0, death_chance=0, species="Creature"):
        self.__name__ = name
        self.__replication_chance__ = replication_chance
        self.__death_chance__ = death_chance
        self.__species__ = species

    def act(self):
        if random.random() <= self.__replication_chance__:
            return "spawn_new_" + self.__species__
        if random.random() <= self.__death_chance__:
            return "die"


class Cat(Creature):
    def __init__(self, name=random.getrandbits(10), replication_chance=0.1, death_chance=0.1):
        Creature.__init__(self, name=name, replication_chance=replication_chance,
                          death_chance=death_chance, species="cat")
