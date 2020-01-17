import os.path 
import simplejson

#le LDD
def create(name,type,base):
	if type.upper() == "DATABASE" :
		path = name
		if os.path.exists(path):
			return "database not created"
		else:
			os.mkdir(name)
			return "database created successfully"
	if type.upper() == "USER":
		f=open(name+".json","w")

	if type.upper() == "TABLE":
		path = name+".json"
		if os.path.exists(base+"/"+path):
			return "Table not created"
		else:
			f=open(base+"/"+path,"w")
			f.write("")
			f.close()
			return "Table created successfully"
def drop(chaine,type,base):
	path = chaine
	if os.path.exists(path):
		if type.upper()=="DATABASE":
		    os.remove(chaine)
		    return "database is droped successfully"
		if type.upper() == "TABLE":
		 	if os.path.exists(base+"/"+path):
		 		os.remove(chaine)
		        #return "table is droped successfully"
	#else:
		#return "database not droped"
def alter(chain):
	pass

#le LMD et le LED
def insert(base,o,bd):
	attr=[]
	donnee=[]
	chaine=''
	attr,donnee = getData(o)
	tab={}
	for x in range(0,len(attr)):
		tab[attr[x]] = donnee[x]
	path = base+".json"
	if os.path.exists(bd+"/"+path):
		with open(bd+"/"+path,"a+") as g:
			g.seek(0,0)
			if g.read()=='':
				simplejson.dump(tab,g,indent=4)
			else:	
				g.write(",\n")
				simplejson.dump(tab,g,indent=4)
		g.close()
		return "insertion successfull"
	else:
		return "insertion not succesfull"
def update(chaine):
	pass
def delete(base,table,option):
	with open(base) as json_data:
	    data_dict = json.load(json_data)
	    liste=[]
	    liste=data_dict.copy()
	    for val in data_dict[table]:
	    	if option==val["nom"]:
	    		liste[table].remove(val)
	    	if option==val["prenom"]:
	    		liste[table].remove(val)
	    	if option==val["age"]:
	    		liste[table].remove(val)
	    data_dict=json.dumps(liste,indent=1)
	    print(data_dict)
	    fichier = open(base,'w')
	    fichier.write(data_dict)
	    fichier.close()

def select(element,base,bd):
	path = base+".json"
	print("element: "+element)
	if os.path.exists(bd+"/"+path):
		with open(bd+"/"+path,"a+") as f:
			f.seek(0,0)
			k=f.read()
		r="[\n"+k+"\n]"
		m=simplejson.loads(r)
		ch = ""
		element1 = element.split(",")
		print(element1,len(element1))
		attr,donnee = getjsondata(m)
		attr1 = []
		donnee1 = []
		if element1[0] == "*":
			attr1 =attr
			donnee1 = donnee
		else:
			t =[]
			for e in element1:
				attr1.append(e) 
			t = []
			for i in range(0,len(attr1)):
				for x in range(0,len(attr)):
					if attr1[i] == attr[x]:
						t.append(x)
			mod =0
			while mod != len(donnee):
				for j in range(0,len(t)):
					for k in range(mod,mod+len(attr)):
						if t[j]+mod == k:
							donnee1.append(donnee[k])
				mod+=len(attr)
		for chaine in attr1:
			ch+="#"+chaine
		ch+="|"
		for chaine1 in donnee1:
			ch+="#"+chaine1
		print(ch)
		n=simplejson.dumps(m,indent=4)
		return ch
	else:
		return "table not exist"
#transaction
def start():
	pass
def commit():
	pass
def rollback():
	pass

#authentification
def auth(user,password):
	return "1"
def adduser(user,password):
	pass
def deluser(user,password):
	pass

#fonctions auxiliaires
def quit():
	pass
def cut(chaine,key):
	return chaine.split(key)
def writejson(chaine,base,table):
	pass
def readjson():
	pass
def addtable(table,base):
	pass
def addEntre():
	pass
def success():
	pass
def abort():
	pass
def space(chaine):
	chaine1=""
	j=0
	for i in range(0,len(chaine)):
		if chaine[i] == " ": 
			if chaine[i-1] == " " or chaine[i-1] == "," or chaine[i-1] == "=" or chaine[i+1] == "," or chaine[i+1] == "=" or chaine[i+1] == "(" or i==0:
				pass
			else:
				chaine1+="#" 
		else:
			if chaine[i] !="(":
				chaine1+=chaine[i]
		if chaine[i] == "(":
				chaine1 += "#("	
	return chaine1
def getData(chaine):
	donnee = chaine.split("(")
	#print(donnee)
	donnee = donnee[1].split(")")
	donnee = donnee[0].split(",")
	tab=[]
	for a in donnee:
		tab.append(a)
	tab_donnee=[]
	tab_attr=[]	
	for b in tab:
		c = b.split("=")
		tab_attr.append(c[0])
		tab_donnee.append(c[1])
	return tab_attr,tab_donnee
def getjsondata(tab):
	attr = []
	donnee = []
	for chaine in tab:
		for cle in chaine.keys():
			if cle in attr:
				pass
			else:
				attr.append(cle)
		for val in chaine.values():
			donnee.append(val)
	print(attr)
	print(donnee)
	return attr,donnee
def describe(table,bd):
	path = table+".json"
	
	if os.path.exists(bd+"/"+path):
		with open(bd+"/"+path,"a+") as f:
			f.seek(0,0)
			k=f.read()
		r="[\n"+k+"\n]"
		m=simplejson.loads(r)
		ch = ""
		attr,donnee = getjsondata(m)
		for chaine in attr:
			ch+="#"+chaine
		return ch
def showtable(base):
	dossier = os.listdir(base)
	ch = ""
	for chaine in dossier:
		ch+="#"+chaine
	return ch	 
def TriNumber(number):
    return number.sort()
def TriNumberinverse():
    return number.sort(reverse=True)
    
def ChaineOrdreCroissante (chaine):
	ch = sorted(chaine)
	return ch
def ChaineOrdreDecroissant(chaine):
	ch = sorted (chaine,reverse=True)
	return ch
	
