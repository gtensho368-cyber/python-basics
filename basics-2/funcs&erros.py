
# Exercise 1
def get_integer():
    while True:
        try:
            return int(input("Enter number: "))
        except ValueError:
            print("Enter valid number.")

get_integer()

# Excercise 2
def divide(a, b):
    try:
        return print(a/b)
    except ZeroDivisionError:
        print("Division by zero.")
        return None

a = 3
b = 1
divide(a, b)

# Excercise 3
def readfile(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return None

filename = input("Enter a filename: ")

if readfile(filename) is not None:
    print(readfile(filename))
else:
    print("File does not exist.")

# Excercise 4
def analyze(numbers):
    try:
        total = 0
        largest = numbers[0]
        smallest = numbers[0]
        for num in numbers:
            total += num

            if num > largest:
                largest = num

            if num < smallest:
                smallest = num

        average = total/len(numbers)
        return total, average, largest, smallest
    except ValueError:
        print("Enter valid numbers.")
        return None

numbers = input("Enter a list of numbers: ")


if analyze(numbers) is not None:
    total, average, largest, smallest = analyze(numbers)
    print(f"Total: {total}, Average: {average}, Largest: {largest}, Smallest: {smallest}")















