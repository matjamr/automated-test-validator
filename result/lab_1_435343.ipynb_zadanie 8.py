# wprowadz liczbę
import math
liczba = int(input("Podaj liczbę: "))
pierw = int(liczba**0.5) + 1

### BEGIN SOLUTION
if liczba == 2:
    print(liczba, "to liczba pierwsza") 

elif liczba % 2 == 0 & liczba != 2 or liczba <= 1:
    print(liczba,"nie jest liczbą pierwszą ")     
    licznik = 0

for dzielnik in range(3, pierw, 2): #nie ma sensu sprawdzać liczb parzystych
    if liczba % dzielnik == 0:
        print (liczba,"nie jest liczbą pierwszą")
        break
print(liczba,"jest liczbą pierwszą") 

### END SOLUTION