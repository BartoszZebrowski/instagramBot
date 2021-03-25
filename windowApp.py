import tkinter as tk
from tkinter import *
from threading import Thread
from logic import *


# Funkcje aplikacji

def getAccouns():
    x = accounts.get("1.0", END)
    return x.split()


def startBot():
    bot = Thread(target=start, args=(
        pLogin.get(), pPassword.get(), getAccouns()))
    bot.start()


def writeConsole(text):
    console.insert(END, text)

# Wyglad okna


window = tk.Tk()
window.title("Instagram bot")
canvas = tk.Canvas(window, height=480, width=640, bg="#282828")
canvas.pack()

frameLeft = tk.Frame(window, bg="#282828")
frameLeft.place(relwidth=0.6, relheight=1)
frameRight = tk.Frame(window, bg="#282828")
frameRight.place(relwidth=0.4, relheight=1, relx=0.6,)

pLogin = tk.Entry(frameLeft, width=30, bg="#E5E5E5")
pLogin.place(relx=0.1, rely=0.1)
pPassword = tk.Entry(frameLeft, width=30, bg="#E5E5E5", show="*")
pPassword.place(relx=0.1, rely=0.2)
accounts = tk.Text(frameLeft, bg="#E5E5E5",
                   width=30, height=30, wrap=WORD)
accounts.place(relx=0.1, rely=0.45, relwidth=0.8, relheight=0.36)

startButton = tk.Button(frameLeft, text="Start", padx=10,
                        pady=5, fg="white", bg="#000000",  command=startBot)
startButton.place(relx=0.1, rely=0.86)
stopButton = tk.Button(frameLeft, text="Stop", padx=10,
                       pady=5, fg="white", bg="#000000")
stopButton.place(relx=0.25, rely=0.86)

console = tk.Text(frameRight, width=30, height=30,
                  wrap=WORD, bg="#E5E5E5", state=DISABLED)
console.place(relx=0.05, rely=0.1, relwidth=0.85, relheight=0.85)

window.mainloop()
