import random
listt = []
for i in range(0, 100):
    listt.append(random.randint(0, 100))
for i in listt[:]:
    if i < 32 or i > 41:
        listt.remove(i)
print(listt)

    