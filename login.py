#start up webserver.py first
from Tkinter import *
import httplib2
from datetime import datetime
import simplejson



class Application(Frame):
    """gui for entering stuff """

    def __init__(self,master):
        """make frame"""
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text = """login""").grid(row = 0,columnspan = 40,sticky = W)

        #create labels to display information needed
        Label(self, text="Password").grid(row=5,sticky=E)
        Label(self, text="E-mail").grid(row=6,sticky=E)
        
        #create places to enter text
        self.passwrd = Entry(self)
        self.passwrd.grid(row=5, column=1, columnspan = 2)
        self.email = Entry(self)
        self.email.grid(row=6, column=1, columnspan = 2) 



        #create submit and cancel buttons
        self.Submit = Button(self,text = "Submit", command = self.reveal).grid(row = 13,column = 2, sticky = E)
        self.Cancel = Button(self,text = "Cancel", command = self.Quit).grid(row = 13, column = 1, sticky = E)



    def reveal(self):
        """shows what was entered. needs to be adjusted to send these items"""
        #get info from those field
        emailEnt = self.email.get()
        okay1 = self.validate(userEnt)
        passwrdEnt = self.passwrd.get()
        okay2 = self.validate(passwrdEnt)
        firstNmEnt = self.firstNm.get()
        lastNmEnt = self.lastNm.get()
        
        if(okay1 == False or okay2 == False):
            #pop up invalid message wait for it to enter again
            print "no good"
        else:
            #place where the json payload happens
            REGISTER = {"user":{"email":emailEnt,
                                "password":passwrdEnt}}
            #url must be changed
            URL = 'http://localhost:8880/form'

            jsondata = simplejson.dumps(REGISTER)
            h = httplib2.Http()
            User, auth_token, other aquarium = h.request(URL,
                                      'POST',
                                      jsondata,
                                      headers={'Content-Type': 'application/json'})
            TOKENS = 'auth_token.txt'
            token_file = open(TOKENS,'w')
            token_file.write("%s" % (auth_token) )
            token_file.close()
            #reenable to stop after valid entry
            #root.destroy()
        
    def validate(self,field):
        if(len(field) < 10):
            return False
        else:
            return True
        
    def Quit(self):
        root.destroy()

root = Tk()
root.title("Login aquarimeter")
root.geometry("200x100")

app = Application(root)

root.mainloop()
