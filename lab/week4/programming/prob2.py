
class myRocket :
  def __init__ (self, x=0, y=0) :
    self.x = x
    self.y = y

  def __str__ (self) :
    return str(self.y)

  def moveup(self) :
    self.y += 1

def test_prob2() :
    my1 = myRocket()
    print("로켓의 높이 : ", my1)

    my1.moveup()
    print("로켓의 높이 : ", my1)