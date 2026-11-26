import tkinter as tk

window = tk.Tk()
window.title("自己紹介アプリ")
window.geometry("400x300")

label = tk.Label(window, text="名前")
label.pack()
entry = tk.Entry(window, width=30)
entry.pack()

label02 = tk.Label(window, text="年齢")
label02.pack()
entry02 = tk.Entry(window, width=10)
entry02.pack()

def hello():
    name = entry.get()
    old = entry02.get()
    print(f"はじめまして、{name}です。{old}歳です。")

button = tk.Button(window, text="自己紹介する", command=hello)
button.pack()

window.mainloop()

