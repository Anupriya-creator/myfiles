num=int(input("Enter the number for its factor:-)"))
count=0
print("The factors of",num,"are:")
for i in range(1,num+1):
    if(num%i==0):
        count=i
        print(count) 
       