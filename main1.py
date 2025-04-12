import pyautogui
import time

# Coordinates where trees appear, adjust as needed
x, y = 380, 675

# RGB color when area is clear
clear_color = (83, 83, 83)

def color_match(c1, c2, tolerance=5 ):
    return all(abs(a - b) <= tolerance for a, b in zip(c1, c2))

while True:
    current_color = pyautogui.pixel(x, y)
    print(f"Mouse at ({x},{y}), current color: {current_color}")

    if color_match(current_color, clear_color) is True:
        print("Obstacle detected, jumping!")
        pyautogui.press('space')
        # break  # remove this if you want it to keep running

    time.sleep(0.05)
