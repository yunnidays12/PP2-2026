#lambda 함수 실습

mylist = [1,2,3,4,5,6,7,8,9]
result = list(map(lambda x : x**2, mylist))
#mylist에 있는 각각의 원소 x를 제곱해서 result에 저장하는 lambda 함수.

print(result) 
#[실행결과] [1,4,9,16,25,36,49,64,81]
