
# Exercise 1
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Enter valid number.")

# Exercise 2
try:
    num_1 = int(input("Enter a number: "))
    num_2 = int(input("Enter another number: "))
    opr = input("Choose an operator(-, +, *, /): ")

    if opr == "-":
        print(num_1-num_2)
    elif opr == "+":
        print(num_1+num_2)
    elif opr == "*":
        print(num_1*num_2)
    elif opr == "/":
        print(num_1/num_2)
    else:
        print("Invalid operation.")
except ValueError:
    print("Enter valid number.")
except ZeroDivisionError:
    print("Division by zero is unknown.")    

# Exercise 3
try: 
    items = [1, 2, 3, 4, 5]
    index = int(input("Enter an index: "))
    print(items[index])
except ValueError:
    print("Invalid index.")
except IndexError:
    print("Invalid index.")

# Exercise 4
file_name = input("Enter a filename: ")

try:
    with open(file_name, "r", encoding="utf_8") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File does not exist.")

# Exercise 5
while True:
    try:
        food = float(input("Enter food price or \"done\": "))
        
        if food == "done":
            break

        with open("expenses.txt", "a", encoding="utf-8") as file:
            file.write(f"{food}\n")

        with open("expenses.txt", "r", encoding="utf-8") as file:
            content = file.read()

        nums_strings = content.splitlines()
        nums = []

        for num in nums_strings:
            nums.append(float(num))
        
        total = sum(nums)
        print(total)
        
    except ValueError:
        print("Enter valid number.")
        continue
            














