
# Excercise 1
def get_integer():
    while True:
        try:
            return int(input("Enter valid integer: "))
        except ValueError:
            print("Invalid input, reapet again.")
            continue

# Exercise 2
def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return None

# Exercise 3
def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        return None

# Exercise 4
def analyze_numbers(numbers):
    try:
        numbers = [int(value) for value in numbers.split()]
    except ValueError:
        return None

    if not numbers:
        return None

    total = sum(numbers)
    average = total / len(numbers)
    largest = max(numbers)
    smallest = min(numbers)

    return total, average, largest, smallest

# Exercise 5
def get_expense():
        expenses = []
        while True:
            try:
                expense = input("Enter expenses or \"done\" when over: ")
                if expense == "done":
                    break
                else:
                    expenses.append(float(expense))
            except ValueError:
                print("Enter valid number.")

        return expenses
                    
def save_expense(amount):
    with open("expenses.txt", "a", encoding="utf-8") as file:
        file.write(str(amount) + "\n")

def get_total(expenses):
        return sum(expenses)




