import requests
import pandas as pd
import sqlite3
import ssl
from datetime import datetime, timedelta
# import du time pour le temps d'attente de chaque importation
import time

# Désactiver la vérification SSL
ssl._create_default_https_context = ssl._create_unverified_context

def get_or_create_polluant_id(conn, polluant):
    cursor = conn.cursor()
    cursor.execute("SELECT Id_Polluant FROM Polluants WHERE Nom_Polluant = ?", (polluant,))
    polluant_id = cursor.fetchone()
    if polluant_id:
        return polluant_id[0]
    else:
        cursor.execute("INSERT INTO Polluants (Nom_Polluant) VALUES (?)", (polluant,))
        conn.commit()
        return cursor.lastrowid

def get_or_create_organisme_id(conn, organisme):
    cursor = conn.cursor()
    cursor.execute("SELECT Id_Organisme FROM Organismes WHERE Nom = ?", (organisme,))
    organisme_id = cursor.fetchone()
    if organisme_id:
        return organisme_id[0]
    else:
        cursor.execute("INSERT INTO Organismes (Nom) VALUES (?)", (organisme,))
        conn.commit()
        return cursor.lastrowid

def get_or_create_type_influence_id(conn, type_influence):
    cursor = conn.cursor()
    cursor.execute("SELECT Id_Type_Influence FROM Types_Influence WHERE Nom_Type_Influence = ?", (type_influence,))
    type_influence_id = cursor.fetchone()
    if type_influence_id:
        return type_influence_id[0]
    else:
        cursor.execute("INSERT INTO Types_Influence (Nom_Type_Influence) VALUES (?)", (type_influence,))
        conn.commit()
        return cursor.lastrowid

def get_or_create_type_evaluation_id(conn, type_evaluation):
    cursor = conn.cursor()
    cursor.execute("SELECT Id_Type_Evaluation FROM Types_Evaluation WHERE Nom_Type_Evaluation = ?", (type_evaluation,))
    type_evaluation_id = cursor.fetchone()
    if type_evaluation_id:
        return type_evaluation_id[0]
    else:
        cursor.execute("INSERT INTO Types_Evaluation (Nom_Type_Evaluation) VALUES (?)", (type_evaluation,))
        conn.commit()
        return cursor.lastrowid

def get_or_create_procedure_mesure_id(conn, procedure_mesure):
    cursor = conn.cursor()
    cursor.execute("SELECT Id_Procedure_Mesure FROM Procedures_Mesure WHERE Nom_Procedure_Mesure = ?", (procedure_mesure,))
    procedure_mesure_id = cursor.fetchone()
    if procedure_mesure_id:
        return procedure_mesure_id[0]
    else:
        cursor.execute("INSERT INTO Procedures_Mesure (Nom_Procedure_Mesure) VALUES (?)", (procedure_mesure,))
        conn.commit()
        return cursor.lastrowid

def get_or_create_type_valeur_id(conn, type_valeur):
    cursor = conn.cursor()
    cursor.execute("SELECT Id_Type_Valeur FROM Types_Valeur WHERE Nom_Types_Valeur = ?", (type_valeur,))
    type_valeur_id = cursor.fetchone()
    if type_valeur_id:
        return type_valeur_id[0]
    else:
        cursor.execute("INSERT INTO Types_Valeur (Nom_Types_Valeur) VALUES (?)", (type_valeur,))
        conn.commit()
        return cursor.lastrowid

def get_or_create_zas_id(conn, Id_Organisme, Code_Zas, Nom_Zas):
    cursor = conn.cursor()
    cursor.execute("SELECT Id_Zas FROM Zas WHERE Code_Zas = ?", (Code_Zas,))
    zas_id = cursor.fetchone()
    if zas_id:
        return zas_id[0]
    else:
        cursor.execute("INSERT INTO Zas (Id_Organisme, Code_Zas, Nom_Zas) VALUES (?,?,?)", (Id_Organisme, Code_Zas, Nom_Zas))
        conn.commit()
        return cursor.lastrowid

def get_or_create_station_id(conn, Id_Zas, Nom_Site, Code_Site, Type_Implantation):
    cursor = conn.cursor()
    cursor.execute("SELECT Id_Station FROM Stations WHERE Code_Site = ?", (Code_Site,))
    station_id = cursor.fetchone()
    if station_id:
        return station_id[0]
    else:
        cursor.execute("INSERT INTO Stations (Id_Zas, Code_Site, Nom_Site, Type_Implantation) VALUES (?,?,?,?)", (Id_Zas, Code_Site, Nom_Site, Type_Implantation))

def get_or_create_discriminant_id(conn, discriminant):
    cursor = conn.cursor()
    cursor.execute("SELECT Id_Discriminant FROM Discriminants WHERE Nom_Discriminant = ?", (discriminant,))
    discriminant_id = cursor.fetchone()
    if discriminant_id:
        return discriminant_id[0]
    else:
        cursor.execute("INSERT INTO Discriminants (Nom_Discriminant) VALUES (?)", (discriminant,))
        conn.commit()
        return cursor.lastrowid

def get_or_create_reglementaire_id(conn, reglementaire):
    cursor = conn.cursor()
    cursor.execute("SELECT Id_Reglementaire FROM Reglementaires WHERE Nom_Reglementaire = ?", (reglementaire,))
    reglementaire_id = cursor.fetchone()
    if reglementaire_id:
        return reglementaire_id[0]
    else:
        cursor.execute("INSERT INTO Reglementaires (Nom_Reglementaire) VALUES (?)", (reglementaire,))
        conn.commit()
        return cursor.lastrowid
    
def insert_mesures(conn, df):
    cursor = conn.cursor()
    for index, row in df.iterrows():
        id_polluant = get_or_create_polluant_id(conn, row['Polluant'])
        id_type_influence = get_or_create_type_influence_id(conn, row['type d\'influence']) if pd.notnull(row['type d\'influence']) and row['type d\'influence'] != '' else None
        id_type_evaluation = get_or_create_type_evaluation_id(conn, row['type d\'évaluation']) if pd.notnull(row['type d\'évaluation']) and row['type d\'évaluation'] != '' else None
        id_procedure_mesure = get_or_create_procedure_mesure_id(conn, row['procédure de mesure']) if pd.notnull(row['procédure de mesure']) and row['procédure de mesure'] != '' else None
        id_type_valeur = get_or_create_type_valeur_id(conn, row['type de valeur']) if pd.notnull(row['type de valeur']) and row['type de valeur'] != '' else None
        id_discriminant = get_or_create_discriminant_id(conn, row['discriminant']) if pd.notnull(row['discriminant']) and row['discriminant'] != '' else None
        id_reglementaire = get_or_create_reglementaire_id(conn, row['Réglementaire']) if pd.notnull(row['Réglementaire']) and row['Réglementaire'] != '' else None
        id_organisme = get_or_create_organisme_id(conn, row['Organisme']) if pd.notnull(row['Organisme']) and row['Organisme'] != '' else None
        id_zas = get_or_create_zas_id(conn, id_organisme, row['Zas'], row['code zas']) if pd.notnull(row['Zas']) and row['Zas'] != '' and pd.notnull(row['code zas']) and row['code zas'] != '' else None
        id_station = get_or_create_station_id(conn, id_zas, row['nom site'], row['code site'], row['type d\'implantation']) if pd.notnull(row['nom site']) and row['nom site'] != '' else None and pd.notnull(row['code site']) and row['code site'] != '' and pd.notnull(row['type d\'implantation']) and row['type d\'implantation'] != ''
        date_debut = datetime.strptime(row['Date de début'], '%Y/%m/%d %H:%M:%S')
        date_fin = datetime.strptime(row['Date de fin'], '%Y/%m/%d %H:%M:%S')
        valeur = row['valeur']
        valeur_brute = row['valeur brute']
        unite_mesure = row['unité de mesure']
        taux_saisie = row['taux de saisie']
        couverture_temporelle = row['couverture temporelle']
        couverture_donnees = row['couverture de données']
        code_qualite = row['code qualité']
        validite = row['validité']
        cursor.execute("""
            INSERT INTO Mesures (Id_Station, Id_Polluant, Id_Type_Influence, Id_Type_Evaluation, Id_Procedure, Id_Type_Valeur, Id_Discriminant, Id_Reglementaire, Id_Organisme, Id_Zas, Date_debut, Date_fin, Valeur, Valeur_Brute, Unite_Mesure, Taux_Saisie, Couverture_Temporelle, Couverture_Donnees, Code_Qualite, Validite) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """,                    (id_station, id_polluant, id_type_influence, id_type_evaluation, id_procedure_mesure, id_type_valeur, id_discriminant, id_reglementaire, id_organisme, id_zas, date_debut, date_fin, valeur, valeur_brute, unite_mesure, taux_saisie, couverture_temporelle, couverture_donnees, code_qualite, validite))
    conn.commit()

def import_data():
    # Déterminer l'année actuelle et les quatre dernières années
    current_year = datetime.now().year
    years = [str(year) for year in range(current_year - 3, current_year + 1)]

    # on lance un chrono pour voir le temps d'une importation toutes les années
    start_time_import_all_years = time.time()

    # Lire le fichier CSV pour chaque jour de chaque année
    for year in years:
        end_date = min(datetime.now(), datetime(int(year), 12, 31))
        current_date = datetime(int(year), 1, 1)

        #on lance un chrono pour voir le temps d'une importation pour une année
        start_time_import_year = time.time()
        while current_date <= end_date:
            file_name = f"FR_E2_{current_date.strftime('%Y-%m-%d')}.csv"
            url_csv = f"https://files.data.gouv.fr/lcsqa/concentrations-de-polluants-atmospheriques-reglementes/temps-reel/{year}/{file_name}"

            try:
                db_name = "SAE401.db"
                conn = sqlite3.connect("database/" + db_name)
                response = requests.head(url_csv, timeout=5)
                response.raise_for_status()
                df = pd.read_csv(url_csv, sep=';')
                # Insérer les données dans la base de données
                print(f"Importation des données pour la date {current_date.strftime('%Y-%m-%d')}...")
                insert_mesures(conn, df)
                # on lance un chrono pour voir le temps d'une importation
                start_time_import_day = time.time()
                print(f"Importation des données pour la date {current_date.strftime('%Y-%m-%d')} terminée.")
                print(" %s secondes" % (time.time() - start_time_import_day))
            except Exception as e:
                print(f"Erreur lors de l'importation des données pour le fichier {file_name} : {e}")

            current_date += timedelta(days=1)
            conn.close()

        print(f"Importation des données pour l'année {year} terminée.")
        print(" %s secondes prit" % (time.time() - start_time_import_year))

    print(f"Importation des données pour toutes les années terminée.")
    print(" %s secondes prit" % (time.time() - start_time_import_all_years))

if __name__ == "__main__":
    import_data()
