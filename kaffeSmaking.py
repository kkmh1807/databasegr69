import sqlite3
import random
import textwrap
from tkinter.tix import MAIN
from pip import main

# Denne filen oppfyller brukerhistorie 1, ved å implementere funksjonene nyKaffeSmaking og seKaffeSmakinger.
# Dermed kan en bruker legge til nye kaffesmakinger og se kaffesmakinger som er lagt ut. SeKaffeSmakinger
# funksjonen henter ut både brukerinput om smaksnotat og poeng, men også all annen relevant informasjon om
# kaffen som er blitt smakt.


def nyKaffeSmaking(epost):

    print("Skriv inn din kaffesmaking")

   # input er brenneri, kaffenavn, poeng, dato og smaksnotat

    # Få inn brukerinput
    brenneri = input("Brenneri: ")
    kaffenavn = input("Kaffenavn: ")

    con = sqlite3.connect("kaffe.db")

    cursor = con.cursor()

    cursor.execute(
        "SELECT * FROM Kaffe WHERE kaffebrenneri = ? and  kaffenavn = ?;", (brenneri, kaffenavn, ))
    coffeeList = cursor.fetchall()

    if(coffeeList == None or len(coffeeList) == 0):
        print("Fant ingen kaffe. ")
        return

    poeng = input("Poeng: ")
    while(not poeng.isdigit and 0 <= poeng <= 10):
        print("Ugyldig poeng, prøv igjen")
        poeng = input("Poeng: ")
    smaksnotat = input("Smaksnotat: ")

    coffeeDictionary = {}
    for row in coffeeList:
        # row[0] er kaffeID og row[2] er dato
        coffeeDictionary[row[0]] = row[2]

    dato = ""
    if len(coffeeDictionary) > 1:
        print("Skriv inn brenningsdato for din kaffe. De mulige datoene er: ")
        for kaffeID in coffeeDictionary:
            print(coffeeDictionary[kaffeID])
        dato = input("Dato(YYYY-MM-DD): ")
        while (not dato in coffeeDictionary.values()):
            print("Ugyldig dato, prøv igjen")
            dato = input("Dato(YYYY-MM-DD): ")

    # Finner kaffeID som hører til dato valgt
    key_list = list(coffeeDictionary.keys())
    val_list = list(coffeeDictionary.values())
    position = val_list.index(dato)
    kaffeID = key_list[position]

    script = 'INSERT INTO kaffesmaking  (kaffesmakingID, smaksnotater,  poeng, dato, epost, kaffeID) VALUES (?, ?, ?, ?, ?, ?)'
    cursor.execute(script, (random.randint(0, 1000000000),
                            smaksnotat, poeng, dato, epost, kaffeID))

    con.commit()
    con.close()


def seKaffeSmakinger():

    print("Kaffesmakinger:")

    con = sqlite3.connect("kaffe.db")

    cursor = con.cursor()

    cursor.execute("""SELECT smaksnotater, poeng, brenningsgrad, KS.dato, K.dato, K.beskrivelse, kaffenavn, kiloprisKR, kaffebrenneri, innhøstingsår, kiloprisTilGårdUSD, F.navn, KB.bønnenavn, KB.artsnavn, KG.høydeOverHavet, KG.navn, KR.navn, KR.landsnavn, B.fornavn, B.etternavn, B.epost
                    FROM Kaffesmaking as KS, Kaffe as K, KaffebønneParti as P, Foredlingsmetode as F, MedBønne as M, Kaffebønne as KB, Kaffegård as KG, KaffeRegion as KR, Bruker as B
                    WHERE KS.kaffeID = K.kaffeID and K.partiID = P.partiID and P.foredlingsID = F.foredlingsID and P.partiID = M.partiID and M.bønnenavn = KB.bønnenavn and P.gårdID = KG.gårdID and KG.regionID = KR.regionID and KS.epost = B.epost""")
    coffeeList = cursor.fetchall()

    for row in coffeeList:
        date = row[3]
        prefix = date + ": "
        preferredWidth = 70
        wrapper = textwrap.TextWrapper(initial_indent=prefix, width=preferredWidth,
                                       subsequent_indent=' '*len(prefix))
        print(wrapper.fill(
            """{} {} ({}) smaker kaffen {} fra {} (brent {}), gir den {} poeng og skriver «{}». Kaffen er {}, {} {} ({}), kommer fra gården {} ({} moh.) i {}, {}, har en kilopris på {} kr og er ifølge brenneriet «{}». Kaffen ble høstet i {} og gården fikk utbetalt {} USD per kg kaffe."""
            .format(row[18], row[19], row[20], row[6], row[8], row[4], row[1],
                    row[0], row[2], row[11], row[12], row[13], row[15], str(
                    row[14]), row[16], row[17],
                    int(row[7]), row[5], row[9], int(row[10])))
              )
    con.commit()
    con.close()


def main():
    seKaffeSmakinger()


if __name__ == "__main__":
    main()
