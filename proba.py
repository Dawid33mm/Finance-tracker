transakcje = []
while True:
    print("===Finansowy menadżer===")
    print("1. wyświetl transakcje")
    print("2. Dodaj transakcje")
    print("3. Usuń transakcje")
    print("0. Wróć")

    powitanie = input("Co chcesz zrobić ")

    if powitanie == "1":
        if transakcje:
            for indeks, transakcja in enumerate(transakcje, start=1):
                print(f"=== Transakcja numer {indeks} ===")
                print(f"Data: {transakcja['Data']}")
                print(f"Kwota: {transakcja['Kwota']:.2f}")
                print(f"Kategoria: {transakcja['Kategoria']}")
                print(f"Opis: {transakcja['Opis']}")
        else:
            print("Brak transakcji")

    elif powitanie == "2":
        print("Wpisz swoją transakcję")
        data = input("Data")
        kwota = float(input("Kwota"))
        kategoria = input("Kategoria")
        opis = input("Opis")
        transakcje.append({
            "Data": data,
            "Kwota": kwota,
            "Kategoria": kategoria,
            "Opis": opis
        })

    elif powitanie == "3":
        print("Oto twoje transakcje")
        if transakcje:
            for indeks, transakcja in enumerate(transakcje, start=1):
                print(f"=== Transakcja numer {indeks} ===")
                print(f"Data: {transakcja['Data']}")
                print(f"Kwota: {transakcja['Kwota']:.2f}")
                print(f"Kategoria: {transakcja['Kategoria']}")
                print(f"Opis: {transakcja['Opis']}")
            try:
                usuniecie = int(input("Którą transakcje chcesz usunać?")) - 1
                if len(transakcje) > usuniecie >= 0:
                    usunieta = transakcje.pop(usuniecie)
                    print(f"usunięto transakcję:{usunieta}")
                else:
                    print("podany numer nie istnieje")
            except ValueError:
                print("Podaj prawidłową wartość")
        else:
            print("Nie masz transakcji")

    elif powitanie == "0":
        print("Do zobaczenia")
        break
    else:
        print("Nieprawidłowa opcja")
