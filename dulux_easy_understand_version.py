
from tkinter import *
from tkinter import messagebox
import sqlite3

# #Declaring conand Creating Cursor
# con = sqlite3.connect('dulux.db')
# cur = con.cursor()

# #Declaring Table
# cur.execute("""CREATE TABLE IF NOT EXISTS maintable(idnote TEXT, mainhead TEXT)""")

# #Inserting Table Fixed Values
# cur.execute("INSERT INTO maintable VALUES('V','Velvet Touch Diamond Glow')")
# cur.execute("INSERT INTO maintable VALUES('W','Weather Shield Max')")
# cur.execute("INSERT INTO maintable VALUES('D','Dulux Super Gloss 5 in 1')")
# cur.execute("INSERT INTO maintable VALUES('C','Colorant')")

# #Creating Mainlist with For Loop
# cur.execute("SELECT * FROM maintable")
# metadatamain = cur.fetchall()
# mainlist = []
# for item in metadatamain:
#     mainlist.append(item[1])

# #-----------------------------------Creating Table for Velvet-------------------------------------
# con.execute("""CREATE TABLE IF NOT EXISTS velvettable(
#                 idnode TEXT,
#                 vnode TEXT,
#                 vnumber TEXT
#             )""")

# #Adding all values in Velvet Table
# vlistvalues = [('V','V90','90'),('V','V92','92'),('V','V94','94'),('V','V95','95'),('V','V96','96'),('V','V97','97')]
# con.executemany("INSERT INTO velvettable VALUES (?,?,?)",vlistvalues)

# #Creating Sub List for Velvet
# cur.execute("SELECT * FROM velvettable")
# velvetdata = cur.fetchall()
# velvetlist = []
# for item in velvetdata:
#     velvetlist.append(item[1])

# #Creating SUB Table for each Velvet
# con.execute("""CREATE TABLE IF NOT EXISTS  vsubtable(
#                 idnode TEXT,
#                 vnode TEXT,
#                 subcatagory TEXT,
#                 quantity INT
#             )""")

# #Adding all values in sub table
# vsubtablevalues = [('V','V90','1 Liter V90',100),('V','V90','4 Liter V90',100),('V','V90','10 Liter V90',100),('V','V90','20 Liter V90',100),
#                 ('V','V92','1 Liter V92',100),('V','V92','4 Liter V92',100),('V','V92','10 Liter V92',100),('V','V92','20 Liter V92',100),
#                 ('V','V94','1 Liter V94',100),('V','V94','4 Liter V94',100),
#                 ('V','V95','1 Liter V95',100),('V','V95','4 Liter V95',100),
#                 ('V','V96','1 Liter V96',100),('V','V96','4 Liter V96',100),
#                 ('V','V97','1 Liter V97',100),('V','V97','4 Liter V97',100)
#                 ]
# con.executemany("INSERT INTO vsubtable VALUES (?,?,?,?)",vsubtablevalues)

# #Creating Sub Table list for Velvet Table
# cur.execute("SELECT * FROM vsubtable")
# vsubtabledata = cur.fetchall()
# vsubtablelist = []
# for item in vsubtabledata:
#     vsubtablelist.append(item[2])


# #---------------------------------------------Creating Table for Weather-------------------------------
# con.execute("""CREATE TABLE IF NOT EXISTS weathertable(
#                 idnode TEXT,
#                 wnode TEXT,
#                 wnumber TEXT
#             )""")

# #Adding all values in Weather Table
# wlistvalues = [('W','W90','90'),('W','W92','92'),('W','W94','94'),('W','W95','95'),('W','W97','97'),('W','W98','98')]
# con.executemany("INSERT INTO weathertable VALUES (?,?,?)",wlistvalues)

# #Creating Sub List for Weather
# cur.execute("SELECT * FROM weathertable")
# weatherdata = cur.fetchall()
# weatherlist = []
# for item in weatherdata:
#     weatherlist.append(item[1])

# #Creating SUB Table for each Weather
# con.execute("""CREATE TABLE IF NOT EXISTS  wsubtable(
#                 idnode TEXT,
#                 wnode TEXT,
#                 subcatagory TEXT,
#                 quantity INT
#             )""")

# #Adding all values in sub table
# wsubtablevalues = [('W','W90','1 Liter W90',100),('W','W90','4 Liter W90',100),('W','W90','10 Liter W90',100),('W','W90','20 Liter W90',100),
#                 ('W','W92','1 Liter W92',100),('W','W92','4 Liter W92',100),('W','W92','10 Liter W92',100),('W','W92','20 Liter W92',100),
#                 ('W','W94','1 Liter W94',100),('W','W94','4 Liter W94',100),('W','W94','10 Liter W94',100),('W','W94','20 Liter W94',100),
#                 ('W','W95','1 Liter W95',100),('W','W95','4 Liter W95',100),('W','W95','10 Liter W95',100),('W','W95','20 Liter W95',100),
#                 ('W','W97','1 Liter W97',100),('W','W97','4 Liter W97',100),('W','W97','10 Liter W97',100),('W','W97','20 Liter W97',100),
#                 ('W','W98','1 Liter W98',100),('W','W98','4 Liter W98',100),('W','W98','10 Liter W98',100),('W','W98','20 Liter W98',100)
#                 ]
# con.executemany("INSERT INTO wsubtable VALUES (?,?,?,?)",wsubtablevalues)

# #Creating Sub Table list for Weather Table
# cur.execute("SELECT * FROM wsubtable")
# wsubtabledata = cur.fetchall()
# wsubtablelist = []
# for item in wsubtabledata:
#     wsubtablelist.append(item[2])


# #-----------------------------------------------------Creating Table for Dulux---------------------------------------------------
# con.execute("""CREATE TABLE IF NOT EXISTS duluxtable(
#                 idnode TEXT,
#                 dnode TEXT,
#                 dname TEXT
#             )""")

# #Adding all values in Dulux Table
# dlistvalues = [('D','Dwhite','White'),('D','Dblack','Black'),('D','Dgoldenbrown','Golden Brown'),('D','Dphirozablue','Phiroza Blue'),
#                 ('D','Damethystshower','Amethyst Shower'),('D','Dskyblue','Sky BLue'),('D','Dmintgreen','Mint Green'),('D','Dpalecream','Pale Cream'),
#                 ('D','Dportuguseblue','Portuguse Blue'),('D','Daquamerine','Aqua Merine'),('D','Dmidbuff','Mid Buff'),('D','Droyalivory','Royal Ivory')]
# con.executemany("INSERT INTO duluxtable VALUES (?,?,?)",dlistvalues)

# #Creating Sub List for Dulux
# cur.execute("SELECT * FROM duluxtable")
# duluxdata = cur.fetchall()
# duluxlist = []
# for item in duluxdata:
#     duluxlist.append(item[1])

# #Creating SUB Table for each Dulux
# con.execute("""CREATE TABLE IF NOT EXISTS  dsubtable(
#                 idnode TEXT,
#                 dnode TEXT,
#                 subcatagory TEXT,
#                 quantity INT
#             )""")

# #Adding all values in sub table
# dsubtablevalues = [('D','Dwhite','4 Liter Dwhite',100),('D','Dwhite','1 Liter Dwhite',100),('D','Dwhite','500 ML Dwhite',100),
#                     ('D','Dblack','4 Liter Dblack',100),('D','Dblack','1 Liter Dblack',100),('D','Dblack','500 ML Dblack',100),
#                     ('D','Dgoldenbrown','4 Liter dgoldenbrown',100),('D','Dgoldenbrown','1 Liter Dgoldenbrown',100),('D','Dgoldenbrown','500 ML Dgoldenbrown',100),
#                     ('D','Dphirozablue','4 Liter Dphirozablue',100),('D','Dphirozablue','1 Liter Dphirozablue',100),('D','Dphirozablue','500 ML Dphirozablue',100),
#                     ('D','Damethystshower','4 Liter Damethystshower',100),('D','Damethystshower','1 Liter Damethystshower',100),('D','Damethystshower','500 ML Damethystshower',100),
#                     ('D','Dskyblue','4 Liter Dskyblue',100),('D','Dskyblue','1 Liter Dskyblue',100),('D','Dskyblue','500 ML Dskyblue',100),
#                     ('D','Dmintgreen','4 Liter Dmintgreen',100),('D','Dmintgreen','1 Liter Dmintgreen',100),('D','Dmintgreen','500 ML Dmintgreen',100),
#                     ('D','Dpalecream','4 Liter Dpalecream',100),('D','Dpalecream','1 Liter Dpalecream',100),('D','Dpalecream','500 ML Dpalecream',100),
#                     ('D','Dportuguseblue','4 Liter Dportuguseblue',100),('D','Dportuguseblue','1 Liter Dportuguseblue',100),('D','Dportuguseblue','500 ML Dportuguseblue',100),
#                     ('D','Daquamerine','4 Liter Daquamerine',100),('D','Daquamerine','1 Liter Daquamerine',100),('D','Daquamerine','500 ML Daquamerine',100),
#                     ('D','Dmidbuff','4 Liter Dmidbuff',100),('D','Dmidbuff','1 Liter Dmidbuff',100),('D','Dmidbuff','500 ML Dmidbuff',100),
#                     ('D','Droyalivory','4 Liter Droyalivory',100),('D','Droyalivory','1 Liter Droyalivory',100),('D','Droyalivory','500 ML Droyalivory',100)
#                 ]
# con.executemany("INSERT INTO dsubtable VALUES (?,?,?,?)",dsubtablevalues)

# #Creating Sub Table list for Dulux Table
# cur.execute("SELECT * FROM dsubtable")
# dsubtabledata = cur.fetchall()
# dsubtablelist = []
# for item in dsubtabledata:
#     dsubtablelist.append(item[2])


# #---------------------------------------------------------Creating Table for Colorant--------------------------------------------------
# con.execute("""CREATE TABLE IF NOT EXISTS coloranttable(
#                 idnode TEXT,
#                 cnode TEXT,
#                 cname TEXT,
#                 quantity INT
#             )""")

# #Adding all values in Colorant Table
# clistvalues = [('C','CYOX','YOX 1 LITER',100),('C','CLFY','LFY 1 LITER',100),('C','CGRL','GRL 1 LITER',100),('C','CTBL','TBL 1 LITER',100),
#                 ('C','CWHT','WHT 1 LITER',100),('C','CMAG','MAG 1 LITER',100),('C','CFFR','FFR 1 LITER',100),('C','CBLK','BLK 1 LITER',100),('C','COXR','OXR 1 LITER',100)
#             ]
# con.executemany("INSERT INTO coloranttable VALUES (?,?,?,?)",clistvalues)

# #Creating Sub List for Colorant
# cur.execute("SELECT * FROM coloranttable")
# colorantdata = cur.fetchall()
# colorantlist = []
# for item in colorantdata:
#     colorantlist.append(item[2])

# con.commit()
# con.close()

# *#$$$$$$$$$##$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$################$$$$$$$$$$$$$$$$$$$$$#################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# *#$$$$$$$$$##$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$################$$$$$$$$$$$$$$$$$$$$$#################$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#==================================================All Time DataBase Running System=================================================================

con = sqlite3.connect('dulux.db')
cur = con.cursor()
curupdate = con.cursor()

#Creating Mainlist with For Loop
cur.execute("SELECT * FROM maintable")
metadatamain = cur.fetchall()
mainlist = []
for item in metadatamain:
    mainlist.append(item[1])

#Creating Sub List for Velvet
cur.execute("SELECT * FROM velvettable")
velvetdata = cur.fetchall()
velvetlist = []
for item in velvetdata:
    velvetlist.append(item[1])

#Creating Sub Table list for Velvet Table
cur.execute("SELECT * FROM vsubtable")
vsubtabledata = cur.fetchall()
vsubtablelist = []
for item in vsubtabledata:
    vsubtablelist.append(item[2])

#Creating Sub List for Weather
cur.execute("SELECT * FROM weathertable")
weatherdata = cur.fetchall()
weatherlist = []
for item in weatherdata:
    weatherlist.append(item[1])

#Creating Sub Table list for Weather Table
cur.execute("SELECT * FROM wsubtable")
wsubtabledata = cur.fetchall()
wsubtablelist = []
for item in wsubtabledata:
    wsubtablelist.append(item[2])

#Creating Sub List for Dulux
cur.execute("SELECT * FROM duluxtable")
duluxdata = cur.fetchall()
duluxlist = []
for item in duluxdata:
    duluxlist.append(item[1])

#Creating Sub Table list for Dulux Table
cur.execute("SELECT * FROM dsubtable")
dsubtabledata = cur.fetchall()
dsubtablelist = []
for item in dsubtabledata:
    dsubtablelist.append(item[2])

#Creating Sub List for Colorant
cur.execute("SELECT * FROM coloranttable")
colorantdata = cur.fetchall()
colorantlist = []
for item in colorantdata:
    colorantlist.append(item[2])


####################################################################################################################################################
####################################################################################################################################################

#Defining Sell Page
def sell():
    newwindow = Toplevel(mainroot, bg='#F7E8F8')
    newwindow.title('Sell Page')
    newwindow.geometry('900x650')
    newwindow.minsize(900,650)
    newwindow.maxsize(900,650)
#Defining frames_______________________________________________________
    frameoption1 = LabelFrame(newwindow,bg='#EECFEF', text="Main Menu")
    frameoption1.pack(pady=20)
    frameoption2 = LabelFrame(newwindow,bg='#EECFEF', text="Sub Menu")
    frameoption2.pack(pady=10)
    frame = LabelFrame(newwindow,bg='#EECFEF', text="Details Below :")
    frame.pack(pady=10)
    framesubmit = LabelFrame(newwindow,bg='#EECFEF',text='')
    framesubmit.pack(pady=10)
#Defining Functions to Refresh the frames____________________________
    def clearframe2():
        for f2 in frameoption2.winfo_children():
            f2.destroy()
    def clearframe():
        for a in frame.winfo_children():
            a.destroy()
    def clearframe1():
        for f in framesubmit.winfo_children():
            f.destroy()
#Defining Sell Events
    def sellselected(event):
        clearframe2()
#Defining Velvet Option Menu
        if sellclicked.get()=='Velvet Touch Diamond Glow':       
#Defining Sell item list function
            def vsubsell(clicked):
                clearframe()
                clearframe1()
###---------------fetching Data of Table---------------------------
                cur.execute("SELECT * FROM vsubtable")
                velvetvirtual = cur.fetchall()
#Creating Blank Dictionary for storing Data
                mydictv = {}
                gotvclicked = vclicked.get()
                usednumberv = 1
#-------------------Looping through Data and generating Lables And Entry Widgets------------
                for i in velvetvirtual:
                    if gotvclicked in i:
                        label = Label(frame,bg='#5356BF',fg='white', text=i[2]).grid(row=usednumberv, column=2, padx=25, pady=30)
                        mydictv.update({i[2]:IntVar()})
                        entryurl = 'entry' + str(usednumberv)
                        entryurl = Entry(frame, textvariable=mydictv[i[2]]).grid(row=usednumberv,column=3, padx=50, pady=30)
                        label1 = Label(frame,bg='#E55E1E',fg='black', text=f'Stock at Present: {i[3]}').grid(row=usednumberv, column=4,padx=60,pady=30)
                        usednumberv += 1
#Defining Function that will response after submitting Data
                        def vsubmitted():
#Looping through Dictionary to get Values_______________________________________
                            for key, value in mydictv.items():
#Looping through List to get the stored value___________________________________
                                for locator in velvetvirtual:
#Matching the Entry keys with the List Keys_____________________________________
                                    if key==locator[2]:
#Converting IntVar to int_______________________________________________________
                                        intvaluev = value.get()
#Deducting and saving the new value in the dictionary___________________________
                                        mydictv.update({key:(locator[3]-intvaluev)})
#Looping with new value to update the database__________________________________
                            for key1, value1 in mydictv.items(): 
                                idv=key1
                                amountv=value1
                                curupdate.execute("""UPDATE vsubtable SET 
                                quantity=? WHERE subcatagory=?""", (amountv,idv))
#Commiting the update___________________________________________________________
                            con.commit()
#Recalling the Sell Item Function to Refresh the Sell Frame
                            vsubsell(clicked)
#__________________-Button for Submitting the Entered Data-_______________________
                button1 = Button(framesubmit, bg='#86D07D', text='Submit')
                button1.grid()
                button1['command'] = vsubmitted

#Generating Option Menu for sub Velvet Menu
            vclicked = StringVar()
            vclicked.set('Choose One From The Sub-Menu')
            labelsell = Label(frameoption2, bg='#F7E8F8',text='Select One: ').grid(row=0, column=0)
            vdrop = OptionMenu(frameoption2, vclicked, *velvetlist, command=vsubsell)
            vdrop.grid(row=0,column=1)       
            
              
                
#Defining Weather OptionMenu
        elif sellclicked.get()=='Weather Shield Max':
#Defining Sell item list function
            def wsubsell(clicked):
                clearframe()
                clearframe1()
###---------------fetching Data of Table---------------------------
                cur.execute("SELECT * FROM wsubtable")
                weathervirtual = cur.fetchall()
#Creating Blank Dictionary for storing Data
                mydictw = {}
                gotwclicked = wclicked.get()
                usednumberw = 1
#-------------------Looping through Data and generating Lables And Entry Widgets------------
                for i in weathervirtual:
                    if gotwclicked in i:
                        label = Label(frame,bg='#5356BF',fg='white', text=i[2]).grid(row=usednumberw, column=2, padx=25, pady=30)
                        mydictw.update({i[2]:IntVar()})
                        entryurl = 'entry' + str(usednumberw)
                        entryurl = Entry(frame, textvariable=mydictw[i[2]]).grid(row=usednumberw,column=3, padx=50, pady=30)
                        label1 = Label(frame,bg='#E55E1E',fg='black', text=f'Stock at Present: {i[3]}').grid(row=usednumberw, column=4,padx=60,pady=30)
                        usednumberw += 1
#Defining Function that will response after submitting Data
                        def wsubmitted():
#Looping through Dictionary to get Values_______________________________________
                            for key, value in mydictw.items():
#Looping through List to get the stored value___________________________________
                                for locator in weathervirtual:
#Matching the Entry keys with the List Keys_____________________________________
                                    if key==locator[2]:
#Converting IntVar to int_______________________________________________________
                                        intvaluew = value.get()
#Deducting and saving the new value in the dictionary___________________________
                                        mydictw.update({key:(locator[3]-intvaluew)})
#Looping with new value to update the database__________________________________
                            for key1, value1 in mydictw.items(): 
                                idw=key1
                                amountw=value1
                                curupdate.execute("""UPDATE wsubtable SET 
                                quantity=? WHERE subcatagory=?""", (amountw,idw))
#Commiting the update___________________________________________________________
                            con.commit()
#Recalling the Sell Item Function to Refresh the Sell Frame
                            wsubsell(clicked)
#__________________-Button for Submitting the Entered Data-_______________________
                button1 = Button(framesubmit, bg='#86D07D', text='Submit')
                button1.grid()
                button1['command'] = wsubmitted
                
            wclicked = StringVar()
            wclicked.set('Choose One')
            labelsell = Label(frameoption2, bg='#F7E8F8',text='Select One: ').grid(row=0, column=0)
            wdrop = OptionMenu(frameoption2, wclicked, *weatherlist, command=wsubsell).grid(row=0, column=1)
            
            
            
# #Defining DuluOptionMenu
        elif sellclicked.get()=='Dulux Super Gloss 5 in 1':
#Defining Sell item list function
            def dsubsell(clicked):
                clearframe()
                clearframe1()
###---------------fetching Data of Table---------------------------
                cur.execute("SELECT * FROM dsubtable")
                duluxvirtual = cur.fetchall()
#Creating Blank Dictionary for storing Data
                mydictd = {}
                gotdclicked = dclicked.get()
                usednumberd = 1
#-------------------Looping through Data and generating Lables And Entry Widgets------------
                for i in duluxvirtual:
                    if gotdclicked in i:
                        label = Label(frame,bg='#5356BF',fg='white', text=i[2]).grid(row=usednumberd, column=2, padx=25, pady=30)
                        mydictd.update({i[2]:IntVar()})
                        entryurl = 'entry' + str(usednumberd)
                        entryurl = Entry(frame, textvariable=mydictd[i[2]]).grid(row=usednumberd,column=3, padx=50, pady=30)
                        label1 = Label(frame,bg='#E55E1E',fg='black', text=f'Stock at Present: {i[3]}').grid(row=usednumberd, column=4,padx=60,pady=30)
                        usednumberd += 1
#Defining Function that will response after submitting Data
                        def dsubmitted():
#Looping through Dictionary to get Values_______________________________________
                            for key, value in mydictd.items():
#Looping through List to get the stored value___________________________________
                                for locator in duluxvirtual:
#Matching the Entry keys with the List Keys_____________________________________
                                    if key==locator[2]:
#Converting IntVar to int_______________________________________________________
                                        intvalued = value.get()
#Deducting and saving the new value in the dictionary___________________________
                                        mydictd.update({key:(locator[3]-intvalued)})
#Looping with new value to update the database__________________________________
                            for key1, value1 in mydictd.items(): 
                                idd=key1
                                amountd=value1
                                curupdate.execute("""UPDATE dsubtable SET 
                                quantity=? WHERE subcatagory=?""", (amountd,idd))
#Commiting the update___________________________________________________________
                            con.commit()
#Recalling the Sell Item Function to Refresh the Sell Frame
                            dsubsell(clicked)
#__________________-Button for Submitting the Entered Data-_______________________
                button1 = Button(framesubmit, bg='#86D07D', text='Submit')
                button1.grid()
                button1['command'] = dsubmitted
                
            dclicked = StringVar()
            dclicked.set('Choose One')
            labelsell = Label(frameoption2, bg='#F7E8F8',text='Select One: ').grid(row=0, column=0)
            ddrop = OptionMenu(frameoption2, dclicked, *duluxlist, command=dsubsell).grid(row=0, column=1)
            
            
# #Defining Colourant Option Menu
        else:
#Defining Sell item list function
            def csubsell(clicked):
                clearframe()
                clearframe1()
###---------------fetching Data of Table---------------------------
                cur.execute("SELECT * FROM coloranttable")
                colorantvirtual = cur.fetchall()
#Creating Blank Dictionary for storing Data
                mydictc = {}
                gotcclicked = cclicked.get()
                usednumberc = 1
#-------------------Looping through Data and generating Lables And Entry Widgets------------
                for i in colorantvirtual:
                    if gotcclicked in i:
                        label = Label(frame,bg='#5356BF',fg='white', text=i[2]).grid(row=usednumberc, column=2, padx=25, pady=30)
                        mydictc.update({i[2]:IntVar()})
                        entryurl = 'entry' + str(usednumberc)
                        entryurl = Entry(frame, textvariable=mydictc[i[2]]).grid(row=usednumberc,column=3, padx=50, pady=30)
                        label1 = Label(frame,bg='#E55E1E',fg='black', text=f'Stock at Present: {i[3]}').grid(row=usednumberc, column=4,padx=60,pady=30)
                        usednumberc += 1
#Defining Function that will response after submitting Data
                        def csubmitted():
#Looping through Dictionary to get Values_______________________________________
                            for key, value in mydictc.items():
#Looping through List to get the stored value___________________________________
                                for locator in colorantvirtual:
#Matching the Entry keys with the List Keys_____________________________________
                                    if key==locator[2]:
#Converting IntVar to int_______________________________________________________
                                        intvaluec = value.get()
#Deducting and saving the new value in the dictionary___________________________
                                        mydictc.update({key:(locator[3]-intvaluec)})
#Looping with new value to update the database__________________________________
                            for key1, value1 in mydictc.items(): 
                                idc=key1
                                amountc=value1
                                curupdate.execute("""UPDATE coloranttable SET 
                                quantity=? WHERE cname=?""", (amountc,idc))
#Commiting the update___________________________________________________________
                            con.commit()
#Recalling the Sell Item Function to Refresh the Sell Frame
                            csubsell(clicked)
#__________________-Button for Submitting the Entered Data-_______________________
                button1 = Button(framesubmit, bg='#86D07D', text='Submit')
                button1.grid()
                button1['command'] = csubmitted
                
            cclicked = StringVar()
            cclicked.set('Choose One')
            labelsell = Label(frameoption2, bg='#F7E8F8',text='Select One: ').grid(row=0, column=0)
            cdrop = OptionMenu(frameoption2, cclicked, *colorantlist, command=csubsell).grid(row=0, column=1)
            
    
#Sell Page First Option
    sellclicked = StringVar()
    sellclicked.set('Choose One From The Main Menu')
    labelsell = Label(frameoption1,bg='#F7E8F8', text='Select One: ').grid(row=0, column=0)
    selldrop = OptionMenu(frameoption1, sellclicked, *mainlist,command=sellselected)
    selldrop.grid(row=0,column=1)




##Defining Status Page---------------------------------------------------------------------------
def status():
    newwindow = Toplevel(mainroot, bg='#F7E8F8')
    newwindow.title('Status Page')
    newwindow.geometry('900x650')
    newwindow.minsize(900,650)
    newwindow.maxsize(900,650)
#Defining frames_______________________________________________________
    frameoption1 = LabelFrame(newwindow,bg='#EECFEF', text="Main Menu")
    frameoption1.pack(pady=20)
    frameoption2 = LabelFrame(newwindow,bg='#EECFEF', text="Sub Menu")
    frameoption2.pack(pady=10)
    frame = LabelFrame(newwindow,bg='#EECFEF', text="Details Below :")
    frame.pack(pady=10)
    framesubmit = LabelFrame(newwindow,bg='#EECFEF',text='')
    framesubmit.pack(pady=10)
#Defining Functions to Refresh the frames____________________________
    def clearframe2():
        for f2 in frameoption2.winfo_children():
            f2.destroy()
    def clearframe():
        for a in frame.winfo_children():
            a.destroy()
    def clearframe1():
        for f in framesubmit.winfo_children():
            f.destroy()
#Defining Sell Events
    def statusselected(event):
        clearframe2()
#Defining Velvet Option Menu
        if statusclicked.get()=='Velvet Touch Diamond Glow':       
#Defining Sell item list function
            def vsubstatus(clicked):
                clearframe()
                clearframe1()
###---------------fetching Data of Table---------------------------
                cur.execute("SELECT * FROM vsubtable")
                velvetvirtual = cur.fetchall()
#Creating Blank Dictionary for storing Data
                gotvclicked = vclicked.get()
                usednumberv = 1
#-------------------Looping through Data and generating Lables And Entry Widgets------------
                for i in velvetvirtual:
                    if gotvclicked in i:
                        label = Label(frame,bg='#5356BF',fg='white', text=i[2]).grid(row=usednumberv, column=2, padx=25, pady=30)
                        label1 = Label(frame,bg='#E55E1E',fg='black', text=f'Stock at Present: {i[3]}').grid(row=usednumberv, column=4,padx=60,pady=30)
                        usednumberv += 1

#Generating Option Menu for sub Velvet Menu
            vclicked = StringVar()
            vclicked.set('Choose One From The Sub-Menu')
            labelsell = Label(frameoption2, bg='#F7E8F8',text='Select One: ').grid(row=0, column=0)
            vdrop = OptionMenu(frameoption2, vclicked, *velvetlist, command=vsubstatus)
            vdrop.grid(row=0,column=1) 

#Defining Weather OptionMenu            
        elif statusclicked.get()=='Weather Shield Max':
            #Defining Sell item list function
            def wsubstatus(clicked):
                clearframe()
                clearframe1()
###---------------fetching Data of Table---------------------------
                cur.execute("SELECT * FROM wsubtable")
                weathervirtual = cur.fetchall()
#Creating Blank Dictionary for storing Data
                gotwclicked = wclicked.get()
                usednumberw = 1
#-------------------Looping through Data and generating Lables And Entry Widgets------------
                for i in weathervirtual:
                    if gotwclicked in i:
                        label = Label(frame,bg='#5356BF',fg='white', text=i[2]).grid(row=usednumberw, column=2, padx=25, pady=30)
                        label1 = Label(frame,bg='#E55E1E',fg='black', text=f'Stock at Present: {i[3]}').grid(row=usednumberw, column=4,padx=60,pady=30)
                        usednumberw += 1

#Generating Option Menu for sub Velvet Menu
            wclicked = StringVar()
            wclicked.set('Choose One From The Sub-Menu')
            labelsell = Label(frameoption2, bg='#F7E8F8',text='Select One: ').grid(row=0, column=0)
            wdrop = OptionMenu(frameoption2, wclicked, *weatherlist, command=wsubstatus)
            wdrop.grid(row=0,column=1) 
            
#Defining Dulux OptionMenu            
        elif statusclicked.get()=='Dulux Super Gloss 5 in 1':
            #Defining Sell item list function
            def dsubstatus(clicked):
                clearframe()
                clearframe1()
###---------------fetching Data of Table---------------------------
                cur.execute("SELECT * FROM dsubtable")
                duluxvirtual = cur.fetchall()
#Creating Blank Dictionary for storing Data
                gotdclicked = dclicked.get()
                usednumberd = 1
#-------------------Looping through Data and generating Lables And Entry Widgets------------
                for i in duluxvirtual:
                    if gotdclicked in i:
                        label = Label(frame,bg='#5356BF',fg='white', text=i[2]).grid(row=usednumberd, column=2, padx=25, pady=30)
                        label1 = Label(frame,bg='#E55E1E',fg='black', text=f'Stock at Present: {i[3]}').grid(row=usednumberd, column=4,padx=60,pady=30)
                        usednumberd += 1

#Generating Option Menu for sub Velvet Menu
            dclicked = StringVar()
            dclicked.set('Choose One From The Sub-Menu')
            labelsell = Label(frameoption2, bg='#F7E8F8',text='Select One: ').grid(row=0, column=0)
            ddrop = OptionMenu(frameoption2, dclicked, *duluxlist, command=dsubstatus)
            ddrop.grid(row=0,column=1)
            
            
        else:
#Defining Sell item list function
            def csubstatus(clicked):
                clearframe()
                clearframe1()
###---------------fetching Data of Table---------------------------
                cur.execute("SELECT * FROM coloranttable")
                colorantvirtual = cur.fetchall()
#Creating Blank Dictionary for storing Data
                gotcclicked = cclicked.get()
                usednumberc = 1
#-------------------Looping through Data and generating Lables And Entry Widgets------------
                for i in colorantvirtual:
                    if gotcclicked in i:
                        label = Label(frame,bg='#5356BF',fg='white', text=i[2]).grid(row=usednumberc, column=2, padx=25, pady=30)
                        label1 = Label(frame,bg='#E55E1E',fg='black', text=f'Stock at Present: {i[3]}').grid(row=usednumberc, column=4,padx=60,pady=30)
                        usednumberc += 1

#Generating Option Menu for sub Velvet Menu
            cclicked = StringVar()
            cclicked.set('Choose One From The Sub-Menu')
            labelsell = Label(frameoption2, bg='#F7E8F8',text='Select One: ').grid(row=0, column=0)
            cdrop = OptionMenu(frameoption2, cclicked, *colorantlist, command=csubstatus)
            cdrop.grid(row=0,column=1)
            
    #Status Page First Option
    statusclicked = StringVar()
    statusclicked.set('Choose One From The Main Menu')
    labelsell = Label(frameoption1,bg='#F7E8F8', text='Select One: ').grid(row=0, column=0)
    statusdrop = OptionMenu(frameoption1, statusclicked, *mainlist,command=statusselected)
    statusdrop.grid(row=0,column=1)





#Defining Stock Page
def stock():
    newwindow = Toplevel(mainroot, bg='#F7E8F8')
    newwindow.title('Sell Page')
    newwindow.geometry('900x650')
    newwindow.minsize(900,650)
    newwindow.maxsize(900,650)
#Defining frames_______________________________________________________
    frameoption1 = LabelFrame(newwindow,bg='#EECFEF', text="Main Menu")
    frameoption1.pack(pady=20)
    frameoption2 = LabelFrame(newwindow,bg='#EECFEF', text="Sub Menu")
    frameoption2.pack(pady=10)
    frame = LabelFrame(newwindow,bg='#EECFEF', text="Details Below :")
    frame.pack(pady=10)
    framesubmit = LabelFrame(newwindow,bg='#EECFEF',text='')
    framesubmit.pack(pady=10)
#Defining Functions to Refresh the frames____________________________
    def clearframe2():
        for f2 in frameoption2.winfo_children():
            f2.destroy()
    def clearframe():
        for a in frame.winfo_children():
            a.destroy()
    def clearframe1():
        for f in framesubmit.winfo_children():
            f.destroy()
#Defining Sell Events
    def stockselected(event):
        clearframe2()
#Defining Velvet Option Menu
        if stockclicked.get()=='Velvet Touch Diamond Glow':       
#Defining Sell item list function
            def vsubstock(clicked):
                clearframe()
                clearframe1()
###---------------fetching Data of Table---------------------------
                cur.execute("SELECT * FROM vsubtable")
                velvetvirtual = cur.fetchall()
#Creating Blank Dictionary for storing Data
                mydictv = {}
                gotvclicked = vclicked.get()
                usednumberv = 1
#-------------------Looping through Data and generating Lables And Entry Widgets------------
                for i in velvetvirtual:
                    if gotvclicked in i:
                        label = Label(frame,bg='#5356BF',fg='white', text=i[2]).grid(row=usednumberv, column=2, padx=25, pady=30)
                        mydictv.update({i[2]:IntVar()})
                        entryurl = 'entry' + str(usednumberv)
                        entryurl = Entry(frame, textvariable=mydictv[i[2]]).grid(row=usednumberv,column=3, padx=50, pady=30)
                        label1 = Label(frame,bg='#E55E1E',fg='black', text=f'Stock at Present: {i[3]}').grid(row=usednumberv, column=4,padx=60,pady=30)
                        usednumberv += 1
#Defining Function that will response after submitting Data
                        def vsubmitted():
#Looping through Dictionary to get Values_______________________________________
                            for key, value in mydictv.items():
#Looping through List to get the stored value___________________________________
                                for locator in velvetvirtual:
#Matching the Entry keys with the List Keys_____________________________________
                                    if key==locator[2]:
#Converting IntVar to int_______________________________________________________
                                        intvaluev = value.get()
#Deducting and saving the new value in the dictionary___________________________
                                        mydictv.update({key:(locator[3]+intvaluev)})
#Looping with value to update the database__________________________________
                            for key1, value1 in mydictv.items():
                                idv=key1
                                amountv=value1
                                curupdate.execute("""UPDATE vsubtable SET 
                                quantity=? WHERE subcatagory=?""", (amountv,idv))
#Commiting the update___________________________________________________________
                            con.commit()
#Recalling the Sell Item Function to Refresh the Sell Frame
                            vsubstock(clicked)
#__________________-Button for Submitting the Entered Data-_______________________
                button1 = Button(framesubmit, bg='#86D07D', text='Submit')
                button1.grid()
                button1['command'] = vsubmitted

#Generating Option Menu for sub Velvet Menu
            vclicked = StringVar()
            vclicked.set('Choose One From The Sub-Menu')
            labelsell = Label(frameoption2, bg='#F7E8F8',text='Select One: ').grid(row=0, column=0)
            vdrop = OptionMenu(frameoption2, vclicked, *velvetlist, command=vsubstock)
            vdrop.grid(row=0,column=1)       
            
              
                
#Defining Weather OptionMenu
        elif stockclicked.get()=='Weather Shield Max':
#Defining Sell item list function
            def wsubstock(clicked):
                clearframe()
                clearframe1()
###---------------fetching Data of Table---------------------------
                cur.execute("SELECT * FROM wsubtable")
                weathervirtual = cur.fetchall()
#Creating Blank Dictionary for storing Data
                mydictw = {}
                gotwclicked = wclicked.get()
                usednumberw = 1
#-------------------Looping through Data and generating Lables And Entry Widgets------------
                for i in weathervirtual:
                    if gotwclicked in i:
                        label = Label(frame,bg='#5356BF',fg='white', text=i[2]).grid(row=usednumberw, column=2, padx=25, pady=30)
                        mydictw.update({i[2]:IntVar()})
                        entryurl = 'entry' + str(usednumberw)
                        entryurl = Entry(frame, textvariable=mydictw[i[2]]).grid(row=usednumberw,column=3, padx=50, pady=30)
                        label1 = Label(frame,bg='#E55E1E',fg='black', text=f'Stock at Present: {i[3]}').grid(row=usednumberw, column=4,padx=60,pady=30)
                        usednumberw += 1
#Defining Function that will response after submitting Data
                        def wsubmitted():
#Looping through Dictionary to get Values_______________________________________
                            for key, value in mydictw.items():
#Looping through List to get the stored value___________________________________
                                for locator in weathervirtual:
#Matching the Entry keys with the List Keys_____________________________________
                                    if key==locator[2]:
#Converting IntVar to int_______________________________________________________
                                        intvaluew = value.get()
#Deducting and saving the new value in the dictionary___________________________
                                        mydictw.update({key:(locator[3]+intvaluew)})
#Looping with value to update the database__________________________________
                            for key1, value1 in mydictw.items(): 
                                idw=key1
                                amountw=value1
                                curupdate.execute("""UPDATE wsubtable SET 
                                quantity=? WHERE subcatagory=?""", (amountw,idw))
#Commiting the update___________________________________________________________
                            con.commit()
#Recalling the Sell Item Function to Refresh the Sell Frame
                            wsubstock(clicked)
#__________________-Button for Submitting the Entered Data-_______________________
                button1 = Button(framesubmit, bg='#86D07D', text='Submit')
                button1.grid()
                button1['command'] = wsubmitted
                
            wclicked = StringVar()
            wclicked.set('Choose One')
            labelsell = Label(frameoption2, bg='#F7E8F8',text='Select One: ').grid(row=0, column=0)
            wdrop = OptionMenu(frameoption2, wclicked, *weatherlist, command=wsubstock).grid(row=0, column=1)
            
            
            
# #Defining DuluOptionMenu
        elif stockclicked.get()=='Dulux Super Gloss 5 in 1':
#Defining Sell item list function
            def dsubstock(clicked):
                clearframe()
                clearframe1()
###---------------fetching Data of Table---------------------------
                cur.execute("SELECT * FROM dsubtable")
                duluxvirtual = cur.fetchall()
#Creating Blank Dictionary for storing Data
                mydictd = {}
                gotdclicked = dclicked.get()
                usednumberd = 1
#-------------------Looping through Data and generating Lables And Entry Widgets------------
                for i in duluxvirtual:
                    if gotdclicked in i:
                        label = Label(frame,bg='#5356BF',fg='white', text=i[2]).grid(row=usednumberd, column=2, padx=25, pady=30)
                        mydictd.update({i[2]:IntVar()})
                        entryurl = 'entry' + str(usednumberd)
                        entryurl = Entry(frame, textvariable=mydictd[i[2]]).grid(row=usednumberd,column=3, padx=50, pady=30)
                        label1 = Label(frame,bg='#E55E1E',fg='black', text=f'Stock at Present: {i[3]}').grid(row=usednumberd, column=4,padx=60,pady=30)
                        usednumberd += 1
#Defining Function that will response after submitting Data
                        def dsubmitted():
#Looping through Dictionary to get Values_______________________________________
                            for key, value in mydictd.items():
#Looping through List to get the stored value___________________________________
                                for locator in duluxvirtual:
#Matching the Entry keys with the List Keys_____________________________________
                                    if key==locator[2]:
#Converting IntVar to int_______________________________________________________
                                        intvalued = value.get()
#Deducting and saving the new value in the dictionary___________________________
                                        mydictd.update({key:(locator[3]+intvalued)})
#Looping with value to update the database__________________________________
                            for key1, value1 in mydictd.items(): 
                                idd=key1
                                amountd=value1
                                curupdate.execute("""UPDATE dsubtable SET 
                                quantity=? WHERE subcatagory=?""", (amountd,idd))
#Commiting the update___________________________________________________________
                            con.commit()
#Recalling the Sell Item Function to Refresh the Sell Frame
                            dsubstock(clicked)
#__________________-Button for Submitting the Entered Data-_______________________
                button1 = Button(framesubmit, bg='#86D07D', text='Submit')
                button1.grid()
                button1['command'] = dsubmitted
                
            dclicked = StringVar()
            dclicked.set('Choose One')
            labelsell = Label(frameoption2, bg='#F7E8F8',text='Select One: ').grid(row=0, column=0)
            ddrop = OptionMenu(frameoption2, dclicked, *duluxlist, command=dsubstock).grid(row=0, column=1)
            
            
# #Defining Colourant Option Menu
        else:
#Defining Sell item list function
            def csubstock(clicked):
                clearframe()
                clearframe1()
###---------------fetching Data of Table---------------------------
                cur.execute("SELECT * FROM coloranttable")
                colorantvirtual = cur.fetchall()
#Creating Blank Dictionary for storing Data
                mydictc = {}
                gotcclicked = cclicked.get()
                usednumberc = 1
#-------------------Looping through Data and generating Lables And Entry Widgets------------
                for i in colorantvirtual:
                    if gotcclicked in i:
                        label = Label(frame,bg='#5356BF',fg='white', text=i[2]).grid(row=usednumberc, column=2, padx=25, pady=30)
                        mydictc.update({i[2]:IntVar()})
                        entryurl = 'entry' + str(usednumberc)
                        entryurl = Entry(frame, textvariable=mydictc[i[2]]).grid(row=usednumberc,column=3, padx=50, pady=30)
                        label1 = Label(frame,bg='#E55E1E',fg='black', text=f'Stock at Present: {i[3]}').grid(row=usednumberc, column=4,padx=60,pady=30)
                        usednumberc += 1
#Defining Function that will response after submitting Data
                        def csubmitted():
#Looping through Dictionary to get Values_______________________________________
                            for key, value in mydictc.items():
#Looping through List to get the stored value___________________________________
                                for locator in colorantvirtual:
#Matching the Entry keys with the List Keys_____________________________________
                                    if key==locator[2]:
#Converting IntVar to int_______________________________________________________
                                        intvaluec = value.get()
#Deducting and saving the new value in the dictionary___________________________
                                        mydictc.update({key:(locator[3]+intvaluec)})
#Looping with value to update the database__________________________________
                            for key1, value1 in mydictc.items(): 
                                idc=key1
                                amountc=value1
                                curupdate.execute("""UPDATE coloranttable SET 
                                quantity=? WHERE cname=?""", (amountc,idc))
#Commiting the update___________________________________________________________
                            con.commit()
#Recalling the Sell Item Function to Refresh the Sell Frame
                            csubstock(clicked)
#__________________-Button for Submitting the Entered Data-_______________________
                button1 = Button(framesubmit, bg='#86D07D', text='Submit')
                button1.grid()
                button1['command'] = csubmitted
                
            cclicked = StringVar()
            cclicked.set('Choose One')
            labelsell = Label(frameoption2, bg='#F7E8F8',text='Select One: ').grid(row=0, column=0)
            cdrop = OptionMenu(frameoption2, cclicked, *colorantlist, command=csubstock).grid(row=0, column=1)
            
    
#Sell Page First Option
    stockclicked = StringVar()
    stockclicked.set('Choose One From The Main Menu')
    labelstock= Label(frameoption1,bg='#F7E8F8', text='Select One: ').grid(row=0, column=0)
    stockdrop = OptionMenu(frameoption1, stockclicked, *mainlist,command=stockselected)
    stockdrop.grid(row=0,column=1)
    
    
    
#Defining Reset Page
def reset():
    newwindow = Toplevel(mainroot, bg='#F7E8F8')
    newwindow.title('Reset Page')
    newwindow.geometry('900x650')
    newwindow.minsize(900,650)
    newwindow.maxsize(900,650)
#Defining frames_______________________________________________________
    frameoption1 = LabelFrame(newwindow,bg='#EECFEF', text="Main Menu")
    frameoption1.pack(pady=20)
    frameoption2 = LabelFrame(newwindow,bg='#EECFEF', text="Sub Menu")
    frameoption2.pack(pady=10)
    frame = LabelFrame(newwindow,bg='#EECFEF', text="Details Below :")
    frame.pack(pady=10)
    framesubmit = LabelFrame(newwindow,bg='#EECFEF',text='')
    framesubmit.pack(pady=10)
#Defining Functions to Refresh the frames____________________________
    def clearframe2():
        for f2 in frameoption2.winfo_children():
            f2.destroy()
    def clearframe():
        for a in frame.winfo_children():
            a.destroy()
    def clearframe1():
        for f in framesubmit.winfo_children():
            f.destroy()
#Defining Sell Events
    def stockselected(event):
        clearframe2()
#Defining Velvet Option Menu
        if stockclicked.get()=='Velvet Touch Diamond Glow':       
#Defining Sell item list function
            def vsubstock(clicked):
                clearframe()
                clearframe1()
###---------------fetching Data of Table---------------------------
                cur.execute("SELECT * FROM vsubtable")
                velvetvirtual = cur.fetchall()
#Creating Blank Dictionary for storing Data
                mydictv = {}
                gotvclicked = vclicked.get()
                usednumberv = 1
#-------------------Looping through Data and generating Lables And Entry Widgets------------
                for i in velvetvirtual:
                    if gotvclicked in i:
                        label = Label(frame,bg='#5356BF',fg='white', text=i[2]).grid(row=usednumberv, column=2, padx=25, pady=30)
                        mydictv.update({i[2]:IntVar()})
                        entryurl = 'entry' + str(usednumberv)
                        entryurl = Entry(frame, textvariable=mydictv[i[2]]).grid(row=usednumberv,column=3, padx=50, pady=30)
                        label1 = Label(frame,bg='#E55E1E',fg='black', text=f'Stock at Present: {i[3]}').grid(row=usednumberv, column=4,padx=60,pady=30)
                        usednumberv += 1
#Defining Function that will response after submitting Data
                        def vsubmitted():
#Looping with value to update the database__________________________________
                            for key1, value1 in mydictv.items():
                                idv=key1
                                amountv=value1.get()
                                curupdate.execute("""UPDATE vsubtable SET 
                                quantity=? WHERE subcatagory=?""", (amountv,idv))
#Commiting the update___________________________________________________________
                            con.commit()
#Recalling the Sell Item Function to Refresh the Sell Frame
                            vsubstock(clicked)
#__________________-Button for Submitting the Entered Data-_______________________
                button1 = Button(framesubmit, bg='#86D07D', text='Submit')
                button1.grid()
                button1['command'] = vsubmitted

#Generating Option Menu for sub Velvet Menu
            vclicked = StringVar()
            vclicked.set('Choose One From The Sub-Menu')
            labelsell = Label(frameoption2, bg='#F7E8F8',text='Select One: ').grid(row=0, column=0)
            vdrop = OptionMenu(frameoption2, vclicked, *velvetlist, command=vsubstock)
            vdrop.grid(row=0,column=1)       
            
              
                
#Defining Weather OptionMenu
        elif stockclicked.get()=='Weather Shield Max':
#Defining Sell item list function
            def wsubstock(clicked):
                clearframe()
                clearframe1()
###---------------fetching Data of Table---------------------------
                cur.execute("SELECT * FROM wsubtable")
                weathervirtual = cur.fetchall()
#Creating Blank Dictionary for storing Data
                mydictw = {}
                gotwclicked = wclicked.get()
                usednumberw = 1
#-------------------Looping through Data and generating Lables And Entry Widgets------------
                for i in weathervirtual:
                    if gotwclicked in i:
                        label = Label(frame,bg='#5356BF',fg='white', text=i[2]).grid(row=usednumberw, column=2, padx=25, pady=30)
                        mydictw.update({i[2]:IntVar()})
                        entryurl = 'entry' + str(usednumberw)
                        entryurl = Entry(frame, textvariable=mydictw[i[2]]).grid(row=usednumberw,column=3, padx=50, pady=30)
                        label1 = Label(frame,bg='#E55E1E',fg='black', text=f'Stock at Present: {i[3]}').grid(row=usednumberw, column=4,padx=60,pady=30)
                        usednumberw += 1
#Defining Function that will response after submitting Data
                        def wsubmitted():
#Looping with value to update the database__________________________________
                            for key1, value1 in mydictw.items(): 
                                idw=key1
                                amountw=value1.get()
                                curupdate.execute("""UPDATE wsubtable SET 
                                quantity=? WHERE subcatagory=?""", (amountw,idw))
#Commiting the update___________________________________________________________
                            con.commit()
#Recalling the Sell Item Function to Refresh the Sell Frame
                            wsubstock(clicked)
#__________________-Button for Submitting the Entered Data-_______________________
                button1 = Button(framesubmit, bg='#86D07D', text='Submit')
                button1.grid()
                button1['command'] = wsubmitted
                
            wclicked = StringVar()
            wclicked.set('Choose One')
            labelsell = Label(frameoption2, bg='#F7E8F8',text='Select One: ').grid(row=0, column=0)
            wdrop = OptionMenu(frameoption2, wclicked, *weatherlist, command=wsubstock).grid(row=0, column=1)
            
            
            
# #Defining DuluOptionMenu
        elif stockclicked.get()=='Dulux Super Gloss 5 in 1':
#Defining Sell item list function
            def dsubstock(clicked):
                clearframe()
                clearframe1()
###---------------fetching Data of Table---------------------------
                cur.execute("SELECT * FROM dsubtable")
                duluxvirtual = cur.fetchall()
#Creating Blank Dictionary for storing Data
                mydictd = {}
                gotdclicked = dclicked.get()
                usednumberd = 1
#-------------------Looping through Data and generating Lables And Entry Widgets------------
                for i in duluxvirtual:
                    if gotdclicked in i:
                        label = Label(frame,bg='#5356BF',fg='white', text=i[2]).grid(row=usednumberd, column=2, padx=25, pady=30)
                        mydictd.update({i[2]:IntVar()})
                        entryurl = 'entry' + str(usednumberd)
                        entryurl = Entry(frame, textvariable=mydictd[i[2]]).grid(row=usednumberd,column=3, padx=50, pady=30)
                        label1 = Label(frame,bg='#E55E1E',fg='black', text=f'Stock at Present: {i[3]}').grid(row=usednumberd, column=4,padx=60,pady=30)
                        usednumberd += 1
#Defining Function that will response after submitting Data
                        def dsubmitted():
#Looping with value to update the database__________________________________
                            for key1, value1 in mydictd.items(): 
                                idd=key1
                                amountd=value1.get()
                                curupdate.execute("""UPDATE dsubtable SET 
                                quantity=? WHERE subcatagory=?""", (amountd,idd))
#Commiting the update___________________________________________________________
                            con.commit()
#Recalling the Sell Item Function to Refresh the Sell Frame
                            dsubstock(clicked)
#__________________-Button for Submitting the Entered Data-_______________________
                button1 = Button(framesubmit, bg='#86D07D', text='Submit')
                button1.grid()
                button1['command'] = dsubmitted
                
            dclicked = StringVar()
            dclicked.set('Choose One')
            labelsell = Label(frameoption2, bg='#F7E8F8',text='Select One: ').grid(row=0, column=0)
            ddrop = OptionMenu(frameoption2, dclicked, *duluxlist, command=dsubstock).grid(row=0, column=1)
            
            
# #Defining Colourant Option Menu
        else:
#Defining Sell item list function
            def csubstock(clicked):
                clearframe()
                clearframe1()
###---------------fetching Data of Table---------------------------
                cur.execute("SELECT * FROM coloranttable")
                colorantvirtual = cur.fetchall()
#Creating Blank Dictionary for storing Data
                mydictc = {}
                gotcclicked = cclicked.get()
                usednumberc = 1
#-------------------Looping through Data and generating Lables And Entry Widgets------------
                for i in colorantvirtual:
                    if gotcclicked in i:
                        label = Label(frame,bg='#5356BF',fg='white', text=i[2]).grid(row=usednumberc, column=2, padx=25, pady=30)
                        mydictc.update({i[2]:IntVar()})
                        entryurl = 'entry' + str(usednumberc)
                        entryurl = Entry(frame, textvariable=mydictc[i[2]]).grid(row=usednumberc,column=3, padx=50, pady=30)
                        label1 = Label(frame,bg='#E55E1E',fg='black', text=f'Stock at Present: {i[3]}').grid(row=usednumberc, column=4,padx=60,pady=30)
                        usednumberc += 1
#Defining Function that will response after submitting Data
                        def csubmitted():
#Looping with value to update the database__________________________________
                            for key1, value1 in mydictc.items(): 
                                idc=key1
                                amountc=value1.get()
                                curupdate.execute("""UPDATE coloranttable SET 
                                quantity=? WHERE cname=?""", (amountc,idc))
#Commiting the update___________________________________________________________
                            con.commit()
#Recalling the Sell Item Function to Refresh the Sell Frame
                            csubstock(clicked)
#__________________-Button for Submitting the Entered Data-_______________________
                button1 = Button(framesubmit, bg='#86D07D', text='Submit')
                button1.grid()
                button1['command'] = csubmitted
                
            cclicked = StringVar()
            cclicked.set('Choose One')
            labelsell = Label(frameoption2, bg='#F7E8F8',text='Select One: ').grid(row=0, column=0)
            cdrop = OptionMenu(frameoption2, cclicked, *colorantlist, command=csubstock).grid(row=0, column=1)
            
    
#Sell Page First Option
    stockclicked = StringVar()
    stockclicked.set('Choose One From The Main Menu')
    labelstock= Label(frameoption1,bg='#F7E8F8', text='Select One: ').grid(row=0, column=0)
    stockdrop = OptionMenu(frameoption1, stockclicked, *mainlist,command=stockselected)
    stockdrop.grid(row=0,column=1)    



#Defining Exit function
def exit():
    con.commit()
    mainroot.destroy()

#Defining Main Page
class mainpage:
    def __init__(self,mainpage):
        self.mainpage = mainpage
        mainpage.title('Dulux')
        mainpage.geometry('300x500')
        mainpage.minsize(300,500)
        mainpage.maxsize(300,500)
        mainframe = LabelFrame(mainpage,bg='#EECFEF',text='Main Menu Options: ')
        mainframe.pack(padx=10,pady=50)
        # boldStyle.configure("Bold.TButton", font = ('14','bold'))
        button1 = Button(mainframe,fg='black',bg='#F7B4AF',font='32', text='Sell Entry', command=sell)
        button2 = Button(mainframe,fg='black',bg='#C5C7F8',font='32', text='Check Status', command=status)
        button3 = Button(mainframe,fg='black',bg='#58ED4E',font='32', text='Stock Entry', command=stock)
        button4 = Button(mainframe,fg='black',bg='#F15432',font='32', text='Reset Stock', command=reset)
        button5 = Button(mainframe,fg='white',bg='#EE170D',font='32', text='Exit', command=exit)
        button1.pack(pady=20)
        button2.pack(pady=20)
        button3.pack(pady=20)
        button4.pack(pady=20)
        button5.pack(pady=20)

mainroot = Tk()
main_gui=mainpage(mainroot)
mainroot.configure(bg='#F7E8F8')
mainroot.mainloop()