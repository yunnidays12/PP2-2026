
class Rectangle :
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def __str__(self) :
        pass

    def set_coordinate(self, replace_x, replace_y) :
        self.x = replace_x
        self.y = replace_y

    def get_coordinate(self) :
        return (self.x, self.y)

    def getArea(self) :
        return self.height * self.width

    def overlap(self, other) :
        pass

def test_prob4() :
    rect1 = Rectangle(0, 0, 100, 100)
    rect2 = Rectangle(10, 10, 100, 100)
    rect1.overlap(rect2)

if __name__ == "__main__" :
    test_prob4()