[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/Julien-Devos/Projet2-Site-Web/blob/master/README.fr.md)
[![fr](https://img.shields.io/badge/lang-fr-blue.svg)](https://github.com/Julien-Devos/Projet2-Site-Web/blob/master/README.md)

# Projet 2 - Site Web

Project 2 of group 1C_3 for the LINFO1002 course at UCLouvain.

The goal of the project is to create a website that analyse data from a 
database to make them more visual.

## Links:

> - **GitHub repository:** <https://github.com/Julien-Devos/Projet2-Site-Web>
> - **Link of the hosted website:** <http://juliendv.eu.pythonanywhere.com>

## Requirements:

  - Needs to have Python 3.8 installed minimum.

  - Needs to have all the required packages installed.
    
    ```batch
    To install them:
    
    $ pip install -r requirements.txt
    ```

## Set-up:

  - If the requirements are met:
  
    ```batch
    On windows:
    
    $ set FLASK_APP=webSite
    $ flask create-db
    
    On Linux/MacOS:
    
    $ export FLASK_APP=webSite
    $ flask create-db
    ```

  - When it's done, you just have to type this command to launch the website:

    ```batch
    $ flask run
    ```
    
  - And then you can go on: <http://127.0.0.1:5000>

## Project file tree:

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