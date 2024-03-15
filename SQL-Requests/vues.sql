-- concentrations moyenne polluants 
CREATE VIEW Concentrations_Moyennes_Polluants AS
SELECT 
    Polluants.Polluant,
    AVG(Mesures.Valeur) AS Concentration_Moyenne
FROM 
    Mesures
INNER JOIN 
    Polluants ON Mesures.Id_Polluant = Polluants.Id_Polluant
GROUP BY 
    Polluants.Polluant;

-- dépassement des seuils réglementaires
CREATE VIEW Depassements_Seuils_Reglementaires AS
SELECT 
    Stations.Code_Site, 
    Polluants.Polluant, 
    Mesures.Date_Debut, 
    Mesures.Date_Fin, 
    Mesures.Valeur
FROM
    Mesures
LEFT JOIN
    Stations ON Mesures.Id_Station = Stations.Id_Station
LEFT JOIN
    Polluants ON Mesures.Id_Polluant = Polluants.Id_Polluant
WHERE
    Mesures.Reglementaire = 'Oui';

-- analyse temporelle des mesures
CREATE VIEW Analyse_Temporelle_Mesures AS
SELECT 
    Stations.Code_Site, 
    Polluants.Polluant, 
    Mesures.Date_Debut, 
    Mesures.Date_Fin, 
    Mesures.Valeur
FROM
    Mesures
LEFT JOIN
    Stations ON Mesures.Id_Station = Stations.Id_Station
LEFT JOIN
    Polluants ON Mesures.Id_Polluant = Polluants.Id_Polluant
ORDER BY
    Mesures.Date_Debut;

-- identification des zones à risques
CREATE VIEW Identification_Zones_Risques AS
SELECT DISTINCT
    Stations.Code_Site, 
    Stations.Nom_Site, 
    Stations.Type_Implantation, 
    Zas.Code_Zas, 
    Zas.Nom_Zas,
    Mesures.Reglementaire
FROM
    Stations
LEFT JOIN
    Zas ON Stations.Id_Zas = Zas.Id_Zas
LEFT JOIN
    Mesures ON Stations.Id_Station = Mesures.Id_Station
WHERE
    Mesures.Reglementaire = 'Oui';

-- comparaison par type de polluant
CREATE VIEW Comparaison_Type_Polluant AS
SELECT 
    Polluants.Polluant, 
    AVG(Mesures.Valeur) AS Concentration_Moyenne
FROM
    Mesures
LEFT JOIN
    Polluants ON Mesures.Id_Polluant = Polluants.Id_Polluant
GROUP BY
    Polluants.Polluant;

-- fréquence dépassement par polluant
CREATE VIEW Frequence_Depassement_Polluant AS
SELECT 
    Polluants.Polluant, 
    COUNT(Mesures.Reglementaire) AS Frequence_Depassement
FROM
    Mesures
LEFT JOIN
    Polluants ON Mesures.Id_Polluant = Polluants.Id_Polluant
WHERE
    Mesures.Reglementaire = 'Oui'
GROUP BY
    Polluants.Polluant;
