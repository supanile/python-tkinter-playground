from tkinter import *

root = Tk()
root.title("โปรแกรมของฉัน")

# ใช้ PhotoImage สำหรับไฟล์ PNG
icon = PhotoImage(file="icons/healthcare.png")
root.iconphoto(False, icon)

root.geometry("300x300+500+200")
root.resizable(0,0)
root.config(bg="pink")

root.mainloop()