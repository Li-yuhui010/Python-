import tkinter as tk

window = tk.Tk()
window.title("入力クリアアプリ")
window.geometry("500x300")

label = tk.Label(window, text="名前を入力してください")
label.pack()

entry = tk.Entry(window, width=30)
entry.pack()

def sure():
    name = entry.get()
    print(f"{name}、こんにちは!")

def sakujyo():
    name01 = entry.delete(0, tk.END)



button01 = tk.Button(window, text="確認する", command=sure)
button01.pack()

button02 = tk.Button(window, text="削除する", command=sakujyo)
button02.pack()


window.mainloop()