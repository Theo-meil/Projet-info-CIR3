from pymongo import MongoClient

def test_mongo_connection():
    # URI de connexion MongoDB Atlas
    uri = "mongodb+srv://theomeilliez:Gv1ZmorY2lczag99@projetcir3full.apni4.mongodb.net/?retryWrites=true&w=majority&appName=projetCIR3full"
    # Initialiser le client MongoDB
    client = MongoClient(uri)

    try:
        # Envoyer une commande ping pour vérifier la connexion
        client.admin.command('ping')
        print("Connexion réussie à MongoDB Atlas avec pymongo 3.11 !")
    except Exception as e:
        print("Erreur lors de la connexion à MongoDB Atlas :")
        print(e)

if __name__ == "__main__":
    test_mongo_connection()
