import pyautogui as pag
import time
from button import Button
from screen import Screen
import logging
from utils import look_for

# TODO: implement exempt list
def donate(screen: Screen, exempt=None):
    # Donate to all open requests possible except those marked
    if not screen.current == 'chat' and screen.validate():
        if not screen.clan(chat=True):
            logging.warning('Failed to switch to chat screen.')
    
    if screen.current == 'chat':
        donated = False
        time.sleep(0.5)
        while look_for('res/donate.png', click=True, gray=False):
            donated = True
            time.sleep(0.2)
        if donated:
            logging.info('Donated successfully.')
        else:
            logging.info("Didn't donate.")
        # TODO: Implement scrolling and rare vs. common vs. epic distinction

def request(screen: Screen, card=None):
    # TODO implement
    pass