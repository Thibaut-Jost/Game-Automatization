try:
    from .Logic.IdleWizard_Auto import IdleWizard_Auto
except ImportError:
    from Logic.IdleWizard_Auto import IdleWizard_Auto
from threading import Thread

"""
Fonction principale pour automatiser le jeu Cookie Clicker.
Elle permet de démarrer différents modes de jeu automatisés pour Cookie Clicker.

Modes disponibles:
    1. Golden Cookie Clicker + AutoClick - Active simultanément l'auto-clicker et le collecteur de cookies dorés

Returns:
    None
"""
class IdleWizard():
    def do_algorithm(self) -> None:
        """
        La fonction principale qui permet de sélectionner et de démarrer le mode de jeu automatisé pour Cookie Clicker.
        """
        print("1 - Full Auto")
        
        numberOfGame = input("Sélectionnez le programme à démarrer : ")
        
        match numberOfGame:
            case "1":
                Thread(target = IdleWizard_Auto).start()

