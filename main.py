import pyautogui, os, time

folder_path = 'images/trees'


region = None
while True:
    print("Searching for trees...")

    try:
        # Load the images from the folder
        file_path1 = os.path.join(folder_path, 'tree7.PNG')
        file_path2 = os.path.join(folder_path, 'tree4.PNG')

        # Locate the images on screen with confidence
        region1 = pyautogui.locateOnScreen(file_path1, confidence=0.5)
        region2 = pyautogui.locateOnScreen(file_path2, confidence=0.5)

        # Check if tree7.PNG is found and if its left is near 500
        if region1 and region1.left <= 500:
            print(f"tree7.PNG found near left {region1.left}, pressing space")
            pyautogui.press('space')

        # Check if tree4.PNG is found and if its left is near 500
        if region2 and region2.left <= 500:
            print(f"tree4.PNG found near left {region2.left}, pressing space")
            pyautogui.press('space')

    except Exception as e:
        print(f"Error: {e}")


# print(f"Image location: {region}")