import time
import threading
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Listener, KeyCode, Controller as KeyboardController


def ClickAndMove():
    """
    AutoClick

    Args:
        delay (double): delay between click
        button (mouseButton): button of mouse (left or right)
        start_stop_key (KeyCode): char on the keyboard to start and stop the autoClick
        exit_key (KeyCode): char on the keyboard to stop the program
    """

    print("Welcome to the antiAFK")
    print("Press '+' to start and stop the click")
    print("Press '-' to stop the program")

    delay = 2.0
    button = Button.left
    start_stop_key = KeyCode(char='+')
    exit_key = KeyCode(char='-')
    key_z = KeyCode(char='z')
    key_s = KeyCode(char='s')

    class AntiAFK(threading.Thread):
        def __init__(self, delay, button, key_z, key_s):
            super(AntiAFK, self).__init__()
            self.button = button
            self.key_z = key_z
            self.key_s = key_s
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
                    mouse.press(self.button)
                    time.sleep(0.05)
                    keyboard.release(self.key_z)
                    time.sleep(0.2)
                    keyboard.press(self.key_z)
                    time.sleep(0.05)
                    keyboard.release(self.key_z)
                    time.sleep(0.2)
                    keyboard.press(self.key_s)
                    time.sleep(0.05)
                    keyboard.release(self.key_s)
                    time.sleep(0.2)
                    time.sleep(self.delay)
                time.sleep(0.1)

    mouse = MouseController()
    keyboard = KeyboardController()
    click_thread = AntiAFK(delay, button, key_z, key_s)
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
