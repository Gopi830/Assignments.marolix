n=int(input("Enter Your Number :"))

def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

op=sum_of_digits(n)
print("Sum of The Digit is :",op)
