class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'





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
        self.inv_condi = {}
        self.choix_inv = {}
        self.inventaire = {}
    
    def add_to_inv(self, choix, objet):
        self.choix_inv[choix] = objet
    
    def add_condi(self, choix, objet):
        self.inv_condi[choix] = objet
        

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
                
                print(f"\nchoix du mec: '{choix_utilisateur}'\ninv_condi: {self.inv_condi}")
                if choix_utilisateur in self.inv_condi:
                    if self.inv_condi[choix_utilisateur] in self.inventaire:
                        print("success")
                        chapitre_actuel = chapitre_actuel.suivant(choix_utilisateur)
                    else:
                        print("Vous ne pouvez pas !")
                        chapitre_actuel.suivant(chapitre_actuel)
                else:
                    chapitre_actuel = chapitre_actuel.suivant(choix_utilisateur)
            except:
                print('problème dans la condition')
            
            
            
            try:
                
                self.inventaire[self.choix_inv[choix_utilisateur]] = 1
            except:
                print("Rien à ajouter à l'inventaire")
            
            
            
            
            
            
            
            
            

intro = Chapitre("Tu te réveilles")
tab = Chapitre("tu ramasses la tablette")
ouvrir_porte = Chapitre("Tu ouvres la portes")
intro.ajouter_choix("ramasser tablette", tab)
tab.ajouter_choix("ouvrir porte", ouvrir_porte)


# Création du livre et lancement
livre = Livre(intro)
livre.add_to_inv("ramasser tablette", "tablette Sheika")
livre.add_condi("ouvrir porte", "tablette Sheika")
livre.lancer()














"""intro = Chapitre("Tu te réveilles après 100 ans dans un monde dévasté. Que voulez-vous faire ?")

partir_a_l_aventure = Chapitre("Tu ramasses ta tablette Sheikah et sors du sanctuaire de la rennaissance. Par où vas-tu commencer ton exploration ?")
se_rendormir = Chapitre("Tu te rendors et abandonne la princesse. Fin !")

debut_explorer_sous_sols = Chapitre("Vous entrez dans le sous sols du chateau d'Hyrule sans aucune armure. Un monstre vous attaque et vous mange Fin!")
vers_plateau_hyrule = Chapitre("Vous vous retrouvez sur le plateau d'Hyrule.")

explorer_la_foret = Chapitre("Vous vous retrouvez dans l'immense forêt d'hyrule.")
explorer_la_ruine = Chapitre("Vous vous retrouvez dans la ruine. Fin !")

champignon = Chapitre("Lorsque vous avez ramassé le champignon, un monstre vous a attaqué.")
baton = Chapitre("Des monstres vous attaquent mais le baton a fait peur aux monstres, ils fuient puis tu ramasses un champignon. Maintenant vous allez dans le chateau d'Hyrule")

baton1 = Chapitre("Lorsque vous avez ramassé le baton, un monstre vous a attaqué et vous être mort.")
se_battre = Chapitre("Bien joué !! Vous avez réussi à battre ce monstre !! Il faut partir car d'autres arrivent !! Vous entrez alors dans le chateau d'Hyrule")





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
"""

