import pprint
adat_gyujto = []
with open("lakossag_2025.csv", "r", encoding="UTF-8") as fajl:
    fajl.readline()
    for sor in fajl:
        adatok = sor.strip().split(";")
        if len(adatok) < 5:
            continue
        leiras = {
            "megyekod": adatok[0],
            "telepules": adatok[1],
            "tipus": adatok[2],
            "ferfi": int(adatok[3].replace(" ", "")),
            "no": int(adatok[4].replace(" ", ""))
        }
        adat_gyujto.append(leiras)

while True:
    print("\t Főmenü \t")
    print("[1] Megye adatai")
    print("[2] Település típusai")
    print("[X] Exit")

    choice = input("Válassz egyet: ").strip().upper()

    if choice == "1":
        megye_bekero = input("Írd be a megyéd azonosítóját: ")
        telepulesek_szama = 0
        osszes_lakos = 0
        varoslakok = 0

        for leiras in adat_gyujto:
            if megye_bekero.upper() == leiras["megyekod"]:
                telepulesek_szama += 1
                osszes_lakos = osszes_lakos + (leiras["ferfi"] + leiras["no"])
                if "város" in leiras["tipus"] or "fővárosi kerület" in leiras["tipus"] or "vármegye székhely" in leiras["tipus"] or "vármegyei jogú város" in leiras["tipus"]:
                    varoslakok = varoslakok + (leiras["ferfi"] + leiras["no"])

        print(f" A beirt {megye_bekero.upper()} kódú megye adatai:")
        print(f"Az ebben a megyében található  települések száma: {telepulesek_szama}")
        print(f"Az ebben a megyében élő emberek száma: {osszes_lakos} fő")
        print(f"A megye városainak lakossága: {varoslakok} fő")

    if choice == "2":
            tipus_lista = {
                "1": "város",
                "2": "község",
                "3": "fővárosi kerület",
                "4": "vármegye székhely",
                "5": "vármegyei jogú város",
                "6": "nagyközség",
            }

            print("[1]  Város")
            print("[2] Község")
            print("[3] Fővárosi kerület")
            print("[4] Vármegye székhely")
            print("[5] Vármegyei jogú város")
            print("[6] Nagyközség")
            tipus_valasztas = input("Válassz egy település típust: ").strip()

            if tipus_valasztas not in tipus_lista:
                print("Nincs ilyen menüpont!")
            else:
                telepules_tipus_bekero = tipus_lista[tipus_valasztas]
                kivalasztottak = []

                for leiras in adat_gyujto:
                    if telepules_tipus_bekero.lower() == leiras["tipus"].lower():
                        kivalasztottak.append(leiras)
                print(f" Összesen {len(kivalasztottak)} darab ilyen település van: ")

                if len(kivalasztottak) == 0:
                    print("Nincs találat ezzel a település típussal :(")
                else:
                    oldal_kezdete = 0  # az aktuális oldal első elemének indexe

                    while True:
                        print("\t Település adatok \t")

                        varosok_elorehaladas = oldal_kezdete
                        for i in range(10):
                            if varosok_elorehaladas < len(kivalasztottak):
                                telepules = kivalasztottak[varosok_elorehaladas]
                                lakossag = telepules["ferfi"] + telepules["no"]
                                print(f"{telepules['telepules']}: {lakossag} fő")
                                varosok_elorehaladas += 1
                            else:
                                break

                        print("[<]  Vissza")
                        print("[>] Tovább")
                        print("[X] Exit")

                        choice2 = input().strip().upper()

                        if choice2 == ">":
                            if oldal_kezdete + 10 < len(kivalasztottak):
                                oldal_kezdete += 10
                            else:
                                print("Ez az utolsó oldal!")
                        elif choice2 == "<":
                            if oldal_kezdete - 10 >= 0:
                                oldal_kezdete -= 10
                            else:
                                print("Ez az első oldal!")
                        elif choice2 == "X":
                            print("Kiléptél a lapozásból!")
                            break

    if choice == "X":
        print("Kiléptél!")
        break