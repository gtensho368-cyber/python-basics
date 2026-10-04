
# Lesson 1
num = int(input("Pick any number: "))

if num == 0:
    print("The number is zero.\n")
elif num < 0:
    print("It's a negative number.\n")
elif num > 0:
    print("It's a positive number.\n")

# Lesson 2
integer = int(input("Pick an integer: "))

if integer % 2 == 0:
    print("It's an even number.\n")
elif integer % 2 != 0:
    print("It's an odd number.\n")

# Lesson 3
age = int(input("How old are you? "))

if age < 13:
    print("You are a child.\n")
elif age > 13 and age <= 17:
    print("You are a teenager.\n")
elif age > 17 and age <= 65:
    print("You are an adult.\n")
else:
    print("You are a senior.\n")

# Lesson 4
correct_username = "admin"
correct_password = "1234"

username_entry = input("Enter the valid username: ")
password_entry = input("Enter valid password: ")

if username_entry == correct_username and password_entry == correct_password:
    print("Login successful.\n")
else:
    print("Invalid Credentials.\n")

# Lesson 5
num_1 = int(input("Pick a number: "))
num_2 = int(input("Pick another number: "))
operation = input("Pick the operation(+, -, *, /): ")

if operation == "+":
    print(f"The sum of the numbers is {num_2+num_1}.")
elif operation == "-":
    print(f"The subtraction of the numbers is {num_1-num_2}")
elif operation == "*":
    print(f"The multiplication of both is {num_2*num_1}.")
elif operation == "/":
    if num_2 == 0 or num_1 == 0:
        print("Division by zero is unknown.")
    else:
        print(f"The division both numbers is {num_1/num_2}.")
else:
    print("Invalid opration.")








