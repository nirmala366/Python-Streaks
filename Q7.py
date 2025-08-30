#print fibonacai sequence upto 10 terms

a = 0
b = 1
print(a,b, end=" ")

for _ in range(10):
    next_term = a + b
    print(next_term, end=" ")
    a,b = b,next_term