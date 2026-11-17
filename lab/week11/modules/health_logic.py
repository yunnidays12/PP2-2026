
from health_db import *

def print_info() :

    print("-----------------------------")
    print("1. 인원 추가")
    print("2. 목록 조회")
    print("3. 검색 및 상세조회")
    print("4. 수정 및 삭제")
    print("5. 통계조회")
    print("6. 파일에서 가져오기")
    print("7. 파일로 저장")
    print("0. 종료")
    print("-----------------------------")

def add_register(name, year, sex, heg, weg) :
    return Person(name, year, sex, heg, weg)

def serech_the_name(user_list, user_name) :
    for user in user_list :
        if user.name == user_name :
            return user.to_list()

    else : return "조회된 이름이 없습니다."

def retouch(user_list, user_name, forwhat, replace_thing) :

    keymapping = {1 : "name", 2 : "year", 3 : "sex", 4 : "heg", 5 : "weg"}

    for user in user_list :
        if user.name == user_name :
            setattr(user, keymapping[forwhat], replace_thing)
            
def statistics(user_list) :
    person_number = len(user_list)

    all_heg, all_weg, all_bmi = 0, 0, 0

    for person in user_list :
        all_heg += person.heg
        all_weg += person.weg
        all_bmi += person.bmi

    return (f"총인원 : {person_number}명"
            f"평균무게 : {round(all_heg / person_number, 3)}"
            f"평균키 : {round(all_heg / person_number, 3)}cm"
            f"평균 몸무게 : {round(all_weg/person_number, 3)}kg")

if __name__ == "__main__" :

    user_list = []

    while True :
        try :
            print_info()
            user_choice = int(input("원하는 메뉴를 선택하세요. : "))

            if user_choice == 1 :
                
                name = input("이름을 입력하세요. : ")

                while True :
                    year = int(input("생년을 입력하세요. : "))
                    if year <= 1900 : print("1900년 이후만 입력할 수 있습니다.")
                    else : break

                while True :
                    sex = input("성별을 입력하세요. (남/여) : ")
                    if sex == "남" or sex == "여" : break
                    else : print("'남' 또는 '여'만 입력해주세요.") 

                while True :    
                    weg = float(input("몸무게를 입력하세요. (단위 : kg) : "))
                    if weg <= 0 : print("0이 아닌 양의 실수여야 합니다.")
                    else : break

                while True :
                    heg = float(input("키를 입력하세요. (단위 : cm) : "))
                    if heg <= 0 : print("0이 아닌 양의 실수여야 합니다.")
                    else : break
        
                user_list.append(add_register(name, year, sex, heg, weg))

            elif user_choice == 2 :
                print(user_list)

            elif user_choice == 3 :
                user_name = input("조회할 사람의 이름을 검색하세요. : ")
                print(serech_the_name(user_list, user_name))

            elif user_choice == 4 :
                user_name = input("정보를 수정할 사람의 이름을 검색하세요. : ")
                print("1. 이름 / 2. 생년 / 3. 성별 / 4. 몸무게 / 5. 키")
                forwhat = int(input("수정할 정보를 고르세요. : "))

                if 1 <= forwhat <= 5 :
                    replace_thing = input("수정할 내용을 입력하세요. : ")
                    retouch(user_list, user_name, forwhat, replace_thing)
                else :
                    print("1 이상 5 이하의 정수만 입력해주세요.")
                    continue

            elif user_choice == 5 : 
                print(statistics(user_list))

        except ValueError :
            print("유효하지 않은 입력값입니다.")