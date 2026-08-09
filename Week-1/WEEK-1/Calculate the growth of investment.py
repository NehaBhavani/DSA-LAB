def power(p, n):
    if n == 0:
        return 1
    elif n > 0:
        return p * power(p, n - 1)
    else:
        return 1 / power(p, -n)
p = float(input("Enter the principal growth factor (p): "))
n = int(input("Enter the number of years (n): "))

result = power(p, n)
print("Result =", result)
