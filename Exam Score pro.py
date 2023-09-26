Marks=eval(input("Enter Your Marks: "))
if Marks>=0 and Marks<60:
    print("F... F means Fail")
elif Marks>=60 and Marks<=69:
    print("D Grade")
elif Marks>=70 and Marks<=79:
    print("C Grade")
elif Marks>=80 and Marks<=89:
    print("B Grade")
elif Marks>=90 and Marks<=100:
    print("A Grade")
else:
    print("please enter invalid marks")