import tkinter as tk

window = tk.Tk()
window.title("メッセージアプリ")
window.geometry("400x300")

def morning():
    print("おはようございます！")

def evening():
    print("こんばんは")


label = tk.Label(window, text="好きなボタンを押してください")
label.pack()

button01 = tk.Button(window, text="おはよう", command=morning)
button01.pack()

button02 = tk.Button(window, text="こんばんは", command=evening)
button02.pack()

window.mainloop()