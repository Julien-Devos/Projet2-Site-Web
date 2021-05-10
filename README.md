[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/Julien-Devos/Projet2-Site-Web/blob/master/README.md)
[![fr](https://img.shields.io/badge/lang-fr-blue.svg)](https://github.com/Julien-Devos/Projet2-Site-Web/blob/master/README.fr.md)

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

## Website screeshots

A screenshots folder is in the project files if needed. The screenshots are made in 
order to have one page on each image, so the format is not always right.
To have the bes representation of the website you have to zoom on the images.

## Project file tree:

```
.
├── Captures d'écran du site 
│   ├── Thème clair
│   ├── Thème sombre
│   └── Version mobile
├── instance
│   └── data.sqlite # Database
├── webSite # python Package
│   ├── sql-data # Folder that contains all sql files
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
│   │   ├── Chart.js # Folder that contains files to use Chart.js
│   │   │   ├── Chart.min.css
│   │   │   └── Chart.min.js
│   │   ├── Fonts 
│   │   │   └── icons.woff # Font used for icons on the website
│   │   ├── img # Folder that contains all the images/logos used on the website
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
│   │   ├── styles # Folder that contains all the css of the website
│   │   │   ├── dark_theme.css
│   │   │   ├── light_theme.css
│   │   │   └── style.css
│   │   └── script.js # Script used to switch theme and update cookies
│   ├── templates # Folder that contains all the html files
│   │   ├── 404.html
│   │   ├── base.html
│   │   ├── figure1.html
│   │   ├── figure2.html
│   │   ├── figure3.html
│   │   ├── figure4.html
│   │   ├── figure5.html
│   │   └── index.html
│   ├── __init__.py # Python file used to start the flask app
│   ├── db_create.py # Python file used to create the database
│   ├── db_init.py # Python file used to init the 'create-db' and more
│   ├── graphs.py # Python file used to return the data that will be used in charts
│   ├── moon.py # Python file used to know the moon phase of a date
│   └── pages.py # Python file used to render all the pages of the website
├── .gitignore    
├── README.fr.md
├── README.md
├── requirements.txt # Contains all the needed packages
└── setup.py # Python file used to install all the needed packages
```