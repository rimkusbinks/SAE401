from flask import Flask, request, jsonify
import sqlite3, datetime

app = Flask(__name__)

# si la méthode n'existe pas on retourne un message d'erreur
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'La méthode demandée n\'existe pas, referez-vous à la documentation pour plus d\'informations'}), 404

def query_db(query, args=(), one=False):
    with sqlite3.connect("database/SAE401.db") as conn:
        conn.text_factory = str  # Use UTF-8
        conn.row_factory = sqlite3.Row  # This enables column access by name: row['column_name'] 
        cur = conn.cursor()
        cur.execute(query, args)
        rv = [dict(row) for row in cur.fetchall()]  # This will convert your row to a dict
        cur.close()
        return (rv[0] if rv else None) if one else rv

# récupération des organismes
@app.route('/organismes')
def get_organismes():
    print(" La méthode get_organismes a été appelée")
    nom_organisme = request.args.get('nom_organisme')
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page - 1) * per_page
    query = 'SELECT * FROM Organismes WHERE 1=1'
    params = []
    if nom_organisme:
        query += ' AND Nom_Organisme = ?'
        params.append(nom_organisme)
    query += ' LIMIT ? OFFSET ?'
    params.extend([per_page, offset])
    result = query_db(query, params)
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des zas
@app.route('/zas')
def get_zas():
    print(" La méthode get_zas a été appelée")
    nom_zas = request.args.get('nom_zas')
    code_zas = request.args.get('code_zas')
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page - 1) * per_page
    query = 'SELECT * FROM Zas WHERE 1=1'
    params = []
    if nom_zas:
        query += ' AND Nom_Zas = ?'
        params.append(nom_zas)
    if code_zas:
        query += ' AND Code_Zas = ?'
        params.append(code_zas)
    query += ' LIMIT ? OFFSET ?'
    params.extend([per_page, offset])
    result = query_db(query, params)
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des stations
@app.route('/stations')
def get_stations():
    print(" La méthode get_stations a été appelée")
    nom_site = request.args.get('nom_site')
    code_site = request.args.get('code_site')
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page - 1) * per_page
    query = 'SELECT * FROM Stations WHERE 1=1'
    params = []
    if nom_site:
        query += ' AND Nom_Site = ?'
        params.append(nom_site)
    if code_site:
        query += ' AND Code_Site = ?'
        params.append(code_site)
    query += ' LIMIT ? OFFSET ?'
    params.extend([per_page, offset])
    result = query_db(query, params)
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des polluants
@app.route('/polluants')
def get_polluants():
    print(" La méthode get_polluants a été appelée")
    nom_polluant = request.args.get('nom_polluant')
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page - 1) * per_page
    query = 'SELECT * FROM Polluants WHERE 1=1'
    params = []
    if nom_polluant:
        query += ' AND Nom_Polluant = ?'
        params.append(nom_polluant)
    query += ' LIMIT ? OFFSET ?'
    params.extend([per_page, offset])
    result = query_db(query, params)
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des types influence
@app.route('/types_influence')
def get_types_influence():
    print(" La méthode get_types_influence a été appelée")
    nom_type_influence = request.args.get('nom_type_influence')
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page - 1) * per_page
    query = 'SELECT * FROM Types_Influence WHERE 1=1'
    params = []
    if nom_type_influence:
        query += ' AND Nom_Type_Influence = ?'
        params.append(nom_type_influence)
    query += ' LIMIT ? OFFSET ?'
    params.extend([per_page, offset])
    result = query_db(query, params)
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des types evaluation
@app.route('/types_evaluation')
def get_types_evaluation():
    print(" La méthode get_types_evaluation a été appelée")
    nom_type_evaluation = request.args.get('nom_type_evaluation')
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page - 1) * per_page
    query = 'SELECT * FROM Types_Evaluation WHERE 1=1'
    params = []
    if nom_type_evaluation:
        query += ' AND Nom_Type_Evaluation = ?'
        params.append(nom_type_evaluation)
    query += ' LIMIT ? OFFSET ?'
    params.extend([per_page, offset])
    result = query_db(query, params)
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des types mesure
@app.route('/procedures_mesure')
def get_procedures_mesure():
    print(" La méthode get_procedures_mesure a été appelée")
    nom_procedure = request.args.get('nom_procedure')
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page - 1) * per_page
    query = 'SELECT * FROM Procedures_Mesure WHERE 1=1'
    params = []
    if nom_procedure:
        query += ' AND Nom_Procedure_Mesure = ?'
        params.append(nom_procedure)
    query += ' LIMIT ? OFFSET ?'
    params.extend([per_page, offset])
    result = query_db(query, params)
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des types valeur
@app.route('/types_valeur')
def get_types_valeur():
    print(" La méthode get_types_valeur a été appelée")
    nom_type_valeur = request.args.get('nom_type_valeur')
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page - 1) * per_page
    query = 'SELECT * FROM Types_Valeur WHERE 1=1'
    params = []
    if nom_type_valeur:
        query += ' AND Nom_Types_Valeur = ?'
        params.append(nom_type_valeur)
    query += ' LIMIT ? OFFSET ?'
    params.extend([per_page, offset])
    result = query_db(query, params)
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des reglementations
@app.route('/reglementations')
def get_reglementations():
    print(" La méthode get_reglementations a été appelée")
    nom_reglementaire = request.args.get('nom_reglementaire')
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page - 1) * per_page
    query = 'SELECT * FROM Reglementaires WHERE 1=1'
    params = []
    if nom_reglementaire:
        query += ' AND Nom_Reglementaire = ?'
        params.append(nom_reglementaire)
    query += ' LIMIT ? OFFSET ?'
    params.extend([per_page, offset])
    result = query_db(query, params)
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des reglementations
@app.route('/discriminants')
def get_discriminants():
    print(" La méthode get_discriminants a été appelée")
    nom_discriminant = request.args.get('nom_discriminant')
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page - 1) * per_page
    query = 'SELECT * FROM Discriminants WHERE 1=1'
    params = []
    if nom_discriminant:
        query += ' AND Nom_Discriminant = ?'
        params.append(nom_discriminant)
    query += ' LIMIT ? OFFSET ?'
    params.extend([per_page, offset])
    result = query_db(query, params)
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des mesures
@app.route('/measurements')
def get_measurements():
    print(" La méthode get_measurements a été appelée")
    nom_organisme = request.args.get('nom_organisme')
    nom_zas = request.args.get('nom_zas')
    code_zas = request.args.get('code_zas')
    nom_site = request.args.get('nom_site')
    code_site = request.args.get('code_site')
    nom_polluant = request.args.get('nom_polluant')
    nom_type_influence = request.args.get('nom_type_influence')
    nom_type_evaluation = request.args.get('nom_type_evaluation')
    nom_procedure = request.args.get('nom_procedure')
    nom_type_valeur = request.args.get('nom_type_valeur')
    nom_reglementaire = request.args.get('nom_reglementaire')
    nom_discriminant = request.args.get('nom_discriminant')
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page - 1) * per_page
    station_id = request.args.get('station_id')
    pollutant_id = request.args.get('pollutant_id')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

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
        Mesures.Unite_Mesure, 
        Mesures.Taux_Saisie, 
        Mesures.Couverture_Temporelle, 
        Mesures.Couverture_Donnees, 
        Mesures.Code_Qualite, 
        Mesures.Validite, 
        Stations.Code_Site, 
        Stations.Nom_Site, 
        Stations.Type_Implantation, 
        Polluants.Nom_Polluant, 
        Types_Influence.Nom_Type_Influence, 
        Types_Evaluation.Nom_Type_Evaluation, 
        Procedures_Mesure.Nom_Procedure_Mesure, 
        Organismes.Nom_Organisme, 
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
    WHERE 1=1
    """
    params = []

    if station_id:
        query += ' AND Mesures.Id_Station = ?'
        params.append(station_id)
    if pollutant_id:
        query += ' AND Mesures.Id_Polluant = ?'
        params.append(pollutant_id)
    if start_date:
        query += ' AND Mesures.Date_Debut >= ?'
        params.append(start_date)
    if end_date:
        query += ' AND Mesures.Date_Fin <= ?'
        params.append(end_date)

    query += ' LIMIT ? OFFSET ?'
    params.extend([per_page, offset])

    result = query_db(query, params)
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des mesures par jour
@app.route('/daily_average')
def get_daily_average():
    print(" La méthode get_daily_average a été appelée")
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page - 1) * per_page
    pollutant_id = request.args.get('pollutant_id')
    station_id = request.args.get('station_id')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if start_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S').strftime('%Y/%m/%d %H:%M:%S')
    if end_date:
        end_date = datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%S').strftime('%Y/%m/%d %H:%M:%S')

    query = 'SELECT AVG(Valeur) as average FROM Mesures WHERE 1=1'
    params = []

    if pollutant_id:
        query += ' AND Id_Polluant = ?'
        params.append(pollutant_id)
    if station_id:
        query += ' AND Id_Station = ?'
        params.append(station_id)
    if start_date and end_date:
        query += ' AND Date_Debut >= ? AND Date_Fin <= ?'
        params.extend([start_date, end_date])

    query += ' LIMIT ? OFFSET ?'
    params.extend([per_page, offset])

    result = query_db(query, params, one=True)
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des mesures
@app.route('/range')
def get_range():
    print(" La méthode get_range a été appelée")
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page - 1) * per_page
    pollutant_id = request.args.get('pollutant_id')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if start_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S').strftime('%Y/%m/%d %H:%M:%S')
    if end_date:
        end_date = datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%S').strftime('%Y/%m/%d %H:%M:%S')

    query = 'SELECT MIN(Valeur) as minimum, MAX(Valeur) as maximum FROM Mesures WHERE 1=1'
    params = []

    if pollutant_id:
        query += ' AND Id_Polluant = ?'
        params.append(pollutant_id)
    if start_date and end_date:
        query += ' AND Date_Debut >= ?'
        params.append(start_date)
    if end_date and start_date:
        query += ' AND Date_Fin <= ?'
        params.append(end_date)

    query += ' LIMIT ? OFFSET ?'
    params.extend([per_page, offset])

    result = query_db(query, params, one=True)
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
