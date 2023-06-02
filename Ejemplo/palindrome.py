
"""
def palindrome(text):
    reversed_text = text[::-1]
    return text == reversed_text

user = input("Digite un texto\n")

if palindrome(user):
    print("El texto Es un palindromo!")
else:
    print("El texto no es un palindrome.")
    """

def es_palindrome(cadena):
    cadena = cadena.lower().replace(" ", "")
    if cadena == cadena[::-1]:
        return True
    else:
        return False

texto = input("Ingrese un texto:\n")
if es_palindrome(texto):
    print("El texto es un palindromo.")
else:
    print("El texto no es un palindromo.")
