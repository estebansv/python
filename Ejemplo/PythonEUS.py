
print("Hola")
print(" como estas")
saludar ="hey"
estado = input()

print(1,2,3,4)
print(1,2,3,4, sep='-')  #sep=',' : separa el testo por comas
print(1,2,3,4,(saludar + " me alegro de que estes " + estado), end='.')  #end='.' : finaliza con un punto
 
edad = input("Cual es tu edad?: ")
print(f"Tienes {edad} años")

7<5
9==3
2<12
88>=5

(5<3)and (4==4) #ambas deben cumplircer para ser true
(1<7)or(3==1)  #tiene que cumplicer 1 para ser true
not(6==7)
False and False #deben cumplirce las dos para ser el valor que se cumple


num1 = int(input("Digite un numero: "))
num2 = int(input("Digite otro numero: "))
print(f"El Resultado es: {num1 + num2}")
