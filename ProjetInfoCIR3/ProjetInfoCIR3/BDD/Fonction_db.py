from pymongo import MongoClient
client = MongoClient('mongodb+srv://theomeilliez:Gv1ZmorY2lczag99@projetcir3full.apni4.mongodb.net/?retryWrites=true&w=majority&appName=projetCIR3full')
db = client["projetcir3"]
# utilisateur 
def Add_Utilisateur(Nom,Prenom,Pseudos,Mot_de_passe,Email,Cb,Status,Winstreak,Win,Lose): #qrcode
    return db.utilisateur.insert_One({nom: Nom,prenom : Prenom , pseudos: Pseudos, Mdp: Mot_de_passe, email: Email, cb:Cb,status : Status, winstreak: Winstreak, win : Win , lose : Lose})  

def Sup_Utilisateur(id):
    return db.utilisateur.delete()


# getteur de la table utilisateur 
def Get_Utilisateur(): 
    return db.utilisateurs.find({},{_id : 1 })
def Get_Utilisateur_Nom(id): 
    return db.utilisateurs.find({_id : id} , {nom : 1 , _id : 0 } )
def Get_Utilisateur_Prenom(id): 
    return db.utilisateurs.find({_id : id} , {prenom : 1 , _id : 0 })
def Get_Utilisateur_Pseudos(id): 
    return db.utilisateurs.find({_id : id} , {pseudos : 1 , _id : 0 })
def Get_Utilisateur_Mot_de_passe(id): 
    return db.utilisateurs.find({_id : id} , {Mdp : 1 , _id : 0 })
def Get_Utilisateur_email(id): 
    return db.utilisateurs.find({_id : id} , {email : 1 , _id : 0 })
def Get_Utilisateur_cb(id): 
    return db.utilisateurs.find({_id : id} , {cb : 1 , _id : 0 })
def Get_Utilisateur_Status(id): 
    user = db.utilisateurs.find_one({_id: id}, {status: 1, _id: 0})
    return user['status'] if user else None
def Get_Utilisateur_Winstreak(id): 
    return db.utilisateurs.find({_id : id} , {winstreak : 1 , _id : 0 })
def Get_Utilisateur_Win(id): 
    return db.utilisateurs.find({_id : id} , {win : 1 , _id : 0 })
def Get_Utilisateur_email(id): 
    return db.utilisateurs.find({_id : id} , {lose : 1 , _id : 0 })

# Setteur de la tabble utilisateur

def Set_Utilisateur_Nom(id,Nom): 
    return db.utilisateurs.update_One({_id : id} ,{"$set" :  {nom : Nom} })
def Set_Utilisateur_Prenom(id,Prenom): 
    return db.utilisateurs.update_One({_id : id} ,{"$set" :  {prenom : Prenom} })
def Set_Utilisateur_Pseudos(id,Pseudos): 
    return db.utilisateurs.update_One({_id : id} ,{"$set" :  {Pseudos : Pseudos} })
def Set_Utilisateur_Mot_de_passe(id,Mot_de_passe): 
    return db.utilisateurs.update_One({_id : id} , {"$set" : {Mdp : Mot_de_passe} })
def Set_Utilisateur_email(id,Email): 
    return db.utilisateurs.update_One({_id : id} ,{"$set" :  {email : Email} })
def Set_Utilisateur_cb(id,Cb): 
    return db.utilisateurs.update_One({_id : id}, {"$set" :  {cb : Cb} })
def Set_Utilisateur_Status(id,Status): 
    return db.utilisateurs.update_One({_id : id} ,{"$set" : {status : Status} })
def Set_Utilisateur_Winstreak(id,Winstreak): 
    return db.utilisateurs.update_One({_id : id} ,{"$set" : {winstreak : Winstreak} })
def Set_Utilisateur_Win(id,Win): 
    return db.utilisateurs.update_One({_id : id},{"$set" : {win : Win} })
def Set_Utilisateur_lose(id,Lose): 
    return db.utilisateurs.update_One({_id : id} ,{"$set" :  {lose : Lose} })




# Equipe
def Add_Equipe(Nom,Tab_joueur,Manageur,Jeux):
    return db.Equipe.insertOne({nom: Nom, tab_joueur : Tab_joueur, manageur : Manageur, jeux : Jeux})

def Sup_Equipe(id):
    return 0

#getteur de Equipe
def Get_Equipe(): 
    return db.Equipes.find({},{_id : 1 })
def Get_Equipe_Nom(id): 
    return db.Equipes.find({_id : id} , {nom : 1 , _id : 0 } )
def Get_Equipe_tab_joueur(id): 
    return db.Equipes.find({_id : id} , {tab_joueur : 1 , _id : 0 })
def Get_Equipe_Manageur(id): 
    return db.Equipes.find({_id : id} , {Manageur : 1 , _id : 0 })
def Get_Equipe_jeux(id): 
    return db.Equipes.find({_id : id} , {jeux : 1 , _id : 0 })

#setteur de Equipes
def Set_Equipes_Nom(id,Nom): 
    return db.Equipes.update_One({_id : id} ,{"$set" :  {nom : Nom} })
def Set_Equipes_tab_joueur(id,Tab_joueurs): 
    return db.Equipes.update_One({_id : id} ,{"$set" :  {tab_joueur : Tab_joueurs} })
def Set_Equipes_Manageur(id,Manageur): 
    return db.Equipes.update_One({_id : id} ,{"$set" :  {manageur : Manageur} })

def Set_Equipes_jeux(id,Jeux): 
    return db.Equipes.update_One({_id : id} ,{"$set" :  {jeux : Jeux} })


#table Event ( tournoi)
def Add_Event(Nom,Date_debut,Date_fin,Places_max,Places_libres,Cash_price,Status):
    return db.Event.insert_one({nom : Nom , date_deput: Date_debut, date_fin : Date_fin, places_max : Places_max, places_libres : Places_libres, cash_price : Cash_price, status : Status})

def Sup_Event():
    return 0

# getteur event 

def Get_Event(): 
    return db.event.find({},{_id : 1 })
def Get_Event_nom(id): 
    return db.event.find({_id : id} , {nom : 1 , _id : 0 } )
def Get_Event_date_debut(id): 
    return db.event.find({_id : id} , {date_debut : 1 , _id : 0 })
def Get_Event_date_fin(id): 
    return db.event.find({_id : id} , {date_fin : 1 , _id : 0 })
def Get_Event_places_max(id): 
    return db.event.find({_id : id} , {places_max: 1 , _id : 0 })
def Get_Event_places_libres(id): 
    return db.event.find({_id : id} , {places_libres : 1 , _id : 0 })
def Get_Event_cash_price(id):
    return db.event.find({_id : id} , {cash_prices : 1 , _id : 0 })
def Get_Event_status(id):
    return db.event.find({_id : id} , {status : 1 , _id : 0 })

#setteur event
def Set_Event_nom(id,Nom): 
    return db.event.update_One({_id : id} ,{"$set" :  {nom : Nom} })
def Set_Event_date_debut(id,Date_debut): 
    return db.event.update_One({_id : id} ,{"$set" :  {date_debut : Date_debut} })
def Set_Event_date_fin(id,Date_fin): 
    return db.event.update_One({_id : id} ,{"$set" :  {date_fin : Date_fin} })
def Set_Event_places_max(id,Places_max): 
    return db.event.update_One({_id : id} , {"$set" : {places_max : Places_max} })
def Set_Event_places_min(id,Places_libres): 
    return db.event.update_One({_id : id} ,{"$set" :  {place_libres: Places_libres} })
def Set_Event_cash_price(id,Cash_price): 
    return db.event.update_One({_id : id}, {"$set" :  {cash_price : Cash_price} })
def Set_Event_Status(id,Status): 
    return db.event.update_One({_id : id}, {"$set" :  {status : Status} })

# match
def Add_Match(Equipe1,Equipe2,Date,Score1,Score2,Wineur):
    return db.Event.insertone({equipe1 : Equipe1, equipe2 : Equipe2, date : Date, score1 : Score1, score2 : Score2, wineur : Wineur})

def Sup_Match():
    return 0


#getteur Match
def Get_Match(): 
    return db.match.find({},{_id : 1 })
def Get_Match_equipe1(id): 
    return db.match.find({_id : id} , {equipe1 : 1 , _id : 0 } )
def Get_Match_equipe2(id): 
    return db.match.find({_id : id} , {equipe2 : 1 , _id : 0 })
def Get_Match_date(id): 
    return db.match.find({_id : id} , {date : 1 , _id : 0 })
def Get_Match_score1(id): 
    return db.match.find({_id : id} , {score1: 1 , _id : 0 })
def Get_Match_score2(id): 
    return db.match.find({_id : id} , {score2 : 1 , _id : 0 })
def Get_Match_wineur(id):
    return db.match.find({_id : id} , {wineur : 1 , _id : 0 })

#setteur Match
def Set_Match_equipe1(id,Equipe): 
    return db.match.updateOne({_id : id} ,{"$set" :  {equipe1 : Equipe} })
def Set_Match_equipe2(id,Equipe): 
    return db.match.updateOne({_id : id} ,{"$set" :  {equipe2 : Equipe} })
def Set_Match_date(id,Date): 
    return db.match.updateOne({_id : id} ,{"$set" :  {date : Date} })
def Set_Match_score1(id,Score): 
    return db.match.updateOne({_id : id} , {"$set" : {score1: Score} })
def Set_Match_score2(id,Score): 
    return db.match.updateOne({_id : id} ,{"$set" :  {score2: Score} })
def Set_Match_wineur(id,Wineur): 
    return db.match.updateOne({_id : id}, {"$set" :  {wineur : Wineur} })
