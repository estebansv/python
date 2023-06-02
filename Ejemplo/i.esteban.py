#variables
cadena = "Estebanq"
numero = 10
decimal = 11.5
fv = True
print(type(cadena))

my_list = [cadena,numero,decimal,fv] #lista ordenada
print(my_list)
print(my_list[3])
my_dict = {"string":cadena,"numero":numero,"float":decimal,"bool":fv} #clave valor
print(my_dict)

my_set = {cadena,numero,decimal,fv} #lista desordenada
print(my_set)

my_tuple = (cadena,numero,decimal,fv)
print(my_tuple)

if cadena == "Esteban":
    print("Es Esteban")
elif cadena!= "Esteban":
    print(f"Es  diferente a esteban porque es {cadena}")
else:
    print("No es esteban")

for set in my_list:
     print(set)

def saludar(name):
    print(f"Hola {name} !")
for repetir in range(3):
    saludar("tete")

#tabla de multiplicar con funcion lambda
tabla_5 = lambda x: x*5
for i in range(1,11):
    resultado = tabla_5(i)
    print(f"5 x {i} = {resultado}")

#sumar un numero con el retorno de una funcion
def sumar(x):
  return x+5
res = sumar(10)
print(res)

#fizzBuzz my @I.esteban
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
            print("Fizz")
    elif i%5==0:
                print("Buzz")
    else:
                    print(i)
#fizzBuzz AI
resultado = []
for i in range(1, 101):
    resultado.append("fizz"*(i%3==0) + "buzz"*(i%5==0) or str(i))
print("\n".join(resultado))
