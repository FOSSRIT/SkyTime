class Button:
    def __init__(self, x, y, width, height, minute=None, hour=None):
        self.x = x
        self.y = y
        self.minute = minute
        self.hour = hour
        self.width = width
        self.height = height
        self.image = None
        self.prevPressed = False

    def pressed(self, x, y, curState):
        if (0 <= x-self.x <= self.width and
           0 <= y-self.y <= self.height and curState) or curState:
            return True
        return False

    def intersects(self, x, y):
        if 0 <= x-self.x <= self.width and \
           0 <= y-self.y <= self.height:
            return True
        return False
