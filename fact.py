def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

print(factorial(5));
