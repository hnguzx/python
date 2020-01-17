def add(a,b):
    print("%d + %d =" % (a,b))
    return a + b
def sub(a,b):
    print("%d - %d =" % (a,b))
    return  a - b
def mul(a,b):
    print("%d * %d =" % (a,b))
    return a*b
def div(a,b):
    print("%d / %d =" % (a,b))
    return a/b

print("let's do some meth with just function")

a= input("a:")
print(type(a))
b= input("b:")
print(type(b))
#age = add(30,2)
#height = sub(30,2)
#weight = mul(30,2)
#iq = div(30,2)

age = add(a,b)
height = sub(a,b)
weight = mul(a,b)
iq = div(a,b)

print("Age: %d, height: %d, weight: %d, iq: %d" % (age,height,weight,iq))
