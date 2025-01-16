from pymongo import MongoClient
client = MongoClient('mongodb+srv://theomeilliez:Gv1ZmorY2lczag99@projetcir3full.apni4.mongodb.net/?retryWrites=true&w=majority&appName=projetCIR3full')
db = client["projetcir3"]
# utilisateur
def Add_Utilisateur(Nom,Prenom,Pseudo,Mot_de_passe,Email,Status,Winstreak=0,Win=0,Lose=0): #qrcode
    return db.utilisateur.insert_one({"nom": Nom,"prenom" : Prenom , "pseudo": Pseudo, "mdp": Mot_de_passe, "email": Email, "status" : Status, "winstreak": Winstreak, "win" : Win , "lose" : Lose})  

def Sup_Utilisateur(id):
    return db.utilisateur.delete_one({"_id" : id})

# getteur de la table utilisateur 
def Get_Utilisateur(): 
    return list(db.utilisateur.find())
def Get_Utilisateur_Id(pseudo):
    id =  db.utilisateur.find_one({"pseudo": pseudo}, {"_id": 1})
    return id["pseudo"] if id else None
def Get_Utilisateur_Nom(id): 
    Nom =db.utilisateurs.find_one({"_id" : id} , {"nom" : 1 , "_id" : 0 } )
    return  Nom["nom"] if Nom else None
def Get_Utilisateur_Prenom(id): 
    Prenom =db.utilisateurs.find_one({"_id" : id} , {"prenom" : 1 , "_id" : 0 })
    return Prenom["prenom"] if Prenom else None
def Get_Utilisateur_Pseudos(id): 
    Pseudos =db.utilisateurs.find_one({"_id" : id} , {"pseudo": 1 , "_id" : 0 })
    return Pseudos["pseudo"] if Pseudos else None
def Get_Utilisateur_Mot_de_passe(id): 
    mdp =db.utilisateurs.find_one({"_id" : id} , {"mdp" : 1 , "_id" : 0 })
    return mdp["mdp"] if mdp else None
def Get_Utilisateur_email(id): 
    email =db.utilisateurs.find_one({"_id" : id} , {"email" : 1 , "_id" : 0 })
    return email["email"] if email else None
def Get_Utilisateur_cb(id): 
    cb =db.utilisateurs.find_one({"_id" : id} , {"cb" : 1 , "_id" : 0 })
    return cb["cb"] if cb else None
def Get_Utilisateur_Status(id): 
    status = db.utilisateurs.find_one({"_id": id}, {"status": 1, "_id": 0})
    return status["status"] if status else None
def Get_Utilisateur_Winstreak(id): 
    winstreak = db.utilisateurs.find_one({"_id" : id} , {"winstreak" : 1 , "_id" : 0 })
    return winstreak["winstreak"] if winstreak else None
def Get_Utilisateur_Win(id): 
    Win = db.utilisateurs.find_one({"_id" : id} , {"win" : 1 , "_id" : 0 })
    return Win["win"] if Win else None
def Get_Utilisateur_email(id):
    lose = db.utilisateurs.find_one({"_id" : id} , {"lose" : 1 , "_id" : 0 })
    return lose["lose"] if lose else None
def Get_Utilisateur_qrcode(id): 
    qrcode =db.utilisateurs.find_one({"_id" : id} , {"qrcode" : 1 , "_id" : 0 })
    return qrcode["qrcode"] if qrcode else None
# Setteur de la tabble utilisateur

def Set_utilisateur(Nom,Prenom,Pseudo,Mot_de_passe,Email,Status,Winstreak,Win,Lose):
    result = db.utilisateurs.update_one({"_id" : id} ,{"$set" : {"nom": Nom,"prenom" : Prenom , "pseudo": Pseudo, "mdp": Mot_de_passe, "email": Email, "status" : Status, "winstreak": Winstreak, "win" : Win , "lose" : Lose} })
    return result.modified_count > 0
def Set_Utilisateur_Nom(id,Nom): 
    result = db.utilisateurs.update_one({"_id" : id} ,{"$set" :  {"nom" : Nom} })
    return result.modified_count > 0
def Set_Utilisateur_Prenom(id,Prenom): 
    result = db.utilisateurs.update_one({"_id" : id} ,{"$set" :  {"prenom" : Prenom} })
    return result.modified_count > 0
def Set_Utilisateur_Pseudos(id,Pseudo): 
    result = db.utilisateurs.update_one({"_id" : id} ,{"$set" :  {"pseudo": Pseudo} })
    return result.modified_count > 0
def Set_Utilisateur_Mot_de_passe(id,Mot_de_passe): 
    result = db.utilisateurs.update_one({"_id" : id} , {"$set" : {"mdp" : Mot_de_passe} })
    return result.modified_count > 0
def Set_Utilisateur_email(id,Email): 
    result = db.utilisateurs.update_one({"_id" : id} ,{"$set" :  {"email" : Email} })
    return result.modified_count > 0
def Set_Utilisateur_cb(id,Cb): 
    result = db.utilisateurs.update_one({"_id" : id}, {"$set" :  {"cb" : Cb} })
    return result.modified_count > 0
def Set_Utilisateur_Status(id,Status): 
    result = db.utilisateurs.update_one({"_id" : id} ,{"$set" : {"status" : Status} })
    return result.modified_count > 0
def Set_Utilisateur_Winstreak(id,Winstreak): 
    result = db.utilisateurs.update_one({"_id" : id} ,{"$set" : {"winstreak" : Winstreak} })
    return result.modified_count > 0
def Set_Utilisateur_Win(id,Win): 
    result =db.utilisateurs.update_one({"_id" : id},{"$set" : {"win" : Win} })
    return result.modified_count > 0
def Set_Utilisateur_lose(id,Lose): 
    result = db.utilisateurs.update_one({"_id" : id} ,{"$set" :  {"lose" : Lose} })
    return result.modified_count > 0
def Set_Utilisateur_lose(id,Qrcode): 
    result = db.utilisateurs.update_one({"_id" : id} ,{"$set" :  {"qrcode" : Qrcode} })
    return result.modified_count > 0




# Equipe
def Add_Equipe(Nom,Tab_joueur,Manageur,Jeux):
    return db.Equipe.insert_one({"nom": Nom, "tab_joueur" : Tab_joueur, "manageur" : Manageur, "jeux" : Jeux})

def Sup_Equipe(id):
    return db.Equipe.delete_one({"_id" : id})

#getteur de Equipe
def Get_Equipe(): 
    return list(db.utilisateur.find())
def Get_Equipe_Nom(id): 
    Nom = db.Equipes.find_one({"_id" : id} , {"nom" : 1 , "_id" : 0 } )
    return Nom["nom"]if Nom else None
def Get_Equipe_tab_joueur(id): 
    tab_joueur =db.Equipes.find_one({"_id" : id} , {"tab_joueur" : 1 , "_id" : 0 })
    return list(tab_joueur["tab_joueur"]) if tab_joueur else None
def Get_Equipe_Manageur(id): 
    Manageur =db.Equipes.find_one({"_id" : id} , {"Manageur" : 1 , "_id" : 0 })
    return Manageur["Manageur"] if Manageur else None
def Get_Equipe_jeux(id): 
    jeux =db.Equipes.find_one({"_id" : id} , {"jeux" : 1 , "_id" : 0 })
    return jeux["jeux"] if jeux else None

#setteur de Equipes
def Set_Equipes(Nom,Tab_joueur,Manageur,Jeux):
    result = db.Equipes.update_one({"_id" : id} ,{"$set" : {"nom": Nom, "tab_joueur" : Tab_joueur, "manageur" : Manageur, "jeux" : Jeux}})
    return result.modified_count > 0
def Set_Equipes_Nom(id,Nom): 
    result = db.Equipes.update_one({"_id" : id} ,{"$set" :  {"nom" : Nom} })
    return result.modified_count > 0
def Set_Equipes_tab_joueur(id,Tab_joueurs): 
    result = db.Equipes.update_one({"_id" : id} ,{"$set" :  {"tab_joueur" : Tab_joueurs} })
    return result.modified_count > 0
def Set_Equipes_Manageur(id,Manageur): 
    result = db.Equipes.update_one({"_id" : id} ,{"$set" :  {"manageur" : Manageur} })
    return result.modified_count > 0
def Set_Equipes_jeux(id,Jeux): 
    result = db.Equipes.update_one({"_id" : id} ,{"$set" :  {"jeux" : Jeux} })
    return result.modified_count > 0

#table Event ( tournoi)
def Add_Event(Nom,Date_debut,Date_fin,Places_max,Places_libres,Cash_price,Status,prix,tab_inscrit):
    return db.Event.insert_one({"nom" : Nom , "date_deput": Date_debut, "date_fin" : Date_fin, "places_max" : Places_max, "places_libres" : Places_libres, "cash_price" : Cash_price, "status" : Status,"prix":prix, "inscrit":tab_inscrit })

def Sup_Event(id):
    return db.Event.delete_one({"_id" : id})

# getteur event 

def Get_Event():     
    return list(db.event.find())
def Get_Event_nom(id): 
    nom = db.event.find_one({"_id" : id} , {"nom" : 1 , "_id" : 0 } )
    return nom["nom"] if nom else None
def Get_Event_date_debut(id): 
    debut = db.event.find_one({"_id" : id} , {"date_debut" : 1 , "_id" : 0 })
    return debut["date_debut"] if debut else None
def Get_Event_date_fin(id): 
    fin = db.event.find_one({"_id" : id} , {"date_fin" : 1 , "_id" : 0 })
    return fin["date_fin"] if fin else None
def Get_Event_places_max(id): 
    max =db.event.find_one({"_id" : id} , {"places_max": 1 , "_id" : 0 })
    return max["places_max"] if max else None
def Get_Event_places_libres(id): 
    libres =db.event.find_one({"_id" : id} , {"places_libres" : 1 , "_id" : 0 })
    return libres["places_libres"] if libres else None
def Get_Event_cash_price(id):
    cash_price = db.event.find_one({"_id" : id} , {"cash_prices" : 1 , "_id" : 0 })
    return cash_price["cash_prices"] if cash_price else None
def Get_Event_status(id):
    status =db.event.find_one({"_id" : id} , {"status" : 1 , "_id" : 0 })
    return status["status"] if status else None
def Get_Event_prix(id):
    prix =db.event.find_one({"_id" : id} , {"prix" : 1 , "_id" : 0 })
    return prix["prix"] if prix else None
def Get_Event_inscrit(id):
    inscrit =db.event.find_one({"_id" : id} , {"inscrit" : 1 , "_id" : 0 })
    return inscrit["inscrit"] if inscrit else None

#setteur event
def Set_Event(Nom,Date_debut,Date_fin,Places_max,Places_libres,Cash_price,Status,prix,tab_inscrit): 
    result = db.event.update_One({"_id" : id} ,{"$set" :   {"nom" : Nom , "date_deput": Date_debut, "date_fin" : Date_fin, "places_max" : Places_max, "places_libres" : Places_libres, "cash_price" : Cash_price, "status" : Status,"prix":prix, "inscrit":tab_inscrit}})
    return result.modified_count > 0
def Set_Event_nom(id,Nom): 
    result = db.event.update_one({"_id" : id} ,{"$set" :  {"nom" : Nom} })
    return result.modified_count > 0
def Set_Event_date_debut(id,Date_debut): 
    result = db.event.update_one({"_id" : id} ,{"$set" :  {"date_debut" : Date_debut} })
    return result.modified_count > 0
def Set_Event_date_fin(id,Date_fin): 
    result = db.event.update_one({"_id" : id} ,{"$set" :  {"date_fin" : Date_fin} })
    return result.modified_count > 0
def Set_Event_places_max(id,Places_max): 
    result = db.event.update_one({"_id" : id} , {"$set" : {"places_max" : Places_max} })
    return result.modified_count > 0
def Set_Event_places_min(id,Places_libres): 
    result = db.event.update_one({"_id" : id} ,{"$set" :  {"place_libres": Places_libres} })
    return result.modified_count > 0
def Set_Event_cash_price(id,Cash_price): 
    result = db.event.update_one({"_id" : id}, {"$set" :  {"cash_price" : Cash_price} })
    return result.modified_count > 0
def Set_Event_Status(id,Status): 
    result = db.event.update_one({"_id" : id}, {"$set" :  {"status" : Status} })
    return result.modified_count > 0
def Set_Event_prix(id,prix): 
    result = db.event.update_one({"_id" : id}, {"$set" :  {"prix" : prix} })
    return result.modified_count > 0
def Set_Event_inscrit(id,inscrit): 
    result = db.event.update_one({"_id" : id}, {"$set" :  {"inscrit" : inscrit} })
    return result.modified_count > 0

# match
def Add_Match(Equipe1,Equipe2,Date,Score1,Score2,Wineur, Arbitre, _event):
    return db.Event.insert_one({"equipe1" : Equipe1, "equipe2" : Equipe2, "date" : Date, "score1" : Score1, "score2" : Score2, "wineur" : Wineur, "arbitre" : Arbitre,"_event" : _event})


def Sup_Match(id):
    return db.match.delete_one({"_id" : id})


#getteur Match
def Get_Match(): 
    return list(db.match.find())
def Get_Match_equipe1(id): 
    equipe1 =db.match.find_one({"_id" : id} , {"equipe1": 1 , "_id" : 0 } )
    return list(equipe1["equipe1"]) if equipe1 else None
def Get_Match_equipe2(id): 
    equipe2 =db.match.find_one({"_id" : id} , {"equipe2" : 1 , "_id" : 0 })
    return list(equipe2["equipe2"]) if equipe2 else None
def Get_Match_date(id): 
    date = db.match.find_one({"_id" : id} , {"date" : 1 , "_id" : 0 })
    return date["date"] if date else None
def Get_Match_score1(id): 
    score1 =db.match.find_one({"_id" : id} , {"score1": 1 , "_id" : 0 })
    return  score1["score1"] if score1 else None
def Get_Match_score2(id): 
    score2 =db.match.find_one({"_id" : id} , {"score2" : 1 , "_id" : 0 })
    return score2["score2"] if score2 else None
def Get_Match_wineur(id):
    wineur = db.match.find_one({"_id" : id} , {"wineur" : 1 , "_id" : 0 })
    return wineur["wineur"] if wineur else None
def Get_Match_Arbitre(id):
    Arbitre = db.match.find_one({"_id" : id} , {"arbitre" : 1 , "_id" : 0 })
    return Arbitre["arbitre"] if Arbitre else None
def Get_Match_event(id):
    event = db.match.find_one({"_id" : id} , {"_event" : 1 , "_id" : 0 })
    return event["_event"] if event else None

#setteur Match
def Set_Match(id,Equipe1,Equipe2,Date,Score1,Score2,Wineur, Arbitre, _event ):
    result = db.match.update_one({"_id" : id} ,{"$set" :  {"equipe1" : Equipe1, "equipe2" : Equipe2, "date" : Date, "score1" : Score1, "score2" : Score2, "wineur" : Wineur, "arbitre" : Arbitre ,"_event": _event} })
    return result.modified_count > 0
def Set_Match_equipe1(id,Equipe): 
    result = db.match.update_one({"_id" : id} ,{"$set" :  {"equipe1" : Equipe} })
    return result.modified_count > 0
def Set_Match_equipe2(id,Equipe): 
    result = db.match.update_one({"_id" : id} ,{"$set" :  {"equipe2" : Equipe} })
    return result.modified_count > 0
def Set_Match_date(id,Date): 
    result = db.match.update_one({"_id" : id} ,{"$set" :  {"date" : Date} })
    return result.modified_count > 0
def Set_Match_score1(id,Score): 
    result = db.match.update_one({"_id" : id} , {"$set" : {"score1": Score} })
    return result.modified_count > 0
def Set_Match_score2(id,Score): 
    result = db.match.update_one({"_id" : id} ,{"$set" :  {"score2": Score} })
    return result.modified_count > 0
def Set_Match_wineur(id,Wineur): 
    result = db.match.update_one({"_id" : id}, {"$set" :  {"wineur" : Wineur} })
    return result.modified_count > 0
def Set_Match_wineur(id,Arbitre): 
    result = db.match.update_one({"_id" : id}, {"$set" :  {"arbitre" : Arbitre} })
    return result.modified_count > 0
def Set_Match_wineur(id,_event): 
    result =db.match.update_one({"_id" : id}, {"$set" :  {"_event" : _event} })
    return result.modified_count > 0

# Inscrit

def Add_Inscrit(utilisateur, event):
    return db.inscrit.insert_one({"utilisateur" : utilisateur , "event" : event})


def Sup_Inscrit(id):
    return db.inscrit.delete_one({"_id" : id})

#getteur inscrit
def Get_Inscrit(): 
    return list(db.inscrit.find())
def Get_inscrit_utilisateur_one(id): 
    utilisateur =db.inscrit.find_one({"_id" : id} , {"utilisateur": 1 , "_id" : 0 } )
    return utilisateur["utilisateur"] if utilisateur else None
def Get_inscrit_event_one(id): 
    event =db.inscrit.find_one({"_id" : id} , {"event" : 1 , "_id" : 0 })
    return event["event"] if event else None
def Get_inscrit_utilisateur_event(event): 
    utilisateur_all =db.inscrit.find({"event" : event} , {"event": 1 , "_id" : 0 } )
    return list(utilisateur_all["event"]) if utilisateur_all else None
def Get_inscrit_event_utilisateur(utilisateur): 
    event_all =db.inscrit.find({"utilisateur" : utilisateur} , {"event" : 1 , "_id" : 0 })
    return event_all["event"] if event_all else None


#setteur de inscrit
def Set_Inscrit(utilisateur, event ):
    result = db.inscrit.update_one({"_id" : id} ,{"$set" :  {"utilisateur" : utilisateur , "event" : event} })
    return result.modified_count > 0
def Set_inscrit_utilisateur(id,utilisateur): 
    result = db.inscrit.update_one({"_id" : id} ,{"$set" :  {"utilisateur" : utilisateur} })
    return result.modified_count > 0
def Set_inscrit_equipe2(id,event): 
    result = db.inscrit.update_one({"_id" : id} ,{"$set" :  {"event" : event} })
    return result.modified_count > 0