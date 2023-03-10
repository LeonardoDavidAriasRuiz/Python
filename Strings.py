#Declaration
firstName = "Leonardo"
lastName = 'Arias'

#link 2...n strings
fullName = firstName + " " + lastName
print(fullName)

mon = "monday"
tue = "tuesday"
week = "Week: {}, {}.".format(mon,tue)
print(week)

week = f"Week days: {mon} and {tue}."
print(week)

#How to use "" or '' in a string
quote = "I'm dancing"
print(quote)

quote = 'She said "Hello"'
print(quote)

#know if a string is inside of another string
print("tuesday" in "monday, tuesday, wensday")

#Size of a string
print(len("Hello"))

#Set the word in lower/uppercase
print("Hello".upper())
print("HEllo".lower())

#Swap cases
print("aaBBccDD".swapcase())

#Set first letter of a string in uppercase
print("leonardo david arias ruiz".capitalize())

#Set first letter of each word of a string in uppercase
print("leonardo david arias ruiz".title())

#Count how many times is a string inside of another string
print("Saturday".count("a"))

#If a string starts / ends in a string
print("Saturday".startswith("Sa"))
print("Saturday".endswith("ay"))

#Replace a part of the string into another
print("Saturday".replace("a", "e"))

#If a string can be an int
print("a".isdigit())
print("2".isdigit())
print("2.2".isdigit())

#Get the character of a string
print("abcdefghijk"[0])
print("abcdefghijk"[1])
print("abcdefghijk"[3])

print("abcdefghijk"[-1])
print("abcdefghijk"[-2])
print("abcdefghijk"[-4])

#Get the part of a string from a position to another         it doesn't get the las letter of the position
print("0123456789"[0:5])
print("0123456789"[:5])
print("0123456789"[5:])
print("0123456789"[5:-1])
print("0123456789"[:])

print("0123456789"[::1])
print("0123456789"[::2])
print("0123456789"[::3])

print("0123456789"[5::1])
print("0123456789"[5::2])
print("0123456789"[5::3])

print("0123456789"[:5:1])
print("0123456789"[:5:2])
print("0123456789"[:5:3])
