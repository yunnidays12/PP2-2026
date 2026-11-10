
import json

class Person :

    count = 1

    def __init__(self, name : str, year : int, sex : str, heg : float, weg : float, bmi : float, state : str):
        self.name = name
        self.year = year
        self.sex = sex
        self.heg = heg
        self.weg = weg
        self.bmi = bmi
        self.state = state
        self.id = f"PP2-{self.count:03d}"

    def to_dict(self) :

        self.count += 1

        return {"id" : self.id,
                "name" : self.name,
                "year" : self.year,
                "sex" : self.sex,
                "height" : self.heg,
                "weight" : self.weg,
                "bmi" : self.bmi,
                "state" : self.state}

def write_txt(path, person) :
    a = person.to_dict()
    line = f"{a["id"]}, {a["name"]}, {a["year"]}, {a["sex"]}, {a["height"]}, {a["weight"]}, {a["bmi"]}, {a["state"]}"

    with open(path, "a", encoding="utf-8") as f :
        f.write(line + "\n")

def write_json(path, person) : 
    a = person.to_dict()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(a, f, ensure_ascii=False, indent=4)

if __name__ == "__main__" :
    
    path = "lab\\week11\\data\\write_json.json"
    person = Person("홍길동", 1995, "남", 175, 72.5, 23.67, "과체중")
    write_json(path, person)