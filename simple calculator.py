def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("select which operation do you want:")
print("1.Add")
print("2.subtract")
print("3.multiply")
print("4.divide")
choice=input("Enter your choice 1/2/3/4:_______")
x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
if choice=='1':
    print(x, "+",y, "=",add(x,y))
elif choice=='2':
    print(x, "-",y, "=",subtract(x,y))
elif choice=='3':
    print(x, "*",y, "=",multiply(x,y))
elif choice=='4':
    print(x, "/",y, "=",divide(x,y))
else:
    print("Invalid input")    

    