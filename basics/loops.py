
# Lesson 1
num = 0

while num < 10:
    num += 1
    print(num)

# Lesson 2
num = int(input("Pick a number: "))

for nums in range(1, 11):
    print(f"{num * nums}")

# Lesson 3
nums = int(input("Pick a number: "))
add = 0 

for num in range(1, nums+1):    
    add += num

print(add)

# Lesson 4
correct_password = "python123"

for attempts in range(3):
    attempt = input("Enter the correct password: ")
    if attempt == correct_password:
        print("Access granted.")
        break
    elif attempts == 2:
        print("Access denied.")

# Lesson 5
secret_number = 7

while True:
    guess = int(input("Enter the correct number: "))

    if guess < secret_number:
        print("Too low.")
    elif guess > secret_number:
        print("Too high.")
    elif guess == secret_number:
        print("Correct!")
        break

















