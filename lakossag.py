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
                continue
            else:
                continue
        print(f" A beirt {megye_bekero.upper()} kódú megye adatai:")
        print(f"Az ebben a megyében található  települések száma: {telepulesek_szama}")
        print(f"Az ebben a megyében élő emberek száma: {osszes_lakos} fő")
        print(f"A megye városainak lakossága: {varoslakok} fő")
        
    if choice == "2":
        telepules_tipus_bekero = input("Írj be egy település típust amire kíváncsi vagy(pl. város, község, stb...: )")
        kivalasztottak = []
        
        for leiras in adat_gyujto:
            if telepules_tipus_bekero.lower() == leiras["tipus"]:
                kivalasztottak.append(leiras)
        print(f" Összesen {len(kivalasztottak)} darab ilyen település van: ")
        
        varosok_elorehaladas = 0

        for i in range(10):
            if varosok_elorehaladas < len(kivalasztottak):
                print(kivalasztottak[varosok_elorehaladas])
                varosok_elorehaladas += 1
            else:
                break
                
        if len(kivalasztottak) == 0:
            print("Nincs találat ezzel a település típussal :(")

        while True:
            print("\t Település adatok \t")
            print("[<]  Vissza")
            print("[>] Tovább")
            print("[X] Exit")

            choice2 = input()
    
    if choice == "X":
        print("Kiléptél")
        break