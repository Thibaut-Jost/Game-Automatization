import numpy as np
import cv2
import pyautogui
import time

def CookieClickerGoldenCookie_And_AutoClick():
    while True:
        time.sleep(0.5)
        
        screen = pyautogui.screenshot()
        screen.save("C:/python/AutomaticGame/Images/Actual_screen.png")
        
        img = cv2.imread("C:/python/AutomaticGame/Images/Actual_screen.png")
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        blurred = cv2.medianBlur(gray, 25) #cv2.bilateralFilter(gray,10,50,50)
        
        minDist = 20
        param1 = 20 #500
        param2 = 40 #200 #smaller value-> more false circles
        minRadius = 20
        maxRadius = 50 #10+
        
        circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, minDist, param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)      
        
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0,:]:
                r, g, b = screen.getpixel((i[0],i[1]))
                cv2.circle(img, (i[0], i[1]), i[2], (b, g, r), 2)
                if (i[0]<1575):
                    pyautogui.press('+')
                    pyautogui.click(i[0],i[1])
                    pyautogui.moveTo(300,440)
                    pyautogui.press('+')
                    
                    

    #Show result for testing:
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

CookieClickerGoldenCookie_And_AutoClick()