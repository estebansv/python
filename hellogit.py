
print( "Hola desde la teminal")
numero = 8
decimal = 2.1
my_bool = True
cadetxt = 'hola a todos'
print("el valor es " + str(numero) + " y el booleano es " + str(my_bool))

print(f"El valor de mi entero es {numero} y el de mi bool {my_bool}")

my_list = [numero, my_bool, cadetxt, decimal]
print(my_list)
print(type(my_list))
print(my_list[2])

#diccionario "clave" : valor
my_dict = {"string" : cadetxt, "int" : numero, "my_bool" : my_bool, "Mi_nombre" : "tete"}
print(type(my_dict))
print(my_dict["Mi_nombre"])
 
if numero != 5:
    print(f"numero no es 5, es {numero}")
elif numero == 4:
        print("numero es 4")
else:
            print("numero es otro")

for my_list2 in my_list:
    print(my_list2)

 
for count in range(8, 0, -2):
        print(count)
 
for count1 in range(8):
        print(count1)

## funcion de declara con def
def my_function():
    print("Hola desde la funcion")

for i in range(10):  
   my_function()

def sumar(a,b):
    result = a+b
    return result

result = sumar(2, 7)
print(result) 
 
## funcion flecha => , lambda 
suma = lambda a,b: a+b

res = suma(1,7)
print(res)