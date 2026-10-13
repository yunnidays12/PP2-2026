
def calculate() :
    a = int(input("첫 번째 정수를 입력하세요. : "))
    b = int(input("두 번째 정수를 입력하세요. : "))

    return (a+b, a-b, a*b, a/b)

if __name__ == "__main__" :
    result = calculate()

    print(f"{result[0]}, {result[1]}, {result[2]}, {result[3]}이 반환되었습니다.")