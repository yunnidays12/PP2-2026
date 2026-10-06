
class Phonebook :
    def __init__(self):
        self.contacts = {}

    def add(self, name, mobile = None, office = None, email = None) :
        self.contacts[name] = (mobile, office, email)

def test_prob7() :
    obj = Phonebook()
    obj.add("KIM", office = "1234567", email = "kim@gmail.com")
    obj.add("Park", office = "234567", email = "pakr@gmail.com")

    print(obj)

if __name__ == "__main__"  :
    test_prob7()