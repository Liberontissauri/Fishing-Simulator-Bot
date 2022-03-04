import cv2
import pyautogui as pyautogui
from python_imagesearch.imagesearch import imagesearch

class Vision:
    def __init__(self) -> None:
        self.template_images_paths = {
            "full_backpack": "./backpack_full.png",
            "bubbling": "./bubble_template.png",
            "minigame_click": "./minigame_click2.png"
        }
        self.monitor = {'top': 0, 'left': 0, 'width': 2560, 'height': 1080}
    def isBackpackFull(self): 
        try:
            x, y = pyautogui.locateCenterOnScreen(self.template_images_paths["full_backpack"])
            return {"x": x, "y": y}
        except:
            return None
    def isBubbling(self):
        pos = imagesearch(self.template_images_paths["bubbling"])
        if pos == [-1, -1]:
            return None
        return pos
    def hasToClickInMinigame(self):
        try:
            x, y = pyautogui.locateCenterOnScreen(self.template_images_paths["minigame_click"], confidence=0.8, region=(
                0, 0, 1500, 1080
            ))
            return {"x": x, "y": y}
        except:
            return None
        pos = imagesearch(self.template_images_paths["minigame_click"])
        if pos == [-1, -1]:
            return None
        return pos