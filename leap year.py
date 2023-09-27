Year = int(input("Enter Year"))
if Year%400==0:
    print("Leap Year")
else:
    if Year%4==0 and Year%100!=0:
        print("Leap year")
    else:
        print("Not Leap year")
