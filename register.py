#start up webserver.py first
from Tkinter import *
"""import httplib2
from datetime import datetime
import simplejson"""

class Application(Frame):
    """gui for entering stuff """

    def __init__(self,master):
        """make frame"""
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self, text = """fill in all fields""").grid(row = 0,columnspan = 40,sticky = W)

        #create labels to display information needed
        #Label(self, text="User").grid(row=4,sticky=E)
        Label(self, text="Password").grid(row=5,sticky=E)
        Label(self, text="E-mail").grid(row=6,sticky=E)
        Label(self, text="First Name").grid(row=7,sticky=E)
        Label(self, text="Last Name").grid(row=8,sticky=E)

        
        #create places to enter text
        #self.user = Entry(self)
        #self.user.grid(row=4, column=1)
        self.passwrd = Entry(self)
        self.passwrd.grid(row=5, column=1,columnspan = 2)
        self.email = Entry(self)
        self.email.grid(row=6, column=1,columnspan = 2) 
        self.firstNm = Entry(self)
        self.firstNm.grid(row=7, column=1,columnspan = 2) 
        self.lastNm = Entry(self)
        self.lastNm.grid(row=8, column=1,columnspan = 2)


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
            print "no good. need more chcracters for password or email"
        else:
            #register area json
            REGISTER = {"user":{"email":emailEnt,
                                "password":passwrdEnt,
                                "first_name":firstNmEnt,
                                "last_name":lastNmEnt}}
            #must change url
            URL = 'http://localhost:8880/form'

            jsondata = simplejson.dumps(REGISTER)
            h = httplib2.Http()
            HTTPcode = h.request(URL,
                                      'POST',
                                      jsondata,
                                      headers={'Content-Type': 'application/json'})
            if(HTTPcode == 200):
                print "everything is allright"

            else:
                print "Validation errors have occured, check JSON for errors"

        
    def validate(self,field):
        if(len(field) < 10):
            return False
        else:
            return True
        
    def Quit(self):
        root.destroy()

root = Tk()
root.title("Register aquarimeter")
root.geometry("200x150")

app = Application(root)

root.mainloop()
