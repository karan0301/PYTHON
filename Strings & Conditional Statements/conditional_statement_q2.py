# WAP to find greatest of 3 numbers

print("Enter three values\n")
num1=input()
num2=input()
num3=input()

if(num1>num2 and num1>num3):
    print("the greatest number is",num1)
elif(num2>num1 and num2>num3):
    print("the greatest number is",num2)
else:
    print("the greatest number is",num3)xml