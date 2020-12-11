import tkinter
import tkinter.messagebox

FONT = "Times New Roman"
WIDTH = 800
HEIGHT = 600

results = [
        "전생에 고양이었을 가능성은 매우 낮습니다.",
        "보통 사람입니다.",
        "특별히 이상한 곳은 없습니다.",
        "꽤 고양이다운 구석이 있습니다.",
        "고양이와 비슷한 성격 같습니다.",
        "고양이와 근접한 성격입니다.",
        "전생에 고양이었을지도 모릅니다.",
        "겉모습은 사람이지만, 속은 고양이일 가능성이 있습니다."
]

def click_btn():
    pts = 0
    for i in range(7):
        if bvar[i].get() == True:
            pts += 1
    cat_ratio = int(100 * pts / 7)
    text.delete("1.0", tkinter.END)
    text.insert("1.0", "<진단결과>\n당신의 고양이 지수는 " + str(cat_ratio) + "%입니다.\n" + results[pts])

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("고양이 지수 진단 게임")
    root.resizable(False, False)

    canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack()
    # 배경 그림
    gazou = tkinter.PhotoImage(file='./image/mina.png')
    canvas.create_image(WIDTH // 2, HEIGHT // 2, image=gazou)

    # 진단 버튼
    button = tkinter.Button(text="진단하기", font=(FONT, 32), bg="lightgreen", command=click_btn)
    button.place(x=400, y=480)

    # 텍스트
    text = tkinter.Text(width=40, height=5, font=(FONT, 16))
    text.place(x=320, y=30)

    # 체크박스
    bvar = [None] * 7
    cbtn = [None] * 7
    ITEM = [
            "높은 곳이 좋다",
            "공을 보면 굴리고 싶어진다",
            "깜짝 놀라면 털이 곤두선다",
            "쥐구멍이 마음에 든다",
            "개에게 적대감을 느낀다",
            "생선 뼈를 발라 먹고 싶다",
            "밤, 기운이 난다"
    ]

    for i in range(7):
        bvar[i] = tkinter.BooleanVar()
        bvar[i].set(False)
        cbtn[i] = tkinter.Checkbutton(
                text=ITEM[i],
                font=(FONT, 12),
                variable=bvar[i],
                bg='#dfe')
        cbtn[i].place(x=400, y=160 + 40 * i)

    root.mainloop()
