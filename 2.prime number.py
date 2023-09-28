n=int(input("Enter Any Number :"))
def cal_prime(n):
    print("Thank You")
for i in range(2,n):
    if n%i == 0:
        print(n,"is not a prime")
        break
else:
    print(n,"is prime")
cal_prime(n)
