from tkinter import *
from tkinter import messagebox
from ML_code import AIML
from API import api
screen = Tk()
screen.title('SPAM DETECTOR AND COMMENT ENHANCER')
screen.geometry("600x600")
screen.iconbitmap('Kearone-Comicons-Email-spam-fire.ico')
screen.resizable(True,False)
def check():
    comment=comment_info.get()
    result=AIML(comment)
    print(result)
    #messagebox.showinfo("output",result)
    Label(screen,text=result,font="50").place(x=180,y=200)
    with open(comment+".txt","w")as f:
        f.write(comment+"\n")
def check2():
    comment2=comment_info2.get()
    response=api(comment2)
    print(response)
    Label(screen,text=response,font="70").place(x=180,y=400)
    with open(comment2+".txt","w")as f:
        f.write(comment2+"\n")
def clear():
    main_entry.delete(0,END)
    main_entry2.delete(0,END)
#label:
Label(screen,text="Spam Comment detector And Comment Enhancer",font="Chaucer",bg="green",fg="orange").pack(fill="both")
Label(screen,text="FOR SPAM COMMENT DETECTION",font="70").place(x=30,y=50)
Label(screen,text="Please Enter your comment here:",font="40").place(x=30,y=90)
Label(screen,text="FOR COMMENT ENHANCEMENT",font="70").place(x=30,y=250)
Label(screen,text="Please enter your comment here:",font="40").place(x=30,y=290)
#entry
comment_info=StringVar()
comment_info2=StringVar()                                                                                                         
main_entry=Entry(screen,font="30",bd=3,textvariable=comment_info)
main_entry.place(x=50,y=140)
main_entry2=Entry(screen,font="30",bd=3,textvariable=comment_info2)
main_entry2.place(x=50,y=350)
#button
Button(screen,text="CHECK",font="20",command=check).place(x=30,y=200)
Button(screen,text="CHECK",font="20",command=check2).place(x=30,y=400)
Button(screen,text="CLEAR",font="20",command=clear).place(x=400,y=400)
mainloop()