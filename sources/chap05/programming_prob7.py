
def getIntRange(a, b, msg) :

    while True :
        user_input = int(input(f"{msg}을 입력하세요. ({a}부터 {b}까지의 값) : "))
        if a <= user_input <= b : break

    return user_input

def main() :
    print("날짜를 입력하시오.(월과 일)")
    month = getIntRange(1, 12, "월")
    day = getIntRange(1, 31, "일")

    print(f"입력된 날짜는 {month}월 {day}일입니다.")

if __name__ == "__main__" :
    main()