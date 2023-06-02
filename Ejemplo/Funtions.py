### funtions ###

def my_funtion():
    print("Esta es una funcion")
my_funtion()
my_funtion()
my_funtion()

def suma(num1, num2):
    print(num1 + num2)

suma(3,4)

def resta_con_retorno(a, b):
    return a - b
print(resta_con_retorno(10,4))

def print_nombre(name,lastname, alias ="Sin alias"):
    print(f"{name} {lastname} {alias}")

print_nombre(lastname = "sanchez", name = "Esteban")
print_nombre("Esteban", "Sanchez", "tete")

def upper_texts(*texts):
    for text in texts:
        print(text.upper(),end=" ")

upper_texts("hola", "tete", "Vecino", "Programación")
upper_texts("\n" "adios") 
