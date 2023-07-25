import random


bushes = [i+1 for i in range(random.randint(3, 9))]

bush_to_collect = random.randint(0, len(bushes) - 1)

if bush_to_collect == 0:
    res = bushes[bush_to_collect] + bushes[bush_to_collect + 1] + bushes[-1]
elif bush_to_collect == len(bushes) - 1:
    res = bushes[bush_to_collect] + bushes[0] + bushes[bush_to_collect - 1]
else:
    res = bushes[bush_to_collect] + bushes[bush_to_collect + 1] + bushes[bush_to_collect - 1]

print(bushes)
print(bush_to_collect + 1)
print(res)
