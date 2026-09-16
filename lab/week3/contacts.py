
#연락처 관리 프로그램
#[기능] 1. 연락처 추가, 2. 연락처 삭제, 3. 연락처 검색, 4. 연락처 출력, 5. 종료
#[구조] {"전화번호" : "이름"}

def print_info() :
    print("===== 연락처 관리 프로그램 =====")
    print("1. 연락처 추가")
    print("2. 연락처 삭제")
    print("3. 연락처 검색")
    print("4. 연락처 출력")
    print("5. 종료")
    print("==============================")

def add_addr(db) :
    number = input("전화번호를 입력하세요. : ")
    name = input("이름을 입력하세요. : ")

    if name not in db :
        db[number] = name
        print(f"{name}님을 저장했습니다.")

    else :
        print(f"{name}님은 이미 저장 되있습니다.")

    return db

def remove_addr(db) :
    number = input("삭제할 전화번호를 입력하세요. : ")
    if number in db :
        print(f"{db[number]}님을 삭제했습니다.")
    else :
        print(f"{number}으로 저장된 연락처가 없습니다.")

    return db

def reserch_addr(db) :
    number = input("검색할 전화번호를 입력하세요. : ")
    if number in db :
        print(f"{number}은 {db[number]}님입니다.")
    else :
        print(f"{number}으로 저장된 연락처가 없습니다.")

def print_db(db) :
    print("==== 현재 연락처 현황 ====")
    for number in db :
        print(f"{number} : {db[number]}")

def main() :
    db = {}
    while True :
        print_info()
        user_choice = int(input("메뉴를 선택하세요. : "))
        if user_choice == 1 :
            add_addr(db)
        elif user_choice == 2 :
            remove_addr(db)
        elif user_choice == 3 :
            reserch_addr(db)
        elif user_choice == 4 :
            pass #집 가서 이후에 짤 것.
