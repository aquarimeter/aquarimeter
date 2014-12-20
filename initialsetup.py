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
        Label(self, text = """Please enter all intial values as indicated.Your settings will be saved in
Aquarimeter Web, the web application which helps you view the status of your
aquarium. It can be at http://aquarium.oconnor.ninja/""").grid(row = 0,column = 0, columnspan = 5,sticky = W)

        #create labels to display information needed

        self.regFrame = LabelFrame(self,text="Login Details for Aquarimeter Web", bd = 5)
        self.regFrame.grid(row=4, column = 0, columnspan=3, rowspan=5, \
                sticky='WENS', padx=5, pady=5)
        Label(self.regFrame, text="E-mail").grid(row=6,sticky=E)
        Label(self.regFrame, text="Password").grid(row=7,sticky=E)
        Label(self.regFrame, text="First Name").grid(row=8,sticky=E)
        Label(self.regFrame, text="Last Name").grid(row=9,sticky=E)
        Label(self.regFrame, text=" ").grid(row=10,sticky=E)
        
        Label(self, text="Ideal Temperature").grid(row=11,sticky=E)
        Label(self, text=" ").grid(row=12,sticky=E)
        Label(self, text="Min temp").grid(row=13, sticky=E)
        Label(self, text="Max temp").grid(row=14, sticky=E)
        Label(self, text=" ").grid(row=15,sticky=E)
        
        #create places to enter text
        self.email = Entry(self.regFrame)
        self.email.grid(row=6, column=1)
        self.passwrd = Entry(self.regFrame)
        self.passwrd.grid(row=7, column=1)
        self.firstNm = Entry(self.regFrame)
        self.firstNm.grid(row=8, column=1) 
        self.lastNm = Entry(self.regFrame)
        self.lastNm.grid(row=9, column=1)

        
        self.idlTemp = Entry(self)
        self.idlTemp.grid(row=11, column=1)
        DEGREES = ["C", "F"]
        var = StringVar(self)
        var.set(DEGREES[0])
        self.DegMenu = apply(OptionMenu, (self,var) + tuple(DEGREES))
        self.DegMenu.grid(row = 11, column = 2)

        self.minTemp = Entry(self)
        self.minTemp.grid(row=13, column=1)
        self.maxTemp = Entry(self)
        self.maxTemp.grid(row=14, column=1)

        #create submit and cancel buttons
        self.Submit = Button(self,text = "Register and save", command = self.connect).grid(row = 16,column = 3, sticky = E)
        self.Cancel = Button(self,text = "Cancel", command = self.cancel).grid(row = 16, column = 2, sticky = E)


    def connect(self):
        """shows what was entered. needs to be adjusted to send these items"""
        if(self.email.get() == "" or self.firstNm.get() == "" or
           self.passwrd.get() == "" or self.lastNm.get() == "" or
           self.idlTemp.get() == "" or self.minTemp.get() == "" or
           self.maxTemp.get() == ""):
            print "fill all required fields"
            self.invalid
        else:    
        #get info from those field
            self.register
            """emailEnt = self.email.get()
            firstNmEnt = self.firstNm.get()
            passwrdEnt = self.passwrd.get()
            lastNmEnt = self.lastNm.get()
            
            idlTempEnt = self.idlTemp.get()
            minTempEnt = self.minTemp.get()
            maxTempEnt = self.maxTemp.get()"""

            
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
root.title("Aquarimeter Intial Setup")

app = Application(root)

root.mainloop()
