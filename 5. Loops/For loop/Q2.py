list=[1,4,9,16,25,36,49,64,81,100]

element = int(input("Enter the number to be searched in the list: "))
flag =0

for i in list:
    if element == i:
        print(i,"is found in the list")
        flag=1


if flag==0:
    print("The number is not found in the list")