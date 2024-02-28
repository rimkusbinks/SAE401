from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def query_db(query, args=(), one=False):
    with sqlite3.connect('../database/SAE401.db') as conn:
        cur = conn.cursor()
        cur.execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv

@app.route('/organismes')
def get_organismes():
    query = 'SELECT * FROM Organismes'
    result = query_db(query)
    return jsonify(result)

@app.route('/zas')
def get_zas():
    query = 'SELECT * FROM Zas'
    result = query_db(query)
    return jsonify(result)

@app.route('/stations')
def get_stations():
    query = 'SELECT * FROM Stations'
    result = query_db(query)
    return jsonify(result)

@app.route('/polluants')
def get_polluants():
    query = 'SELECT * FROM Polluants'
    result = query_db(query)
    return jsonify(result)

@app.route('/types_influence')
def get_types_influence():
    query = 'SELECT * FROM Types_Influence'
    result = query_db(query)
    return jsonify(result)

@app.route('/types_evaluation')
def get_types_evaluation():
    query = 'SELECT * FROM Types_Evaluation'
    result = query_db(query)
    return jsonify(result)

@app.route('/procedures_mesure')
def get_procedures_mesure():
    query = 'SELECT * FROM Procedures_Mesure'
    result = query_db(query)
    return jsonify(result)

@app.route('/types_valeur')
def get_types_valeur():
    query = 'SELECT * FROM Types_Valeur'
    result = query_db(query)
    return jsonify(result)

@app.route('/reglementations')
def get_reglementations():
    query = 'SELECT * FROM Reglementaires'
    result = query_db(query)
    return jsonify(result)

@app.route('/discriminants')
def get_discriminants():
    query = 'SELECT * FROM Discriminants'
    result = query_db(query)
    return jsonify(result)

@app.route('/measurements')
def get_measurements():
    station_id = request.args.get('station_id')
    pollutant_id = request.args.get('pollutant_id')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    query = '''
        SELECT * FROM Mesures
        WHERE Id_Station = ? AND Id_Polluant = ? AND Date_Debut >= ? AND Date_Fin <= ?
    '''
    result = query_db(query, (station_id, pollutant_id, start_date, end_date))
    return jsonify(result)

@app.route('/daily_average')
def get_daily_average():
    pollutant_id = request.args.get('pollutant_id')
    station_id = request.args.get('station_id')
    date = request.args.get('date')
    query = '''
        SELECT AVG(Valeur) as average FROM Mesures
        WHERE Id_Polluant = ? AND Id_Station = ? AND Date_Debut = ?
    '''
    result = query_db(query, (pollutant_id, station_id, date), one=True)
    return jsonify(result)

@app.route('/range')
def get_range():
    pollutant_id = request.args.get('pollutant_id')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    query = '''
        SELECT MIN(Valeur) as minimum, MAX(Valeur) as maximum FROM Mesures
        WHERE Id_Polluant = ? AND Date_Debut >= ? AND Date_Fin <= ?
    '''
    result = query_db(query, (pollutant_id, start_date, end_date), one=True)
    return jsonify(result)
if __name__ == '__main__':
    app.run(debug=True)
