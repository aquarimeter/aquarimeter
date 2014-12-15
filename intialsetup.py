from Tkinter import *

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
        self.Submit = Button(self,text = "Submit", command = self.reveal).grid(row = 13,column = 27, sticky = E)
        self.Cancel = Button(self,text = "Cancel").grid(row = 13, column = 29, sticky = E)

        #this text box only needed for verifying the fileds.delete when not needed anymore
        self.text = Text(self,width = 35,height = 3, wrap = WORD)
        self.text.grid(row = 12,columnspan = 20,sticky = W)

    def reveal(self):
        """shows what was entered. needs to be adjusted to send these items"""
        #get info from thos field
        userEnt = self.user.get()
        emailEnt = self.email.get()
        firstNmEnt = self.firstNm.get()
        passwrdEnt = self.passwrd.get()
        lastNmEnt = self.lastNm.get()
        idlTempEnt = self.idlTemp.get()
        minTempEnt = self.minTemp.get()
        maxTempEnt = self.maxTemp.get()


        self.text.insert(0.0, userEnt)
        self.text.insert(1.1,emailEnt, firstNmEnt, passwrdEnt, firstNmEnt,
                         lastNmEnt, idlTempEnt, minTempEnt, maxTempEnt)
        

root = Tk()
root.title("intial setup")
root.geometry("420x300")

app = Application(root)

root.mainloop()
