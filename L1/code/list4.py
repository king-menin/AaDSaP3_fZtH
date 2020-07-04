lst = list(range(4))
print(lst)
# Вставка в конец
lst.append(4)
print(lst)
# Вставка на позицию
lst.insert(2, -1)
print(lst)
# Выталкивание
last = lst.pop(-1)
print(lst, last)
# Удаление
lst.remove(3)
print(lst)
