from tkinter import *
from tkinter import ttk 
from tkinter import scrolledtext
from tkinter .filedialog import *
import fileinput
from tkinter.messagebox import *

def open_():
    file=askopenfilename()
    for text in fileinput.input(file):
        txt_box.insert(0.0,text)

def save_():
    file=asksaveasfile(mode='w',defaultextension=((".txt"),(".docx")),filetypes=(("Notepad",".txt"),("Word",".Docx")))
    t=txt_box.get(0.0,END)
    file.write(t)
    file.close()

def exit_():
    if askyesno("Exit","Yes/No"):
        showinfo("Exit","Message: Yes")
        root.destroy()
    else:
        showinfo("No")

def image123_ (name):
    global img
    tabs.select(1)
    img=PhotoImage(file=name).subsample(3)
    can.create_image(10,10,image=img,anchor=NW)
    

root=Tk()
root.geometry("400x300")
root.title("Elemendid Tkinteris")

tabs=ttk.Notebook(root)
texts=["1","2","3","4","5","6","7","8"]

#for i in range(8):
#    tab=Frame(tabs)
#    tabs.add(tab,text=texts[i])

tabs=ttk.Notebook(root)
tab1=Frame(tabs)
tab2=Frame(tabs)
tab3=Frame(tabs)
tab4=Frame(tabs)
tabs.add(tab1,text="Esimene")
tabs.add(tab2,text="Teine")
tabs.add(tab3,text="Kolmas")
tabs.add(tab4,text="Neljas")

def funktion(a):
    tabs.select(a)


M=Menu(root)
root.config(menu=M)
m1=Menu(M,tearoff=1)
M.add_cascade(label="Tabs",menu=m1)
m1.add_command(label="Tab1",accelerator='Command+V',command=lambda:funktion(0))
m1.add_separator()
m1.add_command(label="Tab2",command=lambda:funktion(1))
m1.add_command(label="Tab3",command=lambda:funktion(2))
m1.add_command(label="Tab4",command=lambda:funktion(3))
m1.add_separator()

m2=Menu(M,tearoff=0)
M.add_cascade(label="Color",menu=m2)
m2.add_command(label="color1",accelerator='bg color',command=lambda:root.config(bg="yellow"))
m2.add_command(label="color2",command=lambda:root.config(bg="green"))
m2.add_command(label="color3",command=lambda:root.config(bg="red"))
m2.add_command(label="color4",command=lambda:root.config(bg="violet"))
m2.add_separator()

m3=Menu(M,tearoff=0)
M.add_cascade(label="Image",menu=m3)
m3.add_command(label="papich",command=lambda:image123_("papich.png"))
m3.add_command(label="pudge",command=lambda:image123_("pudge.png"))
m3.add_command(label="tinker",command=lambda:image123_("tinker.png"))
m3.add_command(label="x",command=lambda:image123_("x.png"))
m3.add_separator()

btn_open=Button(tab1,text="Open",command=open_)
btn_save=Button(tab1,text="Save",command=save_)
btn_exit=Button(tab1,text="Exit",command=exit_)
txt_box=scrolledtext.ScrolledText(tab1,width=49,height=5)
txt_box.grid(row=0,column=0,columnspan=3)
btn_open.grid(row=1,column=0)
btn_save.grid(row=1,column=1)
btn_exit.grid(row=1,column=2)

can=Canvas(tab2,width=300,height=200,)
can.pack()
tabs.pack(fill="both")
tabs.pack()
root.mainloop()


