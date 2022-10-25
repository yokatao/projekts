a = int(input("podaj lieczbę a:"))
b = int(input("podaj lieczbę b:"))

if b<a:
    a,b = b,a

while a <= b:

    if a % 2 == 1:
        a = a + 1

        continue
    print(a,end=" ")
    a = a + 1
