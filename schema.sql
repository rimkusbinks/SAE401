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
DROP TABLE IF EXISTS Unites_Mesure;
DROP TABLE IF EXISTS Codes_Qualite;

CREATE TABLE Organismes (
    Id_Organisme INTEGER PRIMARY KEY,
    Organisme TEXT UNIQUE -- Organisme
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
    Polluant TEXT UNIQUE -- Polluant
);

CREATE TABLE Types_Influence (
    Id_Type_Influence INTEGER PRIMARY KEY,
    Type_Influence TEXT UNIQUE -- type d'influence
);

CREATE TABLE Types_Evaluation (
    Id_Type_Evaluation INTEGER PRIMARY KEY,
    Type_Evaluation TEXT UNIQUE -- type d'évaluation
);

CREATE TABLE Procedures_Mesure (
    Id_Procedure_Mesure INTEGER PRIMARY KEY,
    Procedure_Mesure TEXT UNIQUE -- procédure de mesure
);

CREATE TABLE Types_Valeur (
    Id_Type_Valeur INTEGER PRIMARY KEY,
    Type_Valeur TEXT UNIQUE -- type de valeur
);

CREATE TABLE Discriminants (
    Id_Discriminant INTEGER PRIMARY KEY,
    Discriminant TEXT UNIQUE -- discriminant
);

CREATE TABLE Unites_Mesure (
    Id_Unite_Mesure INTEGER PRIMARY KEY,
    Unite_Mesure TEXT UNIQUE -- unité de mesure
);

CREATE TABLE Codes_Qualite (
    Id_Code_Qualite INTEGER PRIMARY KEY,
    Code_Qualite TEXT UNIQUE -- code qualité
);

CREATE TABLE Mesures (
    Id_Mesure INTEGER PRIMARY KEY,
    Id_Station INTEGER,
    Id_Polluant INTEGER,
    Id_Type_Influence INTEGER,
    Id_Type_Evaluation INTEGER,
    Id_Procedure_Mesure INTEGER,
    Id_Type_Valeur INTEGER,
    Id_Discriminant INTEGER,
    Id_Organisme INTEGER,
    Id_Zas INTEGER,
    Id_Unite_Mesure INTEGER, -- unité de mesure
    Id_Code_Qualite INTEGER,
    Date_Debut DATE, -- Date de début
    Date_Fin DATE, -- Date de fin
    Valeur REAL, -- valeur
    Valeur_Brute REAL, -- valeur brute
    Taux_Saisie REAL, -- taux de saisie
    Couverture_Temporelle REAL, -- couverture temporelle
    Couverture_Donnees REAL, -- couverture des données
    Validite INTEGER, -- validité
    Reglementaire TEXT, -- Réglementaire
    FOREIGN KEY (Id_Station) REFERENCES Stations(Id_Station),
    FOREIGN KEY (Id_Polluant) REFERENCES Polluants(Id_Polluant),
    FOREIGN KEY (Id_Type_Influence) REFERENCES Types_Influence(Id_Type_Influence),
    FOREIGN KEY (Id_Type_Evaluation) REFERENCES Types_Evaluation(Id_Type_Evaluation),
    FOREIGN KEY (Id_Procedure_Mesure) REFERENCES Procedures_Mesure(Id_Procedure),
    FOREIGN KEY (Id_Type_Valeur) REFERENCES Types_Valeur(Id_Type_Valeur),
    FOREIGN KEY (Id_Discriminant) REFERENCES Discriminants(Id_Discriminant),
    FOREIGN KEY (Id_Organisme) REFERENCES Organismes(Id_Organisme),
    FOREIGN KEY (Id_Zas) REFERENCES Zas(Id_Zas),
    FOREIGN KEY (Id_Unite_Mesure) REFERENCES Unites_Mesure(Id_Unite_Mesure),
    FOREIGN KEY (Id_Code_Qualite) REFERENCES Codes_Qualite(Id_Code_Qualite)
);

SELECT 
    Mesures.Date_Debut, 
    Mesures.Date_Fin, 
    Mesures.Valeur, 
    Mesures.Valeur_Brute, 
    Unites_Mesure.Unite_Mesure, 
    Mesures.Taux_Saisie, 
    Mesures.Couverture_Temporelle, 
    Mesures.Couverture_Donnees, 
    Codes_Qualite.Code_Qualite,
    Mesures.Validite,
    Mesures.Reglementaire,
    Stations.Code_Site, 
    Stations.Nom_Site, 
    Stations.Type_Implantation, 
    Polluants.Polluant, 
    Types_Influence.Type_Influence, 
    Types_Evaluation.Type_Evaluation,
    Types_Valeur.Type_Valeur,
    Discriminants.Discriminant,
    Procedures_Mesure.Procedure_Mesure, 
    Organismes.Organisme, 
    Zas.Code_Zas, 
    Zas.Nom_Zas
FROM Mesures
LEFT JOIN Polluants ON Mesures.Id_Polluant = Polluants.Id_Polluant
LEFT JOIN Types_Influence ON Mesures.Id_Type_Influence = Types_Influence.Id_Type_Influence
LEFT JOIN Types_Evaluation ON Mesures.Id_Type_Evaluation = Types_Evaluation.Id_Type_Evaluation
LEFT JOIN Types_Valeur ON Mesures.Id_Type_Valeur = Types_Valeur.Id_Type_Valeur
LEFT JOIN Discriminants ON Mesures.Id_Discriminant = Discriminants.Id_Discriminant
LEFT JOIN Procedures_Mesure ON Mesures.Id_Procedure_Mesure = Procedures_Mesure.Id_Procedure_Mesure
LEFT JOIN Codes_Qualite ON Mesures.Id_Code_Qualite = Codes_Qualite.Id_Code_Qualite
LEFT JOIN Stations ON Mesures.Id_Station = Stations.Id_Station
LEFT JOIN Zas ON Stations.Id_Zas = Zas.Id_Zas
LEFT JOIN Organismes ON Zas.Id_Organisme = Organismes.Id_Organisme
LEFT JOIN Unites_Mesure ON Mesures.Id_Unite_Mesure = Unites_Mesure.Id_Unite_Mesure;
