#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class Aquarium_Setup:

    #checks required fields is filled before registering
    def validate(self):
        if(not self.valid_Email.get_text() or
           not self.valid_Password.get_text() or
           not self.first_Name.get_text() or
           not self.last_Name.get_text()):
            return False
        else:
            return True

    #checks password is long enough
    def check_length(self,password):
        if(len(password) < 10):
            return False
        else:
            return True
        
    #pop up message box asking to fill all fields
    def error_fill(self):
        info = gtk.MessageDialog(type=gtk.MESSAGE_WARNING, buttons=gtk.BUTTONS_OK)
        info.set_property('title', 'Missing information')
        info.set_property('text', 'Please fill in all fields')
        info.run()
        info.destroy()

    #pop up message for short password
    def error_password(self):
        info = gtk.MessageDialog(type=gtk.MESSAGE_WARNING, buttons=gtk.BUTTONS_OK)
        info.set_property('title', 'Password too short')
        info.set_property('text', 'Password must be at least 10 characters long')
        info.run()
        info.destroy()
        
    #registers with entered information from gui
    def register(self,widget,data=None):
        fill = self.validate()
        long_pwd = self.check_length(self.valid_Password.get_text())
        if(not fill):
            self.error_fill()
        elif(not long_pwd):
            self.error_password()
        else:
            #json payload send should happen here. must be changed to do that
            print self.valid_Email.get_text()
            print self.valid_Password.get_text()
            print self.first_Name.get_text()
            print self.last_Name.get_text()
            self.login()

    #login with password and email
    def login(self):
        #login  must happen here and must save auth_token. must be changec
        print "will now login"

    
    #main gui window
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Aquarimeter Intial Setup")
        self.window.connect("destroy", lambda wid: gtk.main_quit())
        
        main_Box = gtk.VBox(False, 5) #all items will be arranged vertically in here
        self.window.add(main_Box)
        self.window.set_border_width(10)

        label = gtk.Label("Please enter all intial values as indicated. Your"
                          "settings will be saved in\n Aquarimeter Web, the"
                          " web application which helps you view the status "
                          "of your\n aquarium. It can be at http://aquarium."
                          "oconnor.ninja/")
        main_Box.pack_start(label)
        #create fields for registeration information to be entered
        reg_frame = gtk.Frame("Login Details for Aquarimeter Web") 

        #labels for information needed
        info_Box = gtk.HBox(False,5)
        vbox1 = gtk.VBox(False,5)
        info_Box.add(vbox1)

        label = gtk.Label("E-mail")
        vbox1.add(label)
        label = gtk.Label("Password")
        vbox1.add(label)
        label = gtk.Label("First Name")
        vbox1.add(label)
        label = gtk.Label("Last Name")
        vbox1.add(label)

        #fields to enter information
        vbox2 = gtk.VBox(False,5)
        info_Box.add(vbox2)
        
        self.valid_Email = gtk.Entry()
        vbox2.add(self.valid_Email)
        
        self.valid_Password = gtk.Entry()
        vbox2.add(self.valid_Password)
        
        self.first_Name = gtk.Entry()
        vbox2.add(self.first_Name)
        
        self.last_Name = gtk.Entry()
        vbox2.add(self.last_Name)
        
        reg_frame.add(info_Box)
        main_Box.pack_start(reg_frame, False, False, 0)

        #labels for varias temperature settings
        temp_frame = gtk.Frame("Temperature set")
        vbox3 = gtk.VBox(False,5)
        hbox3 = gtk.HBox(False,5)
        hbox3.add(vbox3)
        
        label = gtk.Label("Intial Temperature")
        vbox3.add(label)
        label = gtk.Label("Max Temperature")
        vbox3.add(label)
        label = gtk.Label("Min Temperature")
        vbox3.add(label)

        #temperature selection setting
        vbox4 = gtk.VBox(False,5)
        hbox3.add(vbox4)

        adj = gtk.Adjustment(70.0, 55.0, 85.0, 1.0, 5.0, 0.0)
        spinner = gtk.SpinButton(adj, 0, 0)
        vbox4.add(spinner)
        
        adj = gtk.Adjustment(70.0, 55.0, 85.0, 1.0, 5.0, 0.0)
        spinner2 = gtk.SpinButton(adj, 0, 0)
        vbox4.add(spinner2)
        
        adj = gtk.Adjustment(70.0, 55.0, 85.0, 1.0, 5.0, 0.0)
        spinner3 = gtk.SpinButton(adj, 0, 0)
        vbox4.add(spinner3)

        #temperature units setting
        vbox5 = gtk.VBox(False,5)
        hbox3.add(vbox5)

        combo = gtk.Combo()
        combo.entry.set_text("list")
        slist = [ "F", "C" ]
        combo.set_popdown_strings(slist)
        vbox5.add(combo)
        label = gtk.Label(" ")
        vbox5.add(label)
        label = gtk.Label(" ")
        vbox5.add(label)
        
        temp_frame.add(hbox3)
        main_Box.pack_start(temp_frame, False, False, 0)

        #cancel and submit button section
        hbox10 = gtk.HBox(False,2)
        main_Box.pack_start(hbox10, False,False,0)
        
        button = gtk.Button("Submit and Register")
        button.connect("clicked", self.register)
        hbox10.pack_end(button,False,False,2)
        
        button = gtk.Button("cancel")
        button.connect_object("clicked",gtk.Widget.destroy, self.window)
        hbox10.pack_end(button,False,False,2)

        self.window.show_all()

    def main(self):
        gtk.main()


if __name__ == "__main__":
    Aqua_Setup = Aquarium_Setup()
    Aqua_Setup.main()

