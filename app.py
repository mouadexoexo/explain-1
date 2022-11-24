# -*- coding: utf-8 -*-
from flask_cors import CORS, cross_origin
from flask import Flask,render_template
import pandas as pd
import pandas

app = Flask(__name__)

CORS(app)
pandas.set_option('display.max_columns', 15)

df = pd.read_csv("territories.csv", delimiter= ',')
df1 = pd.read_csv("territory_parents.csv", delimiter= ',')

#--- Dataframe contenant  id, code , name,kind territories.csv
t=df[['id','code','name','kind']]
# ---Dataframe contenant  id, code , name,kind parent_territories.csv
k=df1[['child_id','parent_id']]
#--fusion les deux dataframes pour avoir dataframe contient que les departement
Table=pandas.merge(t[t.kind=='FRDEPA'],k,left_on='id',right_on='parent_id')
#print Table

#----------rename les columns-
new_table = Table[['code','name','child_id']].rename(columns={'code':'code_depart','name': 'name_departement'})
#print new_table


#-------fusion deux datafrme pour liaison entre depart et continent
Departement_continent=pandas.merge(new_table,t,left_on='child_id',right_on='id')
#print Departement_continent


#-------affichage chaque continent a quel departement appartient
resultat = Departement_continent[['code','name_departement','name','kind']]
#print resultat

# -------affichage elu avec id elu comme argument
def codee(x):
    all=resultat[resultat.code==x]
    res=all[all.kind=='FREPCI']
    return res[['code','name_departement','name']]
    
#-------Affichage de tout les EPCI d'un departement comme argument nom de departement
def elu(x):
    all=resultat[resultat.name_departement==x]
    res=all[all.kind=='FREPCI']
    return res[['code','name']]
    

#res=resultat[resultat.kind=='FREPCI']
#final=res.to_json(orient='records')
#print final

#print codee('200070555')
#print elu('Ain')

#--------affichage de tout les elu qui appartient a un departement
#Ain=resultat[resultat.name_departement=='Ain']
#print Ain

#-------------affichage de tt les epci
epc=t[t.kind=='FREPCI']
#print epc


#-----------affichage de tout les deppartement
depart=t[t.kind=='FRDEPA']
#print depart
depart=depart[['id','code','name','kind']].rename(columns={'name':'name_departements','code':'code_departements'})
#depart['epcis'] = 'test'
#list_depart = depart.to_json(orient='records')
#print list_depart
#print depart.to_json(orient='records')
#print depart


#-----------------datafram contient tout les departement et leurs epci
Departement_epci=pandas.merge(new_table,epc,left_on='child_id',right_on='id').rename(columns={'name': 'name_epci'})
Departement_epci=Departement_epci[['code_depart','name_departement','code','name_epci','kind']]
#print Departement_epci.to_json(orient = 'records')

#-------- fusion deux dataframe a partir du nom en commun de departement
resul=pandas.merge(Departement_epci,depart,left_on='name_departement',right_on='name_departements')
#print resul


#--------affichage les epci a partir du code departement
def show_epci(x):
    res=resul[resul.code_depart==x].name_epci
    return res
#print show_epci('01')
test = resul[resul.code_depart=='01']
#print test


#------Convertir vers Json------------------
new_test = test.to_json(orient = 'records')
#print new_test

departement_json=depart.to_json(orient='records')
#print departement_json


#print show_epci('22')
#print resul[['name_departement',]]

#------ affichage des departments comme arguemnt code departement
def code_departement(x):
    nom_departement=depart[depart.code_departements==x]
    return nom_departement[['code_departements','name_departements']]
#print code_departement('01')

#------ affichange de tt departement avec leur epci----------
dict= depart.to_dict('records')
#dict[3]['epci']= list()
#list_epci=[]
list_epci=show_epci('01').to_list()
#print list_epci
#dict[0]['epci']= list_epci
#print depart

#------------------- Creer une liste des epcis de chaque departement---------------
i=0
for ind in depart.index:
    dict[i]['epci']= list()
    list_epci=[]
    list_epci=elu(depart['name_departements'][ind])
    dict[i]['epci']= list_epci
    i=i+1
    

new = pd.DataFrame.from_dict(dict)
new= new.to_json(orient='records')
#print new


@app.route('/departements')
def hello():
    return new

@app.route('/FRDEPA<x>')
def home(x):
    return show_epci(x).to_json(orient = 'records')
if __name__=="__main__":
    app.run(debug=True)
