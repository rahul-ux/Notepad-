from tkinter import*
import os
import sys


from tkinter.filedialog import askopenfilename,asksaveasfile




root = Tk()
root.geometry("1000x600")
root.minsize(1000,600)
#root.maxsize({(screenwidth)x(screenheight)})

root.title("Smart NotePad 1.0")
root.wm_iconbitmap("10.ico")

file = None



"--------------------------------------------------------------------------------------"


"==========================Function======================Area========================="


def new():
	global file
	root.title("Untitled - Smart Notepad 1.0")
	file = None
	textarea.delete(1.0,END)













def openfile():
	global file
	file = askopenfilename(defaultextension=".txt",
		filetypes=[("All Files","*.*"),("TextDocument","*.txt")])

	if file == "":
		file = None


	else:
		root.title(os.path.basename(file) + " -Smart Notepad 1.0")
		textarea.delete(1.0,END)
		f = open(file,"r")
		textarea.insert(1.0,f.read())

		f.close()
	


def save():
	global file
	if file == None:
		file = asksaveasfile(initialfile = "Untitled.txt",defaultextension=".txt",
		filetypes=[("All Files","*.*"),("TextDocument","*.txt")])
		if file == "":
			file = None
		else:
			#save as new file
			f = open(file,"a")
			f.write(textarea.get(1.0,"end"))
			f.colse()


			root.title(os.path.basename(file) + " -Smart Notepad 1.0")

	else:
		f = open(file,"w")
		f.write(textarea.get(1.0,"end"))
		f.close()



def save_as():
	global file
	if file == None:
		file = asksaveasfile(initialfile = "Untitled.txt",defaultextension=".txt",
		filetypes=[("All Files","*.*"),("TextDocument","*.txt")])
		if file == "":
			file = None
		else:
			#save as new file
			f = open(file,"w")
			f.write(textarea.get(1.0,"end"))
			f.colse()


			root.title(os.path.basename(file) + "-Smart Notepad 1.0")

	else:
		f = open(file,"w")
		f.write(textarea.get(1.0,"end"))
		f.colse()


def exit(event):
	sys.exit()


def cut(event):
	textarea.event_generate("<<Cut>>")

def paste(event):
	textarea.event_generate("<<Paste>>")


def copy(event):
	textarea.event_generate("<<Copy>>")




def find(event):
	pass


def delete(event):
	textarea.delete(1.0,END)
	return "break"




def select_all(event=None):
	textarea.tag_add('sel','1.0',END)
	return "break"



"===========================================Preference======================================="


def preference():
	from tkinter import Tk

	root = Tk()

	root.title("Preference")
	root.wm_iconbitmap("19.ico")
	root.geometry("600x400")























	root.mainloop()

def display(event):
	from tkinter import Tk

	root = Tk()

	root.title("Display")
	root.wm_iconbitmap("13.ico")
	root.geometry("600x400")























	root.mainloop()

	

def font(event):
	pass

def new_window(event):
	pass 


def bg(event):
	from tkinter import Tk

	root = Tk()

	root.title("Preference")
	root.wm_iconbitmap("12.ico")
	root.geometry("600x400")
























	root.mainloop()


def fullscreen(event):
	screenwidth = 1600
	screenheight = 1600
	

def about(event):
	from tkinter import Tk

	root = Tk()

	root.title("About")
	root.wm_iconbitmap("12.ico")
	root.geometry("600x400")























	root.mainloop()


def contact(event):
	from tkinter import Tk

	root = Tk()

	root.title("Contact Us")
	root.wm_iconbitmap("11.ico")
	root.geometry("600x400")























	root.mainloop()




def help(event):
	from tkinter import Tk

	root = Tk()

	root.title("Help")
	root.wm_iconbitmap("21.ico")
	root.geometry("600x400")























	root.mainloop()


def search(event):
	from tkinter import Tk

	root = Tk()

	root.title("Search")
	root.wm_iconbitmap("22.ico")
	root.geometry("600x400")























	root.mainloop()






























"=============================Text ============================Area====================="

textarea = Text(root,font="lucida 16 italic",relief="ridge",bd="8",bg="#B4B4FF",wrap=None)
textarea.pack(fill=BOTH,expand=True)

file = None






"===============================Scroll bars=========================================="



Scroll = Scrollbar(textarea,width=14,orient=VERTICAL)
Scroll.pack(side=RIGHT,fill=Y)
Scroll.config(command = textarea.yview)
textarea.configure(yscrollcommand = Scroll.set)



Scroll1 = Scrollbar(textarea,orient=HORIZONTAL,width=14,wrap=None)
Scroll1.pack(side=BOTTOM,fill=X)
Scroll1.config(command = textarea.xview)
textarea.configure(xscrollcommand = Scroll1.set)













"----------------------------------------------------------------------------------------------"


MainMenu = Menu(root)
menu1 = Menu(MainMenu,tearoff=0)

menu1.add_command(label="New",command=new,accelerator="Ctrl+N",underline=7)
menu1.add_command(label="New Window",command=new,accelerator="Ctrl+N",underline=7)
menu1.add_command(label="Open",command=openfile,accelerator="Ctrl+O",underline=7)
menu1.add_command(label="Save",command=save,accelerator="Ctrl+S",underline=7)
menu1.add_command(label="Save As",command=save_as,accelerator="Ctrl+S",underline=7)
menu1.add_separator()
menu1.add_command(label="Page Setup",command=quit)
menu1.add_command(label="Print",command=quit)
menu1.add_separator()
menu1.add_command(label="Exit",command=quit,accelerator="Ctrl+E",underline=7)


root.config(menu = MainMenu)
MainMenu.add_cascade(label="File",menu=menu1)


"========================================================================"

menu2 = Menu(MainMenu,tearoff=0)

menu2.add_command(label="Cut",command=cut,accelerator="Ctrl+X",underline=7)
menu2.add_command(label="Copy",command=copy,accelerator="Ctrl+C",underline=7)
menu2.add_command(label="Paste",command=paste,accelerator="Ctrl+V",underline=7)
menu2.add_command(label="Select All",command=select_all,accelerator="Ctrl+A",underline=7)
menu2.add_command(label="Undo",command=open,accelerator="Ctrl+U",underline=7)
menu2.add_separator()
menu2.add_command(label="Delete",command=delete,accelerator="Ctrl+D",underline=7)
menu2.add_command(label="Print",command=open)
menu2.add_separator()
menu2.add_command(label="Find",command=quit,accelerator="Ctrl+F",underline=7)


root.config(menu = MainMenu)
MainMenu.add_cascade(label="Edit",menu=menu2)

"================================================================================="

# edit menu


#Format Menu

menu3 = Menu(MainMenu,tearoff=0)

menu3.add_command(label="Preference",command=preference,accelerator="Ctrl+P",underline=7)
menu3.add_command(label="Display",command=display)
menu3.add_command(label="Font",command=font)
menu3.add_command(label="Font Size",command=font)
menu3.add_command(label="Background Color",command=bg)
menu3.add_separator()
menu3.add_command(label="Full Screen",command=fullscreen,accelerator="Ctrl+Z",underline=7)
menu3.add_command(label="Exit Full Screen",command=quit)
menu3.add_separator()
menu3.add_command(label="Search",command=search)
menu3.add_command(label="Zoom In",command=open)
menu3.add_command(label="Zoom Out",command=open)
menu3.add_command(label="Bold Text",command=open)



root.config(menu = MainMenu)
MainMenu.add_cascade(label="Settings",menu=menu3)


"====================================================================================="


menu4 = Menu(MainMenu,tearoff=0)

menu4.add_command(label="About",command=about)
menu4.add_command(label="Privacy Polcies",command=open)
menu4.add_command(label="Help",command=help)
menu4.add_command(label="Help On Web",command=help)
menu4.add_separator()
menu4.add_command(label="Version",command=open)
menu4.add_separator()
menu4.add_command(label="About Software",command=open)
menu4.add_command(label="Devloper Contact",command=contact)
menu4.add_separator()
menu4.add_command(label="Social",command=quit)


root.config(menu = MainMenu)
MainMenu.add_cascade(label="Help",menu=menu4)





"==================================KEY=================BINDING====================="
def keybinding():
	textarea.bind("<Control-A>",select_all)
	textarea.bind("<Control-a>",select_all)
	textarea.bind("<Control-N>",new)
	textarea.bind("<Control-n>",new)
	textarea.bind("<Control-O>",openfile)
	textarea.bind("<Control-o>",openfile)

	textarea.bind("<Control-S>",save)
	textarea.bind("<Control-s>",save)

	textarea.bind("<Control-H>",help)
	textarea.bind("<Control-h>",help)

	textarea.bind("<Control-E>",exit)
	textarea.bind("<Control-e>",exit)

	textarea.bind("<Control-Z>",fullscreen)
	textarea.bind("<Control-z>",fullscreen)

	textarea.bind("<Control-P>",preference)
	textarea.bind("<Control-p>",preference)

	textarea.bind("<Control-X>",cut)
	textarea.bind("<Control-x>",cut)

	textarea.bind("<Control-C>",copy)
	textarea.bind("<Control-c>",copy)
	textarea.bind("<Control-V>",paste)
	textarea.bind("<Control-V>",paste)
	textarea.bind("<Control-D>",delete)
	textarea.bind("<Control-d>",delete)

keybinding()








root.mainloop()