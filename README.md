# Projet 2 - Site Web

Projet 2 du groupe 1C_3 pour le cours LINFO1002 à l'UCLouvain.

Le but du projet est de créer un site web qui analyse des
données provenant d'une DataBase pour en faciliter la visualisation.

## Liens:

> - **Lien du Repository GitHub:** <https://github.com/Julien-Devos/Projet2-Site-Web>
> - **Lien du site** <http://juliendv.eu.pythonanywhere.com>

## Installation:

  - Créer un environnement virtuel.

  - Installer les packages nécessaires à l'aide de cette commande:

    ```python
    $ pip install -r requirements.txt
    ```

  - Une fois les packages installés,
  
    ```python
    $ set FLASK_APP=webSite
    $ flask create-db
    $ flask run
    ```
    
  - Rendez vous alors sur: <http://127.0.0.1:5000>

## Arborescence de fichiers du projet:

```
.
├── instance
│   └── data.sqlite # Database
├── webSite # python Package
│   ├── sql-data
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
│   │   ├── Chart.js
│   │   │   ├── Chart.bundle.min.js
│   │   │   ├── Chart.min.css
│   │   │   └── Chart.min.js
│   │   ├── Fonts
│   │   │   └── icons.woff
│   │   ├── img
│   │   │   ├── illustrations
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
│   │   ├── styles
│   │   │   ├── dark_theme.css
│   │   │   ├── light_theme.css
│   │   │   └── style.css
│   │   └── script.js
│   ├── templates
│   │   ├── 404.html
│   │   ├── base.html
│   │   ├── figure1.html
│   │   ├── figure2.html
│   │   ├── figure3.html
│   │   ├── figure4.html
│   │   ├── figure5.html
│   │   └── index.html
│   ├── __init__.py
│   ├── db_create.py
│   ├── db_init.py
│   ├── graphs.py
│   ├── moon.py
│   └── pages.py
├── .gitignore    
├── README.md
├── requirements.txt # Contient les packages à installer
└── setup.py    
```