Year = int(input("Enter Year"))
if Year%400==0:
    print("Leap Year")
else:
    if Year%4==0 or Year%100:
        print("Leap year")
    else:
        print("Not Leap year")