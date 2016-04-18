#!/usr/bin/python

import Tkinter
import smtplib
import string
from random import randrange

top = Tkinter.Tk()

number = [0,1,2,3,4,5,6,7,8,9,0]
letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

fromaddr = 'stecassso.lab@gmail.com'

Ticket = ''
Subject = ''
Person = ''
emailPerson = ''
info = ''
msg = ''



lab = Tkinter.Label( top, text = "to e-mail adress")
lab.grid(row = 0, column = 0, columnspan = 1)

en = Tkinter.Entry( top)

en.grid(row = 0, column = 1)

lab1 = Tkinter.Label(top, text = "subject")
lab1.grid(row = 1, column = 0)
en1 = Tkinter.Entry(top)
en1.grid(row= 1, column = 1)

lab2 = Tkinter.Label(top, text = "person")
lab2.grid(row = 2, column = 0)
en2 = Tkinter.Entry(top)
en2.grid(row = 2, column = 1)

lab3 = Tkinter.Label(top, text = "about")
lab3.grid(row = 3, column = 0)


frame1 = Tkinter.Frame(top,width=80, height=80,bg = '#ffffff',
                  borderwidth=1, relief="sunken")
scrollbar = Tkinter.Scrollbar(frame1) 
editArea = Tkinter.Text(frame1, width=100, height=20, wrap="word",
                   yscrollcommand=scrollbar.set,
                   borderwidth=0, highlightthickness=0)
scrollbar.config(command=editArea.yview)
scrollbar.pack(side="right", fill="y")
editArea.pack(side="left", fill="both", expand=True)
frame1.place(x=100,y=64)


def TicketGen():
    global Ticket
    global Subject
    global Person
    global emailPerson
    global info
    global msg
    Ticket = "%s%s%s%s%s%s%s%s%s" %  (number[randrange(0, 10)],number[randrange(0, 10)],number[randrange(0, 10)],number[randrange(0, 10)], letter[randrange(0,26)],number[randrange(0, 10)],number[randrange(0, 10)],number[randrange(0, 10)],number[randrange(0, 10)])
    Subject = "%s (Ticket %s)" % (en1.get(), Ticket)
    Person = "%s" % (en2.get())
    emailPerson = "%s" % (en.get())
    info = "%s" % (editArea.get(1.0))
    msg = """From: <stecasso.lab@gmail.com>
To: %s
Subject: %s

Dear %s,

%s

Met vriendelijke groet, Best regards,

Stecasso Laboratories


Disclaimer

This e-mail is confidential.  If you are not the intended recipient, you must not disclose or use the information contained in it.  If you have received this e-mail in error, please tell us immediately by return e-mail to stecasso.lab@gmail.com  and delete the document.

E-mails containing unprofessional, discourteous or offensive remarks violate Company policy. You may report employee violations by forwarding the message to stecasso@gmail.com.No recipient may use the information in this e-mail in violation of any civil or criminal statute. Company disclaims all liability for any unauthorized uses of this e-mail or its contents.

This e-mail constitutes neither an offer nor an acceptance of any offer. No contract may be entered into by a Company employee without express approval from an authorized Company manager.

Warning: Computer viruses can be transmitted via e-mail. Company accepts no liability or responsibility for any damage caused by any virus transmitted with this e-mail.

ALL RIGHTS RESERVED 
""" % (emailPerson, Subject, Person, info)
    username = 'stecasso.lab@gmail.com'
    password = 'Laboratorie'
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('stecasso.lab@gmail.com',password)
    server.sendmail(fromaddr, emailPerson, msg)
    server.quit()

def pressed():
    print "%s" % ( en.get() )
    TicketGen() 


frame2 = Tkinter.Frame(top,width=80, height=80,bg = '#ffffff',
                  borderwidth=1, relief="sunken")

but = Tkinter.Button ( frame2, text = "send", command = pressed )
but.pack(side = "right")
frame2.place(x=100,y=370)

top.mainloop()




