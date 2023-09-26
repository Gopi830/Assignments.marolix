Age=eval(input("Enter Your Age: "))
if Age>=0 and Age<=12:
    print("Child")
elif Age>=13 and Age<=19:
    print("Teenager")
elif Age>=20 and Age<=59:
    print("Adult")
else:
    print("senior")