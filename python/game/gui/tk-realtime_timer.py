import tkinter

TIMER = 0
FONT = "Times New Roman"

def count_up():
    global TIMER
    TIMER += 1
    label["text"] = TIMER
    root.after(1000, count_up)    # 1초 후, count_up함수를 재실행

if __name__ == "__main__":
    root = tkinter.Tk()

    label = tkinter.Label(font=(FONT, 80))
    label.pack()

    root.after(1000, count_up)
    root.mainloop()
