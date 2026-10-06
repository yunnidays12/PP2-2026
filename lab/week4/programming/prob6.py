
class Person() :
    def __init__(self, n, m = "01012345678", o = "0212345678", e = "a1234@gmail.com"):
        self.name = n
        self.mobile = m
        self.office = o
        self.email = e

    def __str__ (self) :
        return f"이름 : {self.name} / 전화번호 : {self.mobile} / 사무실 전화번호 : {self.office} / 이메일 : {self.email}"

    def setname(self, new_n) :
        self.name = new_n

    def setemail(self, new_e) :
        self.email = new_e

def test_prob6() :
    p1 = Person("kim", o = "1234567", e = "kim@gmail.com")
    p2 = Person("pakr", o = "234567") 

    p2.setemail("park@company.com")

if __name__ == "__main__" :
    test_prob6()