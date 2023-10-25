n=input("Enter Your Number :")
sum=0
for i in n:
    sum+=int(i)**len(n)
if sum==int(n):
    print("This is Amstrong Number")
else:
    print("This is Not Amstrong Number")