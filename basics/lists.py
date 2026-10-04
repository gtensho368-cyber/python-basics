
# Lesson 1
foods = ["pizza", "burrito", "burger", "döner", "fries"]

print(foods[0])
print(foods[2])
print(foods[-1])

# Lesson 2
numbers = [10, 20, 30, 40, 50]
numbers[1] += 5
numbers.append(60)
numbers.remove(40)

print(numbers)

# Lesson 3
names = ["Max", "John", "Huge", "Mark", "Luke"]

for name in names:
    print(f"Hello {name}!")

# Lesson 4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 29]
num = int(input("Pick a number: "))
found = False

for nums in numbers:
    if nums == num:
        found = True
        break

if found:
    print("Number found!")
else:
    print("Number not found!")

# Lesson 5
numbers = [4, 7, 2, 9, 5]
total = 0
largest = 0
smallest = numbers[0]


for num in numbers:
    total += num

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print(total)
print(largest)
print(smallest)

    








