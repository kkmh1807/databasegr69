import sqlite3
import random


def nyKaffeSmaking(epost):

    print("Skriv inn din kaffesmaking")

   # input er brenneri, kaffenavn, poeng, dato og smaksnotat

    # Få inn brukerinput
    brenneri = input("Brenneri: ")
    kaffenavn = input("Kaffenavn: ")
    poeng = input("Poeng: ")
    while(not poeng.isdigit and 0 <= poeng <= 10):
        print("Ugyldig poeng, prøv igjen")
        poeng = input("Poeng: ")
    smaksnotat = input("Smaksnotat: ")

    con = sqlite3.connect("kaffe.db")

    cursor = con.cursor()

    cursor.execute(
        "SELECT * FROM Kaffe WHERE kaffebrenneri = ? and  kaffenavn = ?;", (brenneri, kaffenavn, ))
    coffeeList = cursor.fetchall()

    if(coffeeList == None or len(coffeeList) == 0):
        print("Fant ingen kaffe. ")
        return

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
    cursor.execute(script, (random.randint(0, 10000000),
                            smaksnotat, poeng, dato, epost, kaffeID))

    con.commit()
    con.close()
