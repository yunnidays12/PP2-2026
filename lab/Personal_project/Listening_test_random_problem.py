
import os
import random
from playsound3 import playsound

def create_soundtrack_folder() :

    soundtrack_name = {1 : "과제이해", 2: "포인트이해", 3: "개요이해", 4: "즉시응답", 5: "통합이해"}

    #파일이 컴퓨터에 없었다면, 생성하고 인사하기.

    if os.path.exists("Personal_project/soundtrack") == False :
        for i in soundtrack_name : 
            os.makedirs(f"Personal_project/soundtrack/{i}({soundtrack_name[i]})")
        print("폴더 생성 완료")
        print("환영합니다!")

    else : #파일이 이미 컴퓨터에 있을 경우, 새로 생성하지 않고 바로 인사
        print("환영합니다!")

def print_info() :
    soundtrack_name = {1: "과제이해", 2:"포인트이해", 3:"개요이해", 4:"즉시응답", 5:"통합이해"}

    print("===랜덤 청해 출제기===")
    for i in soundtrack_name :
        print(f"{i}. {soundtrack_name[i]}")
    print("===================")

    user_choice = int(input("원하는 출제파트를 선택하세요. : "))

    return user_choice

def count_qus(user_choice): #AI 활용. 이해했는지 검토 요망.
    soundtrack_name = {1: "과제이해", 2: "포인트이해", 3: "개요이해", 4: "즉시응답", 5: "통합이해"}
    
    # 1. 사용자가 선택한 파트의 폴더 경로 지정
    folder_path = f"Personal_project/soundtrack/{user_choice}({soundtrack_name[user_choice]})"
    
    # 2. 폴더 존재 여부 확인
    if not os.path.exists(folder_path):
        print(f"경고: {folder_path} 경로를 찾을 수 없습니다.")
        return 0

    # 3. 폴더 내 실제 파일만 카운트 (.DS_Store 등 숨김 파일 및 하위 디렉터리 제외)
    files = [
        f for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f)) and not f.startswith(".")
    ]
    
    number_qus = len(files)
    print(f"선택한 파트의 총 문제 수: {number_qus}개")

    return number_qus

def random_make_number(number_qus) :

    result = []

    while True :
        number_list = [i for i in range(1, number_qus+1)]
        user_input = int(input(f"몇 문제를 출제할까요? (총 {number_qus}문제) : "))
        
        if user_input <= number_qus :
            while len(result) != user_input :
                num = random.choice(number_list)
                if num not in result :
                    result.append(num)

            print("랜덤번호 출제 완료! : ", result)
            return result
        
        else :
            print("출제가능한 문제보다 많습니다.")

def play_mp3(user_choice, random_list) : #playground 모듈 사용할 지 생각해보기. --> 사용해보자.
    pass

def main() :
    create_soundtrack_folder()

    user_input = print_info()
    number_qus = count_qus(user_input)

    random_list = random_make_number(number_qus)

if __name__ == "__main__" :
    main()