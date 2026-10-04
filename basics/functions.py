
# Exercise 1

def greet(name):
    return f"Hello {name}!"

print(greet("Mac"))
print(greet("Sung"))
print(greet("Jin"))

# Exercise 2

def multiply(a, b):
    return a*b

def divide(a, b):
    if b == 0:
        return "division by 0"
    return a/b

def add(a, b):
    return a+b

def minus(a, b):
    return a-b

a = 3
b = 0

print(multiply(a, b))
print(divide(a, b))
print(add(a, b))
print(minus(a, b))

# Exercise 3
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

nums = [2, 4, 5, 6, 7]

for num in nums:
    print(is_even(num))

# Exercise 4
people = {"max": 18, "paul": 34, "shun": 24, "wright": 17, "riel": 45}

def find_age(people, name):
    if name not in people:
        return None
    else:
        return people[name]

other_people = ["jamal", "tyrone", "lebron", "kim", "jin", "wright"]
for name in other_people:
    age = find_age(people, name)

    if age == None:
        pass
    else:
        print(age)

# Exercise 5
def analyze_numbers(numbers):
    even = 0
    total = 0 
    largest = numbers[0]
    smallest = numbers[0]

    for num in numbers:
        if num % 2 == 0:
            even += 1

        if num > largest:
            largest = num

        if num < smallest:
            smallest = num

    total += num

    return total, even, largest, smallest
        

numbers = [4, 7, 2, 9, 6]

print(analyze_numbers(numbers))












