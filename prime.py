n=int(input("Enter Your Number :"))
if n==1:
    print("This is not Prime Number")
if n>1:
    for i in range(2,n):
        if n%2==0:
            print(n,"This is not Prime Number")
            break
        else:
            print(n,"This is Prime Number")