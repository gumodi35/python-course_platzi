my_set = {3, 4, 5}
print("my_set =", my_set)

my_set2 = {"Hola", 23.3, False, True}
print("my_set2 =", my_set2)

my_set3 = {3, 4, 5, 3, 4, 5}
print("my_set3 =", my_set3)

# list --> elemento mutable
# my_set4 = {[1, 2, 3], 5}
# print("my_set4 =", my_set4)

my_list = [1, 1, 2, 3, 4, 4, 5]
my_set = set(my_list)
print(my_set)

my_tuple = ("Hola", "Hola", "Hola", 1)
my_set2 = set(my_tuple)
print(my_set2)

# trabajando con sets
my_set = {1, 2, 3}
print(my_set)

# añadir un elemento con el metodo --> add()
my_set.add(5)
print(my_set)

# añadir varios elementos con el metodo --> update()
my_set.update([1, 2, 5])
print(my_set)

# Añadir multiples elementos 
my_set.update((1, 7, 2), {6, 8})
print(my_set)

# ejercicio para eliminar elementos
my_set = {1, 2, 3, 4, 5, 6, 7}
print(my_set)

# Borrar un elemento existente
my_set.discard(1)
print(my_set)

# Borrar un elemento existente
my_set.remove(2)
print(my_set)

# Borrar un elemento existente
my_set.discard(10)
print(my_set)

# Borrar un elemento inexistente --> error
# my_set.remove(12)
# print(my_set)

my_set = {1, 2, 3, 4, 5, 6, 7}
print(my_set)

# Borrar un elemento aleatorio
my_set.pop()
print(my_set)

# Limpiar el set
my_set.clear()
print(my_set)

