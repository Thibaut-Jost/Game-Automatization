try:
    from .Logic.CookieClicker_AutoClicker import CookieClickerAutoClick
    from .Logic.CookieClicker_GoldenCookie import CookieClickerGoldenCookie
except ImportError:
    from Logic.CookieClicker_AutoClicker import CookieClickerAutoClick
    from Logic.CookieClicker_GoldenCookie import CookieClickerGoldenCookie
from threading import Thread

"""
Fonction principale pour automatiser le jeu Cookie Clicker.
Elle permet de démarrer différents modes de jeu automatisés pour Cookie Clicker.

Modes disponibles:
    1. Golden Cookie Clicker + AutoClick - Active simultanément l'auto-clicker et le collecteur de cookies dorés

Returns:
    None
"""
class CookieClicker():

    def do_algorithm(self) -> None:
        """
        La fonction principale qui permet de sélectionner et de démarrer le mode de jeu automatisé pour Cookie Clicker.
        """
        print("1 - Golden Cookie Clicker + AutoClick")
        print("2 - AutoClick")
        
        numberOfGame = input("Sélectionnez le programme à démarrer : ")
        
        match numberOfGame:
            case "1":
                Thread(target = CookieClickerAutoClick).start()
                Thread(target = CookieClickerGoldenCookie).start()
            case "2":
                Thread(target = CookieClickerAutoClick).start()

