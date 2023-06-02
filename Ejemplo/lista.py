my_list = list()
my_otherlist = ["Rojo", "Hola", 5.34, 123]
my_list = [38, 38, 5.9, "Esteban", "Sanchez", "Ruido38"]
print(my_list)
print(my_otherlist) 
print(len(my_list)) #cuenta la cantida en de elementos en el indice
print(my_list.count(38)) #cuenta las repeticiones de los elementos
my_otherlist.append("TETE")# append inserta un elemento al ultimo nivel
print(my_otherlist)
my_otherlist.insert(2,"5-12-2021")# inserta un elementon en el indice expesificado
print(my_otherlist)

my_list.remove(38)# remove Elimina el primer elemento expesificado(x)
print(my_list)

my_backup_list = my_list.copy()


my_pop_element = my_list.pop(2)# pop elemina el ultimo, pero puesde indicarle cual eliminar(X)
print(my_pop_element)
print(my_list)

del my_list[2]# del elimina elemento expecificado en el indice
print(my_list)

my_list.clear()
print(my_list)
print(my_backup_list)
lista_invertida = list(reversed(my_backup_list))
print(lista_invertida)

lista_invertida.reverse()
print(lista_invertida)

lista = [2,32,4,66,41]
lista1 = ["b","a","r","g","j"]

print(list(reversed(lista)))
lista.sort() # sort ordena por mayor a menor etc
print(lista)
print(list(reversed(lista1)))
print(list(sorted(lista1)))