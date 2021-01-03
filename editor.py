from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
from subprocess import call



def newFile():
    global file
    editor_root.title("Untitled - Text-Editor")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        editor_root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file is None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            # Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            editor_root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    editor_root.destroy()


def cut():
    TextArea.event_generate("<>")


def copy():
    TextArea.event_generate("<>")


def paste():
    TextArea.event_generate("<>")


def about():
    showinfo("Text-Editor", "Text-Editor is Created by Rakesh Yadav & contact me at "
                            "'https://github.com/Er-Rakesh-Yadav'")


def themes():
    showinfo("Themes", "Hye!! Theme section is under-development")


if __name__ == '__main__':
    # Basic tkinter setup
    editor_root = Tk()
    editor_root.title("Untitled - Text-Editor")
    editor_root.wm_iconbitmap("icon1.png")
    editor_root.geometry("640x500")
    editor_root.minsize(400, 30)

    # Add TextArea
    bg_color = "#ccc"
    fg_color = "black"
    TextArea = Text(editor_root, bg=bg_color, fg=fg_color, font="lucida 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    # Lets create a menubar
    MenuBar = Menu(editor_root)

    # File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)
    # To open new file
    FileMenu.add_command(label="New", command=newFile)
    # To Open already existing file
    FileMenu.add_command(label="Open", command=openFile)

    # To save the current file

    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)
    MenuBar.add_cascade(label="File", menu=FileMenu)
    # File Menu ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    # To give a feature of cut, copy and paste
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)

    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    # Edit Menu Ends

    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About Notepad", command=about)
    HelpMenu.add_command(label="Theme", command=themes)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    # Help Menu Ends

    editor_root.config(menu=MenuBar)

    # Adding Scrollbar using rules from Tkinter lecture no 22
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    #editor_root.mainloop()
    editor_root.mainloop()



    class CallPy(object):
        def __init__(self,path='./speech.py'):
            self.path = path

        def call_python_file(self):
            call(["puu","{}".format(self.path)])


if __name__ == "__main__":
    c = CallPy()
    c.call_python_file()




