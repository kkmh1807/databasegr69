import sqlite3
import textwrap
from datetime import date

# Denne filen, sammen med filen "newCoffeeTasting" oppfyller brukerhistorie 1.
# En bruker se kaffesmakinger som er lagt ut. Funksjonen henter ut både
# brukerinput om smaksnotat og poeng, men også all annen relevant informasjon om
# kaffen som er blitt smakt.
def seeCoffeeTastings():

    print("Kaffesmakinger:")

    # Kobler til databasen
    con = sqlite3.connect("kaffe.db")
    con.row_factory = sqlite3.Row
    cursor = con.cursor()

    # Utfører SQL spørringen mot databasen
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

    # For hver rad i resultatet skriver vi ut en kaffesmaking i pent format
    for row in coffeeList:
        date = row[3] # Prefix som viser hvilken dato kaffen ble smakt på
        prefix = date + ": "
        preferredWidth = 70 # Bredden på utprintfeltet
        wrapper = textwrap.TextWrapper(initial_indent=prefix, width=preferredWidth,
                                       subsequent_indent=' '*len(prefix)) # Fint utskriftformat
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
