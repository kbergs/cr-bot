import pyautogui as pag
from screen import Screen
from button import Button
import time

def lose_war(screen: Screen):
    # Switch to clan tab
    

    # Duel if possible
    try:
        duel = pag.locateOnScreen('res/war/duel.png', confidence=0.95)
        duel = Button(*(value / 2 for value in duel))
        pag.click(duel.random_point())
        try:
            battle = pag.locateOnScreen('res/war/battle.png', confidence=0.98, grayscale=False)
            battle = Button(*(value / 2 for value in battle))
            pag.click(battle.random_point())
            print('duel started')

            # Wait for duel to end
            while True:
                try:
                    ok = pag.locateOnScreen('res/navigate/ok.png', confidence=0.95)
                    ok = Button(*(value / 2 for value in ok))
                    pag.click(ok.random_point())
                    time.sleep(2)
                    break
                except pag.ImageNotFoundException:
                    print('Waiting for battle to end...')
            
            # Play 1v1s
            try:
                battle = pag.locateOnScreen('res/war/1v1.png', confidence=0.95)
                battle = Button(*(value / 2 for value in battle))
                pag.click(battle.random_point())
                battle = pag.locateOnScreen('res/war/battle.png', confidence=0.98, grayscale=False)
                battle = Button(*(value / 2 for value in battle))
                pag.click(battle.random_point())
                print('1v1 started')
            except pag.ImageNotFoundException:
                pass
        except:
            print('button not found')
            pass

    except pag.ImageNotFoundException:
        pass