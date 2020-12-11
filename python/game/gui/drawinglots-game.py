import random
import tkinter


FONT = "Times New Roman"
WIDTH = 800
HEIGHT = 600

def click_btn():
    label['text'] = random.choice(["대길", "중길", "소길", "흉"])
    label.update()

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("제비뽑기 게임")
    root.resizable(False, False)    # 화면 고정
    
    canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack()
    gazou = tkinter.PhotoImage(file='image/miko.png')
    canvas.create_image(WIDTH // 2, HEIGHT // 2, image=gazou)

    label = tkinter.Label(root, text="??", font=(FONT, 120), bg="white")
    label.place(x=380, y=60)

    button = tkinter.Button(root, text="제비뽑기", font=(FONT, 36), command=click_btn, fg="skyblue")
    button.place(x=360, y=400)

    root.mainloop()
