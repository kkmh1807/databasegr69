
CREATE TABLE Bruker
(
  epost VARCHAR(320) NOT NULL,
  passord VARCHAR(60) NOT NULL,
  fornavn VARCHAR(50) NOT NULL,
  etternavn VARCHAR(50) NOT NULL,
  PRIMARY KEY (epost)
);

CREATE TABLE Foredlingsmetode
(
  foredlingsID INT NOT NULL,
  navn VARCHAR(50) NOT NULL,
  beskrivelse VARCHAR(500) NOT NULL,
  PRIMARY KEY (foredlingsID)
);

CREATE TABLE Kaffebønne
(
  bønnenavn VARCHAR NOT NULL,
  artsnavn VARCHAR NOT NULL,
  PRIMARY KEY (bønnenavn)
);

CREATE TABLE KaffeRegion
(
  regionID INT NOT NULL,
  navn VARCHAR(50) NOT NULL,
  landsnavn VARCHAR(60) NOT NULL,
  PRIMARY KEY (regionID)
);

CREATE TABLE Kaffegård
(
  gårdID INT NOT NULL,
  høydeOverHavet INT NOT NULL,
  navn VARCHAR(50) NOT NULL,
  regionID INT NOT NULL,
  PRIMARY KEY (gårdID),
  FOREIGN KEY (regionID) REFERENCES KaffeRegion(regionID)
);

CREATE TABLE KanDyrkesAv
(
  gårdID INT NOT NULL,
  bønnenavn VARCHAR NOT NULL,
  PRIMARY KEY (gårdID, bønnenavn),
  FOREIGN KEY (gårdID) REFERENCES Kaffegård(gårdID),
  FOREIGN KEY (bønnenavn) REFERENCES Kaffebønne(bønnenavn)
);

CREATE TABLE KaffebønneParti
(
  partiID INT NOT NULL,
  innhøstingsår INT NOT NULL,
  kiloprisTilGårdUSD FLOAT NOT NULL,
  foredlingsID INT NOT NULL,
  gårdID INT NOT NULL,
  PRIMARY KEY (partiID),
  FOREIGN KEY (foredlingsID) REFERENCES Foredlingsmetode(foredlingsID),
  FOREIGN KEY (gårdID) REFERENCES Kaffegård(gårdID)
);

CREATE TABLE MedBønne
(
  partiID INT NOT NULL,
  bønnenavn VARCHAR NOT NULL,
  PRIMARY KEY (partiID, bønnenavn),
  FOREIGN KEY (partiID) REFERENCES KaffebønneParti(partiID),
  FOREIGN KEY (bønnenavn) REFERENCES Kaffebønne(bønnenavn)
);

CREATE TABLE Kaffe
(
  kaffeID INT NOT NULL,
  brenningsgrad VARCHAR(10) NOT NULL,
  dato DATE NOT NULL,
  beskrivelse VARCHAR(500) NOT NULL,
  kaffenavn VARCHAR(50) NOT NULL,
  kiloprisKR FLOAT NOT NULL,
  kaffebrenneri VARCHAR(50) NOT NULL,
  partiID INT NOT NULL,
  PRIMARY KEY (kaffeID),
  FOREIGN KEY (partiID) REFERENCES KaffebønneParti(partiID)
);

CREATE TABLE Kaffesmaking
(
  kaffesmakingID INT NOT NULL,
  smaksnotater VARCHAR(500) NOT NULL,
  poeng INT NOT NULL,
  dato DATE NOT NULL,
  epost VARCHAR(320) NOT NULL,
  kaffeID INT NOT NULL,
  PRIMARY KEY (kaffesmakingID),
  FOREIGN KEY (epost) REFERENCES Bruker(epost)
  ON UPDATE CASCADE ON DELETE CASCADE,
  FOREIGN KEY (kaffeID) REFERENCES Kaffe(kaffeID)
  ON UPDATE CASCADE ON DELETE CASCADE
);
