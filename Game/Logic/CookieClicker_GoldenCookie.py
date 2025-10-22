import threading
import time
import cv2
import numpy as np
import pyautogui
from pynput.keyboard import Listener, KeyCode

def CookieClickerGoldenCookie():
    
    class GoldenCookie(threading.Thread):
        def __init__(self, delay):
            super(GoldenCookie, self).__init__()
            self.delay = delay
            self.running = False
            self.program_running = True
        
        def start_search_golden(self):
            self.running = True
   
        def stop_search_golden(self):
            self.running = False
        
        def exit(self):
            self.stop_search_golden()
            self.program_running = False
        
        def run(self):
            while self.program_running:
                while self.running:
                    self.check_and_click()
                    time.sleep(self.delay)
                time.sleep(0.1)
        
        def check_and_click(self):
            # Capture the screen
            screen = pyautogui.screenshot()
            screen_np = np.array(screen)
            img = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)
            blurred = cv2.medianBlur(img, 25)
            
            # Parameters for HoughCircles
            minDist = 20
            param1 = 20
            param2 = 40
            minRadius = 20
            maxRadius = 50
            
            # Detect circles in the image
            circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, minDist, param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)
            
            # If circles are detected
            if circles is not None:
                circles = np.uint16(np.around(circles))
                for i in circles[0, :]:
                    r, g, b = screen.getpixel((i[0], i[1]))
                    cv2.circle(screen_np, (i[0], i[1]), i[2], (b, g, r), 2)
                    if i[0] < 1575: 
                        pyautogui.press('+')
                        time.sleep(0.5)
                        pyautogui.click(i[0], i[1])
                        pyautogui.moveTo(300, 440)
                        time.sleep(0.5)
                        pyautogui.press('+')
    
    # Create and start the thread
    goldenCookie_thread = GoldenCookie(delay=0.5)
    goldenCookie_thread.start()
    
    # Define keys for starting/stopping and exiting the program
    start_stop_key = KeyCode(char='+')
    exit_key = KeyCode(char='-')
    
    def on_press(key):
        if key == start_stop_key:
            if goldenCookie_thread.running:
                goldenCookie_thread.stop_search_golden()
            else:
                goldenCookie_thread.start_search_golden()
        elif key == exit_key:
            goldenCookie_thread.exit()
            listener.stop()
    
    # Start listening for key presses
    with Listener(on_press=on_press) as listener:
        listener.join()