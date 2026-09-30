
class Box :
  def __init__(self, l=0, h=0, d=0) :
    self.length = l
    self.heigth = h
    self.depth = d

  def __str__(self) :
    return f"({self.length}, {self.heigth}, {self.depth})"

  def get_volume(self) :
    return str(self.length * self.heigth * self.depth)

def test_prob3() :
    b1 = Box(197853, 1000, 1000)
    print(b1)
    print("상자의 부피는 ", b1.get_volume())

if __name__ == "__main__" :
    test_prob3()