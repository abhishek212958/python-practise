name=input("enter your name")
print(name)

college=input("enter the anme of your collge")
print("the name of my collge is ",college)

age=20
age=int(age)

print(age)
print(type(age))


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a + b)

a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)


age=20
print(age>=18 and age<=22)


day="sunday"
print(day=="sunday" or day=="saturday")

raining = False

print(not raining)

age = 20

if age >= 18:
    print("Eligible to vote")

    age = 16

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

    marks = 75

if marks >= 90:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")

    age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Entry not allowed")

