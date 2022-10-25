litera = input ("Podaj litere")

if (len(litera)>1):
    print ("Wprowadzono wiecej niz 1 litere")
    exit ()
if (len(litera)==0):
    print ("Nie wprowadzono litery")
    exit ()
if ("a"<=litera<="z"):
    print ("Mala litera")
elif("A"<=litera<="Z")  :
    print("Duza litera")
else:
    print("Nie jest litera")

