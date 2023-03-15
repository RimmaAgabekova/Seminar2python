# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

n = int(input("Введите количество монет  "))
import random
rand_list=[]

for i in range(n):
    rand_list.append(random.randint(0,1))
print(rand_list)

counti = 0

for i in rand_list:
    if i == 0:
        counti += 1
        
countj = 0

for j in rand_list:
    if j== 1:
        countj += 1

minnum = min(counti, countj)
print("минимальное количество монет, которые нужно перевернуть:", minnum)