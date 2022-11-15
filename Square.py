class Square():

    def __init__(self, numb_x, numb_y, color, position, can_remove):
        self.number_square = str(numb_x+1) + str(numb_y+1)
        self.color = color
        self.position = position
        self.can_remove = can_remove

    def call_can_remove(self):
        return self.can_remove

    def call_position(self):
        x, y = self.position
        x += 125
        y += 125
        return self.position, x, y,self.can_remove

    def color_square(self):
        return self.color

    def overwriting(self,color):
        self.color=color