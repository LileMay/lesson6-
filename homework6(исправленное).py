my_dikt= {"Lili": 1988, "An": 2005, "Nick": 1967}
print(my_dikt)
print(my_dikt["An"])
my_dikt["Sara"] = 2003
print(my_dikt)
my_dikt["Olha"]= 1986
my_dikt["Sasha"]= 1987
print(my_dikt)
del my_dikt["Olha"]
print(my_dikt.get("Olha"))
print(my_dikt)
my_set ={"w", 1, "o", 2,  2.2, "w", "k", 3,  2, True}
print(my_set)
my_set.update([6, 8])
print(my_set)
my_set.discard("w")
print(my_set)