# wprowadz liczbę
liczba = int(input("Podaj liczbę: "))

### BEGIN SOLUTION
import math
liczba = int(liczba)
sqrt = sqrt(liczba)
sqrt2 = int(sqrt.real)

i = 2
while i < sqrt2:
    if liczba%i == 0:
        print(liczba, " jest nie jest liczbą pierwszą")
        i = i+1 
        
        break
    else: 
        i = i+1 

if i == sqrt2 :print(liczba, "jest liczbą piewrszą")
### END SOLUTION