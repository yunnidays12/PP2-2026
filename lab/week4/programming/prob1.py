
class Cat :
  def __init__(self, name, age) :
    self.name = name
    self.age = age

  def __str__(self) :
    info = self.name + " " + str(self.age)
    return info

  def setName(self) :
    pass

  def getName(self) :
    pass

def test_prob1() :
    missy = Cat("Missy", 3)
    lucky = Cat("Lucky", 5)

    print(missy)
    print(lucky)

if __name__ == "__main__" :
    test_prob1()