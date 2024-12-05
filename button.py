import numpy as np
import pyautogui as pag

class Button:
    def __init__(self, left, top, width, height):
        # Initialize the position and dimensions of the button
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.dead = False
    
    def __repr__(self):
        # String representation of the button
        return f"Button(left={self.left}, top={self.top}, width={self.width}, height={self.height})"
    
    def right(self):
        # Returns the right boundary (left + width)
        return self.left + self.width
    
    def bottom(self):
        # Returns the bottom boundary (top + height)
        return self.top + self.height
    
    def area(self):
        # Returns the area of the button (width * height)
        return self.width * self.height
    
    def contains(self, x, y):
        # Returns True if the point (x, y) is within the button's bounds
        return self.left <= x <= self.right() and self.top <= y <= self.bottom()
    
    def is_dead(self):
        # Return True if the button is dead
        return self.dead
    
    def overlap(self, other):
        # Returns the overlap button with another button, or None if no overlap
        overlap_left = max(self.left, other.left)
        overlap_right = min(self.right(), other.right())
        overlap_top = max(self.top, other.top)
        overlap_bottom = min(self.bottom(), other.bottom())
        
        # If there's no overlap, return None
        if overlap_left >= overlap_right or overlap_top >= overlap_bottom:
            return None
        
        # Return the overlapping button
        overlap_width = overlap_right - overlap_left
        overlap_height = overlap_bottom - overlap_top
        return Button(overlap_left, overlap_top, overlap_width, overlap_height)
    
    def random_point(self):
        # Returns a random point from a normal distribution in the button area
        # Get midpoint in the button
        xmid = self.left + self.width / 2
        ymid = self.top + self.height / 2

        # Get spread (based on 0.15 for a scale of 1)
        xspread = self.width * 0.15
        yspread = self.height * 0.15

        # Generate random x and y
        x = int(np.random.normal(loc=xmid, scale=xspread))
        y = int(np.random.normal(loc=ymid, scale=yspread))

        # Clip points to ensure they stay within the button's bounds
        x = np.clip(x, self.left, self.right())
        y = np.clip(y, self.top, self.bottom())

        return (x, y)
    
    def click(self):
        # clicks a random point within the button
        pag.click(self.random_point())