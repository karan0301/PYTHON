tup = (1,4,9,16,25,36,49,64,81,100)

num = int(input("Enter the number to search for: "))

i = 0
flag = 0

while i< len(tup):
    if tup[i] == num:
        print(num,"is found in the tuple at index",i)
        flag = 1
    i=i+1

if flag == 0:
    print("The number",num,"is not found in the tuple")


