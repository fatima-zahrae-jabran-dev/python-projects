import math
print("quadratic equation solver:ax**2+bx+c=0")
a=float(input("entar a:"))
b=float(input("enter b:"))
c=float(input("enter c:"))
delta=b**2-4*a*c
print("delta=",delta)
if delta>0:
    x1=(-b-math.sqrt(delta))/(2*a)
    x2=(-b+math.sqrt(delta))/(2*a)
    print("two solution")
    print("x1=",x1)
    print("x2=",x2)
elif delta==0:
    x=-b/(2*a)
    print("one solutions")
    print("x=",x)
else:
    print("no real solutions")
    
