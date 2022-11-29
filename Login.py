from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image

root = Tk()
root.title("Log in")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False,False)

img_picture_login_page  = Image.open("picture_login_page.png")
img4 = ImageTk.PhotoImage(img_picture_login_page)
Label(root,image=img4,bg="white").place(x=100,y=80)

def signin():
    username = user.get()
    password = code.get()

    if username == "admin" and password == "1234":
        screen = Toplevel(root)
        screen.title("Hangman Game")
        screen.geometry("925x500+300+200")
        screen.config(bg="white")

        Label(screen,text="เอาเกมส์มาใส่",bg="red",font=("Calibri(Body)",50,"bold")).pack(expand=True)

        screen.mainloop()

    elif username != "admin" and password != "1234":
        messagebox.showerror("Invalid","invalid username and password")

    elif username != "admin":
        messagebox.showerror("Invalid","invalid username")

    elif password != "1234":
        messagebox.showerror("Invalid","invalid password")

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text="Log in",fg="#57a1f8",bg="white",font=("Microsoft YaHei UI Light",23,"bold"))
heading.place(x=120,y=5)

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
#----------------------------------------------------
Button(frame,width=39,pady=7,text="Log in",bg="#57a1f8",fg="white",border=0,command=signin).place(x=35,y=204)
label = Label(frame,text="Don't have any account?",fg="Black",bg="white",font=("Microsoft YaHei UI Light",11))
label.place(x=55,y=270)

sign_up = Button(frame,width=6,text="Register",border=0,bg="white",cursor="hand2",fg="#57a1f8")
sign_up.place(x=225,y=273)

root.mainloop() 