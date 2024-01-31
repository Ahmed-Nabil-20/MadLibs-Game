import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
class program():
    def __init__(self, win = None, textbox1 = None, textbox2 = None, textbox3 = None, root = None, textbox4 = None, textbox5 = None, textbox6 = None, root3 = None, textbox7 = None, textbox8 = None, textbox9 = None, root4 = None, textbox10 = None, textbox11 = None, textbox12 = None, root5 = None, textbox13 = None, textbox14 = None, textbox15 = None, textbox16 =None) -> None:
        self.win = win
        self.root = root
        self.root3 = root3
        self.root4 = root4
        self.root5 = root5
        self.textbox1 = textbox1
        self.textbox2 = textbox2
        self.textbox3 = textbox3
        self.textbox4 = textbox4
        self.textbox5 = textbox5
        self.textbox6 = textbox6
        self.textbox7 = textbox7
        self.textbox8 = textbox8
        self.textbox9 = textbox9
        self.textbox10 = textbox10
        self.textbox11 = textbox11
        self.textbox12 = textbox12
        self.textbox13 = textbox13
        self.textbox14 = textbox14
        self.textbox15 = textbox15
        self.textbox16 = textbox16
    def lvl2_lvl1(self):
        self.root.destroy()
        program.main(self)
    def lvl3_lvl2(self):
        self.root3.destroy()
        program.main2(self)
    def lvl4_lvl3(self):
        self.root4.destroy()
        program.main3(self)
    def lvl5_lvl4(self):
        self.root5.destroy()
        program.main4(self)
    def check(self):
        x = self.textbox1.get()
        y = self.textbox2.get()
        z = self.textbox3.get()
        if x == "player" or "footballer" and y == "football" and z == "stadium":
            messagebox.showinfo("^_^", "You win")
            self.win.destroy()
            program.main2(self)
        else:
            messagebox.showinfo("-_-", "You lose")
    def check2(self):
        x = self.textbox4.get()
        y = self.textbox5.get()
        z = self.textbox6.get()
        if x == "beautiful" and y == "ball" and z == "afternoon":
            messagebox.showinfo("^_^", "You win")
            self.root.destroy()
            program.main3(self)
        else:
            messagebox.showinfo("-_-", "You lose")
    def check3(self):
        x = self.textbox7.get()
        y = self.textbox8.get()
        z = self.textbox9.get()
        if x == "programmer" or "developer" and y == "proramming" and z == "programmes" or "robots":
            messagebox.showinfo("^_^", "You win")
            self.root3.destroy()
            program.main4(self)
            
        else:
            messagebox.showinfo("-_-", "You lose")
    def check4(self):
        x = self.textbox10.get()
        y = self.textbox11.get()
        z = self.textbox12.get()
        if x == "teacher" and y == "school" and z == "teach":
            messagebox.showinfo("^_^", "You win")
            self.root4.destroy()
            program.main5(self)
            
        else:
            messagebox.showinfo("-_-", "You lose")
    def check5(self):
        x = self.textbox13.get()
        y = self.textbox14.get()
        z = self.textbox15.get()
        n = self.textbox16.get()
        if x == "space" and y == "planets" or "planet" and z == "aliens" and n == "rockets":
            messagebox.showinfo("^_^", "You win")
            self.root5.destroy()
            
        else:
            messagebox.showinfo("-_-", "You lose")
    def main(self):
        self.win = tk.Tk()
        self.win.title("MadLibs")
        self.win.iconbitmap("Madlibs.ico")
        width  = int((self.win.winfo_screenwidth() - 500)/2)
        height = int((self.win.winfo_screenheight()- 200)/2)
        self.win.geometry(f"500x200+{width}+{height}")
        self.win.resizable(False, False)
        self.win.configure(background="#1c1919")
        
        lvl_1 = ttk.Label(self.win, text="Level 1", background="#1c1919", font=("Arial", 10), foreground="white")
        lvl_1.place(x= 20, y= 5)

        describtion = ttk.Label(self.win, text="11 persons playing a sport in spesific place.", background="#1c1919", font=("Arial", 10), foreground="white")
        describtion.place(x= 20, y= 25)

        lable1 = ttk.Label(self.win, text="He is a ", background="#1c1919", font=("Arial", 15), foreground="white")
        lable1.place(x= 20, y= 60)

        self.textbox1 = ttk.Entry(self.win, font=("Arial", 15))
        self.textbox1.place(x=95, y=60, width=70)

        lable2 = ttk.Label(self.win, text="playing ", background="#1c1919", font=("Arial", 15), foreground="white")
        lable2.place(x= 175, y= 60)

        self.textbox2 = ttk.Entry(self.win, font=("Arial", 15))
        self.textbox2.place(x=250, y=60, width=75)

        lable3 = ttk.Label(self.win, text="in the ", background="#1c1919", font=("Arial", 15), foreground="white")
        lable3.place(x= 333, y= 60)

        self.textbox3 = ttk.Entry(self.win, font=("Arial", 15))
        self.textbox3.place(x=390, y=60, width=75)
        
        lable_1 = ttk.Label(self.win, text=".", background="#1c1919", font=("Arial", 15), foreground="white")
        lable_1.place(x= 475, y= 60)

        name1 = ttk.Label(self.win, text="Name", background="#1c1919", font=("Arial", 10), foreground="white")
        name1.place(x= 110, y= 110)

        name2 = ttk.Label(self.win, text="Name", background="#1c1919", font=("Arial", 10), foreground="white")
        name2.place(x= 267, y= 110)

        name3 = ttk.Label(self.win, text="Name", background="#1c1919", font=("Arial", 10), foreground="white")
        name3.place(x= 408, y= 110)

        button = ttk.Button(self.win, text="check", command=lambda : program.check(self))
        button.place(x= 100 , y = 150, width=300, height=30)

        self.win.mainloop()
    def main2(self):
        self.root = tk.Tk()
        self.root.title("MadLibs")
        self.root.iconbitmap("Madlibs.ico")
        width  = int((self.root.winfo_screenwidth() - 500)/2)
        height = int((self.root.winfo_screenheight()- 200)/2)
        self.root.geometry(f"500x200+{width}+{height}")
        self.root.resizable(False, False)
        self.root.configure(background="#1c1919")
        
        lvl_2 = ttk.Label(self.root, text="Level 2", background="#1c1919", font=("Arial", 10), foreground="white")
        lvl_2.place(x= 20, y= 5)

        b = ttk.Button(self.root, text="Back", command = lambda: program.lvl2_lvl1(self))
        b.place(x=400, y=1, height=25)

        describtion = ttk.Label(self.root, text="Alot of cute animals having fun with the most lovely game fot them at 12:00", background="#1c1919", font=("Arial", 10), foreground="white")
        describtion.place(x= 20, y= 25)

        lable1 = ttk.Label(self.root, text="Three ", background="#1c1919", font=("Arial", 10), foreground="white")
        lable1.place(x= 20, y= 60)

        self.textbox4 = ttk.Entry(self.root, font=("Arial", 10))
        self.textbox4.place(x=60, y=60, width=60)

        lable2 = ttk.Label(self.root, text="cats playing with ", background="#1c1919", font=("Arial", 10), foreground="white")
        lable2.place(x= 125, y= 60)

        self.textbox5 = ttk.Entry(self.root, font=("Arial", 10))
        self.textbox5.place(x=230, y=60, width=75)

        lable3 = ttk.Label(self.root, text="during ", background="#1c1919", font=("Arial", 10), foreground="white")
        lable3.place(x= 310, y= 60)

        self.textbox6 = ttk.Entry(self.root, font=("Arial", 10))
        self.textbox6.place(x=360, y=60, width=75)
        
        lable_1 = ttk.Label(self.root, text=".", background="#1c1919", font=("Arial", 10), foreground="white")
        lable_1.place(x= 440, y= 60)

        name1 = ttk.Label(self.root, text="Adjective", background="#1c1919", font=("Arial", 10), foreground="white")
        name1.place(x= 63, y= 100)

        name2 = ttk.Label(self.root, text="Name", background="#1c1919", font=("Arial", 10), foreground="white")
        name2.place(x= 247, y= 100)

        name3 = ttk.Label(self.root, text="Name", background="#1c1919", font=("Arial", 10), foreground="white")
        name3.place(x= 380, y= 100)

        button = ttk.Button(self.root, text="check", command=lambda : program.check2(self))
        button.place(x= 100 , y = 150, width=300, height=30)

        self.root.mainloop()
    def main3(self):
        self.root3 = tk.Tk()
        self.root3.title("MadLibs")
        self.root3.iconbitmap("Madlibs.ico")
        width  = int((self.root3.winfo_screenwidth() - 500)/2)
        height = int((self.root3.winfo_screenheight()- 200)/2)
        self.root3.geometry(f"500x200+{width}+{height}")
        self.root3.resizable(False, False)
        self.root3.configure(background="#1c1919")
        
        lvl_3 = ttk.Label(self.root3, text="Level 3", background="#1c1919", font=("Arial", 10), foreground="white")
        lvl_3.place(x= 20, y= 5)

        b = ttk.Button(self.root3, text="Back", command = lambda: program.lvl3_lvl2(self))
        b.place(x=400, y=1, height=25)

        describtion = ttk.Label(self.root3, text="Some one who Making programs , executing codes and making \nmachine move itself.", background="#1c1919", font=("Arial", 10), foreground="white")
        describtion.place(x= 20, y= 25)

        lable1 = ttk.Label(self.root3, text="The ", background="#1c1919", font=("Arial", 10), foreground="white")
        lable1.place(x= 20, y= 60)

        self.textbox7 = ttk.Entry(self.root3, font=("Arial", 10))
        self.textbox7.place(x=50, y=60, width=70)

        lable2 = ttk.Label(self.root3, text="uses ", background="#1c1919", font=("Arial", 10), foreground="white")
        lable2.place(x= 125, y= 60)

        self.textbox8 = ttk.Entry(self.root3, font=("Arial", 10))
        self.textbox8.place(x=160, y=60, width=85)

        lable3 = ttk.Label(self.root3, text="languages to make ", background="#1c1919", font=("Arial", 10), foreground="white")
        lable3.place(x= 255, y= 60)

        self.textbox9 = ttk.Entry(self.root3, font=("Arial", 10))
        self.textbox9.place(x=370, y=60, width=85)
        
        lable_1 = ttk.Label(self.root3, text=".", background="#1c1919", font=("Arial", 10), foreground="white")
        lable_1.place(x= 460, y= 60)

        name1 = ttk.Label(self.root3, text="Name", background="#1c1919", font=("Arial", 10), foreground="white")
        name1.place(x= 65, y= 100)

        name2 = ttk.Label(self.root3, text="Name", background="#1c1919", font=("Arial", 10), foreground="white")
        name2.place(x= 185, y= 100)

        name3 = ttk.Label(self.root3, text="Name", background="#1c1919", font=("Arial", 10), foreground="white")
        name3.place(x= 332, y= 100)

        button = ttk.Button(self.root3, text="check", command=lambda : program.check3(self))
        button.place(x= 100 , y = 150, width=300, height=30)

        self.root3.mainloop()
    def main4(self):
        self.root4 = tk.Tk()
        self.root4.title("MadLibs")
        self.root4.iconbitmap("Madlibs.ico")
        width  = int((self.root4.winfo_screenwidth() - 500)/2)
        height = int((self.root4.winfo_screenheight()- 200)/2)
        self.root4.geometry(f"500x200+{width}+{height}")
        self.root4.resizable(False, False)
        self.root4.configure(background="#1c1919")
        
        lvl_4 = ttk.Label(self.root4, text="Level 4", background="#1c1919", font=("Arial", 10), foreground="white")
        lvl_4.place(x= 20, y= 5)

        b = ttk.Button(self.root4, text="Back", command = lambda: program.lvl4_lvl3(self))
        b.place(x=400, y=1, height=25)

        describtion = ttk.Label(self.root4, text="Someone trimg to make many children to understand something .", background="#1c1919", font=("Arial", 10), foreground="white")
        describtion.place(x= 20, y= 25)

        lable1 = ttk.Label(self.root4, text="The good ", background="#1c1919", font=("Arial", 10), foreground="white")
        lable1.place(x= 20, y= 60)

        self.textbox10 = ttk.Entry(self.root4, font=("Arial", 10))
        self.textbox10.place(x=80, y=60, width=60)

        lable2 = ttk.Label(self.root4, text="go to ", background="#1c1919", font=("Arial", 10), foreground="white")
        lable2.place(x= 145, y= 60)

        self.textbox11 = ttk.Entry(self.root4, font=("Arial", 10))
        self.textbox11.place(x=180, y=60, width=65)

        lable3 = ttk.Label(self.root4, text="to ", background="#1c1919", font=("Arial", 10), foreground="white")
        lable3.place(x= 250, y= 60)

        self.textbox12 = ttk.Entry(self.root4, font=("Arial", 10))
        self.textbox12.place(x=270, y=60, width=55)
        
        lable_1 = ttk.Label(self.root4, text="students the subjects .", background="#1c1919", font=("Arial", 10), foreground="white")
        lable_1.place(x= 330, y= 60)

        name1 = ttk.Label(self.root4, text="Name", background="#1c1919", font=("Arial", 10), foreground="white")
        name1.place(x= 90, y= 100)

        name2 = ttk.Label(self.root4, text="Name", background="#1c1919", font=("Arial", 10), foreground="white")
        name2.place(x= 195, y= 100)

        name3 = ttk.Label(self.root4, text="Verb", background="#1c1919", font=("Arial", 10), foreground="white")
        name3.place(x= 280, y= 100)

        button = ttk.Button(self.root4, text="check", command=lambda : program.check4(self))
        button.place(x= 100 , y = 150, width=300, height=30)

        self.root4.mainloop()
    def main5(self):
        self.root5 = tk.Tk()
        self.root5.title("MadLibs")
        self.root5.iconbitmap("Madlibs.ico")
        width  = int((self.root5.winfo_screenwidth() - 700)/2)
        height = int((self.root5.winfo_screenheight()- 400)/2)
        self.root5.geometry(f"700x400+{width}+{height}")
        self.root5.resizable(False, False)
        self.root5.configure(background="#1c1919")
        
        lvl_4 = ttk.Label(self.root5, text="Level 5", background="#1c1919", font=("Arial", 10), foreground="white")
        lvl_4.place(x= 20, y= 5)

        b = ttk.Button(self.root5, text="Back", command = lambda: program.lvl5_lvl4(self))
        b.place(x=600, y=1, height=25)

        describtion = ttk.Label(self.root5, text="A vast area that many sized big circles.", background="#1c1919", font=("Arial", 15), foreground="white")
        describtion.place(x= 20, y= 25)

        self.textbox13 = ttk.Entry(self.root5, font=("Arial", 15))
        self.textbox13.place(x=20, y=60, width=60)

        lable1 = ttk.Label(self.root5, text=" has many ", background="#1c1919", font=("Arial", 15), foreground="white")
        lable1.place(x= 80, y= 60)

        self.textbox14 = ttk.Entry(self.root5, font=("Arial", 15))
        self.textbox14.place(x=180, y=60, width=60)

        lable2 = ttk.Label(self.root5, text=" that may have pepoles on it, but don't worry", background="#1c1919", font=("Arial", 15), foreground="white")
        lable2.place(x= 245, y= 60)

        self.textbox15 = ttk.Entry(self.root5, font=("Arial", 15))
        self.textbox15.place(x=20, y=120, width=60)

        lable3 = ttk.Label(self.root5, text=" will not invaid us ^_^ .", background="#1c1919", font=("Arial", 15), foreground="white")
        lable3.place(x= 80, y= 120)

        lable4 = ttk.Label(self.root5, text="So we send ", background="#1c1919", font=("Arial", 15), foreground="white")
        lable4.place(x= 20, y= 180)

        self.textbox16 = ttk.Entry(self.root5, font=("Arial", 15))
        self.textbox16.place(x=135, y=180, width=80)

        lable5 = ttk.Label(self.root5, text="to explor this area.", background="#1c1919", font=("Arial", 15), foreground="white")
        lable5.place(x= 225, y= 180)

        name1 = ttk.Label(self.root5, text="Name", background="#1c1919", font=("Arial", 10), foreground="white")
        name1.place(x= 30, y= 90)

        name2 = ttk.Label(self.root5, text="Name", background="#1c1919", font=("Arial", 10), foreground="white")
        name2.place(x= 192, y= 90)

        name3 = ttk.Label(self.root5, text="Name", background="#1c1919", font=("Arial", 10), foreground="white")
        name3.place(x= 30, y= 150)

        name4 = ttk.Label(self.root5, text="Name", background="#1c1919", font=("Arial", 10), foreground="white")
        name4.place(x= 155, y= 210)

        button = ttk.Button(self.root5, text="check", command=lambda : program.check5(self))
        button.place(x= 50 , y = 300, width=600, height=30)

        self.root5.mainloop()

m1 = program()
m1.main()