#calculate factorial of a numbers

n = 5
factorial = 1

for i in range(1, n+1):
    factorial *= i
print(f"factorial of {n} is {factorial}")