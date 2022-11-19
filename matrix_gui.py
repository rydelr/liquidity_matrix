from tkinter import *


class LiqMatrix:
    def __init__(self, master):
        self.master = master

        self.main_frame = None

        self.initial_methods()

    def initial_methods(self):
        self.frames()
        self.run_data_receiving()

    def frames(self):
        self.main_frame = LabelFrame(self.master, bd=4, width=300, height=150)

    def run_data_receiving(self):
        print("call data_receiving.py")
        pass


root = Tk()
root.title("Liquidity Matrix")
root.geometry("400x200")

liq_gui = LiqMatrix(master=root)

root.mainloop()
