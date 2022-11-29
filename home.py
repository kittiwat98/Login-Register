from tkinter import*
from tkinter import messagebox
import ast


dict_animals = {
    "word": ["cat", "dog", "fish", "bird", "elephant", "monkey", "turtle", "panda", "tiger", "kingkong", "pidbull", "shark", "eagle", "dongkey"],
    "hint": ["love fish, 4 leg", "love bone, 4 leg", "live in water", "flying", "big body have tusks", "love banana", "slow, can swim", "love bamboo",
             "eat meat, like lion", "monkey name movie", "species dog", "in water, have fin", "king on sky", "like horse"]
}
lvl = 0
Hearts = 5
Scores = 1000
Scores_total = 0
Wrong = 5
words = dict_animals["word"][lvl]
hints = dict_animals["hint"][lvl]
words = words.upper()
digit = ""

list_word = []  # อักษรที่เราเคยใส่ไปแล้ว
list_ans = []  # อักษรที่พิมพ์ถูก หรือ ตรงกับคำถาม
list_queation = []  # ตัวอักษรในคำถาม
list_showWord = []  # โชตัวอักษรที่กดแล้วมีในคำ
list_showCorrectWord = []  # ตัวอักษรทั้งหมดในคำถาม(รวมตัวซ้ำ)


home = Tk()
home.geometry("1280x720+150+0")
home.title("home")
home.resizable(False, False)

#######################LOG IN#########################################


def click_sigin():
    root = Toplevel(home)
    root.title("Log in")
    root.geometry("925x500+300+200")
    root.configure(bg="#fff")
    root.resizable(False, False)

    img4 = PhotoImage(file="picture_login_page.png")
    Label(root, image=img4, bg="white").place(x=100, y=80)

    def signin():
        global select
        username = user.get()
        password = code.get()

        file = open("datasheet.txt", "r")
        d = file.read()
        r = ast.literal_eval(d)
        file.close()

        # print(r.keys())
        # print(r.values())

        if username in r.keys() and password == r[username]:
            def nextStage():  # ไปเลเวลถัดไปเมื่อผ่านด่าน
                global Hearts
                global Scores
                global Wrong
                global words
                global list_word
                global list_ans
                global list_queation
                global list_showWord
                global list_showCorrectWord
                global emptylabel
                global digit
                global hints
                global lvl
                global my_canvas
                global hmm
                global h1, h2, h3, h4, h5

                words = dict_animals["word"][lvl]
                words = words.upper()
                hints = dict_animals["hint"][lvl]
                list_word.clear()
                list_ans.clear()
                list_queation.clear()
                list_showWord.clear()
                list_showCorrectWord.clear()
                for i in words:  # เอาตัวอักษรคำถามเก็บไว้ใน list_queation
                    if(i not in list_queation):
                        list_queation.append(i)
                        list_queation.sort()

                for i in words:
                    list_showCorrectWord.append(i)

                for i in range(len(words)):
                    list_showWord.append(" _ ")

            def select(user_ans):
                global Hearts
                global Scores
                global Wrong
                global words
                global hints
                global list_word
                global list_ans
                global list_queation
                global Scores_total
                global lvl
                global my_canvas
                global hearts, scores, level, categoty, hint
                global screen
                global han
                global hmm
                global h1, h2, h3, h4, h5

                global digit
                digit = user_ans

                print(list_queation)
                print(list_ans)
                print(list_word)
                print(user_ans)

                if(user_ans not in list_word):
                    if(user_ans in words):  # ถ้ามีตัวอักษรตรงกับคำถามเก็บไว้ใน list_ans
                        print("have word")
                        list_ans.append(user_ans)
                        list_ans.sort()
                        print(f"ans: {list_ans}")
                        showCorrectSelect()
                    else:
                        print("not have")
                        Wrong -= 1
                        Scores = Scores*87/100
                        if(Wrong == 0):
                            Hearts -= 1
                            Wrong = 5
                            print("You die!")
                            my_canvas.itemconfig(hmm, image=h1)
                        print(f"Hearts: {Hearts}, Wrong: {Wrong}")

                        h2 = PhotoImage(file=f"h2.png")
                        h3 = PhotoImage(file=f"h3.png")
                        h4 = PhotoImage(file=f"h4.png")
                        h5 = PhotoImage(file=f"h5.png")
                        if Wrong == 4:
                            my_canvas.itemconfig(hmm, image=h2)
                        elif Wrong == 3:
                            my_canvas.itemconfig(hmm, image=h3)
                        elif Wrong == 2:
                            my_canvas.itemconfig(hmm, image=h4)
                        elif Wrong == 1:
                            my_canvas.itemconfig(hmm, image=h5)
                        list_word.append(user_ans)  # เก็ยตัวอักษรที่เคยตอบ
                else:
                    print("You enter the word already")

                if(list_ans == list_queation):  # เช็คว่าคำถามถูกต้องมั้ยกรอกครบทุกตัวรึยัง
                    Scores_total = Scores_total + Scores
                    lvl += 1
                    print(f"Win! Your score: {Scores_total:.0f}")
                    nextStage()
                    emptylabel.config(text=f"{list_showWord}")

                #hearts, scores, level, categoty, hint
                my_canvas.itemconfig(hearts, text="Hearts: "+str(Hearts))
                my_canvas.itemconfig(scores, text="Scores: "+str(Scores_total))
                my_canvas.itemconfig(level, text="Level: "+str(lvl))
                my_canvas.itemconfig(categoty, text="Categoty: "+str("Animal"))
                my_canvas.itemconfig(hint, text="Hint: "+str(hints))

            def showCorrectSelect():
                global Hearts
                global Scores
                global Wrong
                global words
                global list_word
                global list_ans
                global list_queation
                global list_showWord
                global list_showCorrectWord
                global emptylabel
                global digit
                print(digit)

                # loopเช็คว่าถูกมั้ยถ้าถูกก็ขึ้นตัวอักษร
                for i in range(len(list_showCorrectWord)):
                    if(list_showCorrectWord[i] == digit):
                        list_showWord[i] = " " + digit + " "
                        emptylabel.config(text=f"{list_showWord}")

                return list_showWord

            
            def display():
                global Hearts
                global Scores
                global Wrong
                global words
                global list_word
                global list_ans
                global list_queation
                global list_showWord
                global list_showCorrectWord
                global emptylabel
                global hearts, scores, level, categoty, hint
                global my_canvas
                global screen
                global hmm
                global h1, h2, h3, h4, h5

                nextStage()
                screen = Toplevel(root)
                screen.title("HANGMAN")
                screen.geometry("1280x720")
                screen.option_add("font", "consolas 30")
                #-------------------background-------------------------#
                bg = PhotoImage(file="bggameplay.png")
                my_canvas = Canvas(screen, width=1280, height=720)
                my_canvas.pack(fill="both", expand=True)
                my_canvas.create_image(0, 0, image=bg, anchor="nw")
            #---------------------Left menu----------------------------#
                hearts = my_canvas.create_text(
                    100, 50, text="Hearts:" + str(Hearts), font=("Bitter", 23))
                scores = my_canvas.create_text(
                    100, 100, text="Scores: "+str(Scores_total), font=("Bitter", 23))
                level = my_canvas.create_text(
                    90, 150, text="Level: " + str(lvl), font=("Bitter", 23))
            #---------------------Right menu----------------------------#
                categoty = my_canvas.create_text(
                    600, 50, text="CATEGORY:", font=("Bitter", 23))
                hint = my_canvas.create_text(
                    1000, 50, text="Hint: " + hints, font=("Bitter", 23))

                hamgurber_icon = PhotoImage(file="Hamburger_icon.png")
                hamgurber_btn = Button(
                    screen, image=hamgurber_icon, bg="#9cceeb", bd=0)
                hamgurber = my_canvas.create_window(
                    1230, 30, anchor="nw", window=hamgurber_btn)
            ##############################################################################
                Label(screen, height=2, text=list_showWord, bd=0, font=(
                    'Arial', 20), bg="#dbe8dd", fg="green").place(x=740, y=250)
                emptylabel = Label(screen, height=2, fg="green", font=(
                    'Arial', 20), bg="#dbe8dd")  # หน้าต่างแสดงผลเมื่อแปลงค่า
                emptylabel.place(x=740, y=250)

                ##------------------------Button---------------------------------##
                al = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                for let in al:
                    exec('{}=PhotoImage(file="{}.png")'.format(let, let))

                button = [['b1', 'A', 600, 360], ['b2', 'B', 690, 360], ['b3', 'C', 780, 360], ['b4', 'D', 870, 360], ['b5', 'E', 960, 360], ['b6', 'F', 1050, 360], ['b7', 'G', 1140, 360],
                          ['b8', 'H', 600, 440], ['b9', 'I', 690, 440], ['b10', 'J', 780, 440], ['b11', 'K', 870, 440], [
                              'b12', 'L', 960, 440], ['b13', 'M', 1050, 440], ['b14', 'N', 1140, 440],
                          ['b15', 'O', 600, 520], ['b16', 'P', 690, 520], ['b17', 'Q', 780, 520], ['b18', 'R', 870, 520], [
                    'b19', 'S', 960, 520], ['b20', 'T', 1050, 520], ['b21', 'U', 1140, 520],
                    ['b22', 'V', 690, 600], ['b23', 'W', 780, 600], ['b24', 'X', 870, 600], ['b25', 'Y', 960, 600], ['b26', 'Z', 1050, 600]]
                # letters placement
                for q1 in button:
                    exec('{}=Button(screen,bd=0,command=lambda:select("{}"),font=10,image={},borderwidth=0)'.format(q1[0], q1[1],q1[1]))
                    exec('{}.place(x={},y={})'.format(q1[0], q1[2], q1[3]))

                # hangman images
                h1 = PhotoImage(file=f"h1.png")
                hmm = my_canvas.create_image(260, 450, image=h1)

                my_canvas.update

                screen.mainloop()

            def main():
                global my_canvas

                for i in words:  # เอาตัวอักษรคำถามเก็บไว้ใน list_queation
                    if(i not in list_queation):
                        list_queation.append(i)
                        list_queation.sort()

                display()
            main()
            screen.mainloop()

        else:
            messagebox.showerror("Invalid", "invalid username and password")
    ########################################################################

    def signup_command():
        window = Toplevel(root)
        window.title("Register")
        window.geometry("925x500+300+200")
        window.configure(bg="#fff")
        window.resizable(False, False)

        img4 = PhotoImage(file="picture_register_page.png")
        Label(window, image=img4, bg="white").place(x=50, y=120)

        def signup():
            username = user.get()
            password = code.get()
            confirm_password = confirm.get()

            if password == confirm_password:
                try:
                    file = open('datasheet.txt', 'r+')
                    d = file.read()
                    r = ast.literal_eval(d)

                    dict2 = {username: password}
                    r.update(dict2)
                    file.truncate(0)
                    file.close()

                    file = open('datasheet.txt', 'w')
                    w = file.write(str(r))

                    messagebox.showinfo("Register", "Sucessfully register")
                    window.destroy()

                except:
                    file = open('datasheet.txt', 'w')
                    pp = str({'Username': 'password'})
                    file.write(pp)
                    file.close()

            else:
                messagebox.showerror("Invalid", "Both Password should match")

        def sign():
            window.destroy()

        frame = Frame(window, width=350, height=400, bg="white")
        frame.place(x=480, y=40)

        heading = Label(frame, text="Register", fg="#57a1f8", bg="white", font=(
            "Microsoft YaHei UI Light", 23, "bold"))
        heading.place(x=115, y=5)

        # ----------------USERNAME--------------------------
        def on_enter(e):
            user.delete(0, "end")

        def on_leave(e):
            name = user.get()
            if name == "":
                user.insert(0, "Username")

        user = Entry(frame, width=35, fg="Black", border=0,
                     bg="white", font=("Microsoft YaHei UI Light", 11))
        user.place(x=30, y=80)
        user.insert(0, "Username")
        user.bind("<FocusIn>", on_enter)
        user.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg="Black").place(x=25, y=107)
        # -----------------PASSWORD--------------------------

        def on_enter(e):
            code.delete(0, "end")

        def on_leave(e):
            name = code.get()
            if name == "":
                code.insert(0, "Password")

        code = Entry(frame, width=35, fg="Black", border=0,
                     bg="white", font=("Microsoft YaHei UI Light", 11))
        code.place(x=30, y=150)
        code.insert(0, "Password")
        code.bind("<FocusIn>", on_enter)
        code.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg="Black").place(x=25, y=177)
        # -----------------CONFIRM--------------------------

        def on_enter(e):
            confirm.delete(0, "end")

        def on_leave(e):
            name = confirm.get()
            if name == "":
                confirm.insert(0, "Confirm Password")

        confirm = Entry(frame, width=35, fg="Black", border=0,
                        bg="white", font=("Microsoft YaHei UI Light", 11))
        confirm.place(x=30, y=220)
        confirm.insert(0, "Confirm Password")
        confirm.bind("<FocusIn>", on_enter)
        confirm.bind("<FocusOut>", on_leave)

        Frame(frame, width=295, height=2, bg="Black").place(x=25, y=247)
        # ----------------------------------------------------
        Button(frame, width=39, pady=7, text="Register", bg="#57a1f8",
               fg="white", border=0, command=signup).place(x=35, y=280)
        label = Label(frame, text="I have an account", fg="black",
                      bg="white", font=("Microsoft YaHei UI Light", 11))
        label.place(x=70, y=340)

        sign_in = Button(frame, width=6, text="Log in",
                         border=0, bg="white", fg="blue", command=sign)
        sign_in.place(x=200, y=343)

        window.mainloop()
    ########################################################################
    frame = Frame(root, width=350, height=350, bg="white")
    frame.place(x=480, y=70)

    heading = Label(frame, text="Log in", fg="#57a1f8", bg="white",
                    font=("Microsoft YaHei UI Light", 23, "bold"))
    heading.place(x=120, y=5)

    # ----------------USERNAME--------------------------
    def on_enter(e):
        user.delete(0, "end")

    def on_leave(e):
        name = user.get()
        if name == "":
            user.insert(0, "Username")

    user = Entry(frame, width=35, fg="Black", border=0,
                 bg="white", font=("Microsoft YaHei UI Light", 11))
    user.place(x=30, y=80)
    user.insert(0, "Username")
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg="Black").place(x=25, y=107)

    # -----------------PASSWORD--------------------------
    def on_enter(e):
        code.delete(0, "end")

    def on_leave(e):
        name = code.get()
        if name == "":
            code.insert(0, "Password")

    code = Entry(frame, width=35, fg="Black", border=0,
                 bg="white", font=("Microsoft YaHei UI Light", 11))
    code.place(x=30, y=150)
    code.insert(0, "Password")
    code.bind("<FocusIn>", on_enter)
    code.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg="Black").place(x=25, y=177)
    # ----------------------------------------------------
    Button(frame, width=39, pady=7, text="Log in", bg="#57a1f8",
           fg="white", border=0, command=signin).place(x=35, y=204)
    label = Label(frame, text="Don't have any account?", fg="Black",
                  bg="white", font=("Microsoft YaHei UI Light", 11))
    label.place(x=55, y=270)

    sign_up = Button(frame, width=6, text="Register", border=0,
                     bg="white", cursor="hand2", fg="#57a1f8", command=signup_command)
    sign_up.place(x=225, y=273)

    root.mainloop()
#######################END LOG IN#########################################
# @@@@@@@@@@@@@@@@@@@@@@@@@@ REGISTER @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


def click_signup():
    window = Toplevel(home)
    window.title("Register")
    window.geometry("925x500+300+200")
    window.configure(bg="#fff")
    window.resizable(False, False)

    img4 = PhotoImage(file="picture_register_page.png")
    Label(window, image=img4, bg="white").place(x=50, y=120)

    def signup():
        username = user.get()
        password = code.get()
        confirm_password = confirm.get()

        if password == confirm_password:
            try:
                file = open('datasheet.txt', 'r+')
                d = file.read()
                r = ast.literal_eval(d)

                dict2 = {username: password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file = open('datasheet.txt', 'w')
                w = file.write(str(r))

                messagebox.showinfo("Register", "Sucessfully register")

            except:
                file = open('datasheet.txt', 'w')
                pp = str({'Username': 'password'})
                file.write(pp)
                file.close()

        else:
            messagebox.showerror("Invalid", "Both Password should match")

    def sign():
        window.destroy()

    #img = PhotoImage(file="Home.png")
    # Label(window,image=img,bg="white").place(x=0,y=0)

    frame = Frame(window, width=350, height=400, bg="white")
    frame.place(x=480, y=40)

    heading = Label(frame, text="Register", fg="#57a1f8",
                    bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
    heading.place(x=115, y=5)

    # ----------------USERNAME--------------------------
    def on_enter(e):
        user.delete(0, "end")

    def on_leave(e):
        name = user.get()
        if name == "":
            user.insert(0, "Username")

    user = Entry(frame, width=35, fg="Black", border=0,
                 bg="white", font=("Microsoft YaHei UI Light", 11))
    user.place(x=30, y=80)
    user.insert(0, "Username")
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg="Black").place(x=25, y=107)
    # -----------------PASSWORD--------------------------

    def on_enter(e):
        code.delete(0, "end")

    def on_leave(e):
        name = code.get()
        if name == "":
            code.insert(0, "Password")

    code = Entry(frame, width=35, fg="Black", border=0,
                 bg="white", font=("Microsoft YaHei UI Light", 11))
    code.place(x=30, y=150)
    code.insert(0, "Password")
    code.bind("<FocusIn>", on_enter)
    code.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg="Black").place(x=25, y=177)
    # -----------------CONFIRM--------------------------

    def on_enter(e):
        confirm.delete(0, "end")

    def on_leave(e):
        name = confirm.get()
        if name == "":
            confirm.insert(0, "Confirm Password")

    confirm = Entry(frame, width=35, fg="Black", border=0,
                    bg="white", font=("Microsoft YaHei UI Light", 11))
    confirm.place(x=30, y=220)
    confirm.insert(0, "Confirm Password")
    confirm.bind("<FocusIn>", on_enter)
    confirm.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg="Black").place(x=25, y=247)
    # ----------------------------------------------------
    Button(frame, width=39, pady=7, text="Register", bg="#57a1f8",
           fg="white", border=0, command=signup).place(x=35, y=280)
    label = Label(frame, text="I have an account", fg="black",
                  bg="white", font=("Microsoft YaHei UI Light", 11))
    label.place(x=70, y=340)

    sign_in = Button(frame, width=6, text="Home", border=0,
                     bg="white", fg="blue", command=sign)
    sign_in.place(x=200, y=343)

    window.mainloop()
# @@@@@@@@@@@@@@@@@@@@@@@@@@ END REGISTER @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# background


img = PhotoImage(file="BG.png")
bg = Label(home, image=img)
bg.place(x=0, y=0)

# login button Image

img2 = PhotoImage(file="login_button.png")

# register button Image

img3 = PhotoImage(file="register_button.png")

button_login = Button(home, image=img2, command=click_sigin, borderwidth=0)
button_login.place(x=300, y=250)

button_register = Button(home, image=img3, command=click_signup, borderwidth=0)
button_register.place(x=300, y=380)


home.mainloop()
