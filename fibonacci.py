nterms=int(input("how many terms you want? :"))
count=0
#var1= 12
# var=45
var1=int(input("enter the first number:"))
var=int(input("enter the second number:"))
if nterms<0:
    print(" pls enter the positive integer")
elif nterms==1:
    print("fibonacci series upto", nterms, "terms is:")
    print(var1)
else:
    print("fibonacci series upto", nterms ," terms is:")
    while count<nterms:
        print(var1, end=',')
        var3=var1+var
        var1=var
        var=var3
        count+=1
print()        
        




var3=var1+var
var1=var
var=var3
print()