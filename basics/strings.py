
# Lesson 1
sentence = input("Type a sentence: ")

print(sentence.upper())
print(sentence.lower())
print(len(sentence))
print(sentence[0])
print(sentence[-1])

# Lesson 2
name = input("Give me your first and last name: ")
name = name.strip()
name = name.title()

print(name)

# Lesson 3
text = input("Write a sentence: ").lower()
word = input("Pick a word: ").lower()

if text.find(word) != -1:
    print("Word found!")
else:
    print("Word not found!")

# Lesson 4
sentence = input("Write a sentence: ")
sentence_words = sentence.split()

print(len(sentence_words))

# Lesson 5
password = input("Enter a password: ")

has_digit = False
has_upper = False
has_lower = False

for letter in password:
    if letter.isupper():
        has_upper = True
    elif letter.islower():
        has_lower = True
    elif letter.isdigit():
        has_digit = True

if len(password) >= 8 and has_digit and has_lower and has_upper:
    print("Valid password.")
else:
    print("Invalid password.")




