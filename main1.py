import pyautogui
import time

# Coordinates where trees appear , adjust based on your screen
x, y = 280, 650 # 

# rgb color when area is clear
clear_color = (83, 83, 83)  

while True:
    # get the color of the pixel
    current_color = pyautogui.pixel(x, y)
    # print("looking for the color")
    # if the color changes, jump
    if current_color == clear_color:
        print(f"current color - {current_color}, cler color - {clear_color}")
        # break
        pyautogui.press('space')
        # time.sleep(0.1)  # to prevent multiple jumps for the same tree

    time.sleep(0.05)  # to avoid CPU overload
