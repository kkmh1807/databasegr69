from datetime import date
import sqlite3
import textwrap

from sympy import DenseNDimArray

# Denne filen oppfyller brukerhistorie 3.

def bestBuy():
    # Kobler til databasen
    con = sqlite3.connect("kaffe.db")
    con.row_factory = sqlite3.Row
    cursor = con.cursor()

    # Utfører SQL spørringen mot databasen
    cursor.execute(
        """SELECT kaffebrenneri, kaffenavn, Kaffe.dato as brenningsdato, kiloprisKR,
        avg(poeng)/kaffe.kiloprisKR as gjennomsnittsscore
        FROM Kaffesmaking, Kaffe
        WHERE Kaffesmaking.kaffeID = Kaffe.kaffeID
        GROUP BY Kaffesmaking.kaffeID
        ORDER BY avg(poeng)/kaffe.kiloprisKR DESC""")
    coffeeList = cursor.fetchall()

    if(coffeeList == None or len(coffeeList) == 0):
        print("Det finnes ingen beste kaffe!")
        return
    else:
        print("Toppliste over kaffe som gir deg mest for pengene, sortert synkende:")

    ind = 1
    for row in coffeeList:
        prefix = "Nr." + str(ind) + ": " # Prefix som viser hvilken plass kaffen kom på
        ind += 1
        preferredWidth = 70 # Bredden på utprintfeltet
        wrapper = textwrap.TextWrapper(initial_indent=prefix, width=preferredWidth,
                                       subsequent_indent=' '*len(prefix)) # Fint utskriftformat
        print(wrapper.fill(
            """<<{coffeeName}>>(brent: {burnDate}) fra brenneriet
            {roastery} koster {price}kr og fikk en
            score (poeng-gjennomsnittsscore kontra pris) på {averageScore}"""
            .format(coffeeName=row['kaffenavn'], burnDate=row['brenningsdato'], roastery=row['kaffebrenneri'],
            price=row['kiloprisKR'], averageScore=round(row['gjennomsnittsscore'], 4))))

    con.commit()
    con.close()


def main():
    bestBuy()


if __name__ == "__main__":
    main()
