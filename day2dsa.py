numbers = [10, 20, 30, 40]

numbers.remove(20)

print(numbers)

numbers = [10, 20, 30, 40, 50]

print(numbers)


numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[2])

numbers = [10, 20, 30, 40]

numbers[1] = 100

print(numbers)

numbers = [10, 20, 30]

numbers.append(40)

print(numbers)

numbers = [10, 20, 30]

numbers.insert(1, 100)

print(numbers)

numbers = [10, 20, 30, 40]

numbers.remove(20)

print(numbers)

numbers = [10, 20, 30, 40]

numbers.pop(1)

print(numbers)

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)

    numbers = [10, 20, 30, 40, 50]

target = 30

found = False

for number in numbers:
    if number == target:
        found = True

if found:
    print("Number found")
else:
    print("Number not found")

    