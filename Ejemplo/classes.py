class EmptyPerson:
    pass

print(EmptyPerson)

class Persona:
    def __init__(self, nombre, apellido, edad, sexo):
        self.datos = f"{nombre} {apellido} {edad} {sexo}"
    def camina (self):
        print(f"{self.datos} Informacion Basica.")

  
id = Persona ("tete", "scotf", 36,"M")
print(Persona.camina)
id.camina()