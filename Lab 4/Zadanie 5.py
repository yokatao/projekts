import random
result_list = []

y = 0
while y < 15:
    x = random.uniform(0, 50)
    x = round(x, 2)
    result_list.append(x)
    y += 1
print(result_list)

