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

@app.route('/analyse/concentrations-moyennes/resultat', methods=['POST'])
def afficher_resultats_concentrations_moyennes():
    date_debut = request.form['date_debut']
    date_fin = request.form['date_fin']
    # Effectuer l'analyse en utilisant les dates spécifiées
    # Générer les résultats (ceci est un exemple et devra être adapté)
    resultats = "Résultats de l'analyse ici"
    return render_template('resultats_concentrations_moyennes.html', resultats=resultats)


if __name__ == '__main__':
    app.run(debug=True)
