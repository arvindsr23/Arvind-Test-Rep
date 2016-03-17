import random
import tkinter
from tkinter import *
theAnswers = ['It will happen','It is quite possible', 'It will probably go through', 'It looks very likely', 'The outlook is good', 'It probably will not happen', 'It does not seem likely','It is extremely remote', 'I wouldn''t hedge on it', 'The outlook is not good']
def checkstr(qs,i):
	if i in range(len(theAnswers)):
		return qs+" "+theAnswers[i]
	else:
		return qs+" "+"Out of Range"

def btnprs(a):
	messagebox.showinfo("Your Answer",a)
    	
def magicball():
    top=tkinter.Tk()
    lab=Label(top,text="Enter your wonder here: ")
    lab.pack(side=LEFT)
    inp_txt=Entry(top,bd=5)
    inp_txt.pack(side=RIGHT)
    ans_button=Button(top,text="Magicball",command= lambda: btnprs(checkstr(inp_txt.get(),random.randrange(0,10,1))))
    ans_button.pack(side=BOTTOM)
    top.mainloop()












	

	
	
