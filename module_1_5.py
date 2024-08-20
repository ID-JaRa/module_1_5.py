immutable_var = (1, 2, 'a', 'b')
print(immutable_var)
# immutable_var[1] = 3 # Кортеж неизменяемый тип данных, если нужен неизменяемый список пользуемся кортежем
print(immutable_var)

mutable_list = [ 145, 'apple', True ]
print(mutable_list)
mutable_list[1] = False
print(mutable_list)