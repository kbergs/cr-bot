import pyautogui as pag
from button import Button

def look_for(img: str, click=False, conf=0.95, gray=True):
    try:
        button = pag.locateOnScreen(img, confidence=conf, grayscale=gray)
        button = Button(*(value / 2 for value in button))
        if click:
            button.click()
        return button
    except pag.ImageNotFoundException:
        return None
    

# switch a string between two possible values
def swap_str(str, str1, str2):
    if str == str1:
        return str2
    return str1