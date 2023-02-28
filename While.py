counter = 0

while counter <= 10:
    print(counter)
    counter += 1

counter = 0
while counter <= 10:
    print(counter)
    counter += 1
    if counter == 8:
        break
 
counter = 0
while counter <= 10:
    counter += 1
    if counter == 8:
        continue
    print(counter)
    