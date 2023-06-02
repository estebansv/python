# Diccionaries #

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))


my_other_dict = {"Nombre":"Esteban", "Color":"Morado", "Altura":5.9, "Peso":"175lb"}

my_dict ={
    "Carrera":"Informatica",
    "Matricula":"1085625",
    "Conocimiento":{"Linux","Docker", "Git-Github", "Html","Css","JS","python"},
    "Edad":36,
    1:2023
}

print(f"{my_other_dict} \n {my_dict}" )

print(my_dict["Carrera"]) # verificar que hay en Carrera
my_dict["Calle"] = "Max. Gomez, Jose Contreras" # agregar clave valor
print(my_dict)
print(my_dict[1]) #buscar el [1]

del my_dict[1] #eliminar un valor en el dict
print(my_dict)

print("Matricula" in my_dict)
print("Informatia" in my_dict)
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)
print(my_new_dict.keys())
