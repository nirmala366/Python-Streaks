# count pccurence of each character in string

word = "Programming"
char_count = {}

for char in word:
    if char in char_count:
        char_count[char] += 1

    else:
        char_count[char] = 1

for char, char_count in char_count.items():
    print(char + ':' , char_count)