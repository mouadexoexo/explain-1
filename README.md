#gbarrois-eXplain

[Contexte]

Nos clients sont des entreprises qui ont des projets avec de forts enjeux locaux sur l’acceptabilité par la population et par les élus. Par exemple, les entreprises implémentant des champs d'éoliennes ont envie de pouvoir répondre à des questions telles que: “Est-ce que la population est favorable aux énergies renouvelable ?” ou “Est-ce que le maire d’une ville s’est déjà prononcé en faveur de l'énergie éolien ?”.
Une des composante de notre logiciel consiste à permettre à l’utilisateur 
de retrouver, parmi une base de données exhaustive des élus de France, les élus d’un territoire de son choix (Département, Communauté de commune, Commune…),
effectuer une recherche par nom et prénom pour retrouver un élu pour sur lequel il souhaiterait avoir plus d’information, 
accéder pour un élu spécifique, à ses mandats (passés et en cours) et ses prises de position dans la presse.

[Objectif]

L’objectif de ce projet est de construire en partie une page permettant de visualiser les élus sur un territoire et de faire une recherche sur ces élus par nom prénom.


### Pré-requis

Ce qu'il est requis pour réaliser le projet:

- Python ainsi que ses bibliothèques pandas, flask
- Angular


### Installation

Les étapes pour installer python et ses bibliothéques

_______ Installation python ____________ 


sudo apt-get install python3.7


------------ Installation Pandas et flask ---------------

Tapez la commande : pip3 install pandas
Tapez la commande : pip3 install flask



---------- Installation Angular ----------------

1.installer nodejs et npm https://nodejs.org/fr/download/ 

2.Installer Angular : npm install -g @ angular / cl


## Démarrage
Il faut ouvrir 2 terminal pour lancer le projet.

[Terminal 1] : Entrer dans dossier explain-1 ensuite tapez la commande "python app.py " pour executer le fichier qui est écrit en python "app.py"


[Terminal 2] : Entrer dans le dossier Front qui se trouve dans dossier explain-1 ensuite tapez la commande "npm start"  pour executer la partie Angular Front


