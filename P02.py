# 2. alkalom
import random
'''szam = input("Kérek egy számot:")
if szam.isdigit():
    szam = int(szam)
    if szam > 0:
        print("Pozitív")
    elif szam<0:
        print("Negatív")
    else:
        print("Nulla")
else:
    print("Nem számot adtál meg")

jegy = int(input ("Kérek egy érdemjegyet:"))
while jegy == 1 or jegy > 5 or jegy < 1:
    jegy = int(input("Kérek egy érdemjegyet:"))
    if jegy == 10:
        print("Csillagos ötös")
        break
else:
    print("Jól teljesített")
print("Gratulálunk")'''

kocka = random.randint(1,6)
while True:
    tipp = int(input("Kérek egy tippet:"))
    if tipp == kocka:
        break
print("Sikerült eltalálnod a számot")








