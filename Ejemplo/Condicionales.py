# Conditionals #

import faulthandler


condicion = True

if condicion:
    print("Esto es verdadero")

print("Continuamos en otra linea")

# While #
i = 0   
while i < 10:
    print(i, end=" ") # end=" ", imprime en horizontal los numeros 
    i = i + 1
    # Break #
    if i == 5:
        continue
    # Break #
    if i == 10: 
        break
    # Continue #
    if i == 5:
        continue
    # Continue #
    if i == 10:
        continue
    # Break #   
    if i == 15:
        break

my_condition = 5 * 2

if my_condition == 10:
    print("\n" "Esto es verdadero")
else:
    print("\n" "Esto es falso porque es menor de 10")

print("\n ".join(("Fin de la ejecucion"))+ ", bay")
print("\n".join(("Hola, mundo!")))# imprimir vertical con "\n".join()


def mi_funtion():
    print("Saludos")
    for i in range(1, 7):
        if i % 2== 0:
           print(f"num. {i}")
def mi_funcion():
    print("Hola, mundo!")
    for i in range(5):
        print(i)
    print("Fin del bucle")

mi_funtion()