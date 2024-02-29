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
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page - 1) * per_page
    query = 'SELECT * FROM Organismes LIMIT ? OFFSET ?'
    result = query_db(query, (per_page, offset))
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des zas
@app.route('/zas')
def get_zas():
    print(" La méthode get_zas a été appelée")
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page - 1) * per_page
    query = 'SELECT * FROM Zas LIMIT ? OFFSET ?'
    result = query_db(query, (per_page, offset))
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des stations
@app.route('/stations')
def get_stations():
    print(" La méthode get_stations a été appelée")
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page - 1) * per_page
    query = 'SELECT * FROM Stations LIMIT ? OFFSET ?'
    result = query_db(query, (per_page, offset))
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des polluants
@app.route('/polluants')
def get_polluants():
    print(" La méthode get_polluants a été appelée")
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page - 1) * per_page
    query = 'SELECT * FROM Polluants LIMIT ? OFFSET ?'
    result = query_db(query, (per_page, offset))
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des types influence
@app.route('/types_influence')
def get_types_influence():
    print(" La méthode get_types_influence a été appelée")
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page - 1) * per_page
    query = 'SELECT * FROM Types_Influence LIMIT ? OFFSET ?'
    result = query_db(query, (per_page, offset))
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des types evaluation
@app.route('/types_evaluation')
def get_types_evaluation():
    print(" La méthode get_types_evaluation a été appelée")
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page - 1) * per_page
    query = 'SELECT * FROM Types_Evaluation LIMIT ? OFFSET ?'
    result = query_db(query, (per_page, offset))
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des types mesure
@app.route('/procedures_mesure')
def get_procedures_mesure():
    print(" La méthode get_procedures_mesure a été appelée")
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page - 1) * per_page
    query = 'SELECT * FROM Procedures_Mesure LIMIT ? OFFSET ?'
    result = query_db(query, (per_page, offset))
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des types valeur
@app.route('/types_valeur')
def get_types_valeur():
    print(" La méthode get_types_valeur a été appelée")
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page - 1) * per_page
    query = 'SELECT * FROM Types_Valeur LIMIT ? OFFSET ?'
    result = query_db(query, (per_page, offset))
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des reglementations
@app.route('/reglementations')
def get_reglementations():
    print(" La méthode get_reglementations a été appelée")
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page - 1) * per_page
    query = 'SELECT * FROM Reglementaires LIMIT ? OFFSET ?'
    result = query_db(query, (per_page, offset))
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des reglementations
@app.route('/discriminants')
def get_discriminants():
    print(" La méthode get_discriminants a été appelée")
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    offset = (page - 1) * per_page
    query = '''SELECT * FROM Discriminants LIMIT ? OFFSET ?'''
    result = query_db(query, (per_page, offset))
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des mesures
@app.route('/measurements')
def get_measurements():
    print(" La méthode get_measurements a été appelée")
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

    query = 'SELECT * FROM Mesures WHERE 1=1'
    params = []

    if station_id:
        query += ' AND Id_Station = ?'
        params.append(station_id)
    if pollutant_id:
        query += ' AND Id_Polluant = ?'
        params.append(pollutant_id)
    if start_date:
        query += ' AND Date_Debut >= ?'
        params.append(start_date)
    if end_date:
        query += ' AND Date_Fin <= ?'
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
