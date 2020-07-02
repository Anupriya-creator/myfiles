def ComputeGcd(x,y): 
     if y<x:
        smaller=x
     else:
        smaller=y
     for i in range(1,smaller+1):
        if (x%i==0) and (y%i==0):
            hcf=i
     return hcf
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
lcm=x*y//ComputeGcd(x,y)
print("The LCM of",x,"and",y,"is:",lcm)
