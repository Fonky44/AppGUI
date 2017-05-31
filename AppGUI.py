#!/usr/bin/python3
import tkinter as tk
import random
import time
import math
import turtle
import string
import random
import os
import sys
import re
import threading
import dis
import socket
import xml.sax
import multiprocessing as ms
import webbrowser
import urllib
import urllib.request
from html.parser import HTMLParser
from os.path import join
##----------Functions
In = ("Comic Sans MS", 16)
Inn = ("Calibri", 13)
nn = ("Calibri", 11)
Out = ("Courier New", 10)
small = ("Courier", 10)
smal = ("Courier", 12)
root = tk.Tk()
root.title("Evolution Hub")
Icon = "C:/Users//kalkidan.beyene//Desktop//Python Saves//Screw.ico"
root.iconbitmap(Icon)
Version = "-Version 11.1-"
getme = ""
exeuted = ""
xmlstring = ""
defaultfile = "XML/test.xml"
class monster(object):
    global monsters
    monsters = 0
    def __init__(self):
        print("Iniziliating Monster and base....", end="")
        global monsters
        name = None
        level = 0
        health = 0
        attack = 0
        defense = 0
        monsters += 1
        print(" DONE!")
    def Creation(self, input):
        global monsters
        global name
        mname = input
        mlevel = random.randint(0, 10)
        px = mlevel * 10
        hx = mlevel + 100
        print(px, hx)
        mhealth = random.randint(0, hx)
        mattack = random.randint(0, px)
        mdefense = random.randint(0, px)
        monsters  += 1
        print("Since Dawn, monster have existed but " + str(mname) + " Is the last")
        print(mname + " Level is " + str(mlevel))
        print("His health is on " + str(mhealth))
        print("Hes strength is attack is " + str(mattack))
        print("And his protection level is " + str(mdefense))
        return mname
Monster = monster()
class Basic():
    def __init__(self):
        print("Basic Module loaded")
        self.assets = 20
        self.version = "2"
        self.stage = 0
    def Math(input):
        value = input
        sub = random.randint(0, 100)
        if isinstance(value, int):
            printwill = value - sub
            print(printwill)
        else:
            raise TypeError("Please type in a int")
    def List():
        cmd = "Basic.GetObjects('xmlfilename') (Must be in the XML folder) \n\nBasic.Math(number) Must be an int, chars will create a TypeError!"
        Protonclean(cmd)
    def GetObjects(input):
        ## denne skal andres til å lete etter en spesifikk fil når den brukes :D
        file = input
        folder = "C:/Users/kalkidan.beyene/Desktop/Python Saves/Tkinter and OC/XML/" + file
        xmlfile = open(folder, 'r')
        xml = xmlfile.read()
        Protonclean(xml)
    def BetaObjects():
        file = 1
        
def Protonclean(input):
        ProtonInput.delete('1.0', 'end')
        executed = input
        ProtonInput.insert('end', executed)
class XMLPARSER(xml.sax.ContentHandler):
    def __init__(self):
        self.Game = ""
        self.Place = ""
        self.memory = ""
        self.rate = ""
    def StartElement(self, tag, attributes):
            self.CurrentData = tag
            if tag == "Place":
                Place = tag
                placeid = attributes["placeid"]
                print(Place, placeid)
class Canvo:
    def WaitDelete():
        MainCanvas.delete("all")    
    def CanArc():
        coords = 10, 50, 240, 210
        arc = MainCanvas.create_arc(coords, start = 0, extent = 150, fill = "Blue")
    def CanImage():
        ##Currently not showing image going to work on this later
        coords = 250,200
        filename = tk.PhotoImage(file = "memes/4day.gif")
        Master.filename = filename
        phot = MainCanvas.create_image(coords, image = filename)
        
    def CanLine():
        coords = 10, 50, 240, 210
        line = MainCanvas.create_line(coords, fill = "Red")
    def CanOval():
        coords = 10, 50, 240, 210
        oval = MainCanvas.create_oval(coords, fill = "Green")
    def CanPolygon():
        coords = 10, 50, 240, 210
        polygon = MainCanvas.create_polygon([150,75,225,0,300,75,225,150],     outline='gray', 
            fill='Black', width=5)
def Pi():
    um = input("How many numbers of pi do you want(max 10 000): ")
    a = open('Pi.txt', 'r')
    f = a.read()
    x = list(str(f))
    map(int,x)
    print("3.", end="")
    num = int(um)   
    ##print(x[0:num])
    print(''.join(x[0:num]))

def Unfinished():
    print("This Button is not finished")

def MouseMovement():
    ##PYA har blitt skiftet til XML Editor :D
    root.title("XML Editor")
    frame.grid_remove()
    Mframe.grid_remove()
    Games.grid_remove()
    Update.grid_remove()
    xmlGUI.grid(sticky="WENS")
    xmlGUI.grid_propagate(0)
    default = "This is default :D\n\n If you dont understand how to use this just write in the file directory from above as an example :D"
    xmlinput.insert('1.0', default)
def ball():
    ans = True

    while ans:
        question = input("Ask the magic 8 ball a question:")
    
        answers = random.randint(1,8)
    
        if question == "":
            sys.exit()
    
        elif answers == 1:
            print ("It is certain")
    
        elif answers == 2:
            print ("Outlook good")
    
        elif answers == 3:
            print ("You may rely on it")
    
        elif answers == 4:
            print ("Ask again later")
    
        elif answers == 5:
            print ("ITS SCIENFICIZALLY PROVEN")
    
        elif answers == 6:
            print ("Reply hazy, try again")
    
        elif answers == 7:
            print ("My reply is no")
    
        elif answers == 8:
            print ("My sources say no")
def PW():
    ##This is a retired function, saved for historical reasons
    characters = string.ascii_letters + string.punctuation  + string.digits
    password =  "".join(choice(characters) for x in range(randint(8, 16)))
    print(password)

def moo():
    melding = input('Hva sier KUA?!?!')
    boblelengde = len(melding) + 2
    print(' ____________________')
    print(' ' + '_' * boblelengde)
    print('< ' + melding + ' >')
    print(' --------------------')
    print('     \   ^__^')
    print('      \  (oo)\_______')
    print('         (__)\       )')
    print('             ||----W |')
    print('             ||     ||')

def Triangle():
    turtle.speed(3)
    turtle.shape("arrow")
    turtle.pencolor("blue")
    turtle.pensize(50)
    turtle.forward(200)
    turtle.right(120)
    turtle.pencolor("red")
    turtle.forward(200)
    turtle.right(120)
    turtle.pencolor("green")
    turtle.forward(200)
    turtle.right(120)
    turtle.pencolor("blue")
    turtle.forward(30)

def Bruteforce():
    ## Add path to cmd, regedit and firewall again
    print("BruteForce have currently been disabled")
    regedit = 'C:/Windows/regedit.exe'
    cmd = ''

def ShowLogin():
    root.title("Login")
    frame.grid_remove()
    Mframe.grid_remove()
    Games.grid_remove()
    LoginFrame.grid_propagate(0)
    LoginFrame.grid(sticky="WENS")
    LTL.grid(sticky="WE")
    LTI.focus_set()
    LTI.grid(sticky="WE")
    Back.grid(sticky="WE")
    LTI.focus_set()
def Return():
    root.title("Evolution Hub")
    frame.grid_propagate(0)
    Mframe.grid_propagate(0)
    Games.grid_propagate(0)
    frame.grid()
    Mframe.grid()
    Games.grid()
    LoginFrame.grid_remove()

def Certificate():
    global credentials
    credentials = {}
    with open('Username.txt') as f:
        for line in f:
            user, pwd = line.strip().split(':')
            credentials[user] = pwd

def Get(event):
    global username
    global password
    username = LTL.get()
    password = LTI.get()
    Certificate()
    LoginValidate()

def LoginValidate():
    Certificate()
    global username
    global credentials
    if username in credentials:
        LoginValidate2()
    else:
        print("Wrong Username/Password")

def LoginValidate2():
    if credentials[username] == password:
        LoginValidate3()
    else:
        print("Wrong Username/Password")
        
def Logout():
    ProtonInput.delete('1.0', 'end')
    ProtonGUI.grid_remove()
    LoginFrame.grid_propagate(0)
    LoginFrame.grid()
    Update.grid(sticky="WE")
    
highlightWords = {'if': 'red', 
                  'else': 'red', 
                  'print' : 'green', 
                  '(' : 'blue', 
                  ')' : 'blue', 
                  "'" : "HotPink4",
                  '"' : "HotPink4",
                  "def" : "orange",
                  "=" : "blue",
                  "==" : "red4", 
                  "None" : "red4",
                  "True" : "red4", 
                  "import" : "red",
                  "for" : "red",
                  "open" : "green",
                  "in" : "red",
                  "Fonky44" : "green2",
                  "stdout" : "blue",
                  "stderr" : "maroon",
                  "Made by Fonky44" : "maroon1",
                  '<' : 'blue',
                  '>' : 'blue',
                  '+' : 'blue',
                  '++' : 'blue',
                  'input' : 'green',
                  'float' : 'green',
                  'int' : 'green',
                  'str' : 'green',
                  'range' : 'green',
                  'return' : 'orange',
                  'isinstance' : 'blue',
                  '##' : 'yellow',
                  '#' : 'yellow'
                  }
xmlhighlight = {'<' : 'blue',
                '>' : 'blue',
                "Fonky44" : "green2",
                "Made by Fonky44" : "maroon1",
                "=" : "green",
                '"' : "red",
                "/" : "blue"}
def xmlLight(event):
    for k,v in xmlhighlight.items():
        startIndex = '1.0'
        while True:
            startIndex = xmlinput.search(k, startIndex, 'end')
            if startIndex:
                endIndex = xmlinput.index('%s+%dc' % (startIndex, (len(k))))
                xmlinput.tag_add(k, startIndex, endIndex)
                xmlinput.tag_config(k, foreground=v)
                startIndex = endIndex
            else:
                break
def LoginValidate3():
    Update.grid_remove()
    LoginFrame.grid_remove()
    root.title("Proton Smasher v2")
    ProtonGUI.grid_propagate(0)
    ProtonGUI.grid()
    ## copy og change executed for det du vil skal dukke opp :D
    executed = "Made by Fonky44"
    ProtonInput.insert('1.0', executed)
    for k,v in highlightWords.items():
        startIndex = '1.0'
        while True:
            startIndex = ProtonInput.search(k, startIndex, 'end')
            if startIndex:
                endIndex = ProtonInput.index('%s+%dc' % (startIndex, (len(k))))
                ProtonInput.tag_add(k, startIndex, endIndex)
                ProtonInput.tag_config(k, foreground=v)
                startIndex = endIndex
            else:
                break

def highlighter(event):
    for k,v in highlightWords.items():
        startIndex = '1.0'
        while True:
            startIndex = ProtonInput.search(k, startIndex, 'end')
            if startIndex:
                endIndex = ProtonInput.index('%s+%dc' % (startIndex, (len(k))))
                ProtonInput.tag_add(k, startIndex, endIndex)
                ProtonInput.tag_config(k, foreground=v)
                startIndex = endIndex
            else:
                break

def ProtonGet(event):
    global function
    script = ProtonInput.get("1.0",'end-1c')
    """temp = open("temfile.py", 'w')
    tempwrite = temp.write(script)
    temp.close
    import temfile
    temfile.main()"""
    try:
        exec(script)
        function = script
    except:
        eval(script)
    script = script + ' was executed'
    ProtonOutput.config(text=script)

def File():
    import os
    file = input("File directory: ")
    ##file = "C:/Program Files/Internet Explorer/iexplore.exe"
    print("The current file is: "+ file)
    os.remove(file)
def regular():
    print("Regular expression training")
    ##re.match(pattern, string, flags=0)
    print("re.match(pattern, string, flags=0)")
def showsocket():
    root.title("Socket Hacks")
    SocketGUI.grid_propagate(0)
    SocketGUI.grid()
    SocketGUI.grid_propagate(0)
    frame.grid_remove()
    Mframe.grid_remove()
    Games.grid_remove()
def returnmenu():
    root.title("Evolution Hub")
    frame.grid_propagate(0)
    Mframe.grid_propagate(0)
    Games.grid_propagate(0)
    frame.grid()
    Mframe.grid()
    Games.grid()
    SocketGUI.grid_remove()
def returnxml():
    root.title("Evolution Hub")
    frame.grid_propagate(0)
    Mframe.grid_propagate(0)
    Games.grid_propagate(0)
    frame.grid()
    Mframe.grid()
    Games.grid()
    xmlinput.delete('1.0', 'end')
    xmlGUI.grid_remove()
    Update.grid(sticky="WE")

def taken():
    global pid
    global local
    pid = 3
    local = "Website to steal: "
    GetString = tk.StringVar(SocketGUI, value=local)
    SocketEntry.config(textvariable=GetString)

def took():
    global getme
    global cha
    need = "http://www."
    gotit = str(need) + str(getme)
    cho = urllib.request.urlopen(gotit)
    chi = cho.read()
    ##cha = strip_tags(chi).lower()
    cha = str(chi)
    hml()
def SocketHub():
    if pid == 2:
        website()
    elif pid == 3:
        took()
    else:
        print("ID not found")

def printsocket():
    global getme
    ## edit getme var for ex: getme = "Test" for different output
    GetString = tk.StringVar(SocketGUI, value=getme)
    SocketEntry.config(textvariable=GetString)

def getsocket(event):
    global getme
    output = SocketLog.get()
    output.strip()
    getme = output
    SocketHub()

def hml():
    direct = 'test.html'
    net = open('test.html', 'w')
    us = open('source.txt', 'w')
    backup = """
<h1>ATM</h1>
<p><span style="color: #ff0000;">This isnt done yet</span></p>"""
    net.write(cha)
    us.write(cha)
    webbrowser.open_new_tab(direct)
    net.close
    us.close

def hail():
    pappafant = "https://google.com"
    webbrowser.open_new_tab(pappafant)

def retaken():
    use = open('source.txt', 'w')
    net = open('test.html', 'a+')
    nuse = net.read()
    net.write(nuse)
    use.close
    net.close
    webbrowser.open_new_tab('test.html')
def xmlnewfile(input):
    printfile = input
    xmlinput.delete('1.0', 'end')
    xmlinput.insert('end', printfile)
    for k,v in xmlhighlight.items():
        startIndex = '1.0'
        while True:
            startIndex = xmlinput.search(k, startIndex, 'end')
            if startIndex:
                endIndex = xmlinput.index('%s+%dc' % (startIndex, (len(k))))
                xmlinput.tag_add(k, startIndex, endIndex)
                xmlinput.tag_config(k, foreground=v)
                startIndex = endIndex
            else:
                break
def xmlgetfile(event):
    fileplace = xmlsearch.get()
    if fileplace == 'Fonky44':
        Fonky44 = "WOAH WOAH MATE U FOUND A EASTER EGG COOL BOII"
        xmlnewfile(Fonky44)
    else:
        thefile = open(fileplace, 'r')
        nowfile = thefile.read()
        xmlnewfile(nowfile)
        thefile.close()
def cleanproton():
    ProtonInput.delete('1.0', 'end')
def cleanxml():
    xmlinput.delete('1.0', 'end')
def par(event):
    time.sleep(0.5)
    a = ")"
    ProtonInput.insert('end', a)
def par2(event):
    print("worked")
    a = ")"
    xmlinput.insert('end+1c', a)
def savexml():
    savethis = xmlinput.get('1.0', 'end')
    findthis = xmlsearch.get()
    openthis = open(findthis, 'rw')
    writethis = openthis.write(savethis)
    openthis.close()
            
def CanShow():
    root.title("Cansas Lab")
    frame.grid_remove()
    Mframe.grid_remove()
    Games.grid_remove()
    canGUI.pack_propagate(0)
    cansub.pack_propagate(0)
    cansub2.pack_propagate(0)
    cansub3.pack_propagate(0)
    canGUI.pack()
    cansub.pack()
    cansub2.pack()
    cansub3.pack()
    MainCanvas.pack(fill="x")
    CanOut.pack(side="left")
    CanClear.pack(side="left")
    CanArc.pack(side="left")
    CanImage.pack(side="left")
    CanLine.pack(side="left")
    CanOval.pack(side="left")
    CanPolygon.pack(side="left")
def CanBack():
    canGUI.pack_forget()
    con()
def con():
    root.title("Evolution Hub")
    frame.grid_propagate(0)
    Mframe.grid_propagate(0)
    Games.grid_propagate(0)
    frame.grid()
    Mframe.grid()
    Games.grid()
    
##Master race
Master = tk.Frame(root, bg="Light Blue")
##Frames
root.config(bg="ivory4")
frame = tk.LabelFrame(Master, height="220", width="200", bg="gray7", fg="Red", text="Rip Windows", font="Bold")
Mframe = tk.LabelFrame(Master, height="95", width="200", bg="gray7", fg="Red", text="Stuff", font="Bold")
Games = tk.LabelFrame(Master, height="155", width="200", bg="gray7", fg="Red", text="Games", font="Bold")
Mini = tk.Frame(Master, height="300", width="300", bg="ivory4")
SocketGUI = tk.Frame(Master, height="450", width="420", bg="#8caaf3")
LoginFrame = tk.Frame(Master, height="100", width="100", bg="ivory4")
ProtonGUI = tk.Frame(Master, height="200", width="400", bg="White")
xmlGUI = tk.Frame(Master, height="200", width="400", bg="Black")
canGUI = tk.Frame(Master, height="500", width="500")
cansub = tk.Frame(canGUI, height="400", width="500")
cansub2 = tk.Frame(canGUI, height="50", width="500")
cansub3 = tk.Frame(canGUI, height="50", width="500")
##--------------strings
UsernameString = tk.StringVar(LoginFrame, value="Username")
PasswordString = tk.StringVar(LoginFrame, value="Password")
XmlString = tk.StringVar(xmlGUI, value=xmlstring)
defaultxml = tk.StringVar(xmlGUI, value=defaultfile)
EditorString = tk.StringVar(ProtonGUI, value=exeuted)
VersionString = tk.StringVar(Mini, value=Version)
GetString = tk.StringVar(SocketGUI, value=getme)
##Widgets
PYA = tk.Button(frame, text="XML Editor", fg="gray48", bg="maroon", font="monospace")
xmllabel = tk.Label(xmlGUI, bg="Black", fg="White", font=Inn, text="XML Editor", bd=8)
xmlsearch = tk.Entry(xmlGUI, bg="Black", fg="White", font=nn, textvariable=defaultxml)
xmlinput = tk.Text(xmlGUI, bg="Black", fg="White", font=In, relief="sunken", width="30", height="15")
xmlreturn = tk.Button(xmlGUI, text="Click here to go back", bg="Black", fg="White", font=Inn)
xmlclear = tk.Button(xmlGUI, text="Clear", bg="Black", fg="White", font=Inn, width=11)
xmlsave = tk.Button(xmlGUI, text="Save", bg="Black", fg="White", font=Inn, width=11)
Knapp = tk.Button(frame, text="BruteForce(ADMIN)", fg="gray48", bg="maroon", font="monospace")
html = tk.Button(frame, text="Open Browser", fg="gray48", bg="maroon", font="monospace")
bb = tk.Button(SocketGUI, text="Return", fg="#8caaf3", bg="#3b6705", font="courior")
Socket = tk.Button(frame, text="Sockets", fg="gray48", bg="maroon", font="monospace")
Server = tk.Button(SocketGUI, text="Create Server", fg="#8caaf3", bg="#3b6705", font="Courier")
begone = tk.Button(SocketGUI, text="Website Stealer", fg="#8caaf3", bg="#3b6705", font="Courier")
differ = tk.Button(SocketGUI, text="ReUpload", fg="#8caaf3", bg="#3b6705", font="Courier")
Connect = tk.Button(SocketGUI, text="Connect", fg="#8caaf3", bg="#3b6705", font="Courier")
GO = tk.Button(SocketGUI, text="GO", fg="#8caaf3", bg="#3b6705", font="Courier")
SocketEntry = tk.Label(SocketGUI, bg="#3b6705", fg="#8caaf3", font=small, width="50")
SocketLog = tk.Entry(SocketGUI, bg="#3b6705", fg="#8caaf3", font=smal, width="40")
PIKnapp = tk.Button(Mframe, text="Pi", bg="maroon", fg="gray48", font="Times")
KUA = tk.Button(Games, text="Kua sier?", bg="maroon", fg="gray48", font="Bold")
TRIANGLE = tk.Button(Games, text="Epic Triangle", bg="maroon", fg="gray48", font="Bold")
PASSWORD = tk.Button(Mframe, text="Canvas", bg="maroon", fg="gray48", font="Bold")      
MagicBall = tk.Button(Games, text="Magic 8 Ball", bg="maroon", fg="gray48", font="Bold")
Lore = tk.Button(Games, text="Lore", bg="maroon", fg="gray48", font="Bold")
LTL = tk.Entry(LoginFrame, bg="maroon", fg="Black", font="Bold", textvariable=UsernameString)
LTI = tk.Entry(LoginFrame, bg="maroon", fg="Black", font="Bold",show="*", textvariable=PasswordString)
Login = tk.Button(frame, text="Login", fg="gray48", bg="maroon", font="monospace")
Back = tk.Button(LoginFrame, text="Click here to go back", bg="maroon", fg="Black", font="Bold")
Update = tk.Label(root, bg="Red", fg="Black", font="Bold", relief="groove", text=Version)
LogOut = tk.Button(ProtonGUI, bg="White", fg="gray1", font="Bold", text="Log Out", width=10)
Protonclear = tk.Button(ProtonGUI, bg="White", fg="gray1", font="Bold", text="Clear", width=15)
Protoncmd = tk.Button(ProtonGUI, bg="White", fg="gray1", font="Bold", text="Functions", width=15)
ProtonLabel = tk.Label(ProtonGUI, bg="White", fg="gray1", font=In, text="Script Executor", bd=8)
ProtonInput = tk.Text(ProtonGUI, bg="White", fg="gray1", font=In, relief="sunken", width="30", height="15")
ProtonOutput = tk.Label(ProtonGUI, bg="White", fg="gray1", font=Out, relief="raised", width="30", height="5")
MainCanvas = tk.Canvas(cansub, bg="gray55" , height=400, width=100)
CanOut = tk.Button(cansub3, font="Bold", text="Return", width=10)
CanArc = tk.Button(cansub2, font="Bold", text="Arc", width=10)
CanClear = tk.Button(cansub3, font="Bold", text="Clean", width=10)
CanImage = tk.Button(cansub2, font="Bold", text="PNG", width=10)
CanLine = tk.Button(cansub2, font="Bold", text="Line", width=10)
CanOval = tk.Button(cansub2, font="Bold", text="Oval", width=10)
CanPolygon = tk.Button(cansub2, font="Bold", text="Polygon", width=10)
##Config and bindings
CanOut.config(command=CanBack)
CanArc.config(command=Canvo.CanArc)
CanClear.config(command=Canvo.WaitDelete)
CanImage.config(command=Canvo.CanImage)
CanLine.config(command=Canvo.CanLine)
CanOval.config(command=Canvo.CanOval)
CanPolygon.config(command=Canvo.CanPolygon)
ProtonInput.focus_set()
ProtonInput.bind('<Key>', highlighter)
ProtonInput.bind('<F5>', ProtonGet)
##ProtonInput.bind('<(>', par)
xmlinput.focus_set()
xmlinput.bind('<Key>', xmlLight)
##xmlinput.bind('<(>', par2)
xmlsearch.focus_set()
xmlsearch.bind('<Return>', xmlgetfile)
Knapp.config(command=Bruteforce)
PIKnapp.config(command=Pi)
Socket.config(command=showsocket)
PYA.config(command=MouseMovement)
KUA.config(command=moo)
TRIANGLE.config(command=Triangle)
PASSWORD.config(command=CanShow)
SocketLog.focus_set()
SocketLog.bind('<Return>', getsocket)
MagicBall.config(command=ball)
Login.config(command=ShowLogin)
Back.config(command=Return)
LogOut.config(command=Logout)
Lore.config(command=Monster)
html.config(command=hail)
bb.config(command=returnmenu)
xmlreturn.config(command=returnxml)
Protonclear.config(command=cleanproton)
Protoncmd.config(command=Basic.List)
xmlclear.config(command=cleanxml)
xmlsave.config(command=savexml)
##Server
##Connect
##GO
differ.config(command=retaken)
begone.config(command=taken)
LTI.focus_set()
LTI.bind('<Return>', Get)
##Packing
Master.grid(sticky="WENS")
##  Frame 1
html.grid(sticky="WE")
frame.grid(sticky="W")
frame.grid_propagate(0)
Socket.grid(sticky="WE")
Knapp.grid(sticky="WE")
PYA.grid(sticky="WE")
##  Frame 2
Mframe.grid(sticky="W")
Mframe.grid_propagate(0)
PIKnapp.grid(sticky="WE")
PASSWORD.grid(sticky="WE")
## Login
Login.grid(sticky="W")
LoginFrame.grid()
LTL.grid()
LTI.grid()
Back.grid()
## Games
Games.grid(sticky="WE")
Games.grid_propagate(0)
KUA.grid(sticky="WE")
TRIANGLE.grid(sticky="WE")
MagicBall.grid(sticky="WE")
Lore.grid(sticky="WE")
## Misc
Update.grid(sticky="WE")
## Proto Executor
ProtonGUI.grid(sticky="WENS")
ProtonLabel.grid(row=1, sticky="WE")
ProtonInput.grid(row=2, sticky="WE")
ProtonOutput.grid(row=3, sticky="WES", pady="20")
Protonclear.grid(row=4, sticky="W")
LogOut.grid(row=4)
Protoncmd.grid(row=4,sticky="E")
##SOcket Gui
SocketGUI.grid(sticky="WENS")
SocketGUI.grid_propagate(0)
Server.grid(sticky="W", row=1, column=1)
SocketLog.grid(row=4, column=1, sticky="W")
bb.grid(column=1, row=5)
SocketEntry.grid(sticky="W", row=3, column=1)
Connect.grid(row=1, column=1)
GO.grid(sticky="E", row=1, column=1)
begone.grid(sticky="W", row=2, column=1)
differ.grid(row=2, column=1)
##---XML----
xmlGUI.grid(sticky="WENS")
xmllabel.grid(row=1,sticky="WE")
xmlsearch.grid(row=2,sticky="WE")
xmlinput.grid(row=3,sticky="WE")
xmlclear.grid(row=4,sticky="W")
xmlreturn.grid(row=4)
xmlsave.grid(row=4, sticky="E")
##-----
SocketGUI.grid_remove()
ProtonGUI.grid_remove()
xmlGUI.grid_remove()
##---------------
##After functions
LoginFrame.grid_remove()
username = LTL.get()
password = LTI.get()
root.mainloop()