a = []  # заводим пустой список
for i in range(int(input())):   # считываем количество элемент в списке
    new_element = int(input())  # считываем очередной элемент
    a.append(new_element)       # добавляем его в список
    # последние две строки можно было заменить одной:
    # a.append(int(input()))
print(a)
