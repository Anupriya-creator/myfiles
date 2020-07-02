def lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while(True):
        if (greater%x==0)and (greater%y==0):
            lcm=greater
            break
        greater+=1
    return lcm
x=int(input("enter first number:"))
y=int(input("enter second number:"))
print("The LCM of ",x, "and",y,"is:",lcm(x,y))
            