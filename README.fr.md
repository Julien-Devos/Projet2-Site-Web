[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/Julien-Devos/Projet2-Site-Web/blob/master/README.md)
[![fr](https://img.shields.io/badge/lang-fr-blue.svg)](https://github.com/Julien-Devos/Projet2-Site-Web/blob/master/README.fr.md)

# Projet 2 - Site Web

Projet 2 du groupe 1C_3 pour le cours LINFO1002 à l'UCLouvain.

Le but du projet est de créer un site web qui analyse des
données provenant d'une DataBase pour en faciliter la visualisation.

## Liens:

> - **Lien du Repository GitHub:** <https://github.com/Julien-Devos/Projet2-Site-Web>
> - **Lien du site hébergé:** <http://juliendv.eu.pythonanywhere.com>

## Conditions requises:

  - Avoir Python 3.8 minimum.

  - Avoir installé les packages requis.
    
    ```batch
    Pour les installer:
    
    $ pip install -r requirements.txt
    ```

## Installation:

  - Si les conditions requises sont cochées:
  
    ```batch
    Sur windows:
    
    $ set FLASK_APP=webSite
    $ flask create-db
    
    Sur Linux/MacOS:
    
    $ export FLASK_APP=webSite
    $ flask create-db
    ```

  - Une fois que c'est fait, pour lancer le site il suffit de faire cette commande:

    ```batch
    $ flask run
    ```
    
  - Rendez vous alors sur: <http://127.0.0.1:5000>

## Arborescence de fichiers du projet:

```
.
├── instance
│   └── data.sqlite # base de données
├── webSite # python Package
│   ├── sql-data # Dossier qui contient les fichiers SQL
│   │   ├── animaux_data.sql
│   │   ├── animaux_types_data.sql
│   │   ├── animaux_velages_data.sql
│   │   ├── complications_data.sql
│   │   ├── familles_data.sql
│   │   ├── schema.sql
│   │   ├── types_data.sql
│   │   ├── velages_complications_data.sql
│   │   └── velages_data.sql
│   ├── static
│   │   ├── Chart.js # Dossier qui contient les fichier pour utiliser Chart.js
│   │   │   ├── Chart.min.css
│   │   │   └── Chart.min.js
│   │   ├── Fonts 
│   │   │   └── icons.woff # Police utilisée pour les icons du site
│   │   ├── img # Dossier qui contient toutes les images/logos utilisées sur le site
│   │   │   ├── illustrations
│   │   │   │   ├── farm.png
│   │   │   │   ├── farm2.png
│   │   │   │   ├── Vache 1.jpg
│   │   │   │   ├── Vache 2.jpg
│   │   │   │   ├── Vache 3.jpg
│   │   │   │   ├── Vache 4.jpg
│   │   │   │   ├── Vache 5.jpg
│   │   │   │   └── Vache 6.jpg
│   │   │   ├── logo.ico
│   │   │   ├── logo.png
│   │   │   ├── logo404.png
│   │   │   └── logoKAWAI.png
│   │   ├── styles # Dossier qui contient tout le css du site
│   │   │   ├── dark_theme.css
│   │   │   ├── light_theme.css
│   │   │   └── style.css
│   │   └── script.js # Script utilisé pour changer de theme et mettre le cookie à jour
│   ├── templates # Dossier qui contient tous les fichiers html
│   │   ├── 404.html
│   │   ├── base.html
│   │   ├── figure1.html
│   │   ├── figure2.html
│   │   ├── figure3.html
│   │   ├── figure4.html
│   │   ├── figure5.html
│   │   └── index.html
│   ├── __init__.py # Fichier python utilisé pour lancer l'app flask
│   ├── db_create.py # Fichier python utilisé pour créer la base de données
│   ├── db_init.py # Fichier python utilisé pour initialiser la commande 'create-db' et plus
│   ├── graphs.py # Fichier python utilisé pour retourner les données affichées sur les graphiques
│   ├── moon.py # Fichier python utilisé pour connaitre la phase de la lune d'une date
│   └── pages.py # Fichier python utilisé pour afficher toutes les pages html du site
├── .gitignore    
├── README.fr.md
├── README.md
├── requirements.txt # Contient tous les packages à installer
└── setup.py # Fichier python utilisé pour télécharger tous les packages nécéssaires
```