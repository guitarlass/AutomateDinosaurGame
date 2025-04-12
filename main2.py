import pyautogui
import time
import pygetwindow as gw

# Path to your template image
template_image = 'images/clear_area.png'

# Confidence value (0.9 is stricter, 0.8 allows slight variation)
confidence_threshold = 0.9

# Bring the Dino game window to the foreground
try:
    dino_window = gw.getWindowsWithTitle('Chrome')[0]  # Adjust title if necessary
    if dino_window.isMinimized:
        dino_window.restore()  # Restore if minimized
    dino_window.activate()  # Bring the window to the front
    print("Dino window is now active.")
except IndexError:
    print("Dino window not found!")

# Wait for the Dino game to start (ensure the window is open)
print("Waiting for clear area to appear...")

while True:
    try:
        # Try locating the clear area on the screen
        location = pyautogui.locateOnScreen(template_image, confidence=confidence_threshold)
        if location:
            print("Game ready. Starting obstacle detection...")
            break
    except pyautogui.ImageNotFoundException:
        # ImageNotFoundException will be raised if the image isn't found
        print("Clear area not found. Waiting for Dino game to appear...")
        time.sleep(1)  # Wait a second before trying again

# Monitor for change (i.e., when clear area disappears, obstacle is present)
while True:
    try:
        location = pyautogui.locateOnScreen(template_image, confidence=confidence_threshold)
        if location is None:
            print("Obstacle detected! Jumping.")
            pyautogui.keyDown('space')  # Hold space down
            time.sleep(0.1)  # Hold for a brief moment
            pyautogui.keyUp('space')  # Release space
            time.sleep(0.2)  # Delay between jumps to avoid double jumping
        time.sleep(0.05)
    except pyautogui.ImageNotFoundException:
        # If we can't find the image (Dino minimized or not on screen), we just wait
        print("Clear area not found, waiting...")
        time.sleep(1)  # Wait a second before trying again
