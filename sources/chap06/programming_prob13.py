
# [6장] programming_prob13.py

def print_info(seat_list) :
  print("=" * 80)
  for i in range(1, 11) :
    print(i, end = "\t")
  print("\n")

  for row in range(10) :
    for col in range(10) :
      print(seat_list[row][col], end="\t")
    print("\n")

def reservation() :
  row_num = int(input("원하시는 좌석의 행번호를 입력하세요. (종료는 -1) : "))
  col_num = int(input("원하시는 좌석의 열번호를 입력하세요. (종료는 -1) : "))

  return row_num-1, col_num-1

seat_list = [[0 for _ in range(10)] for _ in range(10)]

while True :

  print_info(seat_list)
  row_num, col_num = reservation()

  if (row_num != -1) and (col_num != -1) :
    if seat_list[row_num][col_num] == 0 :
      print("예약 되었습니다.")
      seat_list[row_num][col_num] = 1
    else : print("이미 예약된 좌석입니다.")

  else :
    print("서비스를 종료합니다.")
    break