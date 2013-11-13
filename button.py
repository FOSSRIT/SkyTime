class Button:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def isClicked(self, x, y, click):
        if 0 <= x-self.x <= self.width and \
           0 <= y-self.y <= self.height and click:
            return True
        return False
