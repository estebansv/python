### for ###
my_list = [35, 24, 38, 29, 60, 17] # guarda datos de forma ordenada de uno en uno     

for element in my_list:
    print(element)

my_dict = {"Nombre":"Esteban", "Color":"Morado", "Altura":5.9, "Peso":"175lb"}#guardan datos en forma clave:valor

for element in my_dict.values():
    print(element)

my_set = {"Html", "Css", "JavaScript", "Pythpn"}# guardan datos que no se repiten

for element in my_set:
    print(element)

my_tuple = (36, 5.9, "Esteban", "Sanchez") #guardan datos que no se puede retocar

for element in my_tuple:
    print(element)

#numeros impares
print("impares del 1 al 10")
for i in range(1,11):
    if i % 2 !=0:
     print(i)

print("pares del 1 al 10")
# numero pares 
for i in range(1, 11):
    if i % 2 ==0:
      print(i)

print("primos del 1 al 20")
#numeros primos
def es_primo(num):

    if num < 2:
       return False
    for i in range(2, num):
        if num % i == 0:
            return False
        return True

for i in range(1, 21):
    if es_primo(i):
       print(i)    

### Loops ###

# while

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: #opcional
    print("my_condition es igual a 10")

while my_condition < 20:
    my_condition +=1
    if my_condition == 15:
        print("Mi condición es 15 y para!")
        break
    print(my_condition)
print("Fin de la ejecucion")
