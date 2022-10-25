a = int(input("podaj lieczbę a:"))
b = int(input("podaj lieczbę b:"))

if b<a:
    a,b=b,a
while b>=a:
    print(a,end=' ')
    a=a+1
