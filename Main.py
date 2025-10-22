#import
from Model.Game.CookieClicker import CookieClicker
from Model.Game.BeeSwarmSimulator import BeeSwarm
from Model.Game.Logic.LeafMoveMouse import leafProgram
from Model.Game.Logic.AntiAFK import ClickAndMove
from Model.Game.IdleWizard import IdleWizard

"""
Fonction pour sélectionner et démarrer un jeu en fonction du nom donné.

Args:
    Sentence (str): Message d'accueil ou d'invite pour l'utilisateur.

Returns:
    Fonction : Lance le programme du jeu sélectionné.
"""

def SelectionGame(Sentence):
    game_existing = ["CookieClicker", "Leaf", "BeeSwarm", "IdleWizard"]
    print(Sentence)
    for i in range (len(game_existing)):
        print(game_existing[i])
    
    nameOfGame = input("Entrez un nom : ")
    print()
    # switch pour sélectionner quel jeu démarrer
    match nameOfGame:
        case "CookieClicker":
            return CookieClicker()
        case "Leaf":
            return leafProgram()
        case "BeeSwarm":
            return ClickAndMove()
        case "IdleWizard":
            return IdleWizard()
        case _:
            return SelectionGame("Le jeu n'existe pas")    
        

if __name__ == "__main__":
    SelectionGame("Bienvenue dans le jeu de sélection, insérez le nom du jeu (pas d'espace et une majuscule pour chaque mot)")
