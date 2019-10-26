x=float(input("x="))
y=float(input("y="))
operation=input("Sign:")
result=None
if operation=="+":
    result=x+y
elif operation=="-":
    result=x-y
elif operation=="*":
    result=x*y
elif operation=="/":
    result=x/y
else:
    print("Error")
print("Result:", result)

