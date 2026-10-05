
import random
import math
import datetime
import pathlib

# Exercise 1: Random number generator
nums = []
total = 0
for times in range(10):
    num = random.randint(1, 100)
    nums.append(num)

for num in nums:
    total += num

average = total/len(nums)

print(average)

# Exercise 2: Random guessing game
num = random.randint(1, 100)
guesses = 0

while True:
    guess = int(input("Enter your number guess: "))
    guesses += 1

    if guess == num:
        print("Correct number.")
        break
    elif guess < num:
        print("Too low")
    else:
        print("Too high")

print(f"The user needed {guesses} guesses.")

# Exercise 3: Math calculator
user = int(input("Enter a number: "))

square_root = math.sqrt(user)
cubed = user ** 3
squared = user ** 2

print(square_root)
print(squared)
print(cubed)

# Exercise 4: Date calculation
birthday = datetime.date(2008, 6, 29)
today = datetime.date.today()
time_passed = today-birthday

print(time_passed)

# Exercise 5: File/folder checker
user = pathlib.Path(input("Enter a file or folder path: "))

print(f"Path exists: {user.exists()}")
print(f"Path is a folder: {user.is_file()}")
print(f"Path is a directory: {user.is_dir()}")






