import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("メッセージ表示アプリ")
window.geometry("500x300")

label = tk.Label(window, text="好きなボタンを押してください")
label.pack()

def inform():
    messagebox.showinfo("お知らせ", "登録成功!")

def warn():
    messagebox.showwarning("警告", "入力内容を確認してください")

def error():
    messagebox.showerror("エラー", "登録失敗!")

button01 = tk.Button(window, text="情報", command=inform)
button01.pack()

button02 = tk.Button(window, text="警告", command=warn)
button02.pack()

button03 = tk.Button(window, text="エラー", command=error)
button03.pack()

window.mainloop()