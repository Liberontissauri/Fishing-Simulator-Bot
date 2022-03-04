import pyautogui
import time

def moveLeft(duration):
    pyautogui.keyDown("a")
    time.sleep(duration)
    pyautogui.keyUp("a")
def moveRight(duration):
    pyautogui.keyDown("d")
    time.sleep(duration)
    pyautogui.keyUp("d")
def moveForward(duration):
    pyautogui.keyDown("w")
    time.sleep(duration)
    pyautogui.keyUp("w")
def moveBack(duration):
    pyautogui.keyDown("s")
    time.sleep(duration)
    pyautogui.keyUp("s")


class Instruction:
    def __init__(self, instruction_type, duration) -> None:
        self.type = instruction_type
        self.duration = duration
    def execute(self):
        match self.type:
            case "left":
                pyautogui.keyDown("a")
                time.sleep(self.duration)
                pyautogui.keyUp("a")
                return
            case "right":
                pyautogui.keyDown("d")
                time.sleep(self.duration)
                pyautogui.keyUp("d")
                return
            case "front":
                pyautogui.keyDown("w")
                time.sleep(self.duration)
                pyautogui.keyUp("w")
                return
            case "back":
                pyautogui.keyDown("s")
                time.sleep(self.duration)
                pyautogui.keyUp("s")
                return
            case "jump":
                pyautogui.ke
                time.sleep(self.duration)
                return



class PlayerMovement:
    def __init__(self) -> None:
        pass
    def StartPath(self, path_to_follow):
        for instruction in path_to_follow:
            pass