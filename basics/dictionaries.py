
# Lesson 1
person = {"name": "Max", "age": 18, "city": "Kiel", "height": "205cm", "student-status": True}
print(person["name"])
print(person["age"])
print(person["city"])
print(person["height"])
print(person["student-status"])

# Lesson 2
person["age"] = 19
person["country"] = "Germany"
person.pop("city")
print(person)

# Lesson 3
people = {"max": 18, "joe": 20, "po": 23, "paul": 15, "leyla": 17}

name = input("Write a name: ").lower()

if name not in people:
    print("Name not found")
else:
    print(people[name])

# Lesson 4
product = {
    "name": "Laptop",
    "price": 800,
    "stock": 5
}

request = int(input("How many laptops do you wanna buy? "))

if request > product["stock"]:
    print("Not enogh stock")
else:
    print(f"That would be {product['price']*request} dollars.")

# Lesson 5
sentence = input("Please, write a sentence: ")
occurence = {}
sentence = sentence.split()

for word in sentence:
    if word in occurence:
        occurence[word] += 1
    else:
        occurence[word] = 1

print(occurence)

















