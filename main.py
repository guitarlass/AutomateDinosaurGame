import pyautogui, os, time

folder_path = 'images/trees'


region = None
while True:
    print("Searching for trees...")

    try:
        # file_path2 = os.path.join(folder_path, 'tree7.PNG')
        # region2 = pyautogui.locateOnScreen(file_path2, confidence=0.8, region=(186, 530, 400, 400))
        #
        # if region2:
        #     print(f"tree7.PNG is near {region2.left}, pressing space")
        #     pyautogui.press('space')

        file_path1 = os.path.join(folder_path, 'tree4.PNG')
        region1 = pyautogui.locateOnScreen(file_path1, confidence=0.8, region=(186, 530, 400, 400))

        if region1:
            print(f"tree4.PNG is near {region1.left}, pressing space")
            pyautogui.press('space')

    except Exception as e:
        print(f"Error: {e}")


# print(f"Image location: {region}")