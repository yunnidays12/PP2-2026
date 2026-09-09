
#"return None"가 아닌, "-> None"으로 대체해도 좋음. 
# return 할 거 없으면 안쓰기도 했으니까.

def print_happy(name:str) -> None : #출력의 부분
    print("안녕하세요.")
    print(name+"님의 생일을 축하합니다.")

def test_happy_birthdays() : #또 이름이 중복 됨.
    print_happy("윤성")
    print_happy("강훈")
    print_happy("민석")
    print_happy("원준")

    #[실행결과] 정상실행

def test_happy_birthdays2() : #최적화 (for문)
    name_list = ["윤성", "강훈", "민석", "원준"]
    for name in name_list :
        print_happy(name)

    #[실행결과] 정상실행

def test_happy_birthday3() :
    print_happy(1) 
    print_happy([1,2,3])
    print_happy(3.141592)

    #[실행결과] TypeError: unsupported operand type(s) for +: 'int' and 'str'
    #즉, 파라미터는 str만 받는데, 왜 갑자기 다른 자료형을 주냐며 프로그램이 멈춰버림.

#모듈화 때문에 이런 방식으로 실행 (이건 그냥 외우자.)
if __name__ == "__main__" :
    test_happy_birthday3()