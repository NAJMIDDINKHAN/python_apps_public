from tkinter import*

def yigindi():

    ason = int(son1.get())
    bson = int(son2.get())
    sum = ason+bson
    hisoblash.configure(text=str(sum))
def ayrma():
    ason = int(son1.get())
    bson = int(son2.get())
    sum = ason - bson
    hisoblash.configure(text=str(sum))
def kupaytma():
    ason = int(son1.get())
    bson = int(son2.get())
    sum = ason * bson
    hisoblash.configure(text=str(sum))
def bulinma():
    ason = int(son1.get())
    bson = int(son2.get())
    sum = ason / bson
    hisoblash.configure(text=str(sum))

def daraja():
    ason = int(son1.get())
    bson = int(son2.get())
    sum = ason ** bson
    hisoblash.configure(text=str(sum))

def ildiz():
    ason = int(son1.get())
    bson = int(son2.get())
    sum = ason ** (1/bson)
    hisoblash.configure(text=str(sum))
oyna = Tk()
oyna.title("kalkuliyator")
oyna.geometry("175x175")
tugma=Button(text="+",command=yigindi,width=5,height=2,bg="#8EFD00")
tugma.place(x=10,y=70)
tugma=Button(text="-",command=ayrma,width=5,height=2,bg="#8EFD00")
tugma.place(x=60,y=70)
tugma=Button(text="*",command=kupaytma,width=5,height=2,bg="#8EFD00")
tugma.place(x=110,y=70)
tugma=Button(text="/",command=bulinma,width=5,height=2,bg="#8EFD00")
tugma.place(x=10,y=120)
tugma=Button(text="x^n",command=daraja,width=5,height=2,bg="#8EFD00")
tugma.place(x=60,y=120)
tugma=Button(text="√",command=ildiz,width=5,height=2,bg="#8EFD00")
tugma.place(x=110,y=120)
son1=Entry()
son1.place(x=10 ,y=10)
son2=Entry()
son2.place(x=10,y=30)
hisoblash=Label(text="javob;")
hisoblash.place(x=10,y=50)
hisoblash=Label(text="?")
hisoblash.place(x=45,y=50)
oyna.mainloop()

