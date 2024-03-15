-- concentrations moyenne polluants 
CREATE VIEW Concentrations_Moyennes_Polluants AS
SELECT 
    Polluants.Polluant,
    AVG(Mesures.Valeur) AS Concentration_Moyenne,
    Mesures.Date_Debut AS Date
FROM 
    Mesures
INNER JOIN 
    Polluants ON Mesures.Id_Polluant = Polluants.Id_Polluant
GROUP BY 
    Polluants.Polluant, 
    Mesures.Date_Debut;

-- dépassement des seuils réglementaires
CREATE VIEW Depassements_Seuils_Reglementaires AS
SELECT 
    Polluants.Polluant, 
    Mesures.Valeur,
    Mesures.Date_Debut AS Date,
    Mesures.Reglementaire
FROM
    Mesures
LEFT JOIN
    Polluants ON Mesures.Id_Polluant = Polluants.Id_Polluant
WHERE
    Mesures.Reglementaire = 'Oui';

-- analyse temporelle des mesures
CREATE VIEW Analyse_Temporelle_Mesures AS
SELECT 
    Mesures.Date_Debut AS Date, 
    Mesures.Valeur,
    Polluants.Polluant
FROM
    Mesures
LEFT JOIN
    Polluants ON Mesures.Id_Polluant = Polluants.Id_Polluant;

-- identification des zones à risques
CREATE VIEW Identification_Zones_Risques AS
SELECT 
    Stations.Id_Station AS Station_Id, 
    Mesures.Valeur,
    Polluants.Polluant,
    Mesures.Reglementaire
FROM
    Stations
LEFT JOIN
    Mesures ON Stations.Id_Station = Mesures.Id_Station
LEFT JOIN
    Polluants ON Mesures.Id_Polluant = Polluants.Id_Polluant
WHERE
    Mesures.Reglementaire = 'Oui';

-- comparaison par type de polluant
CREATE VIEW Comparaison_Type_Polluant AS
SELECT 
    Polluants.Polluant, 
    Mesures.Valeur
FROM 
    Mesures
LEFT JOIN
    Polluants ON Mesures.Id_Polluant = Polluants.Id_Polluant;

-- fréquence dépassement par polluant
CREATE VIEW Frequence_Depassements_Polluant AS
SELECT 
    Polluants.Polluant, 
    COUNT(*) AS Frequence_Depassements
FROM 
    Mesures
LEFT JOIN
    Polluants ON Mesures.Id_Polluant = Polluants.Id_Polluant
WHERE
    Mesures.Reglementaire = 'Oui'
GROUP BY 
    Polluants.Polluant;
