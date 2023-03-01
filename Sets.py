# =======================================================================
#                                S E T S
# =======================================================================

# Can't have the same value more than one time
# Random placed
countries = {"Mexico", "Canada", "USA", "Mexico"}
print(countries)

# Convert from one to sets
string = set("Hola como estas")
print(string)

tuple = set(("abc", "def", "ghi", "abc"))
print(tuple)

list = set([1, 2, 3, 4, 5, 1, 2])
print(list)

#                    -----------------------------------
#                                 C R U D
#                    -----------------------------------


#                                   Read

print(len(countries))
print("USA" in countries)


#                                   Update

countries.add("China")
countries.add("China")
print(countries)

countries.update({"Spain", "Italy"})
print(countries)

#                                    Delete

countries.remove("China")
print(countries)

countries.discard("Japan")
print(countries)

countries.clear()
print(countries)

#                    -----------------------------------
#                             O P E R A T I O N
#                    -----------------------------------

num1 = {1, 2, 3, 4, 5, 6}
num2 = {6, 7, 8, 9, 1, 0}

#                                    Union
print(num1.union(num2))
print(num1 | num2)

#                                 Intersection
print(num1.intersection(num2))
print(num1 & num2)

#                                  Difference
print(num1.difference(num2))
print(num1 - num2)

print(num2.difference(num1))
print(num2 - num1)

#                              Symmetric Difference
print(num1.symmetric_difference(num2))
print(num2 ^ num1)