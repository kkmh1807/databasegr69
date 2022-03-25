import sqlite3
import textwrap
from datetime import date

def seeCoffeeTastings():

    print("Kaffesmakinger:")

    con = sqlite3.connect("kaffe.db")
    con.row_factory = sqlite3.Row
    cursor = con.cursor()

    cursor.execute("""SELECT smaksnotater, poeng, brenningsgrad, KS.dato as smakingsdato, K.dato as brenningsdato,
                    K.beskrivelse, kaffenavn, kiloprisKR, kaffebrenneri, innhøstingsår, kiloprisTilGårdUSD,
                    F.navn as foredlingsmetodenavn, KB.bønnenavn, KB.artsnavn, KG.høydeOverHavet,
                    KG.navn as gårdsNavn, KR.navn as regionsNavn, KR.landsnavn, B.fornavn, B.etternavn, B.epost
                    FROM Kaffesmaking as KS, Kaffe as K, KaffebønneParti as P, Foredlingsmetode as F,
                    MedBønne as M, Kaffebønne as KB, Kaffegård as KG, KaffeRegion as KR, Bruker as B
                    WHERE KS.kaffeID = K.kaffeID and K.partiID = P.partiID and
                    P.foredlingsID = F.foredlingsID and P.partiID = M.partiID and
                    M.bønnenavn = KB.bønnenavn and P.gårdID = KG.gårdID and KG.regionID = KR.regionID
                    and KS.epost = B.epost""")
    coffeeList = cursor.fetchall()

    for row in coffeeList:
        date = row[3]
        prefix = date + ": "
        preferredWidth = 70
        wrapper = textwrap.TextWrapper(initial_indent=prefix, width=preferredWidth,
                                       subsequent_indent=' '*len(prefix))
        print(wrapper.fill(
            """{firstName} {lastName} ({email}) smaker kaffen
            {coffeeName} fra {roastery} (brent {burnDate}), gir den {points} poeng og skriver
            «{tasteNotes}». Kaffen er {burnDegree}, {processingMethod}
            {bean} ({beanSpecies}), kommer fra gården {farmName}
            ({metersAboveSea} moh.) i {region}, {country}, har en kilopris på
            {price} kr og er ifølge brenneriet «{description}». Kaffen ble høstet i
            {harvestDate} og gården fikk utbetalt {priceToFarm} USD per kg kaffe."""
            .format(firstName=row['fornavn'], lastName=row['etternavn'], email=row['epost'],
                    coffeeName=row['kaffenavn'], roastery=row['kaffebrenneri'],
                    burnDate=row['brenningsdato'], points=row['poeng'], tasteNotes=row['smaksnotater'],
                    burnDegree=row['brenningsgrad'], processingMethod=row['foredlingsmetodenavn'],
                    bean=row['bønnenavn'], beanSpecies=row['artsnavn'], farmName=row['gårdsNavn'],
                    metersAboveSea=str(row['høydeOverHavet']), region=row['regionsNavn'],
                    country=row['landsnavn'], price=int(row['kiloprisKR']), description=row['beskrivelse'],
                    harvestDate=row['innhøstingsår'], priceToFarm=int(row['kiloprisTilGårdUSD'])))
              )
    con.commit()
    con.close()


def main():
    seeCoffeeTastings()


if __name__ == "__main__":
    main()
