n=input("Enter Your Number :")
check=True
for i in n:
    if i!="0" and i!="1":
        check=False
if check == True:
    print(n," is a Binary Number")
else:
    print(n,"is Not Binary Number")


num = int(input("please give a number : "))
while(num>0):
    j=num%10
    if j!=0 and j!=1:
        print("num is not binary")
        break
    num=num//10
    if num==0:
        print("num is binary") 