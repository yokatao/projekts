print('''
1) domowanie
2) odejmowanie 
3) mnożenie
4) dzielenie
5) potęgowanie
''')



X = int(input("What kind of operation do you want to perform?"))
a = int(input("Podaj a:"))
b = int(input("Podaj b:"))
if X == 1:
   print (a+b)
if X == 2:
   print(a - b)
if X == 3:
   print(a * b)
if X == 4:
   print(a / b)
if X == 5:
   print(a ** b)
else:
    print('not a valid number')
