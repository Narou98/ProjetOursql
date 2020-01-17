from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import json
#import users.json


app = Flask(__name__)
api = Api(app)

"""
	*************************************************
	************Fonction GET de select***************
	*************************************************
"""
@app.route('/users/<string:name>', methods=['GET'])
#name="table1"
def get(name):
	with open ('users.json') as fichier:
		dictionnaireGlobal=json.load(fichier)
		print (dictionnaireGlobal[name])
		for i in range(len(dictionnaireGlobal[name])):
			print(dictionnaireGlobal[name][i])
		return (json.dumps(dictionnaireGlobal[name], indent = 4))



"""
	*******************************************************************************************
	************Fonction GET avec précision (id) -->select  avec where ou having***************
	*******************************************************************************************
"""
@app.route('/user_id/<string:table_name>/<string:colone>/<int:nb_id>', methods = ['get'])
def get_id(table_name,colone,nb_id) :
	with open("users.json") as fichier:
		dictionnaireGlobal=json.load(fichier)
		liste=[]
		liste=dictionnaireGlobal.copy()
		for j in liste[table_name]:
			if j[colone]==nb_id:
				#print(json.dumps(liste[table_name]))
				return json.dumps(liste[table_name][(nb_id)-1])


"""
	*************************************************************************
	************Fonction PUT-->UPDATE****************************************
	*************************************************************************
"""
@app.route('/update/<string:table_name>/<int:nb_id>', methods = ['PUT'])
def update(table_name,nb_id) :
	with open("users.json") as fichier:
		dictionnaireGlobal=json.load(fichier)
		liste=[]
		liste=dictionnaireGlobal.copy()
		for j in liste[table_name]:
			if j["id"]==nb_id:
				data = request.get_json()
				liste[table_name].remove(j)
				liste[table_name].append(data)
				dictionnaireGlobal=json.dumps(liste[table_name],indent=4)
				fichier=open("users.json","w")
				fichier.write(dictionnaireGlobal)
				fichier.close()
				return json.dumps(liste[table_name],indent=4)





"""
	*************************************************************************
	************Fonction POST -->insertion des enregistrements***************
	*************************************************************************
"""

@app.route('/insert/<string:table_name>', methods = ['POST'])
def post(table_name) :
	data = request.get_json()
	with open("users.json") as fichier:
		dictionnaireGlobal=json.load(fichier)
		liste=[]

		liste=dictionnaireGlobal.copy()
		liste[table_name].append(data)
		dictionnaireGlobal=json.dumps(liste,indent=4)
		fichier=open("users.json","w")
		fichier.write(dictionnaireGlobal)
		fichier.close()
	return data

#post ("table1",enregistrement)



"""
	*************************************************************************
	************Fonction DELETE -->suppression d'enregistrements***************
	*************************************************************************
"""

@app.route('/delete/<string:table_name>/<string:colone>/<int:id>', methods = ['delete'])
def delete(table_name,id,colone) :
	with open("users.json") as fichier:
		dictionnaireGlobal=json.load(fichier)
		liste=[]
		liste=dictionnaireGlobal.copy()
		for j in liste[table_name]:
			if j[colone]==id:
				liste[table_name].remove(j)
			dictionnaireGlobal=json.dumps(liste,indent=4)
			fichier=open("users.json","w")
			fichier.write(dictionnaireGlobal)
			fichier.close()
			return dictionnaireGlobal
	
			
		liste[table_name].remove(liste[table_name][j])


			
#get(name)
if __name__ == '__main__':
	app.run(debug = True, port =8889)