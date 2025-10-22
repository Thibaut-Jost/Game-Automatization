import time
import threading
import pyautogui

from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

    
    
def IdleWizard_Auto():
    
    """AutoClick
    
    Args:
        delay (double): delay between click
        button (mouseButton): button of mouse (left or right)
        start_stop_key (KeyCode): char on the keyboard to start and stop the autoClick
        exit_key (KeyCode): char on the keyboard to stop the program
        

    """
    
    print("Welcome to the autoSelect for Idle Wizard")
    print("Press '+' to start and stop the click")
    print("Press '-' to stop the program")

    delay = 0.25
    button = Button.left
    start_stop_key = KeyCode(char='+')
    exit_key = KeyCode(char='-')

    class ClickMouse(threading.Thread):
        def __init__(self, delay, button):
           super(ClickMouse, self).__init__()
           self.button = button
           self.delay = delay
           self.running = False
           self.program_running = True

        def start_clicking(self):
            self.running = True

        def stop_clicking(self):
            self.running = False

        def exit(self):
            self.stop_clicking()
            self.program_running = False

        def run(self):
            #Describe each position to move the mouse
            coords = [(1220, 480), (1060, 330), (800, 360),(620, 480)]
            while self.program_running:
                while self.running:
                    counter_delay_checker = 30
                    for i in coords:
                        #Move the mouve
                        pyautogui.moveTo(i[0], i[1])
                        #Click with the mouse
                        mouse.click(self.button)
                        #Pause between mouvement
                        time.sleep(self.delay)

                    """Move the mouse to the center of the screen then appromimatly each 30 seconds,
                           we check if something spawn on the spawner"""
                        
                    #Move the mouve to the center of the screen
                    pyautogui.moveTo(960, 540)
                    #Click with the mouse by looking at the counter
                    for i in range (counter_delay_checker):
                        for j in range(round(1/self.delay)):
                            if not listener.running or self.running == False:
                                #Cut the program if the listener is not running
                                break
                            #no need else
                            mouse.click(self.button)
                            time.sleep(self.delay)
                #Anti crash sleep    
                time.sleep(0.15) 


    mouse = Controller()
    click_thread = ClickMouse(delay, button)
    click_thread.start()
    
    
    def on_press(key):
        try:
            if key.char == '+':
                if click_thread.running:
                    click_thread.stop_clicking()
                else:
                    click_thread.start_clicking()

            elif key.char == '-':
                click_thread.exit()
                return False  # this stops the listener safely

        except AttributeError:
            # Some keys (like shift, ctrl) don't have 'char'
            pass

    
    with Listener(on_press=on_press) as listener:
        listener.join()
