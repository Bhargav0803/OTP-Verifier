from twilio.rest import Client
import random
from tkinter import *
from tkinter import messagebox

class otp_verifier(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x550")
        self.resizable(False,False)

    def Labels(self):
        self.c = Canvas(self,bg= "white",width=400,height=280)
        self.c.place(x=100,y=60)

        self.Login_Title=Label(self,text="OTP Verification",font="bold,20",bg="white")
        self.Login_Title.place(x=210,y=90)

    def Entry(self):
        self.User_Name=Text(self,borderwidth=2,wrap="word",wodth=29,height=2)
        self.User_Name.place(x=190,y=160)

    def Buttons(self):
        self.submitButtonImage=PhotoImage(file="submit.png")
        self.submitButton=Buton(self,image=self.submitButtonImage,command=self.checkOTP,border=0)
        self.submitButton.place(x=208,y=240)







    def checkOTP(self):
        try:
            self.userInput=int(self.User_name.get(1.0,"end-1c"))
            if self.userInput==self.n:
                messagebox.showinfo("showinfo", "Login Success")
                self.n="done"

            elif self.n=="done":
                messagebox.showinfo("showinfo", "Already Login")
            else:
                messagebox.showinfo("showinfo", "Wrong OPT")
        except:
            messagebox.showinfo("showinfo", "Invalid OTP")
            
                
                

if __name__=="__main__":
    window=Login_Form
