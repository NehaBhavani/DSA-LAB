def countdown(n):
    if n <= 0:         
        print("Launch")
        return
    print(n)
    countdown(n - 1)
n = int(input("Enter the countdown number: "))
countdown(n)
