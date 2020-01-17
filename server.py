# coding: utf-8 
import socket
import threading
import os
import oursql

class ClientThread(threading.Thread):
    def __init__(self, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))
    def run(self):
        base="."    
        print("Connexion de %s %s" % (self.ip, self.port, ))
        r = self.clientsocket.recv(100000)
        info_connect = r.decode()
        info_connect = oursql.space(info_connect)     
        requete = oursql.cut(info_connect,"#")   
        if requete[0].upper() == "OURSQL":
            if requete[1].upper() == "-U":
                user = requete[2]
                if requete[3].upper() == "-P": 
                    password = requete[4]
                    auth = oursql.auth(user,password)
                    self.clientsocket.send(auth.encode())
        b=auth
        if b == "1":
            while True:
                r = self.clientsocket.recv(100000)
                chaine = r.decode()
                chaine = oursql.space(chaine)
                requete = oursql.cut(chaine,"#")
                if requete[0].upper() == "CREATE":
                    create=oursql.create(requete[2],requete[1],base)
                    self.clientsocket.send(create.encode())    
                if requete[0].upper() == "DROP":
                    drop = oursql.drop(requete[1],requete[3],base)
                    self.clientsocket.send(drop.encode())    
                if requete[0].upper() == "ALTER":
                    """requete="ALTER TABLE Etudiants DROP age"
                    requeteSub=requete.split()
                    if(requeteSub[0].upper()=="ALTER"):
                        res =verif_syntax_Alter(requeteSub)
                        if(res[0]==True):
                            res1=verif_Existence_Alter(res[1], res[2], "ecole.json")
                            if (res1[0]==True):
                                print(traitement_Alter(res[1], res[2], "ecole.json"))
                            else:
                                print(res1[1])
                        else:
                            print(res[1])"""
                    pass
                    
                if requete[0].upper() == "INSERT":
                    if base != ".":
                        insert=oursql.insert(requete[2],requete[3],base)
                        self.clientsocket.send(insert.encode()) 
                    else:
                        insert = "veuillez selectionner une base"
                        self.clientsocket.send(insert.encode())
                if requete[0].upper() == "UPDATE":
                    print ("Entrer l'option")
                    option= input()
                    print ("Entrer l'attribut pour la mise a jour")
                    attribut = input()
                    update = oursql.update(requete[2],requete[1],option,attribut)
                    pass
                if requete[0].upper() == "DELETE":
                    print ("Entrer l'option")
                    option= input()
                    delete = oursql.delete(requete[2],requete[1],option)
                if requete[0].upper() == "SELECT":
                    if base != ".":
                        select = oursql.select(requete[1],requete[3],base)
                        self.clientsocket.send(select.encode()) 
                    else:
                        select = "veuiller selectionner une base"
                        self.clientsocket.send(select.encode()) 
                if requete[0].upper() == "ADDUSER":
                    pass
                if requete[0].upper() == "DELUSER":
                    pass
                if requete[0].upper() == "QUIT":
                    pass
                if requete[0].upper() == "START":
                    pass
                if requete[0].upper() == "COMMIT":
                    pass
                if requete[0].upper() == "ROLLBACK":
                    pass
                if requete[0].upper() == "USE":
                    base = requete[1]
                    use = base+" now selected";
                    self.clientsocket.send(use.encode()) 
                if requete[0].upper() == "DESCRIBE":
                    if base != ".":
                        desc = oursql.describe(requete[1],base)
                        self.clientsocket.send(desc.encode()) 
                    else:
                        select = "veuiller selectionner une base"
                        self.clientsocket.send(select.encode()) 
                if requete[0].upper() == "SHOW":

                    if requete[1].upper() == "DATABASES":
                        pass
                    if requete[1].upper() == "TABLES":
                        if base != ".":
                            show = oursql.showtable(base)
                            self.clientsocket.send(show.encode()) 
                        else:
                            show = "veuiller selectionner une base"
                            self.clientsocket.send(show.encode()) 
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("",8888))

while True:
    tcpsock.listen(10)
    print( "En écoute...")
    (clientsocket, (ip, port)) = tcpsock.accept()
    newthread = ClientThread(ip, port, clientsocket)
    newthread.start()
