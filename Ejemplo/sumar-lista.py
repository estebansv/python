def suma_lista(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma
        
num =[1,2,3,4,5]
resultado = suma_lista(num)
print("La suma de los número es:",resultado)