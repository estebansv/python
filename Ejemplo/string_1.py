# Formateo

name, username, age = "Esteban", "Ruido38", 36

print("mi Nombre es {} {} y mi edad es {}".format(name, username, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, username, age))

print(f"mi nombre es {name} {username} y mi edad es {age}")

#Desempaquetado de caracteres
lenguage = "python"
a, b, c, d, e, f = lenguage
print(a)
print(e)

#división

#imprime la "y,t"
lenguage_slice = lenguage[1:3]
print(lenguage_slice)

#imprime desde la y en adelante
lenguage_slice = lenguage[1:]
print(lenguage_slice)

#imprime la o
lenguage_slice = lenguage[-2]
print(lenguage_slice)
 
 # Reverse

#imprime pyhton alreves
reversed_lenguage = lenguage[::-1]
print(reversed_lenguage)

# Funciones

print(lenguage.capitalize())
print(lenguage.upper())
print(lenguage.lower())
print(lenguage.isnumeric())
print("1".isnumeric())
print(lenguage.count("a"))
print(lenguage.upper().isupper())  #isupper  compara si esta en masyuscula
