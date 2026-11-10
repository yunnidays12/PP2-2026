
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
        self.id = f"PP2-{Person.count:04d}"
        Person.count += 1

    def to_dict(self) :

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
    line = f"{a["id"]},{a["name"]},{a["year"]},{a["sex"]},{a["height"]},{a["weight"]},{a["bmi"]},{a["state"]}"

    try :
        with open(path, "a", encoding="utf-8") as f :
            f.write(line + "\n")

    except FileNotFoundError :
         print("파일을 찾을 수 없습니다.")

def read_txt(path) :
    result = []
    try :
        with open(path, "r", encoding="utf-8") as f:
            all_data = f.readlines()
            for text in all_data :
                clean_data = [x.strip() for x in text.strip().split(",")]
                result.append(clean_data)
            return result
        
    except FileNotFoundError :
        print("파일을 찾을 수 없습니다.")

def write_json(path, person) : 
    a = person.to_dict()
    try :
        with open(path, "w", encoding="utf-8") as f:
            json.dump(a, f, ensure_ascii=False, indent=4)

    except FileNotFoundError :
        print("파일을 찾을 수 없습니다.")

def read_json(path) :
    try :
        with open(path, "r", encoding="utf-8") as f :
            data = json.load(f)
        return data

    except FileNotFoundError :
        print("파일을 찾을 수 없습니다.")