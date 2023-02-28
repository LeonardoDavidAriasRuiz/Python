
numbers = [0,1,2,3,4,5,6,7,8,9]
print(numbers)
print(type(numbers))

print(numbers[6])
print(numbers[0:3])
print(numbers[:3])
print(numbers[5:9])
print(numbers[5:])

print(numbers[::2])

print(23 in numbers)

differentsTypes = [0,"1", 2.3, True]
print(differentsTypes)
print(type(differentsTypes))

print(True in differentsTypes)

# ================================
#   Creat, Read, Update, Delete
# ================================

#C
numbers = [1,2,3,5]

#R
print(numbers)
print(numbers.index(3))

#U
numbers[-1] = 4
numbers.append(5)
numbers.insert(0,0) #(position, value)
numbers += [6,7]

print(numbers)

#D
numbers.remove(7)
numbers.pop()  #Take out the last value and return it
numbers.pop(0) #Take out the value in the position and return it
print(numbers)

# ===========================
#       List functions
# ===========================

numbers = [5,3,7,2]
numbers.sort()
print(numbers)

list = ["a", "ab", "aa"]
list.sort()
print(list)

# ===========================
#          Matriz
# ===========================
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]