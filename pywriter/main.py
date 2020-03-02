from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os




def new():
    global file
    root.title("Untitled - PyNotepad")
    file=None
    textRegion.delete(1.0, END)


def Open():
    global file
    file=askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*" ),("Text Documents", "*.txt")])

    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"- PyNotepad")
        textRegion.delete(1.0,END)
        f= open(file,"r")
        textRegion.insert(1.0,f.read())
        f.close()


def save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
        if file=="":
            file=None
        else:
            f = open(file, "w")
            f.write(textRegion.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
    else:
        # Save the file
        f = open(file, "w")
        f.write(textRegion.get(1.0, END))
        f.close()


def Quit():
    root.quit()


def cut():
    textRegion.event_generate("<<cut>>")


def copy():
    textRegion.event_generate("<<copy>>")


def paste():
    textRegion.event_generate("<<paste>>")


def about():
    tl=Toplevel(root)
    tl.title("About")
    abouthc= "Notepad By:\nShreyas HC\nshreyashc018@gmail.com\n\n\nUsing: Python3\nPackage used:Tkinter + os"
    Label(tl,text=abouthc,width=35,height=15,bg="#FF5733").pack()




root = Tk()
root.title("Untitled - PyNotepad")
root.geometry("650x450")


textRegion = Text(root, font = "Verdana 12")
file = None
textRegion.pack(fill=BOTH, expand = TRUE,)

menubar = Menu(root)

fileM = Menu(menubar, tearoff = 0)
fileM.add_command(label="New  ",command=new)
fileM.add_command(label="Open  ",command=Open)
fileM.add_command(label="save  ",command=save)
fileM.add_command(label="Quit  ",command=Quit)

menubar.add_cascade(label="File ",menu=fileM)

editM = Menu(menubar,tearoff = 0)
editM.add_command(label = "Copy   (ctrl+c)", command=copy)
editM.add_command(label = "Cut     (ctrl+x)", command=cut)

editM.add_command(label = "Paste  (ctrl+v)", command=paste)

menubar.add_cascade(label="Edit",menu=editM)

HelpM = Menu(menubar, tearoff=0)
HelpM.add_command(label = "About Py Notepad", command=about)
menubar.add_cascade(label="Help", menu=HelpM)


root.config(menu=menubar)

scrollbary = Scrollbar(textRegion)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbary.config(command=textRegion.yview)
textRegion.config(yscrollcommand=scrollbary.set)


# scrollbarx = Scrollbar(textRegion)
# scrollbarx.pack(side=BOTTOM,fill=X)
# scrollbarx.config(command=textRegion.xview)
# textRegion.config(xscrollcommand=scrollbary.set)

root.mainloop()
