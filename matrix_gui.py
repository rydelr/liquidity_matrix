from tkinter import *
import liq_matrix_core


class LiqMatrix:
    def __init__(self, master):
        self.master = master

        self.core = liq_matrix_core.LiqMatrixCore()
        self.main_frame = None

        self.initial_methods()

    def initial_methods(self):
        self.frames()
        self.run_core()

    def frames(self):
        self.main_frame = LabelFrame(self.master, bd=4, width=300, height=150)

    def run_core(self):
        self.core.run_data_receiving()





root = Tk()
root.title("Liquidity Matrix")
root.geometry("400x200")

liq_gui = LiqMatrix(master=root)

root.mainloop()
