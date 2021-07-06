import random
#Кількість рандомних чисел та їх діапазон
random_list = [random.randrange(-100,100) for i in range(30)]
print("\nрандомые числа(-100/100): ", random_list)
#пошук максимального числа
max_element = max(random_list)
#пошук порядкового номеру числа
position = random_list.index(max_element)
print("\nМакс. значение: ", max_element, "\nпозиция: ", position + 1)
new_list=[]
#умова непарних чисел
for element in random_list:
    if (element % 2) == 1:
        new_list.append(element)
if len(new_list) == 0:
  print("\nнет нечетного числа")
else:
#Виведення списку непарних чисел
  new_list.sort(reverse=True)
  print("\nНовый лист:", new_list)
