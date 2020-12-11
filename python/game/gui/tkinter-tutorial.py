import tkinter

# Font 확인
#import tkinter.font
#print(tkinter.font.families())
FONT = "Times New Roman"

def click_btn():
    button["text"] = "클릭했습니다"

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("첫번째 Canvas")
    #root.geometry("800x600")    # 화면크기
    canvas = tkinter.Canvas(root, width=400, height=600)
    canvas.pack()

    gazou = tkinter.PhotoImage(file="image/hyunju.png")
    canvas.create_image(200, 300, image=gazou)    # 이미지의 center좌표임

    label = tkinter.Label(root, text="라벨 문자열", font=(FONT, 24))
    label.place(x=200, y=100)

    button = tkinter.Button(
            root,
            text='버튼 문자열',
            font=(FONT, 24),
            command=click_btn

    )
    button.place(x=200, y=200)
    root.mainloop()
