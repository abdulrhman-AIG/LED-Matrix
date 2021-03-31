# Control an LED Matrix through Raspberry Pi & Tkinter

# Importing Libraries
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = App()
    app.title("LED Matrix Controller")
    app.geometry("500x500")
    app.mainloop()