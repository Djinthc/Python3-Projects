##   XVI Olimpiada Informatyczna - Zadanie "Bajtackie Zoo"

def poprzestawiajSlonie(plik):

## Listy
    masy = []
    ust1 = []
    ustkon = []
    INF = 100000000
    
    
## Pobieramy dane
    plik = open(plik, "r")
    linie = plik.readlines()
    for dana in linie[1].split(" "):
        masy.append(int(dana))
    for dana in linie[2].split(" "):
        ust1.append(int(dana)-1)
    for dana in linie[3].split(" "):
        ustkon.append(int(dana)-1)


## Konstrukcja permutacji
    matfalse = [False for i in range(len(masy))]
    tempust = [None for i in range(len(masy))]
    for i in range(len(masy)):
        tempust[ustkon[i]] = ust1[i]


## Obliczamy
    wynik = 0
    for i in range(len(masy)):
        if not matfalse[i]:
            minc = INF
            suma = 0
            lenc = 0
            slon = i
            x = True

            while x:
                minc = min(minc, masy[slon])
                suma += masy[slon]
                slon = tempust[slon]
                matfalse[slon] = True
                lenc += 1
                if slon == i:
                    x = False

            wynik += min(suma + (lenc - 2) * minc, suma + minc + (lenc + 1) * min(masy))
            
    return wynik


