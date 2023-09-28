n=int(input("Enter a Number  :"))

def cal_factorial(n):
    factorial=1
    if n == 0 or n == 1:
        return 1
    for i in range(1, n+1):
        factorial = factorial * i
    return factorial
    
output = cal_factorial(n)
print("Factorial Number", n ,"is :", output)