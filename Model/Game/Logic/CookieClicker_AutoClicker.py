import time
import threading


from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

    
    
def CookieClickerAutoClick():
    
    """AutoClick
    
    Args:
        delay (double): delay between click
        button (mouseButton): button of mouse (left or right)
        start_stop_key (KeyCode): char on the keyboard to start and stop the autoClick
        exit_key (KeyCode): char on the keyboard to stop the program
        

    """
    
    print("Welcome to the autoClick for Cookie Clicker")
    print("Press '+' to start and stop the click")
    print("Press '-' to stop the program")

    delay = 0.15
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
            while self.program_running:
                while self.running:
                    mouse.click(self.button)
                    time.sleep(self.delay)
                time.sleep(0.15)


    mouse = Controller()
    click_thread = ClickMouse(delay, button)
    click_thread.start()
    
    
    
    def on_press(key):
        if key == start_stop_key:
            if click_thread.running:
                click_thread.stop_clicking()
            else:
                click_thread.start_clicking()
                
        elif key == exit_key:
            click_thread.exit()
            listener.stop()

    
    
    with Listener(on_press=on_press) as listener:
        listener.join()
