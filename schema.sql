DROP TABLE IF EXISTS Mesures;
DROP TABLE IF EXISTS Types_Valeur;
DROP TABLE IF EXISTS Procedures_Mesure;
DROP TABLE IF EXISTS Types_Evaluation;
DROP TABLE IF EXISTS Types_Influence;
DROP TABLE IF EXISTS Polluants;
DROP TABLE IF EXISTS Stations;
DROP TABLE IF EXISTS Zas;
DROP TABLE IF EXISTS Organismes;
DROP TABLE IF EXISTS Reglementaires;
DROP TABLE IF EXISTS Discriminants;

CREATE TABLE Organismes (
    Id_Organisme INTEGER PRIMARY KEY,
    Nom_Organisme TEXT UNIQUE -- Organisme
);

CREATE TABLE Zas (
    Id_Zas INTEGER PRIMARY KEY,
    Id_Organisme INTEGER,
    Code_Zas TEXT UNIQUE, -- code zas
    Nom_Zas TEXT, -- Zas
    FOREIGN KEY (Id_Organisme) REFERENCES Organismes(Id_Organisme)
);

CREATE TABLE Stations (
    Id_Station INTEGER PRIMARY KEY,
    Id_Zas INTEGER,
    Code_Site TEXT UNIQUE, --code site
    Nom_Site TEXT, -- nom site
    Type_Implantation TEXT, -- type d'implantation
    FOREIGN KEY (Id_Zas) REFERENCES Zas(Id_Zas)
);

CREATE TABLE Polluants (
    Id_Polluant INTEGER PRIMARY KEY,
    Nom_Polluant TEXT UNIQUE -- Polluant
);

CREATE TABLE Types_Influence (
    Id_Type_Influence INTEGER PRIMARY KEY,
    Nom_Type_Influence TEXT UNIQUE -- type d'influence
);

CREATE TABLE Types_Evaluation (
    Id_Type_Evaluation INTEGER PRIMARY KEY,
    Nom_Type_Evaluation TEXT UNIQUE -- type d'évaluation
);

CREATE TABLE Procedures_Mesure (
    Id_Procedure_Mesure INTEGER PRIMARY KEY,
    Nom_Procedure_Mesure TEXT UNIQUE -- procédure de mesure
);

CREATE TABLE Types_Valeur (
    Id_Type_Valeur INTEGER PRIMARY KEY,
    Nom_Types_Valeur TEXT UNIQUE -- type de valeur
);

CREATE TABLE Reglementaires (
    Id_Reglementaire INTEGER PRIMARY KEY,
    Nom_Reglementaire TEXT UNIQUE -- Réglémentaire
);

CREATE TABLE Discriminants (
    Id_Discriminant INTEGER PRIMARY KEY,
    Nom_Discriminant TEXT UNIQUE -- discriminant
);

CREATE TABLE Mesures (
    Id_Mesure INTEGER PRIMARY KEY,
    Id_Station INTEGER,
    Id_Polluant INTEGER,
    Id_Type_Influence INTEGER,
    Id_Type_Evaluation INTEGER,
    Id_Procedure INTEGER,
    Id_Type_Valeur INTEGER,
    Id_Discriminant INTEGER,
    Id_Reglementaire INTEGER,
    Id_Organisme INTEGER,
    Id_Zas INTEGER,
    Date_Debut DATE, -- Date de début
    Date_Fin DATE, -- Date de fin
    Valeur REAL, -- valeur
    Valeur_Brute REAL, -- valeur brute
    Unite_Mesure TEXT, -- unité de mesure
    Taux_Saisie REAL, -- taux de saisie
    Couverture_Temporelle REAL, -- couverture temporelle
    Couverture_Donnees REAL, -- couverture des données
    Code_Qualite TEXT, -- code qualité
    Validite INTEGER, -- validité
    FOREIGN KEY (Id_Station) REFERENCES Stations(Id_Station),
    FOREIGN KEY (Id_Polluant) REFERENCES Polluants(Id_Polluant),
    FOREIGN KEY (Id_Type_Influence) REFERENCES Types_Influence(Id_Type_Influence),
    FOREIGN KEY (Id_Type_Evaluation) REFERENCES Types_Evaluation(Id_Type_Evaluation),
    FOREIGN KEY (Id_Procedure) REFERENCES Procedures_Mesure(Id_Procedure),
    FOREIGN KEY (Id_Type_Valeur) REFERENCES Types_Valeur(Id_Type_Valeur),
    FOREIGN KEY (Id_Discriminant) REFERENCES Discriminants(Id_Discriminant),
    FOREIGN KEY (Id_Reglementaire) REFERENCES Reglementaires(Id_Reglementaire),
    FOREIGN KEY (Id_Organisme) REFERENCES Organismes(Id_Organisme),
    FOREIGN KEY (Id_Zas) REFERENCES Zas(Id_Zas)
);
