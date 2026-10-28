# Read and write files
# Exercises 1
with open("hello.txt", "w", encoding="utf-8") as file:
    file.write("Hello\n")
    file.write("World\n")
    file.write("Hello World!\n")

with open("hello.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)

# Exercise 2
note = input("May you please, write a note: ")

with open("notes.txt", "a", encoding="utf-8") as file:
    file.write(note + "\n")

# Exercise 3
with open("text-file.txt", "r", encoding="utf-8") as file:
    content = file.read()

content_list = content.split()
words_num = len(content_list)
character_count = len(content)
lines = content.split("\n")
lines_num = len(lines)

# Exercise 4
name = input("What is your name? ")
age = input("What is your age? ")
grade = input("What is your grade? ")

with open("students.txt", "w", encoding="utf-8") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Grade: {grade}\n")

with open("students.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)

# Exercise 5
while True:
    try:
        food = input("Enter expense or 'done': ")

        if food.lower() == "done":
            break

        food = float(food)

        with open("expenses.txt", "a", encoding="utf-8") as file:
            file.write(f"{food}\n")

        with open("expenses.txt", "r", encoding="utf-8") as file:
            content = file.read()

        nums_strings = content.splitlines()
        nums = []

        for num in nums_strings:
            nums.append(float(num))

        total = sum(nums)
        print(f"Total: {total}")

    except ValueError:
        print("Enter a valid number.")








