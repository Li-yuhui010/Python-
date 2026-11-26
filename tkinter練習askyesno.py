import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("終了確認アプリ")
window.geometry("500x300")

label = tk.Label(window, text="Python勉強中")
label.pack()

def tixing():
    message = messagebox.askyesno("確認", "本当に勉強を終了しますか？")
    
    if message:
        print(label.config(text="今日の勉強は終了しました", foreground="green"))

    else:
        print(messagebox.showinfo("お知らせ", "引き続き頑張りましょう!"))

button = tk.Button(window, text="終了する", command=tixing)
button.pack()

window.mainloop()

