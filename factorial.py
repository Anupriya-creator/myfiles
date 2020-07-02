var=int(input("enter the number for the factorial:"))
factorial=1
if var<0:
    print("please enter a positive integer")
elif var==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,var+1):
        factorial=factorial*i
    print("The factorial of",var,"is",factorial,)
        
        
    
    