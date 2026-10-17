transakcje = []

while True:
    print("\n === FINANCE MANAGER ===")
    print("1. Dodaj transakcje ")
    print("2. Wyświetl transakcje ")
    print("3. Usuń transakcje ")
    print("4. Podsumowanie")
    print("0. Wyjdź ")

    wybor = input("Co chcesz zrobić? ")

    if wybor == "1":
        print("\nPodaj swoją transkację ")
        data = input("Data transakcji ")
        kwota = float(input("Wartość transakcji "))
        kategoria = input("Kategoria transakcji ")
        opis = input("Opis transakcji ")
        print("Wybierz typ transakcji: \n 1. Przychód \n 2. Wydatek")
        typ = input("Typ transakcji ")
        if typ == "1":
            prawidlowy_typ = "Przychód"
        elif typ == "2":
            prawidlowy_typ = "Wydatek"
        else:
            print("zła opcja")
            continue
        if prawidlowy_typ:
            transakcje.append({
                            "Data": data,
                            "Kwota": kwota,
                            "Kategoria": kategoria,
                            "Opis": opis,
                            "Typ": prawidlowy_typ
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
                print(f"Typ: {transakcja['Typ']}")
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
                print(f"Typ: {transakcja['Typ']}")
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
    elif wybor == "4":
        print("=== Oto twoje podsumowanie ===")
        suma_wydatków = 0
        suma_przychodów = 0
        for transakcja in transakcje:
            if transakcja['Typ'] == "Wydatek":
                suma_wydatków += transakcja['Kwota']
            elif transakcja['Typ'] == "Przychód":
                suma_przychodów += transakcja['Kwota']
        print(f"Wydatki: {suma_wydatków}")
        print(f"Przychody: {suma_przychodów}")
        print(f"Saldo: {suma_przychodów - suma_wydatków}")
    else:
        print("Nieprawidłowa opcja")