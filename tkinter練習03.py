import tkinter as tk

window = tk.Tk()
window.title("ログインシステム")
window.geometry("500x300")

def hello():
    name = entry01.get()
    password = entry02.get()
    if name == "admin" and password == "1234":
        print("ログイン成功！")
    else:
        print("ユーザー名またはパスワードが違います")
                  

label01 = tk.Label(window, text="ユーザー名")
label01.pack()

entry01 = tk.Entry(window, width=30)
entry01.pack()

label02 = tk.Label(window, text="パスワード")
label02.pack()

entry02 = tk.Entry(window, width=30)
entry02.pack()

button = tk.Button(window, text="ログイン", command=hello)
button.pack()

window.mainloop()