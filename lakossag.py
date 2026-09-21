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

        if telepulesek_szama == 0:
            print('Nincs ilyen megyekód! \n')
        
        else:   
            print(f" A beirt {megye_bekero.upper()} kódú megye adatai:")
            print(f"Az ebben a megyében található  települések száma: {telepulesek_szama}")
            print(f"Az ebben a megyében élő emberek száma: {osszes_lakos} fő")
            print(f"A megye városainak lakossága: {varoslakok} fő")           
        

    if choice == "2":
        tipusok = sorted(set(leiras["tipus"] for leiras in adat_gyujto))

        print("Elérhető típusok:", ", ".join(tipusok))
        telepules_tipus_bekero = input("Írd be a település típusát: ").strip().lower()

        if telepules_tipus_bekero not in tipusok:
            print("Nincs ilyen típus!")
        else:
            kivalasztottak = [
                leiras for leiras in adat_gyujto
                if leiras["tipus"] == telepules_tipus_bekero
            ]

            print(f" Összesen {len(kivalasztottak)} darab ilyen település van: ")

            oldalmeret = 10
            oldalak = [kivalasztottak[i:i + oldalmeret] for i in range(0, len(kivalasztottak), oldalmeret)]
            aktualis_oldal = 0

            while True:
                print("\t Település adatok \t")
                for telepules in oldalak[aktualis_oldal]:
                    lakossag = telepules["ferfi"] + telepules["no"]
                    print(f"{telepules['telepules']}: {lakossag} fő")

                print(f"({aktualis_oldal + 1}. / {len(oldalak)}. oldal)")
                print("[<] Vissza  [>] Tovább  [X] Exit")
                choice2 = input().strip().upper()

                if choice2 == ">":
                    if aktualis_oldal + 1 < len(oldalak):
                        aktualis_oldal += 1
                    else:
                        print("Ez az utolsó oldal!")
                elif choice2 == "<":
                    if aktualis_oldal - 1 >= 0:
                        aktualis_oldal -= 1
                    else:
                        print("Ez az első oldal!")
                elif choice2 == "X":
                    print("Kiléptél a lapozásból!")
                    break
             
    if choice == "X":
        print("Kiléptél!")
        break