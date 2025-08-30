#count vowels in a string

vowels = "aeiou"
word = input("enter a word ")

count = 0
for char in word:
    if char in vowels:
        count += 1

print(f"Total vowels in the {word} is {count}")