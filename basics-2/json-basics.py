
import json

# Excersise 1
person = {
    "name": "Max",
    "age": 18,
    "skills": ["Python", "Webdev", "Electronics"]
}

with open("person.json", "w", encoding="utf-8") as file:
    json.dump(person, file, indent=4)

with open("person.json", "r", encoding="utf-8") as file:
    person = json.load(file)

print(person["name"])
print(person["age"])
print(person["skills"])

# Exercise 2
while True:
    try:
        with open("contacts.json", "r", encoding="utf-8") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}
    except json.JSONDecodeError:
        print("Invalid JSON.")
        break


    phone = input("Enter phone contact: ") 
    name = input("Enter name: ")

    for names in contacts:
        if names == name:
            break

    if len(phone) == 11 and phone.isdigit():
        contacts[name] = phone
    else:
        print("Invalid number.")

    
    with open("contacts.json", "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4)


    choice = input("Type \"done\" when you want it to be over or enter to continue: ")

    if choice == "done":
        print(contacts)
        break
    else:
        continue

# Exercise 3
inventory = {"apple": [2, 4], "banana": [3, 6], "orange": [5, 7]}


with open("inventory.json", "w", encoding="utf-8") as file:
    json.dump(inventory, file, indent=4)

try:
    with open("inventory.json", "r", encoding="utf-8")  as file:
        inventory = json.load(file)
except FileNotFoundError:
    print("File not found.")
except json.JSONDecodeError:
    print("Invalid JSON.")

for product in inventory.values():
    print(f"{product} price is {product[0]}")

total_value = 0

for product in inventory.values():
    total_value += product[1] * product[0]

under_5 = []
for product, value in inventory.items():

    if value[1] < 5:
        under_5.append(product)

for products in under_5:
    print(f"{products} have less than 5 items remaining.")

# Exercise 4
try:
    with open("expenses.json", "r", encoding="utf-8") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = {}
except json.JSONDecodeError:
    print("Invalid JSON.")


    while True:
        try:
            expense_name = input("Enter the expenses name, type \"done\" to exit: ")
            if expense_name == "done":
                break

            expense_amount = float(input("Enter expense amount: "))

            expenses[expense_name] = expense_amount
        except ValueError:
            print("Enter valid number: ")

with open("expenses.json", "w", encoding="utf-8") as file:
    json.dump(expenses, file, indent=4)

with open("expenses.json", "r", encoding="utf-8") as file:
    expenses = json.load(file)

total = 0
for expence in expenses.values():
    total += expence

print(f"The total expense is {total}.")

# Exercise 5
try:
    with open("settings.json", "r", encoding="utf-8") as file:
        settings = json.load(file)
except FileNotFoundError:
    settings = {}
except json.JSONDecodeError:
    print("Invalid json.")
    settings = {}

while True:
    exit = input("Type anything and enter to exit: ")
    if exit:
        break
    username = input("Choose a new username if you want: ")
    if not username:
        continue
    else:
        settings["username"] = username
        theme = input("Enter theme(light or dark): ")
        if theme == "light" or theme == "dark":
            settings["theme"] = theme
            notifications = bool(input("Enter if notifications are true or false: ").lower())
            notifications_input = input("Enable notifications? (true/false): ").lower()
            if notifications_input == "true":
                settings["notifications"] = True
            elif notifications_input == "false":
                settings["notifications"] = False
            else:
                print("Enter true or false.")
                continue
            break
        else:
            continue
            

with open("settings.json", "w", encoding="utf-8") as file:
    json.dump(settings, file, indent=4)








