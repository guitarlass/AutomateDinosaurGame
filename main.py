import pyautogui, os, time

tree_path = 'images/trees/x'
bird_path = 'images/trees/y'


region = (420, 710, 400 , 350)
bird_region = (215, 600, 200, 120)


def detectAndJump(region, folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.PNG'):
            file_path1 = os.path.join(folder_path, filename)
            # Attempt to locate the image in the given region
            region_location = pyautogui.locateOnScreen(file_path1, region=region, confidence=0.3 )

            if region_location:
                print(f"{filename} found at {region_location}, pressing space")
                return True  # Tree detected
        return False  # No trees detected

# clear_path = 'images/clear_area.png'
# def detectAndJump2(region, filename):
#     region1 = pyautogui.locateOnScreen(filename, confidence=0.9) # ,, region=region
#     # region=(186, 530, 400, 400)
#     if not region1:
#         print(f"obstacle detected pressing space")
#         return True
#     else:
#         print(f"NO obstacle")
#         return False  # No tree found

# while True:
#     print("Searching for trees...")
#
#     try:
#         if detectAndJump2(region, clear_path):
#             pyautogui.press('space')
#         # if detectAndJump(bird_region, bird_path):
#         #     pass
#             # pyautogui.press('down')
#     except Exception as e:
#         print(f"Error: {e}")


while True:
    print("Searching for trees...")

    try:
        if detectAndJump(region, tree_path):
            pyautogui.press('space')
        # if detectAndJump(bird_region, bird_path):
        #     pass
            # pyautogui.press('down')
    except Exception as e:
        print(f"Error: {e}")

    # Add a small delay between searches to prevent spamming and allow images to move
    # time.sleep(0.2)
# while True:
#     print("Searching for trees...")
#
#     try:
#         # file_path2 = os.path.join(folder_path, 'tree7.PNG')
#         # region2 = pyautogui.locateOnScreen(file_path2, confidence=0.8, region=(215, 490, 200, 200))
#         # #
#         # if region2:
#         #     print(f"tree7.PNG is near {region2.left}, pressing space")
#         #     pyautogui.press('space')
#
#         file_path1 = os.path.join(folder_path, 'tree7.PNG')
#         region1 = pyautogui.locateOnScreen(file_path1, confidence=0.5, region=(215, 490, 200, 200)) # ,
#         # region=(186, 530, 400, 400)
#         if region1:
#             print(f"tree7.PNG is near {region1.left}, {region1.top}, {region1.width}, {region1.height}, pressing space")
#
#             pyautogui.press('space')
#
#     except Exception as e:
#         print(f"Error: {e}")


# print(f"Image location: {region}")
