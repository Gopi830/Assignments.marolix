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
print("Thank You")

n=int(input("Enter Your NUmber :"))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
result = factorial(n)
print("Factorial of n is:", result)
