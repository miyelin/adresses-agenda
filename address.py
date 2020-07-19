from tkinter import *
import tkinter.messagebox
from functools import partial

def main():
    def create():
        scroll = Scrollbar(frame)

        names = Listbox(frame,  width=35, height=15, yscrollcommand=scroll.set)
        for name in namesl:
            if name != None: names.insert(END, name.rstrip())
        names.place(x=1, y=40)

        scroll.config(command=names.yview)

        adb = Button(frame, text="new entry", command=add).place(y=313, x=30)
        sv = Button(frame, text="save and quit", command=save).place(x=130, y=313)
        scroll.place(x=140, y=120)

    def save():
        wf = open("addresses.txt", "w")
        index = len(namesl)
        if len(namesl) > 0:
            for a in range(index):
                if namesl[a] != None:
                    wf.write(namesl[a])
                    wf.write(email[a])
                    wf.write(phone[a])
                    wf.write(city[a])
                    wf.write(street[a])
        quit()

    def add(*args):
        def rmv(n):
            for item in all:
                item[n] = None
            new.destroy()
            create()
        def upd(n):
            for item in range(len(all)):
                all[item][n] = str(entries[item].get())+"\n"
            new.destroy()
            create()

        def addl():
            for s in range(len(ls)): ls[s] = str(ls[s].get())

            bool = 0
            for x in namesl:
                if (ls[0]+"\n") == x: bool += 1
            if bool == 0:
                for i in range(len(ls)): ls[i] = str(ls[i]) + "\n"
                for item in range(len(all)):
                    all[item].append(ls[item])
                new.destroy()
                create()
            else: w = tkinter.messagebox.showinfo("WARNING", "this name already exists, please choose a different one")


        new = Toplevel()
        new.geometry("255x200")
        ls = [StringVar(),StringVar(), StringVar(), StringVar(), StringVar()]

        n = Message(new, text="name", width=100).place(x=10, y=10)
        ne = Entry(new, textvariable=ls[0])
        ne.place(x=63, y=10)
        e = Message(new, text="E-mail", width=100).place(x=10, y=40)
        ee = Entry(new, textvariable=ls[1])
        ee.place(x=63, y=40)
        p = Message(new, text="phone", width=100).place(x=11, y=70)
        pe = Entry(new, textvariable=ls[2])
        pe.place(x=63, y=70)
        c = Message(new, text="city", width=100).place(x=11, y=100)
        ce = Entry(new, textvariable=ls[3])
        ce.place(x=63, y=100)
        s = Message(new, text="street", width=100).place(x=11, y=130)
        se = Entry(new, textvariable=ls[4])
        se.place(x=63, y=130)
        b = Button(new, text="add new", command=addl).place(x=10, y=160)
        entries = [ne, ee, pe, ce, se]

        if len(args) > 0:
            idx = len(namesl) + 1
            for num in range(len(namesl)):
                if (str(fndVar.get())+"\n") == str(namesl[num]): idx = num

            if idx > len(namesl):
                new.destroy()
                nf = tkinter.messagebox.showinfo("not found", "entry not found")
            else:
                c = 0
                for e in entries:
                    e.insert(0, all[c][idx].rstrip())
                    c+=1

            try:
                rm = partial(rmv, idx)
                r = Button(new, text="remove", command=rm).place(x=92, y=160)
                update = partial(upd, idx)
                u = Button(new, text="update", command=update).place(x=170, y=160)
            except: return


    namesl = []
    email = []
    phone = []
    city = []
    street = []
    all = [namesl, email, phone, city, street]
    root = Tk()
    root.geometry("286x345")
    root.resizable(width=0, height=0)
    fndVar = StringVar()
    frame = Frame(root, bg="white").place()
    find = Message(frame, text="search:", width=100).place(x=10, y=10)
    fndEnt = Entry(frame, textvariable=fndVar).place(x=70, y=10)

    srch = partial(add, namesl, email, phone, city, street)
    ent = Button(frame, text="▷", bd=0, command=srch).place(x=200, y=5)

    f = open("addresses.txt", "r")
    c = 0
    for a in f:
        if c % 5 == 0:         namesl.append(a)
        elif (c - 1) % 5 == 0: email.append(a)
        elif (c - 2) % 5 == 0: phone.append(a)
        elif (c - 3) % 5 == 0: city.append(a)
        elif (c - 4) % 5 == 0: street.append(a)
        c += 1

    create()
    root.mainloop()

main()
