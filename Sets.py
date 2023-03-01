
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

# =====================
#       C R U D
# =====================


# Read

print(len(countries))
print("USA" in countries)


# Update

countries.add("China")
countries.add("China")
print(countries)

countries.update({"Spain", "Italy"})
print(countries)

# Delete

countries.remove("China")
print(countries)

countries.discard("Japan")
print(countries)

countries.clear()
print(countries)