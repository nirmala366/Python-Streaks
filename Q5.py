#reverse a word using for loop

word = "Python"

for i in range(len(word) -1, -1, -1):
    print(word[i] ,  end=" ")