#Write a program that takes an integer as input and prints "even" if its an even number and "odd" its an odd number
n=eval(input("Enter Any Number: "))
if n%2==0:
    print("{} is even number".format(n))
else:
    print("{} is odd number".format(n))