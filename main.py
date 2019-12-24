from creatures import Creature, Cat, Mouse
from world import World
import random
import matplotlib.pyplot as plt

cat_config = {
    "speed": 1,
    "replication_chance": 0.1,
    "death_chance": 0.1
}
mouse_config = {
    "speed": 10,
    "replication_chance": 1,
    "death_chance": 0
}

MOUSE_LOSES_THRESHOLD = 0.01
MOUSE_EATING_REPLICATION_GAIN = 0.15
MOUSE_SPAWNS = 10
FOOD_COUNT = 60
INITIAL_CAT_COUNT = 50
INITIAL_MOUSE_COUNT = 1000
ITERATIONS = 3000


def create_creature(Creature: Creature, config):
    return Creature(name=config.get("name", "creature"), replication_chance=config.get("replication_chance", 0.1), death_chance=config.get("death_chance", 0.1))


w = World("Phantasialand", initial_food=FOOD_COUNT)
w.creatures["cats"] = []
w.creatures["mice"] = []

for i in range(1, INITIAL_CAT_COUNT + 1):
    w.creatures["cats"].append(create_creature(Cat, cat_config))
for i in range(1, INITIAL_MOUSE_COUNT + 1):
    w.creatures["mice"].append(create_creature(Mouse, mouse_config))

csv_lines = []
cats = []
mice = []
food_raw = []


try:
    for i in range(ITERATIONS + 1):
        for i in range(1, MOUSE_SPAWNS + 1):
            w.creatures["mice"].append(create_creature(Mouse, mouse_config))
        # if i >= 500 and i <= 700:
        #     w.food_count = FOOD_COUNT
        start_food_count = w.food_count
        for j in w.creatures["cats"]:
            action = j.act()
            if action == "spawn_new_cat":
                w.creatures["cats"].append(
                    create_creature(Cat, cat_config))
            if action == "die":
                w.creatures["cats"].pop(0)
            if action == "eat":
                if w.food_count > 0:
                    w.food_count -= 1
                    j.reset_energy()
                else:
                    try:
                        w.creatures["cats"].pop(0)
                    except IndexError:
                        pass
            if random.random() < MOUSE_LOSES_THRESHOLD:
                try:
                    w.creatures["mice"].pop(0)
                except IndexError:
                    pass
                j.reset_energy()
                j.__replication_chance__ += MOUSE_EATING_REPLICATION_GAIN
            else:
                j.__energy__ -= 10
        cats.append(len(w.creatures["cats"]))
        mice.append(len(w.creatures["mice"]))
        string = str(i) + ", " + \
            str(len(w.creatures["cats"])) + ", " + \
            str(len(w.creatures["mice"])) + ", " + str(start_food_count)
        print(string)
        csv_lines.append(string + "\n")
        w.act(i)
        food_raw.append(start_food_count)
except KeyboardInterrupt:
    pass
finally:
    f = open("creature_data.csv", "w")
    f.write("t, n\n")
    f.writelines(csv_lines)
    f.close()

    plt.ioff()
    plt.plot(cats, label="cats")
    plt.plot(mice, label="mice")
    plt.plot(food_raw, label="food")
    plt.title("EvolutionSimulator")
    plt.xlabel("iterations")
    plt.ylabel("n")
    plt.legend()
    plt.show()
