import tkinter as tk

window = tk.Tk()
window.title("挨拶アプリ")
window.geometry("500x300")

label = tk.Label(window, text="名前を入力してください")
label.pack()

entry = tk.Entry(window, width=30)
entry.pack()

def hello():
    name = entry.get()
    print(f"こんにちは、{name}さん")

button = tk.Button(window, text="挨拶する", command=hello)
button.pack()


window.mainloop()



