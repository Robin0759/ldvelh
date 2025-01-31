class Chapitre:
    def __init__(self, texte):
        self.texte = texte
        self.choix = {}  # Dictionnaire pour les choix possibles

    def ajouter_choix(self, choix, chapitre_suivant):
        self.choix[choix] = chapitre_suivant


    def suivant(self, choix):
        return self.choix.get(choix, None)
    
    
class Livre:
    def __init__(self, chapitre_depart):
        self.chapitre_depart = chapitre_depart
        self.choix_inv = {}
        self.inventaire = {}
    
    def add_to_inv(self, choix, objet):
        self.choix_inv[choix] = objet
        

    def lancer(self):
        chapitre_actuel = self.chapitre_depart
        while chapitre_actuel:
            print(chapitre_actuel.texte)
            if not chapitre_actuel.choix:
                print("Fin de l'histoire.")
                print(self.inventaire)
                break
            
            print("\nChoix disponibles :")
            for i, choix in enumerate(chapitre_actuel.choix.keys(), 1):
                print(f"{i}. {choix}")
            choix_utilisateur = input("Votre choix : ")
            try:
                print(f"inventaire: {self.choix_inv[choix_utilisateur]}")
                self.inventaire[self.choix_inv[choix_utilisateur]] = 1
            except:
                pass
            
            chapitre_actuel = chapitre_actuel.suivant(choix_utilisateur)
            
            
            





intro = Chapitre("\nTu te réveilles après 100 ans dans un monde dévasté. Que voulez-vous faire ?")

partir_a_l_aventure = Chapitre("\nTu ramasses ta tablette Sheikah et sors du sanctuaire de la rennaissance. Par où vas-tu commencer ton exploration ?")
se_rendormir = Chapitre("\nTu te rendors et abandonne la princesse. Fin !")

debut_explorer_sous_sols = Chapitre("\nVous entrez dans le sous sols du chateau d'Hyrule sans aucune armure. Un monstre vous attaque et vous mange Fin!")
vers_plateau_hyrule = Chapitre("\nVous vous retrouvez sur le plateau d'Hyrule.")

explorer_la_foret = Chapitre("\nVous vous retrouvez dans l'immense forêt d'hyrule.")
explorer_la_ruine = Chapitre("\nVous vous retrouvez dans la ruine. Fin !")

champignon = Chapitre("\nLorsque vous avez ramassé le champignon, un monstre vous a attaqué.")
baton = Chapitre("\nDes monstres vous attaquent mais le baton a fait peur aux monstres, ils fuient puis tu ramasses un champignon. Maintenant vous allez dans le chateau d'Hyrule")

baton1 = Chapitre("\nLorsque vous avez ramassé le baton, un monstre vous a attaqué et vous être mort.\n\nVous entrez alors dans le chateau d'Hyrule.")
se_battre = Chapitre("\nBien joué !! Vous avez réussi à battre ce monstre !! Il faut partir car d'autres arrivent !! \n\nVous entrez alors dans le chateau d'Hyrule. ")

fuir = Chapitre("\nEn ouvrant le coffre, un monstre s'en prend à vous. Fin !")
fuir = Chapitre("\nVous avez décidé de fuir. ")

ouvrir_coffre = Chapitre("\nEn ouvrant le coffre, un monstre s'en prend à vous. Fin !")
ouvrir_coffre = Chapitre("\nVous avez décidé de fuir. ")




# Ajout des choix
intro.ajouter_choix("Partir à l'aventure", partir_a_l_aventure)
intro.ajouter_choix("Se rendormir", se_rendormir)


partir_a_l_aventure.ajouter_choix("Explorer les sous-sols du chateau d'Hyrule", debut_explorer_sous_sols)
partir_a_l_aventure.ajouter_choix("Aller vers le plateau d'Hyrule", vers_plateau_hyrule)

vers_plateau_hyrule.ajouter_choix("Explorer la foret", explorer_la_foret)
vers_plateau_hyrule.ajouter_choix("Explorer la ruine", explorer_la_ruine)

explorer_la_foret.ajouter_choix("Ramasser un champignon", champignon)
explorer_la_foret.ajouter_choix("Ramasser un baton", baton)

champignon.ajouter_choix("Ramasser un baton pour se défendre", baton1)
champignon.ajouter_choix("Se battre à main nue", se_battre)

se_battre.ajouter_choix("Ouvrir le coffre", ouvrir_coffre)
se_battre.ajouter_choix("Fuir avant qu'il ne soit trop tard", fuir)

baton1.ajouter_choix("Ouvrir le coffre", ouvrir_coffre)
baton1.ajouter_choix("Fuir avant qu'il ne soit trop tard", fuir)

fuir.ajouter_choix("Ouvrir le coffre", ouvrir_coffre)
fuir.ajouter_choix("Fuir avant qu'il ne soit trop tard", fuir)



# Création du livre et lancement
livre = Livre(intro)
livre.add_to_inv("Ramasser un champignon", "champignon")
livre.lancer()