import pyautogui, os, time

folder_path = 'images/trees'


region = None
while True:
    print("Searching for trees...")
    for filename in os.listdir(folder_path):
        try:
            file_path = os.path.join(folder_path, filename)
            region = pyautogui.locateOnScreen(file_path, confidence=0.9)  # Lower the confidence
            if region:
                print(f"Image found!: {filename} was located in {region}")
                pyautogui.press('space')
        except pyautogui.ImageNotFoundException:
            print("Image not found, retrying...")
    # time.sleep(2)

# print(f"Image location: {region}")