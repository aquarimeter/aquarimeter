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
        Label(self, text = """Please enter all intial values as indicated. Your settings will be saved in
Aquarimeter Web, the web application which helps you view the status of your
aquarium. It can be at http://aquarium.oconnor.ninja/""").grid(row = 0,columnspan = 40,sticky = W)

        #create labels to display information needed
        Label(self, text="User").grid(row=4,sticky=E)
        Label(self, text="E-mail").grid(row=5,sticky=E)
        Label(self, text="Password").grid(row=6,sticky=E)
        Label(self, text="First Name").grid(row=7,sticky=E)
        Label(self, text="Last Name").grid(row=8,sticky=E)
        Label(self, text="Ideal Temperature").grid(row=9,sticky=E)
        Label(self, text="Min temeprature").grid(row=10,sticky=E)
        Label(self, text="Max temperature").grid(row=11,sticky=E)
        
        #create places to enter text
        self.user = Entry(self)
        self.user.grid(row=4, column=1)
        self.email = Entry(self)
        self.email.grid(row=5, column=1)
        self.passwrd = Entry(self)
        self.passwrd.grid(row=6, column=1)
        self.firstNm = Entry(self)
        self.firstNm.grid(row=7, column=1) 
        self.lastNm = Entry(self)
        self.lastNm.grid(row=8, column=1)
        self.idlTemp = Entry(self)
        self.idlTemp.grid(row=9, column=1)
        self.minTemp= Entry(self)
        self.minTemp.grid(row=10, column=1)
        self.maxTemp = Entry(self)
        self.maxTemp.grid(row=11, column=1)

        #create submit and cancel buttons
        self.Submit = Button(self,text = "Register and save", command = self.connect).grid(row = 13,column = 27, sticky = E)
        self.Cancel = Button(self,text = "Cancel", command = self.cancel).grid(row = 13, column = 9, sticky = E)


    def connect(self):
        """shows what was entered. needs to be adjusted to send these items"""
        if(self.user.get() == "" or self.email.get() == "" or
           self.firstNm.get() == "" or self.passwrd.get() == "" or
           self.lastNm.get() == "" or self.idlTemp.get() == "" or
           self.minTemp.get() == "" or self.maxTemp.get() == ""):
            print "enter all fields"
            self.invalid
        else:    
        #get info from those field
            self.register
            userEnt = self.user.get()
            emailEnt = self.email.get()
            firstNmEnt = self.firstNm.get()
            passwrdEnt = self.passwrd.get()
            lastNmEnt = self.lastNm.get()
            idlTempEnt = self.idlTemp.get()
            minTempEnt = self.minTemp.get()
            maxTempEnt = self.maxTemp.get()

            
    def cancel(self):
        root.destroy()

    def register(self):
        #register area json
        REGISTER = {"user":{"email":self.email.get(),
                            "password":self.passwrd.get(),
                            "first_name":self.firstNmget(),
                            "last_name":self.lastNm.get()}}
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
                self.login

        else:
                print "Validation errors have occured, check JSON for errors"

    def login():
        #login and get username and auth_token
        emailEnt = self.email.get()
        passwrdEnt = self.passwrd.get()

        
        if(emailEnt == "" or passwrdEnt == ""):
            #pop up invalid message wait for it to enter again
            print "no good"
        else:
            #place where the json payload happens
            ########
            LOGIN = {"user":{"email":emailEnt,
                                "password":passwrdEnt}}
            #url must be changed
            URL = 'http://localhost:8880/form'

            jsondata = simplejson.dumps(LOGIN)
            h = httplib2.Http()
            User, auth_token, aquariums = h.request(URL,
                                      'POST',
                                      jsondata,
                                      headers={'Content-Type': 'application/json'})
            #must place in aquarimteter program
            TOKENS = 'auth_token.txt'
            token_file = open(TOKENS,'w')
            token_file.write("%s" % (auth_token) )
            token_file.close()
            
    def invalid(self):
        
        print "invalid"

root = Tk()
root.title("intial setup")
root.geometry("420x250")

app = Application(root)

root.mainloop()
