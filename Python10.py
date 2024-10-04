from tkinter import *
from tkinter.filedialog import *
#สร้างหน้าจอ
root = Tk() 
#ตั้งค่าหน้าจอ
root.title("โปรแกรมของฉัน")
icon = PhotoImage(file="icons/healthcare.png")
root.iconphoto(False, icon)
root.geometry("300x300+500+200")
root.resizable(0,0)

def selectFile():
    myFile=askopenfilename(title="เปิดไฟล์",initialdir="./",filetypes=(("Text Files","*.txt"),("All Files","*")))
    
    with open(myFile,"r",encoding="utf8") as f:
        Label(root,text=f.read()).pack()

btn1=Button(root,text="เลือกไฟล์",command=selectFile).pack()

root.mainloop()