
#[요구조건] 버튼을 누르면 콜백 신호가 돌아오도록 한다.

from tkinter import *

window = Tk()
window.title("OOButton")
window.geometry("600x400")

# [라벨] 마우스의 위치와 상태를 저장하는 event을 이용하기.

def on_label_cilcked(event) :
    print(f"라벨이 클릭되었습니다. : {event}")
    # [출력결과 中] 라벨이 클릭되었습니다. : <ButtonPress event state=Mod1 num=1 x=26 y=9>

label = Label(window, text = "Break your limit")
label.bind("<Double-1>", on_label_cilcked)
# [참고] bind에서 정의된 조건을 만족해야만, 뒤 함수가 실행되게 한다.
label.pack()

# [버튼] 함수와 command를 이용해서 신호가 돌아오도록 하기.

def on_btn1_cilcked(event) :
    print(f"버튼이 클릭되었습니다. : {event}")
    # [출력결과 中] 버튼이 클릭되었습니다. : <ButtonPress event state=Mod1 num=1 x=22 y=17>
    label.config(text = f"버튼1이 클릭되었습니다. : {event}")
    # [출력결과] label에 버튼1이 클릭되었다와 event의 정보가 출력된다.
    
# btn1 = Button(window, text = "Click your limit.", bg = "#000000", fg = "#ffffff", command = on_btn1_cilcked)
btn1 = Button(window, text = "Click your limit.", bg = "#000000", 
              fg = "#ffffff", width = 30, height=20)
btn1.bind("<Button-1>", on_btn1_cilcked)
btn1.pack()

window.mainloop()