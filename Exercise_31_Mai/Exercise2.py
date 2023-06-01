flag=0
while(flag==0):
    a=input("Enter a positive integer number: ")
    if(not a.isdigit()):
         print("not a number, try again")
    else:
        a=int(a)
        print(f"your number is {a}")
        flag=1

flag=0  
while(flag==0):
    b=input("Enter another number: ")
    if(not b.isdigit()):
         print("not a number, try again")
    else:
        b=int(b)
        print(f"your number is {b}")
        flag=1
c=a%b
print(f"The remainder of division of {a} by {b} is {c}")