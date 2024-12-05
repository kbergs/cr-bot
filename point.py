class Point:
    def __init__(self, x=0, y=0):
        """
        Initializes a Point object with optional x and y coordinates.
        Default values are (0, 0).
        """
        self.x = x
        self.y = y
    
    def __repr__(self):
        """
        String representation of the Point object, useful for debugging.
        """
        return f"Point(x={self.x}, y={self.y})"