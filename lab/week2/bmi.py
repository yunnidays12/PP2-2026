
def cal_bmi(height, weight) -> float :
    """
    result : bmi 계산한 값.
    state : 아래에 있는 bmi에 따른 상태
    """
    result = weight / ((height)*0.01)**2
    state = ""

    if 20 > result : state = "저체중"
    elif 20<=result<25 : state = "표준"
    elif 25<=result<30 : state = "과체중"
    elif result>= 30 : state = "비만"

    return state, result

def main() :
    height = float(input("키를 입력해주세요. (단위 : cm) : "))
    weight = float(input("몸무게를 입력해주세요. (단위 : kg) : "))

    state ,result = cal_bmi(height, weight)
    print(f"당신의 bmi는 {result:.3f}입니다.")
    print(f"당신은 {state} 입니다.")

if __name__ == "__main__" :
    main()