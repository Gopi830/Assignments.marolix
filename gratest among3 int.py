n1=int(input("Enter the Number 1 :"))
n2=int(input("Enter the Number 2 :"))
n3=int(input("Enter the Number 3 :"))
if n1>n2 and n1>n3:
    print(n1,"this is the largest number")
elif n2>n1 and n2>n3:
    print(n2,"this is the largest number")
else:
    print(n3,"this is the largest number")