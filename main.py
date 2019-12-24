from creatures import Cat
from world import World
import random
import matplotlib.pyplot as plt

SPEED = 1
REPLICATION_CHANCE = 0.1
DEATH_CHANCE = 0.1
FOOD_COUNT = 100
INITIAL_CAT_COUNT = 5000
ITERATIONS = 1500

w = World("Phantasialand", initial_food=FOOD_COUNT)
for i in range(1, INITIAL_CAT_COUNT):
    w.creatures.append(
        Cat("cat" + str(i), REPLICATION_CHANCE, DEATH_CHANCE, speed=SPEED))

statue = []
csv_lines = []
raw = []
food_raw = []

for i in range(ITERATIONS):
    for j in w.creatures:
        action = j.act()
        if action == "spawn_new_cat":
            w.creatures.append(
                Cat(name="cat", replication_chance=REPLICATION_CHANCE, death_chance=DEATH_CHANCE, speed=SPEED))
        if action == "die":
            w.creatures.pop(0)
        if action == "eat":
            if w.food_count > 0:
                w.food_count -= 1
                j.reset_energy()
            else:
                w.creatures.pop(0)
    statue.append(w.creatures)
    raw.append(len(w.creatures))
    string = str(i) + ", " + str(len(w.creatures)) + ", " + str(w.food_count)
    print(string)
    csv_lines.append(string + "\n")
    w.act(i)
    food_raw.append(w.food_count)

f = open("creature_data.csv", "w")
f.write("t, n\n")
f.writelines(csv_lines)
f.close()

plt.ioff()
plt.plot(raw)
plt.plot(food_raw)
plt.xlabel("iterations")
plt.ylabel("number cats / food_count")
plt.show()
