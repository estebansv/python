"""
from colorama import  Fore, Style

print(Fore.YELLOW + "Hello word")
print(Style.RESET_ALL)
"""
for num in range(0, 10, 3):
    print("El Valor es: {0}".format (num))

for i in range(1, 13):
    print("{0} x {1} es: {2}".format(i, i, (i * i)))

for nom in ["Esteban", "Braulio", "Juan Miguel", "Albania"]:
    print("Cantidad de letras de {0} es: {1}".format (nom, len(nom)))

""" * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"
 """
texto = input("Ingrese un texto: ")
print(texto.replace("a", "4").replace("e", "3").replace("i", "1").replace("o", "0").replace("u", "5"))

def convertir_a_leet(texto):
    leet = {
        "a": "4",
        "e": "3",
        "i": "1",
        "o": "0",
        "s": "5",
        "t": "7"
    }
    resultado = ""
    for letra in texto:
        if letra.lower() in leet:
            resultado += leet[letra.lower()]
        else:
            resultado += letra
    return resultado

texto = input("Introduce un texto: ")
texto_en_leet = convertir_a_leet(texto)
print(texto_en_leet)
        