transakcje = []

while True:
    print("\n === FINANCE MANAGER ===")
    print("1. Dodaj transakcje ")
    print("2. Wyświetl transakcje ")
    print("3. Usuń transakcje ")
    print("0. Wyjdź ")

    wybor = input("Co chcesz zrobić? ")

    if wybor == "1":
        print("\nPodaj swoją transkację ")
        data = input("Data transakcji ")
        kwota = float(input("Wartość transakcji "))
        kategoria = input("Kategoria transakcji ")
        opis = input("Opis transakcji ")
        transakcje.append({
        "Data": data,
        "Kwota": kwota,
        "Kategoria": kategoria,
        "Opis": opis
        })

    elif wybor == "2":
        if transakcje:
            print("oto twoje dotychczasowe transakcje")
            for indeks, transakcja in enumerate(transakcje, start=1):
                print(f"\n === Transakcja numer {indeks} ===")
                print(f"Data: {transakcja['Data']}")
                print(f"Kwota: {transakcja['Kwota']:.2f}")
                print(f"Kategoria: {transakcja['Kategoria']}")
                print(f"Opis: {transakcja['Opis']}")
        else:
            print("Nie masz żadnych transakcji")
    elif wybor == "3":
        print("Oto twoje transakcje: ")
        if transakcje:
            for indeks, transakcja in enumerate(transakcje, start=1):
                print(f"\n === Transakcja numer {indeks} ===")
                print(f"Data: {transakcja['Data']}")
                print(f"Kwota: {transakcja['Kwota']:.2f}")
                print(f"Kategoria: {transakcja['Kategoria']}")
                print(f"Opis: {transakcja['Opis']}")
            try:
                usuniecie = int(input("Którą transakcje chcesz usunąć?")) - 1
                if len(transakcje) > usuniecie >= 0:
                    usunieta = transakcje.pop(usuniecie)
                    print(f"usunięto transkację {usunieta}")
                else:
                    print("Podany numer nie istnieje")
            except ValueError:
                print("wpisz poprawny numer transakcji")
                
        else:
            print("Nie masz żadnych transakcji")
    elif wybor == "0":
        print("Do zobaczenia")
        break
    else:
        print("Nieprawidłowa opcja")