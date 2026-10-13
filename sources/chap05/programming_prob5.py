

def checkPass(p) :

    upper_list = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    lower_list = ["abcdefghijklmnopqrstuvwxyz"]
    number_list = ["0123456789"]

    if len(p) >= 8 :
        upper_cnt = 0
        lower_cnt = 0
        number_cnt = 0

        for char in p :
            if char in upper_list : upper_cnt += 1
            if char in lower_list : lower_cnt += 1
            if char in number_list : number_cnt += 1

        if (1<=upper_cnt) and (1<=lower_cnt) and (1<=number_cnt) :
            print("사용할 수 있습니다.")
            return True

        else : 
            print("사용할 수 없습니다. 다시 입력하세요.")
            return False


    else :
        print("사용할 수 없습니다. 다시 입력하세요.")
        return False

def main() :

    while True :
        user_password = input("패스워드를 입력하세요. : ")
        output_bit = checkPass(user_password)
        
        if output_bit == True : break

if __name__ == "__main__" :
    main()