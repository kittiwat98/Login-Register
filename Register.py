from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image
import ast

window = Tk()
window.title("Register")
window.geometry("925x500+300+200")
window.configure(bg="#fff")
window.resizable(False,False)

img_picture_login_page  = Image.open("picture_register_page.png")
img4 = ImageTk.PhotoImage(img_picture_login_page)
Label(window,image=img4,bg="white").place(x=50,y=120)

def signup():
    username = user.get()
    password = code.get()
    confirm_password = confirm.get()

    if password == confirm_password:
        try:
            file = open('datasheet.txt','r+')
            d = file.read()
            r = ast.literal_eval(d)

            dict2 = {username:password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file=open('datasheet.txt','w')
            w = file.write(str(r))

            messagebox.showinfo("Register","Sucessfully register")
        
        except:
            file = open('datasheet.txt','w')
            pp = str({'Username':'password'})
            file.write(pp)
            file.close()

    else:
        messagebox.showerror("Invalid","Both Password should match")



#img = PhotoImage(file="Home.png")
#Label(window,image=img,bg="white").place(x=0,y=0)

frame=Frame(window,width=350,height=400,bg="white")
frame.place(x=480,y=40)

heading = Label(frame,text="Register",fg="#57a1f8",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
heading.place(x=115,y=5)

#----------------USERNAME--------------------------
def on_enter(e):
    user.delete(0,"end")

def on_leave(e):
    name = user.get()
    if name =="":
        user.insert(0,"Username")

user = Entry(frame,width=35,fg="Black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
user.place(x=30,y=80)
user.insert(0,"Username")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg="Black").place(x=25,y=107)
#-----------------PASSWORD--------------------------
def on_enter(e):
    code.delete(0,"end")

def on_leave(e):
    name = code.get()
    if name =="":
        code.insert(0,"Password")

code = Entry(frame,width=35,fg="Black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
code.place(x=30,y=150)
code.insert(0,"Password")
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg="Black").place(x=25,y=177)
#-----------------CONFIRM--------------------------
def on_enter(e):
    confirm.delete(0,"end")

def on_leave(e):
    name = confirm.get()
    if name =="":
        confirm.insert(0,"Confirm Password")

confirm = Entry(frame,width=35,fg="Black",border=0,bg="white",font=("Microsoft YaHei UI Light",11))
confirm.place(x=30,y=220)
confirm.insert(0,"Confirm Password")
confirm.bind("<FocusIn>", on_enter)
confirm.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg="Black").place(x=25,y=247)
#----------------------------------------------------
Button(frame,width=39,pady=7,text="Register",bg="#57a1f8",fg="white",border=0,command=signup).place(x=35,y=280)
label = Label(frame,text="I have an account",fg="black",bg="white",font=("Microsoft YaHei UI Light",11))
label.place(x=70,y=340)

sign_in = Button(frame,width=6,text="Log in",border=0,bg="white",fg="blue")
sign_in.place(x=200,y=343)

window.mainloop()