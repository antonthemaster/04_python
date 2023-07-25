import random


fst_arr = [random.randint(1, 99) for _ in range(random.randint(3, 15))]
scd_arr = [random.randint(1, 99) for _ in range(random.randint(3, 15))]

res = tuple(sorted(fst_arr + scd_arr))

print(res)
