from datetime import date
import sqlite3
import textwrap

from sympy import DenseNDimArray

# Denne filen oppfyller brukerhistorie 3.


def besteKjøp():
    con = sqlite3.connect("kaffe.db")
    cursor = con.cursor()

    cursor.execute(
        """SELECT kaffebrenneri, kaffenavn, kiloprisKR, avg(poeng)/kaffe.kiloprisKR
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
        prefix = "Nr." + str(ind) + ": "
        ind += 1
        preferredWidth = 70
        wrapper = textwrap.TextWrapper(initial_indent=prefix, width=preferredWidth,
                                       subsequent_indent=' '*len(prefix))
        print(wrapper.fill(
            "<<{}>> fra brenneriet {} koster {}kr og fikk en score (poeng-gjennomsnittsscore kontra pris) på {}".format(row[1], row[0], row[2], round(row[3], 4))))

    con.commit()
    con.close()


def main():
    besteKjøp()


if __name__ == "__main__":
    main()
