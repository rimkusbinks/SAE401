from flask import Flask, request, jsonify
from datetime import datetime
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)
# route pour si l'utilisateur accède à une méthode qui n'existe pas
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'La méthode demandée n\'existe pas, referez-vous à la documentation pour plus d\'informations'}), 404

def query_db(query, args=(), one=False):
    with sqlite3.connect("database/SAE401.db") as conn:
        conn.text_factory = str
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(query, args)
        rv = [dict(row) for row in cur.fetchall()]
        cur.close()
        return (rv[0] if rv else None) if one else rv

# route pour obtenir les organismes
@app.route('/organismes')
def get_organismes():
    organisme = request.args.get('organisme')
    page = request.args.get('page', default=1, type=int)
    par_page = request.args.get('par_page', default=10, type=int)
    offset = (page - 1) * par_page
    query = "SELECT Id_Organisme, Organisme FROM Organismes WHERE 1=1"
    params = []
    if organisme:
        query += " AND Organisme LIKE ?"
        params.append(f"%{organisme}%")
    query += " ORDER BY Organisme LIMIT ? OFFSET ?"
    params.extend([par_page, offset])
    result = query_db(query, params)
    return jsonify(result)

# route pour obtenir les zas
@app.route('/zas')
def get_zas():
    nom_zas = request.args.get('nom_zas')
    code_zas = request.args.get('code_zas')
    page = request.args.get('page', default=1, type=int)
    par_page = request.args.get('par_page', default=10, type=int)
    offset = (page - 1) * par_page
    query = "SELECT Id_Zas, Code_Zas, Nom_Zas FROM Zas WHERE 1=1"
    params = []
    if nom_zas:
        query += " AND Nom_Zas LIKE ?"
        params.append(f"%{nom_zas}%")
    if code_zas:
        query += " AND Code_Zas = ?"
        params.append(code_zas)
    query += " ORDER BY Nom_Zas LIMIT ? OFFSET ?"
    params.extend([par_page, offset])
    result = query_db(query, params)
    return jsonify(result)

# route pour obtenir les stations
@app.route('/stations')
def get_stations():
    nom_site = request.args.get('nom_site')
    code_site = request.args.get('code_site')
    page = request.args.get('page', default=1, type=int)
    par_page = request.args.get('par_page', default=10, type=int)
    offset = (page - 1) * par_page
    params = []
    query = "SELECT Id_Station, Code_Site, Nom_Site, Type_Implantation FROM Stations WHERE 1=1"

    if nom_site:
        query += " AND Nom_Site LIKE ?"
        params.append(f"%{nom_site}%")
    if code_site:
        query += " AND Code_Site = ?"
        params.append(code_site)

    query += " ORDER BY Nom_Site LIMIT ? OFFSET ?"
    params.extend([par_page, offset])

    result = query_db(query, params)
    return jsonify(result)

# route pour obtenir les polluants
@app.route('/polluants')
def get_polluants():
    polluant = request.args.get('polluant')
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page - 1) * per_page
    query = "SELECT Id_Polluant, Polluant FROM Polluants WHERE 1=1"
    params = []
    if polluant:
        query += " AND Polluant LIKE ?"
        params.append(f"%{polluant}%")
    query += " LIMIT ? OFFSET ?"
    params.extend([per_page, offset])
    result = query_db(query, params)
    return jsonify(result)

# route pour obtenir les types d'influence
@app.route('/types_influence')
def get_types_influence():
    type_influence = request.args.get('type_influence')
    page = request.args.get('page', default=1, type=int)
    par_page = request.args.get('par_page', default=10, type=int)
    offset = (page - 1) * par_page
    query = "SELECT Id_Type_Influence, Type_Influence FROM Types_Influence WHERE 1=1"
    params = []
    if type_influence:
        query += " AND Type_Influence LIKE ?"
        params.append(f"%{type_influence}%")
    query += " LIMIT ? OFFSET ?"
    params.extend([par_page, offset])
    result = query_db(query, params)
    return jsonify(result)

# route pour obtenir les types d'évaluation
@app.route('/types_evaluation')
def get_types_evaluation():
    type_evaluation = request.args.get('type_evaluation')
    page = request.args.get('page', default=1, type=int)
    par_page = request.args.get('par_page', default=10, type=int)
    offset = (page - 1) * par_page
    query = "SELECT Id_Type_Evaluation, Type_Evaluation FROM Types_Evaluation WHERE 1=1"
    params = []
    if type_evaluation:
        query += " AND Type_Evaluation LIKE ?"
        params.append(f"%{type_evaluation}%")
    query += " LIMIT ? OFFSET ?"
    params.extend([par_page, offset])
    result = query_db(query, params)
    return jsonify(result)

# route pour obtenir les procédures de mesure
@app.route('/procedures_mesure')
def get_procedures_mesure():
    procedure_mesure = request.args.get('procedure_mesure')
    page = request.args.get('page', default=1, type=int)
    par_page = request.args.get('par_page', default=10, type=int)
    offset = (page - 1) * par_page
    query = "SELECT Id_Procedure_Mesure, Procedure_Mesure FROM Procedures_Mesure WHERE 1=1"
    params = []
    if procedure_mesure:
        query += " AND Procedure_Mesure LIKE ?"
        params.append(f"%{procedure_mesure}%")
    query += " LIMIT ? OFFSET ?"
    params.extend([par_page, offset])
    result = query_db(query, params)
    return jsonify(result)

# route pour obtenir les types de valeur
@app.route('/types_valeur')
def get_types_valeur():
    type_valeur = request.args.get('type_valeur')
    page = request.args.get('page', default=1, type=int)
    par_page = request.args.get('par_page', default=10, type=int)
    offset = (page - 1) * par_page
    query = "SELECT Id_Type_Valeur, Type_Valeur FROM Types_Valeur WHERE 1=1"
    params = []
    if type_valeur:
        query += " AND Type_Valeur LIKE ?"
        params.append(f"%{type_valeur}%")
    query += " LIMIT ? OFFSET ?"
    params.extend([par_page, offset])
    result = query_db(query, params)
    return jsonify(result)

# route pour obtenir les discriminants
@app.route('/discriminants')
def get_discriminants():
    discriminant = request.args.get('discriminant')
    page = request.args.get('page', default=1, type=int)
    par_page = request.args.get('par_page', default=10, type=int)
    offset = (page - 1) * par_page
    query = "SELECT Id_Discriminant, Discriminant FROM Discriminants WHERE 1=1"
    params = []
    if discriminant:
        query += " AND Discriminant LIKE ?"
        params.append(f"%{discriminant}%")
    query += " LIMIT ? OFFSET ?"
    params.extend([par_page, offset])
    result = query_db(query, params)
    return jsonify(result)

# route pour obtenir les unites de mesure
@app.route('/unites_mesure')
def get_unites_mesure():
    unite_mesure = request.args.get('unite_mesure')
    page = request.args.get('page', default=1, type=int)
    par_page = request.args.get('par_page', default=10, type=int)
    offset = (page - 1) * par_page
    query = "SELECT Id_Unite_Mesure, Unite_Mesure FROM Unites_Mesure WHERE 1=1"
    params = []
    if unite_mesure:
        query += " AND Unite_Mesure LIKE ?"
        params.append(f"%{unite_mesure}%")
    query += " LIMIT ? OFFSET ?"
    params.extend([par_page, offset])
    result = query_db(query, params)
    return jsonify(result)

# route pour obtenir les codes de qualité
@app.route('/codes_qualite')
def get_codes_qualite():
    code_qualite = request.args.get('code_qualite')
    page = request.args.get('page', default=1, type=int)
    par_page = request.args.get('par_page', default=10, type=int)
    offset = (page - 1) * par_page
    query = "SELECT Id_Code_Qualite, Code_Qualite FROM Codes_Qualite WHERE 1=1"
    params = []
    if code_qualite:
        query += " AND Code_Qualite LIKE ?"
        params.append(f"%{code_qualite}%")
    query += " LIMIT ? OFFSET ?"
    params.extend([par_page, offset])
    result = query_db(query, params)
    return jsonify(result)

# route pour obtenir les mesures 
@app.route('/measurements')
def get_measurements():
    print("La méthode get_measurements a été appelée")
    page = request.args.get('page', default=1, type=int)
    par_page = request.args.get('par_page', default=10, type=int)
    offset = (page - 1) * par_page
    organisme = request.args.get('organisme')
    nom_zas = request.args.get('nom_zas')
    code_zas = request.args.get('code_zas')
    nom_site = request.args.get('nom_site')
    code_site = request.args.get('code_site')
    polluant = request.args.get('polluant')
    type_influence = request.args.get('type_influence')
    type_evaluation = request.args.get('type_evaluation')
    procedure_mesure = request.args.get('procedure_mesure')
    type_valeur = request.args.get('type_valeur')
    unite_mesure = request.args.get('unite_mesure')
    code_qualite = request.args.get('code_qualite')
    validite = request.args.get('validite', type=int)
    station_id = request.args.get('station_id', type=int)
    pollutant_id = request.args.get('pollutant_id', type=int)
    zas_id = request.args.get('zas_id', type=int)
    unite_mesure_id = request.args.get('unite_mesure_id', type=int)
    code_qualite_id = request.args.get('code_qualite_id', type=int)
    type_valeur_id = request.args.get('type_valeur_id', type=int)
    organisme_id = request.args.get('organisme_id', type=int)
    discriminant_id = request.args.get('discriminant_id', type=int)
    type_evaluation_id = request.args.get('type_evaluation_id', type=int)
    type_influence_id = request.args.get('type_influence_id', type=int)
    procedure_mesure_id = request.args.get('procedure_mesure_id', type=int)
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    unite_mesure = request.args.get('unite_mesure')
    code_qualite = request.args.get('code_qualite')
    validite = request.args.get('validite', type=int)

    if start_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S').strftime('%Y/%m/%d %H:%M:%S')
    if end_date:
        end_date = datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%S').strftime('%Y/%m/%d %H:%M:%S')

    query = """
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
        Stations.Code_Site, 
        Stations.Nom_Site, 
        Polluants.Polluant, 
        Types_Influence.Type_Influence, 
        Types_Evaluation.Type_Evaluation, 
        Procedures_Mesure.Procedure_Mesure, 
        Organismes.Organisme, 
        Zas.Code_Zas, 
        Zas.Nom_Zas
    FROM Mesures
    LEFT JOIN Polluants ON Mesures.Id_Polluant = Polluants.Id_Polluant
    LEFT JOIN Types_Influence ON Mesures.Id_Type_Influence = Types_Influence.Id_Type_Influence
    LEFT JOIN Types_Evaluation ON Mesures.Id_Type_Evaluation = Types_Evaluation.Id_Type_Evaluation
    LEFT JOIN Procedures_Mesure ON Mesures.Id_Procedure_Mesure = Procedures_Mesure.Id_Procedure_Mesure
    LEFT JOIN Stations ON Mesures.Id_Station = Stations.Id_Station
    LEFT JOIN Zas ON Stations.Id_Zas = Zas.Id_Zas
    LEFT JOIN Organismes ON Zas.Id_Organisme = Organismes.Id_Organisme
    LEFT JOIN Unites_Mesure ON Mesures.Id_Unite_Mesure = Unites_Mesure.Id_Unite_Mesure
    LEFT JOIN Codes_Qualite ON Mesures.Id_Code_Qualite = Codes_Qualite.Id_Code_Qualite
    WHERE 1=1
    """
    params = []

    # Appliquer les filtres basés sur les arguments
    if station_id is not None:
        query += ' AND Mesures.Id_Station = ?'
        params.append(station_id)
    if pollutant_id is not None:
        query += ' AND Mesures.Id_Polluant = ?'
        params.append(pollutant_id)
    if start_date:
        query += ' AND Mesures.Date_Debut >= ?'
        params.append(start_date)
    if end_date:
        query += ' AND Mesures.Date_Fin <= ?'
        params.append(end_date)
    if unite_mesure:
        query += ' AND Unites_Mesure.Unite_Mesure = ?'
        params.append(unite_mesure)
    if code_qualite:
        query += ' AND Codes_Qualite.Code_Qualite = ?'
        params.append(code_qualite)
    if validite is not None:
        query += ' AND Mesures.Validite = ?'
        params.append(validite)
    if organisme:
        query += ' AND Organismes.Organisme LIKE ?'
        params.append(f'%{organisme}%')
    if nom_zas:
        query += ' AND Zas.Nom_Zas LIKE ?'
        params.append(f'%{nom_zas}%')
    if code_zas:
        query += ' AND Zas.Code_Zas = ?'
        params.append(code_zas)
    if nom_site:
        query += ' AND Stations.Nom_Site LIKE ?'
        params.append(f'%{nom_site}%')
    if code_site:
        query += ' AND Stations.Code_Site = ?'
        params.append(code_site)
    if polluant:
        query += ' AND Polluants.Polluant LIKE ?'
        params.append(f'%{polluant}%')
    if type_influence:
        query += ' AND Types_Influence.Type_Influence LIKE ?'
        params.append(f'%{type_influence}%')
    if type_evaluation:
        query += ' AND Types_Evaluation.Type_Evaluation LIKE ?'
        params.append(f'%{type_evaluation}%')
    if procedure_mesure:
        query += ' AND Procedures_Mesure.Procedure_Mesure LIKE ?'
        params.append(f'%{procedure_mesure}%')
    if type_valeur_id:
        query += ' AND Mesures.Id_Type_Valeur = ?'
        params.append(type_valeur_id)
    if unite_mesure_id:
        query += ' AND Mesures.Id_Unite_Mesure = ?'
        params.append(unite_mesure_id)
    if code_qualite_id:
        query += ' AND Mesures.Id_Code_Qualite = ?'
        params.append(code_qualite_id)
    if validite is not None:
        query += ' AND Mesures.Validite = ?'
        params.append(validite)
    if station_id:
        query += ' AND Mesures.Id_Station = ?'
        params.append(station_id)
    if pollutant_id:
        query += ' AND Mesures.Id_Polluant = ?'
        params.append(pollutant_id)
    if zas_id:
        query += ' AND Stations.Id_Zas = ?'
        params.append(zas_id)
    if organisme_id:
        query += ' AND Zas.Id_Organisme = ?'
        params.append(organisme_id)
    if discriminant_id:
        query += ' AND Mesures.Id_Discriminant = ?'
        params.append(discriminant_id)
    if type_evaluation_id:
        query += ' AND Mesures.Id_Type_Evaluation = ?'
        params.append(type_evaluation_id)
    if type_influence_id:
        query += ' AND Mesures.Id_Type_Influence = ?'
        params.append(type_influence_id)
    if procedure_mesure_id:
        query += ' AND Mesures.Id_Procedure_Mesure = ?'
        params.append(procedure_mesure_id)

    query += ' LIMIT ? OFFSET ?'
    params.extend([par_page, offset])

    result = query_db(query, params)
    return jsonify(result)

def query_db(query, args=(), one=False):
    with sqlite3.connect("database/SAE401.db") as conn:  # Assurez-vous du chemin
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(query, args)
        rv = [dict(row) for row in cur.fetchall()]
        cur.close()
        return (rv[0] if rv else None) if one else rv

@app.route('/api/concentrations-moyennes')
def get_concentration_moyennes():
    query = "SELECT Polluant, AVG(Concentration_Moyenne) as Concentration_Moyenne FROM Concentrations_Moyennes_Polluants GROUP BY Polluant"
    data = query_db(query)
    return jsonify(data)

def get_db_connection():
    conn = sqlite3.connect("database/SAE401.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/api/depassements-seuils')
def depassements_seuils():
    # Récupérer les paramètres de la requête
    code_site = request.args.get('code_site')
    polluant = request.args.get('polluant')
    date_debut = request.args.get('date_debut')

    # Construction de la requête SQL de base
    query = '''
    SELECT Code_Site, Polluant, Date_Debut, Date_Fin, Valeur
    FROM Depassements_Seuils_Reglementaires
    WHERE 1=1
    '''

    # Préparation des paramètres pour sécuriser la requête
    params = []
    if code_site:
        query += ' AND Code_Site = ?'
        params.append(code_site)
    if polluant:
        query += ' AND Polluant = ?'
        params.append(polluant)
    if date_debut:
        # Utiliser la fonction strftime pour convertir le format de date si nécessaire
        query += ' AND Date_Debut >= datetime(?, "start of day")'
        params.append(date_debut)

    # Connexion à la base de données et exécution de la requête
    conn = sqlite3.connect("database/SAE401.db") 
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, params)
    result = cur.fetchall()
    cur.close()
    conn.close()

    # Convertir les rangées de la base de données en dictionnaires
    depassements = [dict(row) for row in result]

    # Renvoyer les données au format JSON
    return jsonify(depassements)

@app.route('/api/analyse-temporelle')
def get_analyse_temporelle():
    # Paramètres optionnels pour le filtrage
    code_site = request.args.get('code_site')
    polluant = request.args.get('polluant')
    date_debut = request.args.get('date_debut')
    date_fin = request.args.get('date_fin')

    # Construction de la requête SQL de base
    query = '''
    SELECT Code_Site, Polluant, Date_Debut, Date_Fin, Valeur
    FROM Analyse_Temporelle_Mesures
    WHERE 1=1
    '''

    # Préparation des paramètres pour sécuriser la requête
    params = []
    if code_site:
        query += ' AND Code_Site = ?'
        params.append(code_site)
    if polluant:
        query += ' AND Polluant = ?'
        params.append(polluant)
    if date_debut:
        query += ' AND Date_Debut >= ?'
        params.append(date_debut)
    if date_fin:
        query += ' AND Date_Fin <= ?'
        params.append(date_fin)

    # Exécution de la requête
    result = query_db(query, params)

    # Renvoyer les données au format JSON
    return jsonify(result)


@app.route('/api/zones-risques')
def zones_risques():
    # Récupération des paramètres de la requête
    code_site = request.args.get('code_site')
    polluant = request.args.get('polluant')
    date_debut = request.args.get('date_debut')
    date_fin = request.args.get('date_fin')

    # Vérifiez que tous les paramètres nécessaires sont fournis
    if not (code_site and polluant and date_debut and date_fin):
        return jsonify({"error": "Tous les paramètres (code_site, polluant, date_debut, date_fin) sont nécessaires."}), 400

    # Connexion à la base de données et requête
    try:
        conn = sqlite3.connect("database/SAE401.db")  # Remplacer par le chemin réel vers votre base de données
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('''
            SELECT Stations.Code_Site, Polluants.Polluant, Mesures.Date_Debut, Mesures.Date_Fin, Mesures.Valeur
            FROM Mesures
            JOIN Stations ON Mesures.Id_Station = Stations.Id_Station
            JOIN Polluants ON Mesures.Id_Polluant = Polluants.Id_Polluant
            WHERE Stations.Code_Site = ? AND Polluants.Polluant = ? AND (Mesures.Date_Debut BETWEEN ? AND ?)
            ORDER BY Mesures.Date_Debut ASC
        ''', (code_site, polluant, date_debut, date_fin))
        data = cur.fetchall()
        cur.close()
        return jsonify([dict(row) for row in data])
    except sqlite3.Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
