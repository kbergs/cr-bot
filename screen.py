import pyautogui as pag
import time
from button import Button
from utils import look_for

# Primary class for selecting certain screens in app
class Screen:
    def __init__(self):
        # Initialize the current screen as unknown
        self.current = None
    
    def __repr__(self):
        # String representation of the button
        return f"Screen(current={self.current})"
    
    def validate(self):
        return True
    
    def home(self):
        # Navigate to home screen
        if self.current == 'home' and self.validate():
            return True
        while True:
            # Arbitrarily exit out of any nested screens
            if look_for('res/navigate/x.png', click=True):
                continue
            if look_for('res/navigate/ok.png', click=True):
                continue
            if look_for('res/navigate/close.png', click=True):
                continue
            
            # Try to find tabs and exit loop once found
            if look_for('res/navigate/home.png', click=True, gray=False):
                break
            if look_for('res/navigate/home*.png'):
                break
            if look_for('res/navigate/gamemode.png', click=True):
                break

            return False

        # Set screen variable
        self.current = 'home'
    
    def shop(self):
        # Navigate to shop
        if self.current == 'shop' and self.validate():
            return True
        
        # Make sure tabs are viewable
        if not self.current or self.current == 'tasks':
            self.home()
        
        # Go to shop, or return false if unable
        if look_for('res/navigate/shop.png', click=True):
            self.current = 'shop'
            return True
        return False
    
    def market(self):
        # Navigate to market within shop
        if not self.current == 'shop' and self.validate():
            self.shop()
        
        # Loop until market is selected
        time.sleep(0.5)
        shop = look_for('res/navigate/shop*.png')
        while not look_for('res/navigate/market.png') and shop:
            shop.click()
            time.sleep(0.8)
        if shop:
            return True
        return False

    def clan(self, chat=False):
        # TODO: debug

        # Navigate to main clan or chat screen
        if self.current == 'clan' and not chat and self.validate():
            return True
        elif self.current == 'chat' and chat and self.validate():
            return True
        
        # Make sure tabs are viewable
        if not self.current or self.current == 'tasks':
            self.home()

        # Go to correct screen, or return false if unable
        if look_for('res/navigate/clan.png', click=True):
            x = look_for('res/navigate/x.png')      # x having a value means chat is open
            if chat and not x:
                if look_for('res/navigate/clan*.png', click=True):
                    self.current = 'chat'
                    return True
                return False
            if not chat and x:
                x.click()
                self.current = 'clan'
                return True
            if chat:
                self.current = 'chat'
            else:
                self.current = 'clan'
            return True
        return False
    
    def tasks(self):
        # Navigate to tasks menu
        if not self.current == 'home' and self.validate():
            self.home()
        
        # TODO: Implement based on screenshot

    def events(self):
        # Navigate to events menu

        # TODO: Implement
        pass