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

#######################################################  Database Connection#####################################################
#######################################################  Database Connection#####################################################
try:
    con = sqlite3.connect('dulux.db')
    cur = con.cursor()

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
        
except Exception as e:
    messagebox.showerror('Error',e)
    
finally:
    con.commit()

#######################################################  Tkinter Programming Starts ##############################################################
#######################################################  Tkinter Programming Starts ##############################################################

## Class for new window layout and title
class Window_layout:
    def __init__(self,window_title):
        self.window_title=window_title
        
    def new_window(self):
        self.window = Toplevel(mainroot, bg='#F7E8F8')
        self.window.title(self.window_title)
        self.window.geometry('900x700')
        self.window.minsize(900,700)
        self.window.maxsize(900,700)

## Class for Creating Option Menu
class Option_Menu(Frame):
    def __init__(self,clicker,frame_id,list_name,command_name):
        super().__init__()
        self.clicker=clicker
        self.frame_id=frame_id
        self.list_name=list_name
        self.command_name=command_name
        
    def create_menu(self):
        self.clicker = StringVar()
        self.clicker.set('Choose One From The Main Menu')
        label = Label(self.frame_id,bg='#F7E8F8', text='Select One: ').grid(row=0, column=0)
        drop = OptionMenu(self.frame_id, self.clicker, *self.list_name,command=self.command_name)
        drop.grid(row=0,column=1)

##Class for Creating Frames and Deleting Frames
class Frame_creation:
    def __init__(self, window_name, frame_name):
        self.window_name = window_name
        self.frame_name = frame_name
        self.frame = LabelFrame(self.window_name,bg='#EECFEF', text=self.frame_name)
        self.frame.pack(pady=20)
    #Deleting Frames    
    def clear_frame(self):
        for i in self.frame.winfo_children():
            i.destroy()

##Defining Function that will response after submitting Data
def entry_func(click_event,data_set,dict_name,frame_id,frame_id2,table_name,identifier):
    try:
        con = sqlite3.connect('dulux.db')
        curupdate = con.cursor()
    #Refreshing the Frame
        for i in frame_id2.winfo_children():
            i.destroy()

        for a, b in dict_name.items():
            dict_name.update({a:int(b.get())})

    # Specifying Action Only for Sell Entry and Addition Entry            
        if identifier == 'Sell' or identifier == 'Add':
        #Looping through Dictionary to get Values_______________________________________
            for key, value in dict_name.items():
        #Looping through List to get the stored value___________________________________
                for locator in data_set:
        #Matching the Entry keys with the List Keys_____________________________________
                    if key==locator[2]:
        # Specifying Action for Sell Entry______________________________________________
                        if identifier == 'Sell':
        #Deducting and saving the new value in the dictionary___________________________
                            dict_name.update({key:(locator[3]-value)})
        # Specifying Action for Stock Adding Entry______________________________________
                        else:
        #Deducting and saving the new value in the dictionary___________________________
                            dict_name.update({key:(locator[3]+value)})

    #Looping with new value to update the database______________________________________
        for key1, value1 in dict_name.items(): 
            id=key1
            amount=value1
            curupdate.execute(f'UPDATE {table_name} SET quantity=? WHERE subcatagory=?', (amount,id))
        
    except Exception as e:
        messagebox.showerror('Error',e)
        
    finally:
#Recalling the Main Function to Refresh the Full Frame with new Values__________
        detail_view(click_event,frame_id,frame_id2,table_name,identifier)
#Commiting the update___________________________________________________________
        con.commit()



#Defining Sell item list function
def detail_view(click_event,frame_id,frame_id2,table_name,identifier):
# Declaring Random Dictionary to store Data
    dict1 = {}
    
    try:
        con = sqlite3.connect('dulux.db')
        cur = con.cursor()
#Getting Values from the Database
        cur.execute(f'SELECT * FROM {table_name}')
        virtual = cur.fetchall()
        usednumber = 1
#----------------Looping through Data and generating Lables And Entry Widgets------------
        for i in virtual:
            if click_event in i:
                if identifier == 'Sell' or identifier == 'Add' or identifier == 'Reset':
                    label = Label(frame_id,bg='#5356BF',fg='white', text=i[2]).grid(row=usednumber, column=2, padx=25, pady=30)
                    dict1.update({i[2]:StringVar()})
                    entryurl = 'entry' + str(usednumber)
                    entryurl = Entry(frame_id, textvariable=dict1[i[2]]).grid(row=usednumber,column=3, padx=50, pady=30)
                    label1 = Label(frame_id,bg='#E55E1E',fg='black', text=f'Stock at Present: {i[3]}').grid(row=usednumber, column=4,padx=60,pady=30)
                    usednumber += 1
                else:
                    label = Label(frame_id,bg='#5356BF',fg='white', text=i[2]).grid(row=usednumber, column=2, padx=25, pady=30)
                    label1 = Label(frame_id,bg='#E55E1E',fg='black', text=f'Stock at Present: {i[3]}').grid(row=usednumber, column=4,padx=60,pady=30)
                    usednumber += 1
#Button Call Function   
        def save():
#Calling the Function to save Value in DataBase
            entry_func(click_event,virtual,dict1,frame_id,frame_id2,table_name,identifier)
# Submit Button to Save Value  
        if identifier == 'Sell' or identifier == 'Add' or identifier == 'Reset':         
            button1 = Button(frame_id2, bg='#86D07D', text='Submit')
            button1.grid()
            button1['command'] = save            

    except Exception as e:
        messagebox.showerror('Error',e)
        
    finally:
        con.commit()


#Defining Sell Page
def sell():
    # Instantiating window from the Window_Layout Class
    window1 = Window_layout('Sell Entry Page')
    window1.new_window()
    # Instantiating Frames from the Frame_creation Class
    frame1 = Frame_creation(window1.window, 'Main Menu')
    frame2 = Frame_creation(window1.window, 'Sub Menu')
    frame3 = Frame_creation(window1.window, 'Details Below: ')
    frame4 = Frame_creation(window1.window, '')

    # Defining Response Function of First Option Menu
    def menu_second(event):
    # Refreshing 2nd Menu Frame
        frame2.clear_frame()
    # Comparing Clicked Value with the List
        if event=='Velvet Touch Diamond Glow':
    # Defining Response Function of Second Option Menu
            def menu_thirdv(new_event):
    # Refreshing Details and Submit Buttons Frames
                frame3.clear_frame()
                frame4.clear_frame()
    # Calling The function That will Show the Details and it will call the Submit Button Function
                detail_view(new_event, frame3.frame, frame4.frame, 'vsubtable', 'Sell')                            
    # Second Option Menu        
            click2 = StringVar()
            menu2 = Option_Menu(click2, frame2.frame, velvetlist, menu_thirdv)
            menu2.create_menu()
        elif event=='Weather Shield Max':
    # Defining Response Function of Second Option Menu
            def menu_thirdw(new_event):
    # Refreshing Details and Submit Buttons Frames
                frame3.clear_frame()
                frame4.clear_frame()
    # Calling The function That will Show the Details and it will call the Submit Button Function
                detail_view(new_event, frame3.frame, frame4.frame, 'wsubtable', 'Sell') 
    # Second Option Menu  
            click2 = StringVar()
            menu2 = Option_Menu(click2, frame2.frame, weatherlist, menu_thirdw)
            menu2.create_menu()
        elif event=='Dulux Super Gloss 5 in 1':
    # Defining Response Function of Second Option Menu
            def menu_thirdd(new_event):
    # Refreshing Details and Submit Buttons Frames
                frame3.clear_frame()
                frame4.clear_frame()
    # Calling The function That will Show the Details and it will call the Submit Button Function
                detail_view(new_event, frame3.frame, frame4.frame, 'dsubtable', 'Sell')  
    # Second Option Menu 
            click2 = StringVar()
            menu2 = Option_Menu(click2, frame2.frame, duluxlist, menu_thirdd)
            menu2.create_menu() 
        else:
    # Defining Response Function of Second Option Menu
            def menu_thirdc(new_event):
    # Refreshing Details and Submit Buttons Frames
                frame3.clear_frame()
                frame4.clear_frame()
    # Calling The function That will Show the Details and it will call the Submit Button Function
                detail_view(new_event, frame3.frame, frame4.frame, 'coloranttable', 'Sell')  
    # Second Option Menu 
            click2 = StringVar()
            menu2 = Option_Menu(click2, frame2.frame, colorantlist, menu_thirdc)
            menu2.create_menu() 
    
# First Option Menu
    click1 = StringVar()
    menu1 = Option_Menu(click1, frame1.frame, mainlist, menu_second)
    menu1.create_menu()
    


#Defining Status Page
def status():
    # Instantiating window from the Window_Layout Class
    window1 = Window_layout('Status Check Page')
    window1.new_window()
    # Instantiating Frames from the Frame_creation Class
    frame1 = Frame_creation(window1.window, 'Main Menu')
    frame2 = Frame_creation(window1.window, 'Sub Menu')
    frame3 = Frame_creation(window1.window, 'Details Below: ')
    frame4 = Frame_creation(window1.window, '')

    # Defining Response Function of First Option Menu
    def menu_second(event):
    # Refreshing 2nd Menu Frame
        frame2.clear_frame()
    # Comparing Clicked Value with the List
        if event=='Velvet Touch Diamond Glow':
    # Defining Response Function of Second Option Menu
            def menu_thirdv(new_event):
    # Refreshing Details and Submit Buttons Frames
                frame3.clear_frame()
                frame4.clear_frame()
    # Calling The function That will Show the Details and it will call the Submit Button Function
                detail_view(new_event, frame3.frame, frame4.frame, 'vsubtable', '')                            
    # Second Option Menu        
            click2 = StringVar()
            menu2 = Option_Menu(click2, frame2.frame, velvetlist, menu_thirdv)
            menu2.create_menu()
        elif event=='Weather Shield Max':
    # Defining Response Function of Second Option Menu
            def menu_thirdw(new_event):
    # Refreshing Details and Submit Buttons Frames
                frame3.clear_frame()
                frame4.clear_frame()
    # Calling The function That will Show the Details and it will call the Submit Button Function
                detail_view(new_event, frame3.frame, frame4.frame, 'wsubtable', '') 
    # Second Option Menu  
            click2 = StringVar()
            menu2 = Option_Menu(click2, frame2.frame, weatherlist, menu_thirdw)
            menu2.create_menu()
        elif event=='Dulux Super Gloss 5 in 1':
    # Defining Response Function of Second Option Menu
            def menu_thirdd(new_event):
    # Refreshing Details and Submit Buttons Frames
                frame3.clear_frame()
                frame4.clear_frame()
    # Calling The function That will Show the Details and it will call the Submit Button Function
                detail_view(new_event, frame3.frame, frame4.frame, 'dsubtable', '')  
    # Second Option Menu 
            click2 = StringVar()
            menu2 = Option_Menu(click2, frame2.frame, duluxlist, menu_thirdd)
            menu2.create_menu() 
        else:
    # Defining Response Function of Second Option Menu
            def menu_thirdc(new_event):
    # Refreshing Details and Submit Buttons Frames
                frame3.clear_frame()
                frame4.clear_frame()
    # Calling The function That will Show the Details and it will call the Submit Button Function
                detail_view(new_event, frame3.frame, frame4.frame, 'coloranttable', '')  
    # Second Option Menu 
            click2 = StringVar()
            menu2 = Option_Menu(click2, frame2.frame, colorantlist, menu_thirdc)
            menu2.create_menu() 
    
# First Option Menu
    click1 = StringVar()
    menu1 = Option_Menu(click1, frame1.frame, mainlist, menu_second)
    menu1.create_menu()
    


#Defining Stock Entry Page
def stock():
    # Instantiating window from the Window_Layout Class
    window1 = Window_layout('New Stock Entry Page')
    window1.new_window()
    # Instantiating Frames from the Frame_creation Class
    frame1 = Frame_creation(window1.window, 'Main Menu')
    frame2 = Frame_creation(window1.window, 'Sub Menu')
    frame3 = Frame_creation(window1.window, 'Details Below: ')
    frame4 = Frame_creation(window1.window, '')

    # Defining Response Function of First Option Menu
    def menu_second(event):
    # Refreshing 2nd Menu Frame
        frame2.clear_frame()
    # Comparing Clicked Value with the List
        if event=='Velvet Touch Diamond Glow':
    # Defining Response Function of Second Option Menu
            def menu_thirdv(new_event):
    # Refreshing Details and Submit Buttons Frames
                frame3.clear_frame()
                frame4.clear_frame()
    # Calling The function That will Show the Details and it will call the Submit Button Function
                detail_view(new_event, frame3.frame, frame4.frame, 'vsubtable', 'Add')                            
    # Second Option Menu        
            click2 = StringVar()
            menu2 = Option_Menu(click2, frame2.frame, velvetlist, menu_thirdv)
            menu2.create_menu()
        elif event=='Weather Shield Max':
    # Defining Response Function of Second Option Menu
            def menu_thirdw(new_event):
    # Refreshing Details and Submit Buttons Frames
                frame3.clear_frame()
                frame4.clear_frame()
    # Calling The function That will Show the Details and it will call the Submit Button Function
                detail_view(new_event, frame3.frame, frame4.frame, 'wsubtable', 'Add') 
    # Second Option Menu  
            click2 = StringVar()
            menu2 = Option_Menu(click2, frame2.frame, weatherlist, menu_thirdw)
            menu2.create_menu()
        elif event=='Dulux Super Gloss 5 in 1':
    # Defining Response Function of Second Option Menu
            def menu_thirdd(new_event):
    # Refreshing Details and Submit Buttons Frames
                frame3.clear_frame()
                frame4.clear_frame()
    # Calling The function That will Show the Details and it will call the Submit Button Function
                detail_view(new_event, frame3.frame, frame4.frame, 'dsubtable', 'Add')  
    # Second Option Menu 
            click2 = StringVar()
            menu2 = Option_Menu(click2, frame2.frame, duluxlist, menu_thirdd)
            menu2.create_menu() 
        else:
    # Defining Response Function of Second Option Menu
            def menu_thirdc(new_event):
    # Refreshing Details and Submit Buttons Frames
                frame3.clear_frame()
                frame4.clear_frame()
    # Calling The function That will Show the Details and it will call the Submit Button Function
                detail_view(new_event, frame3.frame, frame4.frame, 'coloranttable', 'Add')  
    # Second Option Menu 
            click2 = StringVar()
            menu2 = Option_Menu(click2, frame2.frame, colorantlist, menu_thirdc)
            menu2.create_menu() 
    
# First Option Menu
    click1 = StringVar()
    menu1 = Option_Menu(click1, frame1.frame, mainlist, menu_second)
    menu1.create_menu()
    



#Defining Reset Stock Page
def reset():
    # Instantiating window from the Window_Layout Class
    window1 = Window_layout('Reset Stock Page')
    window1.new_window()
    # Instantiating Frames from the Frame_creation Class
    frame1 = Frame_creation(window1.window, 'Main Menu')
    frame2 = Frame_creation(window1.window, 'Sub Menu')
    frame3 = Frame_creation(window1.window, 'Details Below: ')
    frame4 = Frame_creation(window1.window, '')

    # Defining Response Function of First Option Menu
    def menu_second(event):
    # Refreshing 2nd Menu Frame
        frame2.clear_frame()
    # Comparing Clicked Value with the List
        if event=='Velvet Touch Diamond Glow':
    # Defining Response Function of Second Option Menu
            def menu_thirdv(new_event):
    # Refreshing Details and Submit Buttons Frames
                frame3.clear_frame()
                frame4.clear_frame()
    # Calling The function That will Show the Details and it will call the Submit Button Function
                detail_view(new_event, frame3.frame, frame4.frame, 'vsubtable', 'Reset')                            
    # Second Option Menu        
            click2 = StringVar()
            menu2 = Option_Menu(click2, frame2.frame, velvetlist, menu_thirdv)
            menu2.create_menu()
        elif event=='Weather Shield Max':
    # Defining Response Function of Second Option Menu
            def menu_thirdw(new_event):
    # Refreshing Details and Submit Buttons Frames
                frame3.clear_frame()
                frame4.clear_frame()
    # Calling The function That will Show the Details and it will call the Submit Button Function
                detail_view(new_event, frame3.frame, frame4.frame, 'wsubtable', 'Reset') 
    # Second Option Menu  
            click2 = StringVar()
            menu2 = Option_Menu(click2, frame2.frame, weatherlist, menu_thirdw)
            menu2.create_menu()
        elif event=='Dulux Super Gloss 5 in 1':
    # Defining Response Function of Second Option Menu
            def menu_thirdd(new_event):
    # Refreshing Details and Submit Buttons Frames
                frame3.clear_frame()
                frame4.clear_frame()
    # Calling The function That will Show the Details and it will call the Submit Button Function
                detail_view(new_event, frame3.frame, frame4.frame, 'dsubtable', 'Reset')  
    # Second Option Menu 
            click2 = StringVar()
            menu2 = Option_Menu(click2, frame2.frame, duluxlist, menu_thirdd)
            menu2.create_menu() 
        else:
    # Defining Response Function of Second Option Menu
            def menu_thirdc(new_event):
    # Refreshing Details and Submit Buttons Frames
                frame3.clear_frame()
                frame4.clear_frame()
    # Calling The function That will Show the Details and it will call the Submit Button Function
                detail_view(new_event, frame3.frame, frame4.frame, 'coloranttable', 'Reset')  
    # Second Option Menu 
            click2 = StringVar()
            menu2 = Option_Menu(click2, frame2.frame, colorantlist, menu_thirdc)
            menu2.create_menu() 
    
# First Option Menu
    click1 = StringVar()
    menu1 = Option_Menu(click1, frame1.frame, mainlist, menu_second)
    menu1.create_menu()




#Defining Exit function
def exit():
    con.commit()
    mainroot.destroy()


    

####  Class of Main Page / Defining Main Page using Tkinter  ####
class mainpage:
    def __init__(self,mainpage):
        self.mainpage = mainpage
        self.mainpage.title('Dulux')
        self.mainpage.geometry('300x500')
        self.mainpage.minsize(300,500)
        self.mainpage.maxsize(300,500)
        self.mainframe = LabelFrame(self.mainpage,bg='#EECFEF',text='Main Menu Options: ')
        self.mainframe.pack(padx=10,pady=50)
        self.button1 = Button(self.mainframe,fg='black',bg='#F7B4AF',font='32', text='Sell Entry', command=sell)
        self.button2 = Button(self.mainframe,fg='black',bg='#C5C7F8',font='32', text='Check Status', command=status)
        self.button3 = Button(self.mainframe,fg='black',bg='#58ED4E',font='32', text='Stock Entry', command=stock)
        self.button4 = Button(self.mainframe,fg='black',bg='#F15432',font='32', text='Reset Stock', command=reset)
        self.button5 = Button(self.mainframe,fg='white',bg='#EE170D',font='32', text='Exit', command=exit)
        self.button1.pack(pady=20)
        self.button2.pack(pady=20)
        self.button3.pack(pady=20)
        self.button4.pack(pady=20)
        self.button5.pack(pady=20)

mainroot = Tk()
main_gui = mainpage(mainroot)
mainroot.configure(bg='#F7E8F8')
mainroot.mainloop()