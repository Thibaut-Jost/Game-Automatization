from Game.Logic.IdleWizard_Auto import IdleWizard_Auto
from threading import Thread

"""
Fonction principale pour automatiser le jeu Cookie Clicker.
Elle permet de démarrer différents modes de jeu automatisés pour Cookie Clicker.

Modes disponibles:
    1. Golden Cookie Clicker + AutoClick - Active simultanément l'auto-clicker et le collecteur de cookies dorés

Returns:
    None
"""
def IdleWizard():
    print("1 - Full Auto")
    
    numberOfGame = input("Sélectionnez le programme à démarrer : ")
    
    match numberOfGame:
        case "1":
            Thread(target = IdleWizard_Auto).start()

