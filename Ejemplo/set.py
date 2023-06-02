## Set ##

my_set = set()
my_other_set = {} # inicial mente es un dict pero si agregamos datos en forma set sera un set
print(type(my_set))
print(type(my_other_set))

my_other_set = {"Esteban", "Sanchez", 36}
print(my_other_set)

print(len(my_other_set))
my_other_set.add("Ruido38")
print(my_other_set) # un set no es una estrutura ordenada, no usa index
my_other_set.add("Ruido38")# un set no admite repeticiones
print(my_other_set)

my_other_set.remove("Esteban")

print(my_other_set)

my_set = {"Html", "Css", "JavaScript", "Pythpn"}
my_set.union({"Rojo"})
print(my_set.union(my_other_set))
print(my_set)
print(my_set.difference(my_other_set))


