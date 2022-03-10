## Najlepsze wyniki MENU. Program powstał podczas pracy z książką Michela Dawsona "Python dla każdego" polecam!

wyniki = []
wybor = None

while wybor != "0":
    print("""
    Najlepsze Wyniki

    0 - Zakończ
    1 - Pokaż wyniki
    2 - Dodaj wynik
    3 - Usuń wynik
    4 - Posortuj wyniki""")
    wybor = input("Wybierasz: ")
    print()

## Pokaż wyniki 
    if wybor == "1":
        print("Najlepsze wyniki")
        for wynik in wyniki:
            print(wynik)
   
 # wyświetl tabelę najlepszych wyników
 #elif choice == "1":
 #print("Najlepsze wyniki\n")
 #print("GRACZ\tWYNIK")
 #for entry in scores:
 #score, name = entry
 #print(name, "\t", score 



## Dodaj wynik
    elif wybor == "2":
        entry = name, score = (input("Podaj imię gracza: "),int(input("Podaj wynik: ")))
        wyniki.append(entry)
       
 #name = input("Podaj nazwę gracza: ")
 #score = int(input("Jaki wynik gracz uzyskał?: "))
 #entry = (score, name)
 #scores.append(entry)
 #scores.sort(reverse=True)
 #scores = scores[:5] # zachowaj tylko 5 najlepszych wyników    




    elif wybor == "3":
        wynik = int(input("Który wynik usunąć?: "))
        if wynik in wyniki:
            wyniki.remove(wynik)
        else:
            print(wynik , "nie ma na liście wyników.")
    elif wybor == "4":
        wyniki.sort()
    else:
        print("Niestety nie jest to prawidłowy wybór")
