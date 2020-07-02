var=int(input("sum of how many natural no. do you want:"))
if var<0:
    print("please enter a positive term")
#else:                                                      #by formula
    #print("The sum of natural no. upto",var,"is",var*(var+1)/2)
    
else:
    sum=0
    while(var>0):                 #by while loop
        sum+=var
        var-=1
        
    print("the sum is",sum)    