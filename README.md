# SAE 4.01

## Introduction

SAE 4.01 est un projet de gestion et d'analyse de données environnementales, axé en particulier sur la qualité de l'air et les mesures de pollution. Ce dépôt contient des scripts pour l'importation et la gestion de ces données, ainsi que le schéma de base de données nécessaire pour les stocker et les organiser.

## Prérequis

- Python 3.x
- Bibliothèques : requests, pandas, sqlite3, ssl
- Base de données SQLite

## Installation

Clonez le dépôt et installez les bibliothèques Python requises en utilisant :

```bash
pip install requests pandas sqlite3 ssl datetime
```

## Configuration de la base de données

Avant d'exécuter le script d'importation, configurez votre base de données à l'aide du fichier schema.sql. Ce fichier contient des commandes SQL pour créer les tables nécessaires au stockage des données sur la pollution. Pour créer la base de données, à la racide de votre clone git, dans un dossier "database", exécutez :

```sql
sqlite3 SAE401.db < schema.sql
```

## Instructions d'importation des données

Le script import_data.py est utilisé pour importer les données de pollution dans la base de données. Ce script récupère les données d'une source spécifiée, les traite et les stocke dans la base de données. Il gère la création d'identifiants uniques pour différents polluants et assure l'intégrité des données.

Pour exécuter le script, utilisez :

```bash
python import_data.py
```

Assurez-vous que votre base de données est configurée et accessible par le script.

## Contribution

Les contributions au projet SAE 4.01 sont les bienvenues. Veuillez vous assurer de suivre le style de code et les lignes directrices de contribution du projet.
