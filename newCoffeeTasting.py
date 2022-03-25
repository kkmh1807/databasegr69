import sqlite3
import random
import textwrap
from tkinter.tix import MAIN
from pip import main
from datetime import date


# Denne filen, sammen med filen "seeCoffeeTastings" oppfyller brukerhistorie 1.
# Med funksjonen kan en bruker legge til nye kaffesmakinger.
def newCoffeeTasting(email):

    print("Skriv inn din kaffesmaking")

    # Få inn brukerinput
    roastery = input("Brenneri: ")
    coffeeName = input("Kaffenavn: ")

    # Kobler til databasen
    con = sqlite3.connect("kaffe.db")
    cursor = con.cursor()

    # Basert på brukerinput prøver vi å finne en kaffe som samsvarer. Vi utfører SQL spørringen mot databasen

    cursor.execute(
        "SELECT kaffeID, dato FROM Kaffe WHERE kaffebrenneri = ? and  kaffenavn = ?;", (roastery, coffeeName, ))
    coffeeList = cursor.fetchall()


    # Vi skal nå finne riktig kaffeID. Vi har nå fått tilbake et uvisst antall kaffe
    # basert på sql spørring med kaffebrenneri og kaffenavn som input. Brenningsdato
    # trengs dersom det er flere versjoner av samme kaffe.
    coffeeID = ""
    if(coffeeList == None or len(coffeeList) == 0):
        # Dersom det ikke finnes noen kaffe som samsvarer med brukerinput
        # vil en feilmelding printes til bruker og kaffesmakingen avbrytes.
        print("Fant ingen kaffe. ")
        return
    # Dersom det kun finnes 1 kaffe i listen har vi allerede funnet
    # riktig kaffe og har da riktig kaffeID.
    elif len(coffeeList) == 1:
        coffeeID = coffeeList[0][0]
    # Det finnes altså flere kaffe i listen, og vi må da få brukerinput på
    # brenningsdato for å identifisere riktig kaffe.
    else:
        # Oppretter en liste over brenningsdatoer for kaffen.
        coffeeBurnDates = {}
        for row in coffeeList:
            # row[0] er kaffeID og row[2] er dato
            coffeeBurnDates[row[0]] = row[1]

        burnDate = ""
        print("Skriv inn brenningsdato for din kaffe. De mulige datoene er: ")
        for row in coffeeList:
            print(row[1])
        burnDate = input("Dato(YYYY-MM-DD): ")
        while (not burnDate in coffeeBurnDates.values()):
            print("Ugyldig dato, prøv igjen")
            burnDate = input("Dato(YYYY-MM-DD): ")

        # Finner kaffeID som hører til valgt dato
        coffeeIDs = list(coffeeBurnDates.keys())
        dates = list(coffeeBurnDates.values())
        position = dates.index(burnDate)
        coffeeID = coffeeIDs[position]

    # Nå har man hentet ut riktig kaffe for kaffesmakingen, og vi
    # fortsetter å hente brukerinput for poeng og smaksnotat.
    points = input("Poeng: ")
    while(not points.isdigit and 0 <= points <= 10):
        print("Ugyldig poeng, prøv igjen")
        points = input("Poeng: ")
    tasteNotes = input("Smaksnotat: ")

    # All brukerinput er hentet ut, og vi kjører sql spørring for
    # å sette inn kaffesmakingen.
    script = "INSERT INTO kaffesmaking  (kaffesmakingID, smaksnotater,  poeng, dato, epost, kaffeID) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(script, (random.randint(0, 1000000000), tasteNotes, points, date.today(), email, coffeeID))

    con.commit()
    con.close()


def main():
    newCoffeeTasting()


if __name__ == "__main__":
    main()
