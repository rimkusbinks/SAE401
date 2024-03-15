from flask import Flask, render_template, request, send_file
import matplotlib.pyplot as plt
import io
import pandas as pd
import sqlite3

app = Flask(__name__)

# Route pour afficher le formulaire
@app.route('/')
def home():
    return render_template('formulaire.html')

# Route pour traiter le formulaire et générer la visualisation
@app.route('/visualiser', methods=['POST'])
def visualiser():
    station_id = request.form['station_id']
    date_debut = request.form['date_debut']
    date_fin = request.form['date_fin']
    polluant = request.form['polluant']
    
    # Fonction pour récupérer les données et générer le graphique
    img = generer_graphique(station_id, date_debut, date_fin, polluant)
    
    return send_file(img, mimetype='image/png', as_attachment=True, attachment_filename='visualisation.png')

def generer_graphique(station_id, date_debut, date_fin, polluant):
    # Exemple de connexion à la base de données SQLite et récupération des données
    conn = sqlite3.connect('chemin/vers/ta/base_de_donnees.db')
    query = f"SELECT * FROM mesures WHERE station_id = {station_id} AND date BETWEEN '{date_debut}' AND '{date_fin}' AND polluant = '{polluant}'"
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    # Générer le graphique
    plt.figure()
    plt.plot(df['date'], df['valeur'])
    plt.title(f'Visualisation pour {polluant} de {date_debut} à {date_fin}')
    plt.xlabel('Date')
    plt.ylabel('Valeur')
    
    # Sauvegarder le graphique dans un objet BytesIO
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    
    return img

if __name__ == '__main__':
    app.run(debug=True)
