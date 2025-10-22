import pyautogui
import keyboard
import random
import time
import threading


#Program statement
running = False

def leafProgram():
    
    """Move the mouse randomly
    

    Returns
    -------
    None.

    """
    
    def move_mouse_randomly():
        
        """Mouvement mouse
        
        Args:
            running (bool): indicate if the program running or not
            screen_width (size): actual width of the screen
            screen_height (size): actual height of the screen 
            x (int): random pixel x of the screen
            y (int): random pixel y of the screen

        Returns
        -------
        None.

        """
        
        global running
        screen_width, screen_height = pyautogui.size()
        while running:
            #Move your mouse in random location
            x = random.randint(0, screen_width - 1)
            y = random.randint(0, screen_height - 1)
            #Move the mouve with time for realism
            pyautogui.moveTo(x, y, duration=0.05)
            #Pause between mouvement
            time.sleep(0.1) 

    def start_moving():
        global running
        if not running:
            running = True
            threading.Thread(target=move_mouse_randomly).start()

    def stop_moving():
        global running
        running = False
    
    keyboard.add_hotkey('ctrl+shift+1', start_moving)
    keyboard.add_hotkey('ctrl+shift+2', stop_moving)
    print("Welcome to the random move mouse for Leaf Blower Revolution")
    print("Click on Ctrl+Shift+1 to start the moving of your mouse")
    print("Click on Ctrl+Shift+2 to stop the moving of your mouse") 
    print("Click on Ctrl+C to quit")
    # Keep the program on listening to stop when crtl+c press
    keyboard.wait('ctrl+c')