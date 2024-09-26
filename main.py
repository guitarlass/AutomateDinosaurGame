import pyautogui, os, time

tree_path = 'images/trees/x'
bird_path = 'images/trees/y'

region = (215,500, 200, 180)
bird_region = (215, 600, 200, 120)


def detectAndJump(region, folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.PNG'):
            file_path1 = os.path.join(folder_path, filename)
            region1 = pyautogui.locateOnScreen(file_path1, confidence=0.3) # ,, region=region
            # region=(186, 530, 400, 400)
            if region1:
                print(f"{filename} is near {region1.left}, {region1.top}, {region1.width}, {region1.height}, pressing space")
                return True
            # if detectx:
            #     print(f"{file_path} is near {detectx.left}, pressing space")
                  # Tree found, no need to check further
    return False  # No tree found


while True:
    print("Searching for trees...")

    try:
        # if detectAndJump(region, tree_path):
        #     pyautogui.press('space')
        if detectAndJump(bird_region, bird_path):
            pass
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
