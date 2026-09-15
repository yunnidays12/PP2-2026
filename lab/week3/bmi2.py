
def cal_bmi(height, weight) :
    """
    Args :
        height (float) : 키 (cm 단위)
        weigth (float) : 몸무게 (kg 단위)
    
    Returns :
        tuple[str, float] : (비만도 판정 문자열, bmi 계산값)
    """
    result = weight / ((height)*0.01)**2
    state = ""

    if 20 > result : state = "저체중"
    elif 20<=result<25 : state = "표준"
    elif 25<=result<30 : state = "과체중"
    elif result>= 30 : state = "비만"

    return state, result

def stu_input() :
    std_name = input("학생의 이름을 입력하세요. : ")
    std_height = float(input("학생의 키를 입력하세요. (단위 : cm) : "))
    std_weight = float(input("학생의 몸무게를 입력하세요. (단위 : kg) : "))
    return [std_name, std_weight, std_height]

def stu_cnt() :
    std_cnt = int(input("학생의 수를 입력하세요. (단위 : 명) : "))
    return std_cnt
    

def main() :
    std_list = []
    cnt = stu_cnt()
    for _ in range(cnt) :
        std_list.append(stu_input())

    for std in std_list :
        state, result = cal_bmi(std[2], std[1])
        print(f"{std[0]}님은 {state}이고 bmi 수치는 {result:.3f}입니다.")

if __name__ == "__main__" :
    main()
