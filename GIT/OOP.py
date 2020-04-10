class Vehicule:
    def __init__(self,nom,couleur,roues):
        self.proprietaire= nom
        self.couleur=couleur
        self.roues=roues



class Voiture (Vehicule):

    def __init__(self,nom,couleur,roues,marque,modele,borneKM):
        super().__init__(nom,couleur,roues)
        self.marque = marque
        self.modele=modele
        self.borneKM=borneKM
        
    def peinture(self, nvl_couleur):
        self.couleur=nvl_couleur
        print("Ma voiture est maintenant", self.couleur)
    
    def afficher(self):
        print (self.proprietaire, "possede une",self.marque, self.modele )
        
    def avance(self):
        self.borneKM += 1
        print ("nouvelle borne kilometrique: ",self.borneKM)
        

class Avion (Vehicule):

    def __init__(self,nom,couleur,roues,depart,arrivee,latitude,longitude):
        super().__init__(nom,couleur,roues)
        self.depart = depart
        self.arrivee=arrivee
        self.latitude = latitude
        self.longitude = longitude
    
    def aller_simple(self):
        self.depart=self.arrivee
        print("depart:", self.depart, "arrivee:", self.arrivee)
        
    def retour(self):
        self.arrivee, self.depart=self.depart, self.arrivee
        print("depart:", self.depart, "arrivee:", self.arrivee)
        
    def avance(self):
        self.latitude -= 1
        self.longitude +=5
        print("latitude: ", self.latitude, " longitude: ", self.longitude)
    

v=Voiture("Roxana","rouge",4,"Tesla","modele 3")
v.peinture("noire")
v.afficher()
v.avance()
a=Avion("AirFrance","blanc",8,"France","Italie")
a.retour()
a.avance()
a.aller_simple()
