-- concentrations moyenne polluants 
CREATE VIEW Concentrations_Moyennes_Polluants AS
SELECT 
    Polluants.Polluant,
    AVG(Mesures.Valeur) AS Concentration_Moyenne,
    strftime('%Y-%m-%d %H:%M:%S', Mesures.Date_Debut) AS Date
FROM 
    Mesures
INNER JOIN 
    Polluants ON Mesures.Id_Polluant = Polluants.Id_Polluant
GROUP BY 
    Polluants.Polluant, 
    strftime('%Y-%m-%d %H:%M:%S', Mesures.Date_Debut);


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
    AVG(Mesures.Valeur) AS Moyenne_Valeur,
    Polluants.Polluant,
    COUNT(Mesures.Id_Mesure) AS Nombre_Depassements
FROM
    Stations
INNER JOIN
    Mesures ON Stations.Id_Station = Mesures.Id_Station
INNER JOIN
    Polluants ON Mesures.Id_Polluant = Polluants.Id_Polluant
WHERE
    Mesures.Reglementaire = 'Oui'
GROUP BY
    Stations.Id_Station, Polluants.Polluant;


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
