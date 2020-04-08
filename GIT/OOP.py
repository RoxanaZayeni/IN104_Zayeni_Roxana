class Vehicule:
    def __init__(self,nom,couleur,roues):
        self.proprietaire= nom
        self.couleur=couleur
        self.roues=roues



class Voiture (Vehicule):

    def __init__(self,nom,couleur,roues,marque,modele):
        super().__init__(nom,couleur,roues)
        self.marque = marque
        self.modele=modele
        
    def peinture(self, nvl_couleur):
        self.couleur=nvl_couleur
        print("Ma voiture est maintenant", self.couleur)
    
    def afficher(self):
        print (self.proprietaire, "possede une",self.marque, self.modele )
        

class Avion (Vehicule):

    def __init__(self,nom,couleur,roues,depart,arrivee):
        super().__init__(nom,couleur,roues)
        self.depart = depart
        self.arrivee=arrivee
    
    def aller_simple(self):
        self.depart=self.arrivee
        print("depart:", self.depart, "arrivee:", self.arrivee)
        
    def retour(self):
        self.arrivee, self.depart=self.depart, self.arrivee
        print("depart:", self.depart, "arrivee:", self.arrivee)
    

v=Voiture("Roxana","rouge",4,"Tesla","modele 3")
v.peinture("noire")
v.afficher()
a=Avion("AirFrance","blanc",8,"France","Italie")
a.retour()
a.aller_simple()