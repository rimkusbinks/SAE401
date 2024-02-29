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
    cursor.execute("SELECT Id_Polluant FROM Polluants WHERE Polluant = ?", (polluant,))
    polluant_id = cursor.fetchone()
    if polluant_id:
        return polluant_id[0]
    else:
        cursor.execute("INSERT INTO Polluants (Polluant) VALUES (?)", (polluant,))
        conn.commit()
        return cursor.lastrowid

def get_or_create_organisme_id(conn, organisme):
    cursor = conn.cursor()
    cursor.execute("SELECT Id_Organisme FROM Organismes WHERE Organisme = ?", (organisme,))
    organisme_id = cursor.fetchone()
    if organisme_id:
        return organisme_id[0]
    else:
        cursor.execute("INSERT INTO Organismes (Organisme) VALUES (?)", (organisme,))
        conn.commit()
        return cursor.lastrowid

def get_or_create_type_influence_id(conn, type_influence):
    cursor = conn.cursor()
    cursor.execute("SELECT Id_Type_Influence FROM Types_Influence WHERE Type_Influence = ?", (type_influence,))
    type_influence_id = cursor.fetchone()
    if type_influence_id:
        return type_influence_id[0]
    else:
        cursor.execute("INSERT INTO Types_Influence (Type_Influence) VALUES (?)", (type_influence,))
        conn.commit()
        return cursor.lastrowid

def get_or_create_type_evaluation_id(conn, type_evaluation):
    cursor = conn.cursor()
    cursor.execute("SELECT Id_Type_Evaluation FROM Types_Evaluation WHERE Type_Evaluation = ?", (type_evaluation,))
    type_evaluation_id = cursor.fetchone()
    if type_evaluation_id:
        return type_evaluation_id[0]
    else:
        cursor.execute("INSERT INTO Types_Evaluation (Type_Evaluation) VALUES (?)", (type_evaluation,))
        conn.commit()
        return cursor.lastrowid

def get_or_create_procedure_mesure_id(conn, procedure_mesure):
    cursor = conn.cursor()
    cursor.execute("SELECT Id_Procedure_Mesure FROM Procedures_Mesure WHERE Procedure_Mesure = ?", (procedure_mesure,))
    procedure_mesure_id = cursor.fetchone()
    if procedure_mesure_id:
        return procedure_mesure_id[0]
    else:
        cursor.execute("INSERT INTO Procedures_Mesure (Procedure_Mesure) VALUES (?)", (procedure_mesure,))
        conn.commit()
        return cursor.lastrowid

def get_or_create_type_valeur_id(conn, type_valeur):
    cursor = conn.cursor()
    cursor.execute("SELECT Id_Type_Valeur FROM Types_Valeur WHERE Type_Valeur = ?", (type_valeur,))
    type_valeur_id = cursor.fetchone()
    if type_valeur_id:
        return type_valeur_id[0]
    else:
        cursor.execute("INSERT INTO Types_Valeur (Type_Valeur) VALUES (?)", (type_valeur,))
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
    cursor.execute("SELECT Id_Discriminant FROM Discriminants WHERE Discriminant = ?", (discriminant,))
    discriminant_id = cursor.fetchone()
    if discriminant_id:
        return discriminant_id[0]
    else:
        cursor.execute("INSERT INTO Discriminants (Discriminant) VALUES (?)", (discriminant,))
        conn.commit()
        return cursor.lastrowid
    
def get_or_create_unite_mesure_id(conn, unite_mesure):
    cursor = conn.cursor()
    cursor.execute("SELECT Id_Unite_Mesure FROM Unites_Mesure WHERE Unite_Mesure = ?", (unite_mesure,))
    unite_mesure_id = cursor.fetchone()
    if unite_mesure_id:
        return unite_mesure_id[0]
    else:
        cursor.execute("INSERT INTO Unites_Mesure (Unite_Mesure) VALUES (?)", (unite_mesure,))
        conn.commit()
        return cursor.lastrowid
    
def get_or_create_code_qualite_id(conn, code_qualite):
    cursor = conn.cursor()
    cursor.execute("SELECT Id_Code_Qualite FROM Codes_Qualite WHERE Code_Qualite = ?", (code_qualite,))
    code_qualite_id = cursor.fetchone()
    if code_qualite_id:
        return code_qualite_id[0]
    else:
        cursor.execute("INSERT INTO Codes_Qualite (Code_Qualite) VALUES (?)", (code_qualite,))
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
        id_organisme = get_or_create_organisme_id(conn, row['Organisme']) if pd.notnull(row['Organisme']) and row['Organisme'] != '' else None
        id_zas = get_or_create_zas_id(conn, id_organisme, row['code zas'], row['Zas']) if pd.notnull(row['Zas']) and row['Zas'] != '' and pd.notnull(row['code zas']) and row['code zas'] != '' else None
        id_station = get_or_create_station_id(conn, id_zas, row['nom site'], row['code site'], row['type d\'implantation']) if pd.notnull(row['nom site']) and row['nom site'] != '' else None and pd.notnull(row['code site']) and row['code site'] != '' and pd.notnull(row['type d\'implantation']) and row['type d\'implantation'] != ''
        id_unite_mesure = get_or_create_unite_mesure_id(conn, row['unité de mesure']) if pd.notnull(row['unité de mesure']) and row['unité de mesure'] != '' else None
        id_code_qualite = get_or_create_code_qualite_id(conn, row['code qualité']) if pd.notnull(row['code qualité']) and row['code qualité'] != '' else None
        date_debut = row['Date de début']
        date_fin = row['Date de fin']
        valeur = row['valeur']
        valeur_brute = row['valeur brute']
        taux_saisie = row['taux de saisie']
        couverture_temporelle = row['couverture temporelle']
        couverture_donnees = row['couverture de données']
        validite = row['validité']
        reglementaire = row['Réglementaire']
        cursor.execute("""
            INSERT INTO Mesures (Id_Station, Id_Polluant, Id_Type_Influence, Id_Type_Evaluation, Id_Procedure_Mesure, Id_Type_Valeur, Id_Discriminant, Id_Organisme, Id_Zas, Id_Unite_Mesure, Id_code_qualite, Date_debut, Date_fin, Valeur, Valeur_Brute, Taux_Saisie, Couverture_Temporelle, Couverture_Donnees, Validite, Reglementaire) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """,                    (id_station, id_polluant, id_type_influence, id_type_evaluation, id_procedure_mesure, id_type_valeur, id_discriminant, id_organisme, id_zas, id_unite_mesure, id_code_qualite, date_debut, date_fin, valeur, valeur_brute, taux_saisie, couverture_temporelle, couverture_donnees, validite, reglementaire))
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
