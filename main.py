# Control an LED Matrix through Raspberry Pi & Tkinter

# Importing Libraries
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Buttons
        self.button_1 = tk.Button(
            text="1", height=2, width=3, command=lambda: toggle(self, "button_1")
        )
        self.button_1.grid(column=0, row=0)

        self.button_2 = tk.Button(
            text="2", height=2, width=3, command=lambda: toggle(self, "button_2")
        )
        self.button_2.grid(column=1, row=0)

        self.button_3 = tk.Button(
            text="3", height=2, width=3, command=lambda: toggle(self, "button_3")
        )
        self.button_3.grid(column=2, row=0)

        self.button_4 = tk.Button(
            text="4", height=2, width=3, command=lambda: toggle(self, "button_4")
        )
        self.button_4.grid(column=0, row=1)

        self.button_5 = tk.Button(
            text="5", height=2, width=3, command=lambda: toggle(self, "button_5")
        )
        self.button_5.grid(column=1, row=1)

        self.button_6 = tk.Button(
            text="6", height=2, width=3, command=lambda: toggle(self, "button_6")
        )
        self.button_6.grid(column=2, row=1)

        self.button_7 = tk.Button(
            text="7", height=2, width=3, command=lambda: toggle(self, "button_7")
        )
        self.button_7.grid(column=0, row=2)

        self.button_8 = tk.Button(
            text="8", height=2, width=3, command=lambda: toggle(self, "button_8")
        )
        self.button_8.grid(column=1, row=2)

        self.button_9 = tk.Button(
            text="9", height=2, width=3, command=lambda: toggle(self, "button_9")
        )
        self.button_9.grid(column=2, row=2)

        # Button Toggle Function
        def toggle(self, bn_number):
            # Getattr calls a variable called 'bn_number' from 'self'
            if getattr(self, bn_number)["relief"] == tk.RAISED:
                getattr(self, bn_number)["relief"] = tk.SUNKEN
                # Turn GPIO ON
            else:
                getattr(self, bn_number)["relief"] = tk.RAISED
                # Turn GPIO OFF


if __name__ == "__main__":
    app = App()
    app.title("Controller")
    app.mainloop()