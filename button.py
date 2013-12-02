class Button:
    def __init__(self, x, y, width, height, minute, hour):
        self.x = x
        self.y = y
        self.minute = minute
        self.hour = hour
        self.width = width
        self.height = height
        self.images = []

    def click(self, x, y, click):
        if 0 <= x-self.x <= self.width and \
           0 <= y-self.y <= self.height and \
           click and not self.clicked:
            return True
        return False
