import json

def zapisz_dane(dane):
    with open("dane.json", "w", encoding="utf-8") as plik:
        json.dump(dane, plik, indent=4)

try:
    with open("dane.json", "r", encoding="utf-8") as pliczek:
        dane = json.load(pliczek)
except FileNotFoundError:
    print("Nie znaleziono pliku")
    dane = []

while True:
    print("\n === FINANCE MANAGER ===")
    print("1. Dodaj dane ")
    print("2. Wyświetl dane ")
    print("3. Usuń dane ")
    print("4. Podsumowanie")
    print("0. Wyjdź ")

    wybor = input("Co chcesz zrobić? ")

    if wybor == "1":
        print("\nPodaj swoją transkację ")
        data = input("Data transakcji ")
        try:
            kwota = float(input("Wartość transakcji "))
        except ValueError:
            print("Błędna wartość")
            continue
        if kwota <= 0:
            print("Błędna wartość. Podaj liczbę dodatnią")
            continue
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
            dane.append({
                        "Data": data,
                        "Kwota": kwota,
                        "Kategoria": kategoria,
                        "Opis": opis,
                        "Typ": prawidlowy_typ
                        })
        zapisz_dane(dane)
    elif wybor == "2":
        if dane:
            print("oto twoje dotychczasowe dane")
            for indeks, transakcja in enumerate(dane, start=1):
                print(f"\n === Transakcja numer {indeks} ===")
                print(f"Data: {transakcja['Data']}")
                print(f"Kwota: {transakcja['Kwota']:.2f}")
                print(f"Kategoria: {transakcja['Kategoria']}")
                print(f"Opis: {transakcja['Opis']}")
                print(f"Typ: {transakcja['Typ']}")
        else:
            print("Nie masz żadnych transakcji")
    elif wybor == "3":
        print("Oto twoje dane: ")
        if dane:
            for indeks, transakcja in enumerate(dane, start=1):
                print(f"\n === Transakcja numer {indeks} ===")
                print(f"Data: {transakcja['Data']}")
                print(f"Kwota: {transakcja['Kwota']:.2f}")
                print(f"Kategoria: {transakcja['Kategoria']}")
                print(f"Opis: {transakcja['Opis']}")
                print(f"Typ: {transakcja['Typ']}")
            try:
                usuniecie = int(input("Którą dane chcesz usunąć?")) - 1
                if len(dane) > usuniecie >= 0:
                    usunieta = dane.pop(usuniecie)
                    zapisz_dane(dane)
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
        for transakcja in dane:
            if transakcja['Typ'] == "Wydatek":
                suma_wydatków += transakcja['Kwota']
            elif transakcja['Typ'] == "Przychód":
                suma_przychodów += transakcja['Kwota']
        print(f"Wydatki: {suma_wydatków}")
        print(f"Przychody: {suma_przychodów}")
        print(f"Saldo: {suma_przychodów - suma_wydatków}")
    else:
        print("Nieprawidłowa opcja")
