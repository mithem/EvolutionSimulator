from creatures import Cat
from world import World
import random
import matplotlib.pyplot as plt

w = World("Phantasialand")
for i in range(1, 1000):
    w.creatures.append(Cat("cat" + str(i)))

statue = []
csv_lines = []
raw = []

for i in range(500):
    for j in w.creatures:
        action = j.act()
        if action == "spawn_new_cat":
            w.creatures.append(Cat("cat"))
        if action == "die":
            w.creatures.pop(0)
    statue.append(w.creatures)
    raw.append(len(w.creatures))
    string = str(i) + ", " + str(len(w.creatures))
    print(string)
    csv_lines.append(string + "\n")

f = open("creature_data.csv", "w")
f.write("t, n\n")
f.writelines(csv_lines)
f.close()

plt.ioff()
plt.plot(raw)
plt.show()
