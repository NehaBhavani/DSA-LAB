def factorial(n):
    if n == 0 or n == 1:     
        return 1
    elif n > 1:               
        return n * factorial(n - 1)
    else:                    
        return "Factorial not defined for negative numbers"

n = int(input("Enter a number: "))

result = factorial(n)
print("Factorial =", result)
