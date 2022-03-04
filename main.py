import time
import pyautogui
import vision

myvision = vision.Vision()

def main():
    while True:
        bubble_pos = myvision.isBubbling()
        if bubble_pos:
            pyautogui.click(myvision.monitor["width"]/2, myvision.monitor["height"]/2)
            starting_time = time.time()
            while time.time() - starting_time < 13:
                pos = myvision.hasToClickInMinigame()
                if pos and pos["x"] < myvision.monitor["width"]/2 + 100:
                    pyautogui.click(myvision.monitor["width"]/2, myvision.monitor["height"]/2)
            pyautogui.click(myvision.monitor["width"]/2, myvision.monitor["height"]/2)
    pass

main()