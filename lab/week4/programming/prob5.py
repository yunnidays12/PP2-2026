
class Triangle :
    def __init__ (self, a1, a2, a3, value = 3) :
        self.angel1 = a1
        self.angel2 = a2
        self.angle3 = a3
        self.numberOfsides = value

    def __str__(self) :
        return f"삼각형의 각 : {self.angel1}, {self.angel2}, {self.angle3}"
    
    def setAngle1(self, value) :
        self.angel1 = value

    def setAngle2(self, value) :
        self.angle2 = value

    def checkAngles(self) : 
        if (self.angel1 + self.angel2 + self.angle3 == 180) :
            return "올바른 삼각형입니다."
        else : return "올바르지 않은 삼각형입니다."

def test_prob5() :
    triangle = Triangle(90, 30, 60)
    print(triangle.checkAngles())