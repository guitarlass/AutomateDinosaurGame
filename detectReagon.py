import pyautogui
import cv2
import numpy as np
from PIL import Image

# Define the region

region = (520, 710, 400 , 400) # (left, top, width, height)

# Take a full screenshot
screenshot = pyautogui.screenshot()
screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

# Draw rectangle on screenshot
x, y, w, h = region
cv2.rectangle(screenshot_cv, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Show image with rectangle
cv2.imshow("Region Preview", screenshot_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()
