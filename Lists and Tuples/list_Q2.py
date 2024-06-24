#WAP to check if the list is palindrome or not

lis=[]

print("enter the length of the list")

for i in range(int(input())):
    lis.append(int(input()))

print(lis)

lis2 = list.reverse(lis)

if(lis==lis2):
    print("The list is palindromic")
else:
    print("The list is not palindromic")