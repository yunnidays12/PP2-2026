
class Tv :
    def __init__(self):
        self.number = 0
        self.vol = 0
        self.on = True

    def turnOn(self) :
        self.on = True

    def turnOff(self) :
        self.on = False

    def changeChannel(self, number) :
        self.number = number

    def changeVolume(self, vol) :
        self.vol = vol

tv1 = Tv()
tv1.turnOn()

tv2= Tv()
tv2.turnOff()

print("티비가 켜졌습니다." if tv1.on == True else "티비가 꺼졌습니다.")
print("티비가 켜졌습니다." if tv2.on == True else "티비가 꺼졌습니다.")