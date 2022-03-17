INSERT INTO Bruker (epost, passord, fornavn, etternavn) values ('test@test.test', 'test', 'test', 'testesen');
INSERT INTO Bruker (epost, passord, fornavn, etternavn) values ('ola@normann.no', 'passord123', 'Ola', 'Normann');
INSERT INTO Bruker (epost, passord, fornavn, etternavn) values ('kari@normann.no', 'idiot123', 'Kari', 'Normann');
INSERT INTO KaffeRegion (regionID, navn, landsnavn) values ('0', 'Pereira', 'Colombia');
INSERT INTO KaffeRegion (regionID, navn, landsnavn) values ('1', 'Santa Ana', 'El Salvador');
INSERT INTO KaffeRegion (regionID, navn, landsnavn) values ('2', 'Calarcá', 'Colombia');
INSERT INTO KaffeGård (gårdID, høydeOverHavet, navn, regionID) values ('0', '1500', 'Nombre de Dios', '1');
INSERT INTO KaffeGård (gårdID, høydeOverHavet, navn, regionID) values ('1', '1200', 'Nombre de Playa', '0');
INSERT INTO KaffeGård (gårdID, høydeOverHavet, navn, regionID) values ('2', '1000', 'Nombre de Vamos', '0');
INSERT INTO KaffeBønne (bønnenavn, artsnavn) values ('Bourbon', 'c. arabica');
INSERT INTO KaffeBønne (bønnenavn, artsnavn) values ('Typica', 'c. arabica');
INSERT INTO KaffeBønne (bønnenavn, artsnavn) values ('Liberica', 'c. liberica');
INSERT INTO Foredlingsmetode (foredlingsID, navn, beskrivelse) values ('0', 'Vasket', 'Vi vasket det veldig godt.');
INSERT INTO Foredlingsmetode (foredlingsID, navn, beskrivelse) values ('1', 'Tørket', 'Vi tørket det veldig godt.');
INSERT INTO Foredlingsmetode (foredlingsID, navn, beskrivelse) values ('2', 'Bærtørket', 'Vi bærtørket det.');
INSERT INTO KanDyrkesAv (gårdID, bønnenavn) values ('0', 'Bourbon');
INSERT INTO KanDyrkesAv (gårdID, bønnenavn) values ('1', 'Typica');
INSERT INTO KanDyrkesAv (gårdID, bønnenavn) values ('1', 'Liberica');
INSERT INTO KaffeBønneParti (partiID, innhøstingsår, kiloprisTilGårdUSD, foredlingsID, gårdID) values ('0', '2021', '8', '2', '0');
INSERT INTO KaffeBønneParti (partiID, innhøstingsår, kiloprisTilGårdUSD, foredlingsID, gårdID) values ('1', '2011', '10', '1', '1');
INSERT INTO KaffeBønneParti (partiID, innhøstingsår, kiloprisTilGårdUSD, foredlingsID, gårdID) values ('2', '2022', '6', '0', '1');
INSERT INTO MedBønne (partiID, bønnenavn) values ('0', 'Bourbon');
INSERT INTO MedBønne (partiID, bønnenavn) values ('1', 'Typica');
INSERT INTO MedBønne (partiID, bønnenavn) values ('2', 'Liberica');
INSERT INTO Kaffe (brenningsgrad, dato, beskrivelse, kaffenavn, kiloprisKR, kaffebrenneri, kaffeID, partiID) values ('lysbrent', '2022-01-20', 'En velsmakende og kompleks kaffe for
mørketiden', 'Vinterkaffe 2022', '600', 'Trondheims-brenneriet Jacobsen & Svart', '0', '0');
INSERT INTO Kaffe (brenningsgrad, dato, beskrivelse, kaffenavn, kiloprisKR, kaffebrenneri, kaffeID, partiID) values ('lysbrent', '2022-02-20', 'En velsmakende og kompleks kaffe for
mørketiden, med ny smak', 'Vinterkaffe 2022', '660', 'Trondheims-brenneriet Jacobsen & Svart', '1', '1');
INSERT INTO Kaffe (brenningsgrad, dato, beskrivelse, kaffenavn, kiloprisKR, kaffebrenneri, kaffeID, partiID) values ('lysbrent', '2021-01-20', 'En velsmakende og kompleks kaffe for
mørketiden', 'Vinterkaffe 2021', '600', 'Trondheims-brenneriet Jacobsen & Svart', '2', '2');
INSERT INTO KaffeSmaking (kaffesmakingID, smaksnotater, poeng, dato, epost, kaffeID) values ('0', 'Wow
– en odyssé for smaksløkene: sitrusskall, melkesjokolade, aprikos!', '10', '2022-01-20', 'ola@normann.no', '0');
INSERT INTO KaffeSmaking (kaffesmakingID, smaksnotater, poeng, dato, epost, kaffeID) values ('1', 'Wow bortimot
– en odyssé for smaksløkene: sitrusskall, melkesjokolade, aprikos!', '9', '2022-01-22', 'ola@normann.no', '1');
INSERT INTO KaffeSmaking (kaffesmakingID, smaksnotater, poeng, dato, epost, kaffeID) values ('2', 'Wow nesten
– en odyssé for smaksløkene: sitrusskall, melkesjokolade, aprikos!', '8', '2022-01-23', 'ola@normann.no', '2');