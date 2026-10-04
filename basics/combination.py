
# Exercise 1
students = [{
    "name": "Max",
    "age": 21,
    "grade": 84
}, {
    "name": "Mal",
    "age": 19,
    "grade": 87
}, {
    "name": "Mao",
    "age": 20,
    "grade": 99
}, {
    "name": "Mad",
    "age": 18,
    "grade": 80
}, {
    "name": "Mac",
    "age": 17,
    "grade": 65
}]

def find_students(students, name):
    for student in students:
        if student["name"].lower() == name.lower():
            return student

        return None

name = input("Enter a name: ")

student = find_students(students, name)

if student is not None:
    print(student)
else:
    print("Student not found.")

# Exercise 2
def analyze_grade(grades):
    lowest = grades[0]
    highest = grades[0]
    total = 0
    failed = 0
    passed = 0

    for grade in grades:
        if grade < lowest:
            lowest = grade

        if grade > highest:
            highest = grade

        if grade < 50:
            failed += 1
        else:
            passed += 1

        total += grade

    average = total/len(grades)

    return average, lowest, highest, failed, passed

grades = [85, 72, 91, 64, 88, 55, 79]

analyze_grade(grades)

# Exercise 3
products = {
    "apple": 1.50,
    "bread": 2.00,
    "milk": 1.20,
    "rice": 3.50
}

def total_expense(products):
    total = 0

    while True:
        user = input("Enter a product you want to buy or type \"done\" to end purchases: " ).lower()

        if user in products:
            total += products[user]
        elif user == "done":
            break
        else:
            print("Product not found.")


    return total

expense = total_expense(products)
    
print(expense)

# Excercise 4
def analyzer(numbers):
    lowest = numbers[0]
    highest = numbers[0]
    total = 0
    evens = []
    odds = []

    for num in numbers:
        if num > highest:
            highest = num
        if num < lowest:
            lowest = num

        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)

        total += num

    average = total/len(numbers)

    return average, lowest, highest, len(evens), len(odds)

    

user =  input("Enter a series of numbers seperated by space: ")
user_list = user.split()
user_nums = []

for num in user_list:
    user_nums.append(int(num))

average, lowest, highest, evens, odds = analyzer(user_nums)

print(
    f"The analyzer results are: {average} average, "
    f"{lowest} lowest number, {highest} highest number, "
    f"{evens} even numbers and {odds} odd numbers."
)

# Exercise 5
def login(users, username, password):
    if username in users and password == users[username]:
        return True

    return False
    
users = {
    "max": "python123",
    "john": "hello456",
    "paul": "secret789"
}

for chances in range(3):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if login(users, username, password):
        print("Login successful.")
        break
    else:
        print("Invalid credentials.")
        if chances == 2:
            print("Access denied.")
        

    



    
    














