from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def query_db(query, args=(), one=False):
    with sqlite3.connect("database/SAE401.db") as conn:
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
    query = 'SELECT * FROM Organismes'
    result = query_db(query)
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des zas
@app.route('/zas')
def get_zas():
    print(" La méthode get_zas a été appelée")
    query = 'SELECT * FROM Zas'
    result = query_db(query)
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des stations
@app.route('/stations')
def get_stations():
    print(" La méthode get_stations a été appelée")
    query = 'SELECT * FROM Stations'
    result = query_db(query)
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des polluants
@app.route('/polluants')
def get_polluants():
    print(" La méthode get_polluants a été appelée")
    query = 'SELECT * FROM Polluants'
    result = query_db(query)
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des types influence
@app.route('/types_influence')
def get_types_influence():
    print(" La méthode get_types_influence a été appelée")
    query = 'SELECT * FROM Types_Influence'
    result = query_db(query)
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des types evaluation
@app.route('/types_evaluation')
def get_types_evaluation():
    print(" La méthode get_types_evaluation a été appelée")
    query = 'SELECT * FROM Types_Evaluation'
    result = query_db(query)
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des types mesure
@app.route('/procedures_mesure')
def get_procedures_mesure():
    print(" La méthode get_procedures_mesure a été appelée")
    query = 'SELECT * FROM Procedures_Mesure'
    result = query_db(query)
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des types valeur
@app.route('/types_valeur')
def get_types_valeur():
    print(" La méthode get_types_valeur a été appelée")
    query = 'SELECT * FROM Types_Valeur'
    result = query_db(query)
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des reglementations
@app.route('/reglementations')
def get_reglementations():
    print(" La méthode get_reglementations a été appelée")
    query = 'SELECT * FROM Reglementaires'
    result = query_db(query)
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des reglementations
@app.route('/discriminants')
def get_discriminants():
    print(" La méthode get_discriminants a été appelée")
    query = 'SELECT * FROM Discriminants'
    result = query_db(query)
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des mesures
@app.route('/measurements')
def get_measurements():
    print(" La méthode get_measurements a été appelée")
    station_id = request.args.get('station_id')
    pollutant_id = request.args.get('pollutant_id')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    query = '''
        SELECT * FROM Mesures
        WHERE Id_Station = ? AND Id_Polluant = ? AND Date_Debut >= ? AND Date_Fin <= ?
    '''
    result = query_db(query, (station_id, pollutant_id, start_date, end_date))
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des moyennes journalières
@app.route('/daily_average')
def get_daily_average():
    print(" La méthode get_daily_average a été appelée")
    pollutant_id = request.args.get('pollutant_id')
    station_id = request.args.get('station_id')
    date = request.args.get('date')
    query = '''
        SELECT AVG(Valeur) as average FROM Mesures
        WHERE Id_Polluant = ? AND Id_Station = ? AND Date_Debut = ?
    '''
    result = query_db(query, (pollutant_id, station_id, date), one=True)
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

# récupération des moyennes horaires
@app.route('/range')
def get_range():
    print(" La méthode get_range a été appelée")
    pollutant_id = request.args.get('pollutant_id')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    query = '''
        SELECT MIN(Valeur) as minimum, MAX(Valeur) as maximum FROM Mesures
        WHERE Id_Polluant = ? AND Date_Debut >= ? AND Date_Fin <= ?
    '''
    result = query_db(query, (pollutant_id, start_date, end_date), one=True)
    if result:
        print("La requête a retourné des résultats")
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
