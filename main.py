list = []
list.append(3)
name = 'Добрый день!'
list.append(name)
list.insert(0, 'Привет')
print(list)

list.reverse()
print(list)

print(len(list))
print(list[0][7:11])
print("Индекс элемента - ", list.index('Привет'))

list.pop(1)
print(list)

list.remove('Привет')
print(list)

list[0] = 100
print(list)

list_1 = [1,2,3]
list_2 = [4,5,6]

list_1 = list_1 + list_2
print(list_1)