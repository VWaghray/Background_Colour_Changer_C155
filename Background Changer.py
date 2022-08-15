from tkinter import *
import random 
root = Tk()
root.geometry("400x400")
root.title("Background Colour Changer")

colours = {"colour":["red","#eb3734","orange","#eb7134","purple","#8034eb","blue","#3467eb","green","#49eb34","pink","#eb34c3","light blue","#34ebde"]}

def change():
    r = random.randint(0, 13)
    clr = colours["colour"][r]
    print(clr)
    root.configure(bg = clr)
    
    
    
btn = Button(text = "Click Me", command = change)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()
    