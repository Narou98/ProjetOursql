# coding: utf-8
import socket
import oursql

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("", 8888))
chaine = input(">>") # utilisez raw_input() pour les anciennes versions python
s.send(chaine.encode())
auth = s.recv(100000)
if auth.decode() == "1":
	while True:
		requete = input("oursql>>")
		s.send(requete.encode())
		ch = s.recv(100000)
		r = requete.split(" ")
		if r[0].upper() == "SELECT" :
			ch1 = ch.decode() 
			
			if ch1 == "veuiller selectionner une base":
				print(ch1)
			else: 
				attr = ch1.split("|")[0]
				donnee = ch1.split("|")[1]
				attr1 = attr.split("#")
				donnee1 = donnee.split("#")
				attr2 = []
				donnee2 =[]
				for x in range(1,len(attr1)):
					attr2.append(attr1[x])
				for x in range(1,len(donnee1)):
					donnee2.append(donnee1[x])
				
				mod = 0
				for x in range(0,len(attr2)):
					print("{:^15s}".format("_______________"),end='')
				print('')
				for x in range(0,len(attr2)):
					print("{:^15s}".format(attr2[x]),end='')
					if x!= len(attr2) -1:
						print("|",end='')
				print('')
				for x in range(0,len(attr2)):
					print("{:^15s}".format("_______________"),end='')
				print('')
				while(mod != len(donnee2)):
					for x in range(mod,mod+len(attr2)):
						print("{:^15s}".format(donnee2[x]),end='')
						if x != mod+len(attr2) -1:
							print("|",end='')
					mod+=len(attr2)
					print('')
				for x in range(0,len(attr2)):
					print("{:^15s}".format("_______________"),end='')
				print('')	
		if r[0].upper() == "DESCRIBE":
			ch1 = ch.decode()
			if ch1 == "veuiller selectionner une base":
				print(ch1)
			else:
				#print(ch1)
				attr2 = ch1.split("#")
				for x in range(1,len(attr2)):
					print("{:^15s}".format("_______________"),end='')
				print('')
				for x in range(1,len(attr2)):
					print("{:^15s}".format(attr2[x]),end='')
					if x!= len(attr2) -1:
						print("|",end='')
				print('')
				for x in range(1,len(attr2)):
					print("{:^15s}".format("_______________"),end='')
				print('')		
		if r[0].upper() == "SHOW":
			ch1 = ch.decode()
			print(ch1)
			if ch1 == "veuiller selectionner une base":
				print(ch1)
			else:
				dossier = ch1.split("#")
				print("{:^15s}".format("________________"),end='')
				print("")

				print("{:^15s}".format("Tables"),end='')
				print("|")
				print("{:^15s}".format("________________"),end='')
				print('')
				for x in range(1,len(dossier)):
					print("{:^15s}|".format(dossier[x]))	
		else:
			print(ch.decode())