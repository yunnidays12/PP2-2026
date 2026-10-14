# [6장] programming_prob15.py

def solution(coin_list) :

  answer = 1
  answer_list = []

  for i in range(1, len(coin_list)) :

    if coin_list[i-1] == coin_list[i] : answer += 1
    else : 
      answer_list.append(answer)
      answer = 1

  return max(answer_list)

coin_list = [1,0,1,1,1,0,0,1,0,1,0,1,1]
print(solution(coin_list))