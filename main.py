import tkinter as tk
from idlelib import window
from tkinter import *

import self as self



class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.__init_main()



    def __init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)


        btn_open_dialog = tk.Button(toolbar, text="Dokumenty przyhodowe", command=self.open_dialog, bg='#d7d8e0', bd=0, compound=tk.TOP)
        btn_open_dialog.pack(side=tk.LEFT)



    def open_dialog(self):
        Child()




class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('Dokumenty prychodowe')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()






if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("MagazynPro")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()


