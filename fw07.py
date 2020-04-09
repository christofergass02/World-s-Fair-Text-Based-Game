# fw07.py
from sys import exit
import time
import random
#total = 240 (time in minutes)
gold = 3.25

# choices: [yes, no], [left, right]

# ['YES', 'Yes', 'yes', 'yeah', 'Y', 'y']
# ['NO', 'No', 'no', 'nah', 'N', 'n']
# ['LEFT', 'Left', 'left', 'L', 'l']
# ['RIGHT', 'Right', 'right', 'R', 'r']

#(2) African Pavilion
def african_pav(): 
#    time = 45
    global gold
    print("As you come up to the entrance of the pavilion\nyou are asked to pay 50 cents.")
    afria()
def afria():
    choice = input("Do you pay to enter the pavilion?\nyes or no?\n ")
    if choice == "yes":
        gold - 0.50  
        print("You have",gold)
        print("")
        afrib()
    elif choice == "no":
        print("Alright, let's go to THE UNISPHERE.")
        unisphere()
    else:
        print("I didn't understand that.\n")
        afria()

def afrib():
    print("The pavilion is made up of round huts that represent 24 nations\nof sub-Saharan Africa and stands on a broad platform\nerected on stilts above water.")
    print("As you walk into the pavilion you hear the sounds of chanting and drum beats.\nAs you walk in the open-air entertainment area\nyou see Watsui men from Rwanda perform a spirited dance\nand demonstrate their ability at high-jumping.\nBurundi drummers and West African dancers also perform.")
    print("After taking the performance you consider where to go next.")
    print("To the left is THE NEW JERSEY PAVILION and to the right is THE UNISPHERE.")
    afri1()
def afri1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE NEW JERSEY PAVILION.")
        nj_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE UNISPHERE.")
        unisphere()
    else:
        print("I didn't understand that.\n")
        afri1()

#(3) Alaska Pavilion
def alaska_pav():
#    time = 30     
    print("While in the igloo shaped pavilion you observe\nthe 32-square-foot topographical model of Alaska.")
    print("Where would you like to go to next?")
    print("To the left is THE MISSOURI PAVILION\nand to the right is THE WISCONSIN PAVILION.")
    al1()
def al1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left": 
        print("\nYOU ARE AT THE MISSOURI PAVILION.")
        missouri_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE WISCONSIN PAVILION.")
        wisconsin_pav()
    else:
        print("I didn't understand that.\n")
        al1()

#(6) American Indian Pavilion
def amind_pav():
#   time = 30
    global gold
    print("As you come up to the entrance of the pavilion\nyou are asked to pay 50 cents.")
    aminda()
def aminda():
    choice = input("Do you pay to enter the pavilion?\nyes or no?\n ")
    if choice == "yes":
        gold - 0.50  
        print("You have",gold)
        print("")
            
            
            
        amind1()
    elif choice == "no":
        print("After you see the time on the Communications Arch near you\nyou realize that it is time to go home for dinner.")
        print("I hope you enjoyed the 1964-1965 World's Fair. Goodbye.")
        time.sleep(5)
        exit()    
    else:
        print("I didn't understand that.\n")
        aminda()

def amind1():    
    print("Where would you like to go to next?")
    print("To the left is WALTER'S INTERNATIONAL WAX MUSEUM\nand to the right is THE CHUNG KING INN.")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left": 
        print("\nYOU ARE AT WALTER'S INTERNATIONAL WAX MUSEUM.")
        walters_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE CHUNG KING INN.")
        cki_pav()
    else:
        print("I didn't understand that.\n")
        amind1()

#(8) American-Israel Pavilion
def americanisrael_pav():
#    time = 25
    global gold
    print("As you come up to the entrance of the pavilion\nyou are asked to pay 25 cents.")
    amera()
def amera():
    choice = input("Do you pay to enter the pavilion?\nyes or no?\n ")
    if choice == "yes":
        gold - 0.25  
        print("You have",gold)
        print("")
        amerb()
    elif choice == "no":
        print("Alright, let's go to THE MISSOURI PAVILION.")
        missouri_pav()
    else:
        print("What was that?")
        amera()

def amerb():
    print("Within the pavilion you enjoy scenes and artifacts portraying 4,000 years of Jewish history.\nAfter you walk around the Pavilion and to its top\nyou consider which Pavilion to head to next.")
    print("Do you head left to THE HALL OF FREE ENTERPRISE PAVILION\nor right to THE SWITZERLAND PAVILION")
    amer1()
def amer1():    
    choice = input("Which way do you go?\nleft or right?\n ")    
    if choice == "left":
        print("\nYOU ARE AT THE HALL OF FREE ENTERPRISE PAVILION")
        hall_pav()   
    elif choice == "right":
        print("\nYOU ARE AT THE SWITZERLAND PAVILION")
        switzerland_pav()
    else:
        print("I didn't understand that.\n")
        amer1()

# Astral Fountain
def astral_foun(): 
#    time = 10 
    print("You enjoy the orchestration of the fountain and the atmosphere of the Fair.")   
    print("Where would you like to go from here?")
    print("To the left is THE AMERICAN INDIAN PAVILION\nand to the right is THE CONTINENTAL CIRCUS.")
    ast1()
def ast1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE AMERICAN INDIAN PAVILION.")
        amind_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE CONTINENTAL CIRCUS.")
        circus_pav()
    else:
        print("I didn't understand that.\n")
        ast1()

#(11) Austria Pavilion
def austria_pav():    
#    time = 60      
    print("The pavilion is in the shape of an 'A', which you find out is to\nsymbolize Austria as a land of mountains and tourism.\nWithin the wooden structure you hear the music of Mozart and Strauss\nas you learn about the nation's industry, products and handicraft.")
    print("Do you head left to THE JAPAN PAVILION\nor right to THE ROCKET THROWER SCULPTURE?")
    aus1()
def aus1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE JAPNA PAVILION.")
        japan_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE ROCKET THROWER SCULPTURE.")
        rocket()
    else:
        print("I didn't understand that.\n")
        aus1()

#(14) Belgium Pavilion
def belgium_pav():
#    time = 60
    global gold
    print("As you come up to the entrance of the pavilion\nyou are asked to pay 60 cents.")
    bela()
def bela():
    choice = input("Do you pay to enter the pavilion?\nyes or no?\n ")
    if choice == "yes":
        gold - 0.60  
        print("You have",gold)
        print("")
        belb()
    elif choice == "no":
        print("Of course, lets go to THE VATICAN PAVILION.")
        vatican_pav()
    else:
        print("I didn't understand that.\n")
        bela()

def belb():
    print("As you walk through the pavilion you enjoy the sight of no less than a hundred houses,\na replica of the fifteenth-century Gothic church of Saint Nicholas,\na town hall with an underground rathskeller, forty shops, a canal,\nan arched stone bridge and Gille Dancers.")
    print("Which are clowns with wooden shoes, ostrich-feather headdresses and bells\nthat dance through the streets to the sound of drums and brass instruments.")
    print("You learn that the Gilles hark back to 1540, when Belgium was ruled by Spain,\nand the conquistidors' triumph over Peruvian Indians was celebrated at Mardi Gras.")
    print("To your left you see THE LOUISIANNA PAVILION,\nand to the right is THE VATICAN PAVILION?")
    bel1()
def bel1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE LOUISIANNA PAVILION")
        louisiana_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE VATICAN PAVILION")
        vatican_pav()
    else:
        print("I didn't understand that.\n")
        bel1()

#(24) Christian Science Pavilion
def christianscience_pav():
#    time = 30 
    print("The pavilion is in a star-shape\nand their is descriptions of the faith\nwith displays and recorded testimonials.")
    print("After walking around the pavilion you decide on where to head to next.")
    print("To the left is THE HALL OF FREE ENTERPRISE PAVILION")
    print("and to the right is THE SWITZERLAND PAVILION.")
    chris1()
def chris1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE HALL OF FREE ENTERPRISE PAVILION.")
        hall_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE SWITZERLAND PAVILION.")
        switzerland_pav()
    else:
        print("I didn't understand that.\n")
        chris1()

#(26) Chrysler Pavilion
def chrysler_pav():
#    time = 60     
    print("You enter an exhibit that is on one of five islands that make up the pavilion.\nThe exhibit is titled Engineering Island and is in the shape\nof a 100-foot engine with a 50-foot dragon for a crankshaft.\nWithin the exhibit there is a turbine engine on display developed by Chrysler.\nOn another island, which is the shape of the company's Pentastar symbol,\nis the Puppet Show exhibit. A 24-minute musical comedy.")
    print("After walking around the rest of the pavilion you decide it is time to head on home for dinner.")
    print("I hope you enjoyed the 1964-1965 World's Fair. Goodbye.")
    time.sleep(5)
    exit()    

#() Chung King Inn
def cki_pav():
#    time = 30
    global gold
    print("You know ")
    print("You hear they have a meal with seven types of Chinese foods and a beverage that is only a dollar.")
    ckia()
def ckia():    
    choice = input("Do you decide to purchase a meal for one dollar?\nyes or no\n ")
    if choice == "yes":
        gold - 1 
        print("You have",gold)
        print("")
        print("You are seated outside in the Oriental garden and are treated to a meal of\nchicken chow mein, fried rice, shrimp egg roll, chow mein fried noodles,\nfruit roll, egg foo young and sauce, a fortune cookie and a soda.\nYou eat most of your meal, but can not conceive eating another bite.\nOn your way out your waitress hands you a bundle of firecrackers.\n'Oh boy, can't wait to play with those' you think to yourself.")
        cki1()
    elif choice == "no":
        print("Of course, as you please.")
        cki1()
    else:
        print("I’m sorry, I didn’t catch that.\n")
        ckia()

def cki1():
    print("After walking around the fair for a little longer you decide it is time to go on home.")
    print("I hope you enjoyed the 1964-1965 World's Fair. Goodbye.")
    time.sleep(5)
    exit() 

#(28) Clairol Pavilion
def clairol_pav():
#    time = 5
    print("As soon as you walk up to the pavilion\nyou are told 'Women 16 and older only.'")
    print("You turn around and consider where to go from here.")
    time.sleep(3)
    print("To the left is THE TOWER OF LIGHT PAVILION and to the right is THE FOUNTAIN OF THE PLANETS.")
    clair1()
def clair1():    
    choice = input("Which way do you go?\nleft or right\n ")
    if choice == "left":
        print("YOU ARE AT THE TOWER OF LIGHT PAVILION.")
        tol_pav()
    elif choice == "right":
        print("YOU ARE AT THE FOUNTAIN OF THE PLANETS.")
        planets_foun()   
    else:
        print("I didn't understand that.\n")
        clair1()

#(30) Continental Circus
def circus_pav():
#    time = 90
    global gold
    print("Walking up to the brightly colored circus tent, you are asked to pay a dollar to enter.")
    cca()
def cca():    
    choice = input("Do you decide to enter the circus?\nyes or no\n ")
    if choice == "yes":
        gold - 1  
        print("You have",gold)
        print("")
        print("You enter the large yellow and white circus tent and try to take in everything that is going on.\nThere are acrobats, chimpanzees who play instruments, daredevil trapeze artists,\nequestrian horses, as well as all sorts of animal acts\nwith elephants and a gorilla that does bicycle tricks.\n")
        cc1()
    elif choice == "no":
        print("Of course, as you please.")
        cc1()
    else:
        print("I’m sorry, I didn’t catch that.\n")
        cca()

def cc1():
    print("After enjoying your day at the fair you decide it is time to go on home.")
    print("I hope you enjoyed the 1964-1965 World's Fair. Goodbye.")
    time.sleep(5)
    exit()  

#(37) Eastman Kodak Pavilion
def eastman_pav():
#    time = 45
    print("Atop the pavilion are five color photographs, each 30 by 36 feet\nin size and change every four weeks.\nWhile you walk around the pavilion you notice\na sad figure with shabby clothing and clown makeup.")
    east1()
def east1():    
    choice = input("Do you approach the figure?\nyes or no\n ")
    if choice == "yes":
        print("\nYou find out the figure is none other than Emitt Kelly Jr,\nwhich is the Pavilion's mascot.\nAfter you do your best miming act with Emitt\nyou decide where to head to next.")
        east2()
    elif choice == "no":
        print("\nOf course, as you please.")
        print("As you find your way out of the pavilion you decide where to head to next.")
        east2()   
    else:
        print("I didn't understand that.\n")
        east1()
    
def east2():
    print("Where do you want to go?")
    print("To the left is THE FIRST NATIONAL CITY BANK PAVILION\nand to the right is THE GARDEN OF MEDITATION.")    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE FIRST NATIONAL CITY BANK PAVILION.")
        fncb_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE GARDEN OF MEDITATION.")
        garden_pav()
    else:       
        print("I didn't understand that.\n")
        east2()

# Fountain of the Fairs
def fairs_foun():
#    time = 10
    print("As you take in the pavilions around the fountain,\nyou notice a man wearing a white suit holding numerous blueprints.\nThere are a few men around him and they are all pointing\nto something on one of the blueprints that is opened up.\nBehind and around the group of men there are numerous people huddled around them.")
    moses()
def fairs1():    
    print("To the left is THE JOHNSON WAX PAVILION and to the right is THE AUSTRIA PAVILION.")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE JOHNSON WAX PAVILION.")
        jw_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE AUSTRIA PAVILION.")
        austria_pav()
    else:
        print("I didn't understand that.\n")
        fairs1()

#(40) First National City Bank Pavilion
def fncb_pav():
#    time = 10 
    print("Which you find out is the fair's only bank with a branch.") 
    print("After contemplating what you would do with a few extra bucks\nyou consider which pavilion to head to next.")
    print("Do you go left to THE GARDEN OF MEDITATION,\nor right to THE CHRISTIAN SCIENCE PAVILION?")
    fncb1()
def fncb1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE GARDEN OF MEDITATION.")
        garden_pav()   
    elif choice == "right":
        print("\nYOU ARE AT THE CHRISTIAN SCIENCE CENTER.")
        christianscience_pav()
    else:
        print("I’m sorry, I didn’t catch that.\n")
        fncb1()

#(45) Garden of Meditation
def garden_pav():
#    time = 20     
    print("As you continue to walk through the Garden\nyou notice the hum of the busy Fair become quieter and quieter.\nAll around you are trees, as well as laurel and azaleas.\nAlso in the Garden are Biblical references and a quotation from Sir Francis Bacon.")
    gar1() 
def gar1():
    choice = input("Would you like to read the quote or know more about one of the Biblical verses?\nyes or no\n ")
    if choice == "yes":
        randint = random.randint(0,3)
        if randint == 1: 
            print("\nNumbers 6:24-26 - 'The Lord bless you\n and keep you;\nthe Lord make his face shine on you\n and be gracious to you;\nthe Lord turn his face toward you\n and give you peace.'\n")
            gar2()        
        elif randint == 2:
            print("\nMica 6:8 - 'He has shown you, O mortal, what is good.\n And what does the Lord require of you?\nTo act justly and to love mercy\n and to walk humbly with your God.'\n")
            gar2()
        elif randint == 3:
            print("\nRomans 12:10 & 12 - 'Be devoted to one another in love. Honor one another above\nyourselves. Never be lacking in zeal, but keep your spiritual\n fervor, serving the Lord. Be joyful in hope, patient in affliction,\n faithful in prayer.'\n")
            gar2()        
        elif randint == 4:
            print("\n'God Almighty first planted a Garden.\nAnd indeed it is the purest of human pleasures.\nIt is the greatest refreshment to the spirits of man.' -Francis Bacon\n")
            gar2()
    elif choice == "no":
        print("Of course, let's move on.\n")        
        gar2()
    else:
        print("I didn't understand that.\n")
        gar1()

def gar2():
    print("After you relax in the Garden,\nyou contemplate where to head to next.")
    print("Do you head left to THE BELGUIM PAVILION,\nor right to THE CHRISTIAN SCIENCE PAVILION?")
    gar3()
def gar3():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE BELGIUM PAVILION.")
        belgium_pav()       
    elif choice == "right":
        print("\nYOU ARE AT THE CHRISTIAN SCIENCE PAVILION.")
        christianscience_pav()
    else:            
        print("I'm sorry, I didn't understand that.\n")
        gar3()

#(46) General Cigar Pavilion
def gc_pav():
#    time = 30
    print("Before you enter the pavilion you take in the sight of 12-foot smoke rings float into the air.\nWhile inside you watch a magic show presented by Mark Wilson.\nThe magician causes human beings and objects to appear from nowhere, float and vanish.")
    print("After you enjoy the show you decide where to head to next.")
    print("To the left is THE SOLAR FOUNTAIN and to the right is THE JAPAN PAVILION ")
    gc1()
def gc1():
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE SOLAR FOUNTAIN")
        solar_foun()
    elif choice == "right":
        print("\nYOU ARE AT THE JAPAN PAVILION.")
        japan_pav()
    else:
        print("I didn't understand that.\n")
        gc1()

#(47) General Electric Pavilion
def ge_pav():
#    time = 45
    print("As you enter the large dome structure you head to the exhibit 'Progressland',\nproduced by Walt Disney and depicts the history of electricity.")
    print("The exhibit has four sections that depict different time periods\nand the electricity capabilites they had during that time period, starting with the 1890's.")
    print("before you exit the pavilion you watch a demonstration of a controlled thermonuclear fusion.\nYou watch as a magnetic field squeezes a plasma of deuterium gas for\na few millionths of a second at a temperature of 20 million degrees Fahrenheit.")
    print("Where would you like to go next?")
    print("To the left is THE TOWER OF LIGHT PAVILION and to the right is THE CLAIROL PAVILION ")
    ge1()
def ge1():
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE TOWER OF LIGHT PAVILION")
        tol_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE CLAIROL PAVILION.")
        clairol_pav()
    else:
        print("I didn't understand that.\n")
        ge1()

#(48) General Motors Pavilion
def gm_pav(): 
#    time = 40   
    print("After waiting in line to get in to the pavilion you are welcomed by a hostess\nand run straight for The New Futurama ride. You sit in a seat equipped with speakers\nthat supply a narration for the ride.")   
    gm1() 
def gm1():
    choice = input("Would you like to know more about one of the parts of the exhibit?\nyes or no\n ")
    if choice == "yes":
        randint = random.randint(0,5)
        if randint == 1: 
            print("A trip to the moon starts the ride taking the visitor past a scale model\nwhose craters and canyons are dotted with manned 'lunar-crawlers' and commuter space ships.\n") 
            gm2()
        elif randint == 2:
            print("Life under the ice is depicted in a display that shows an all-weather port\ncut deep into the Antarctic ice shelf. Under the ice cap is a weather station,\nwhere technicians prepare forecasts embracing whole continents.\n") 
            gm2()
        elif randint == 3:
            print("In an underwater scene, drills tap the ocean floor for oil,\nminerals are hauled away by submarine train, and vacationers relax in a suboceanic resort\nand, equipped with oxygen, ride about outside on 'aqua-scooters.'\n") 
            gm2()
        elif randint == 4:
            print("Visiting the jungle, spectators see a machine that fells towering trees with searing laser light.\nA road builder, scaled to appear five stories high and longer than three football fields,\nfollows the timber-cutter. It levels and grades, leaving a divided, multilane superhighway in its path.\nThe road serves a city that processes the products (lumber, chemicals and farm commodities) drawn from the tamed jungle.\n") 
            gm2()
        elif randint == 5:
            print("In the desert, crops thrive in soil irrigated with subterranean or desalted sea water.\nMachines operated by remote control plant and harvest the crops.\n")
            gm2()
        elif randint == 6:
            print("The city of the future is shown complete with midtown airports, high-speed bus-trains, superskyscrapers,\nmoving sidewalks and underground conveyor belts for freight.\nAround the city is part of an intercontinental highway.\n")
            gm2()
    elif choice == "no":
        print("Of course, let's move on.\n")
        gm2()   
    else:
        print("I didn't understand that.\n")
        gm1()

def gm2():
    print("After you walk through the pavilion you decide it is time to go home.")
    print("I hope you enjoyed the 1964-1965 World's Fair. Goodbye.")
    time.sleep(5)
    exit()

#(49) Greece Pavilion
def greece_pav():
#    time = 20
    print("While inside you look over large photomurals of Athens\nseen through the pillars of the Parthenon.")
    print("As you walk around the pavilion you learn about the nation's\nindustrial developement, agricultural progress\nand contemporary sculpture and ceramics.")
    print("Where would you like to go next?")
    print("To the left is THE AFRICAN PAVILION and to the right is THE UNISPHERE.")
    gre1()
def gre1():
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE AFRICAN PAVILION")
        african_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE UNISPHERE.")
        unisphere()
    else:
        print("I didn't understand that.\n")
        gre1()

#(51) Guinea Pavilion
def guinea_pav():
#    time = 15
    print("You take a bridge leading to three buildings that make up the pavilion.\nWhile inside you watch members of Les Ballet Africains perform\ntheir interpretations of Guinean dances.")
    print("Before you exit the pavilion you look over the many tribal carvings and jewelry on display.\nWhere do you decide to go next?")
    print("To the left is THE SIERRA LEONE PAVILION and to the right is THE JORDAN PAVILION.")
    gui1()
def gui1():
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE SIERRA LEONE PAVILION")
        sierra_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE JORDAN PAVILION.")
        jordan_pav()
    else:
        print("I didn't understand that.\n")
        gui1()

#(53) Hall of Free Enterprise Pavilion
def hall_pav():
#    time = 35    
    print("")
    print("There is someone talking on an oval stage,\nbut you see a device called the Answer Machine that catches your eye.")
    halla()
def halla():
    choice = input("Would you like to know the answer to one of the questions on the wall?\nleft or right?\n ") 
    if choice == "yes":
        print("\nThe answer to why can't individuals have everything they want is . . .")
        time.sleep(3)
        print("Individuals cannot have everything they want because\nthey are constrained by a budget. Goods and services cost money,\nmeaning you need to work and get paid in order to consume the goods and services they want.\nFor most people unfortunately, the money made by working is significantly less than\nthe value of the amount of goods and services they want.")
        hallb()
    elif choice == "no":
        print("Of course, lets move on.")
        hallb()
    else:
        print("I didn't understand that.\n")
        halla()

def hallb():
    print("After walking through the pavilion you decide where to go next.")
    print("To the left is THE VATICAN PAVILION")
    print("and to the right is THE INTERNATIONAL PAVILION.")
    hall2()
def hall2():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE VATICAN PAVILION.")
        vatican_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE INTERNATIONAL PAVILION.")
        international_pav()
    else:
        print("Can you say that again, please.\n")
        hall2()

#(64) International Plaza
def international_pav():
#    time = 30     
    global gold
    print("You enjoy displays such as U.N. postage stamps,\nworks of art and food specialties.")
    print("While walking about the pavilion you notice fairgoers eating a strange pastry.")
    print("So you walk up to a food vendor and ask what the pastry everyone is eating\n.The vendor tells you it is a Belguim waffle and asks if you want one.\n")
    int1()
def int1():    
    choice = input("Do you decide to buy a Belguim waffle for one dollar?\nyes or no\n ")
    if choice == "yes":
        gold - 1  
        print("You have",gold)
        print("")
        print("As you look over the quite large pastry in amazement\nyou wonder how to start to eat it.\nYou decide to attack it and don't worry about it\nfalling all over your shirt and pants.")
        print("'Mmmmmm, that is delicious', you say out loud.\n")
        inta()
    elif choice == "no":
        print("Of course, as you please.")
        inta()
    else:
        print("I’m sorry, I didn’t catch that.\n")
        int1()

def inta():
    print("After enjoying the sights, sounds, and smells of the plaza\nyou consider your next destination.")
    print("To the left is THE NEW YORK STATE PAVILION")
    print("and to the right is THE SWEDEN PAVILION.")
    int2()
def int2():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE NEW YORK STATE PAVILION.")
        nysb_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE SWEDEN PAVILION.")
        sweden_pav()
    else:
        print("I didn't understand that.\n")
        int2()

#(66) Japan Pavilion
def japan_pav():    
#    time = 40   
    print("As you enter the first of three stone buildings that represent Japan,\nyou look over the imaculate stone craftsmanship of the structure\nthat is surrounded by a moat filled with water.\nWhile inside you you learn of Japan's emergence as an industrial nation.")
    print("While in the concession area of the pavilion you look over some of the statistics of Japan.")
    jpn1() 
def jpn1():
    choice = input("Would you like to read the quote or know more about one of the Biblical verses?\nyes or no\n ")
    if choice == "yes":
        randint = random.randint(0,2)
        if randint == 1: 
            print("\nLand Area: 142,732 Square Miles, 1/21 that of the United States of America.\n")
            jpn2()        
        elif randint == 2:
            print("\nPopulation: 88,374,000 as of January 1, 1964, 7th in the World.\n")
            jpn2()
        elif randint == 3:
            print("\nPopulation Density: 674 persons per square mile.\n")
            jpn2()        
    elif choice == "no":
        print("Of course, let's move on.\n")        
        jpn2()
    else:
        print("I didn't understand that.\n")
        jpn1()

def jpn2():
    print("After you take in the rest of the pavilion you decide where to go next.")
    print("Do you head left to THE UNITED ARAB REPUBLIC PAVILION\nor right to THE ROCKET THROWER SCULPTURE.")    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE UNITED ARAB REPUBLIC PAVILION.")
        uar_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE ROCKET THROWER SCULPTURE.")
        rocket()
    else:
        print("I didn't understand that.\n")
        jpn2()

#(68) Johnson Wax Pavilion
def jw_pav():    
#    time = 40      
    print("You walk up the ramp into the golden disc-shaped pavilion\nthat contains a 500-seat theater and watch 'To Be Alive'.\nAn 18-minute documentary film that utilizes three seperate screens\nto depict the daily lives of people around the world.")
    print("After you enjoy the film you notice a sign for an exhibit titled 'Children's Entertainment Center'.")
    jw1()
def jw1():    
    choice = input("Do you decide to enter?\nyes or no?\n ") 
    if choice == "yes":
        print("Inside the Childrens Entertainment Center you climb through a 'fun machine',\na mazelike device full of mirrors that fracture images,\nsqueeze-bulbs that emit strange noises and cranks that operate robots.\n")
        print("On your way out you decide where to go to next.")
        print("Do you head left to THE JAPAN PAVILION\nor right to THE AUSTRIA PAVILION.")    
        jw2()
    elif choice == "no":
        print("Alright, where would you like to go to next?")
        print("Do you head left to THE JAPAN PAVILION\nor right to THE AUSTRIA PAVILION.")    
        jw2()
    else:
        print("I didn't understand that.\n")
        jw1()  

def jw2():
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE JAPAN PAVILION.")
        japan_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE AUSTRIA PAVILION.")
        austria_pav()
    else:
        print("I didn't understand that.\n")
        jw2()

#(69) Jordan Pavilion
def jordan_pav():    
#    time = 60   
    print("Before you walk into the pavilion you take in and look over\nthe Column of Jerash that sits outside the building.\nYou also find out that the Roman column was gifted to New York City\nand that it will remain on display within the park after the fair.\nAfter taking in the historic column you walk in to the pavilion and enter\nthe exhibit 'Two Thousand Years' and view one of the Dead Sea Scrolls\nin a replica of the cave where it was discovered.")
    print("After you walk through the rest of the pavilion\nyou decide where you would like to go to next.")
    print("Do you head left to THE MOROCCO PAVILION\nor right to THE GREECE PAVILION?")
    jor1()
def jor1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE MOROCCO PAVILION.")
        mor_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE GREECE PAVILION.")
        greece_pav()
    else:
        print("I didn't understand that.\n")
        jor1()

#(72) Lebanon Pavilion
def lebanon_pav():    
#    time = 45
    print("Once you enter the pavilion you are greeted with\na 80-million-year-old fossil found in lebanon.\nThe fossil is inset into a green onyx bas-relief map\nthat shows the locations of Lebanon's principal towns.")
    print("After you take in the rest of the exhibits within the pavilon you decide where to go next.") 
    print("Do you head left to THE PHILIPINES PAVILION\nor right to THE UNISPHERE?")
    leb1()
def leb1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE UNISPHERE.")
        unisphere()
    elif choice == "right":
        print("\nYOU ARE AT THE PHILIPPINES REPUBLIC PAVILION.")
        phil_pav()
    else:
        print("I didn't understand that.\n")
        leb1()

# Light Fixture
def light():
#    time = 10
    print("As you stop to tie your shoe, you look up to notice\nthe multi-shaped and colored light fixtures\nthat surround the fairgrounds. There are hundreds of them\nand you notice that they all seem to be different.")


#(76) Louisiana Pavilion
def louisiana_pav():    
#    time = 30    
    global gold
    print("As you walk around the pavilion you enjoy the sights\nof a re-creation of New Orlean's Bourbon Street.\n")
    print("The sounds from the center of the pavilion\nhave you tapping your feet as you take a moment to watch the jazzmen\nplaying in a revolving bandstand in what is called Jazzland.")
    print("You hear there is a place to dance for teenagers and head to check it out.\nOnce you arrive at the Teen-Age Center, you are asked to pay one dollar.")
    loua()
def loua():
    choice = input("Do you pay to enter the Teen-Age Center?\nyes or no?\n ")
    if choice == "yes":
        gold - 1
        print ("You have",gold)
        print("")



        loub()
    elif choice == "no":
        print("\nOf course, as you please. Let's move on.")
        loub()
    else:
        print("I didn't understand that.\n")
        loua()

    loub()
def loub():
    print("After taking in the rest of the pavilion you consider the next place to go.")
    print("Do you head left to THE WESTINGHOUSE PAVILION\nor right to THE NEW YORK STATE PAVILION?")
    lou1()
def lou1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE WESTINGHOUSE PAVILION.")
        westinghouse_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE NEW YORK STATE PAVILION.")
        nysc_pav()
    else:
        print("I didn't understand that.\n")
        lou1()

#(83) Malaysia Pavilion
def malaysia_pav():
#    time = 20    
    print("During your visit to this new country's pavilion,\nyou walk to the center of the building\nand enjoy the sight of orchids and ferns that surround a small lily pond.")
    print("Also within the pavilion are visual devices\nand taped commentaries on pickup phones.\nWhich aquaint visitors to the pavilion with Malaysia's\npeople, government, industry and arts.")
    print("Where would you like to go to now?")
    print("To the left is THE NEW JERSEY PAVILION and to the right is THE UNISPHERE.")
    mal1()
def mal1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE NEW JERSEY PAVILION.")
        westinghouse_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE UNISPHERE.")
        minnesota_pav()
    else:
        print("I didn't understand that.\n")
        mal1()

#(83) Minnesota Pavilion
def minnesota_pav():
#    time = 25     
    print("As you walk up the ramp into the pavilion,\nyou take in the odd shaped exterior of the building.\nWhich takes the shape of a polyhedron with a cluster\nof seven units that make up the whole pavilion.")
    print("While walking around inside\nyou learn about Minnesota's instrustrial production.")
    print("Where would you like to go to now?")
    print("To the left is THE LOUISIANNA\nand to the right is THE NEW YORK STATE PAVILION.")
    minn1()
def minn1():
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE LOUISIANA PAVILION.")
        louisiana_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE NEW YORK STATE PAVILION.")
        nysb_pav()
    else:
        print("I’m sorry, I didn’t catch that.\n")
        minn1()

#(83) Missouri Pavilion
def missouri_pav():
#    time = 15 
    print("As you walk around the pavilion you visit exhibits that contain\na replica of the 'Spirit of St. Louis', the plane Charles A. Lindbergh\nflew from New York to Paris in 1927, two space capsules, Mercury and Gemini,\nand mementos of famous Missourians such as author Mark Twain,\npoet Eugene Field, and artists Thomas Hart Benton and George Caleb Bingham.")
    print("After you wonder through the rest of the pavilion you decide where to go to next?")
    print("To the left is THE GENERAL MOTORS PAVILION\nand to the right is THE WISCONSIN PAVILION.")
    miss1()
def miss1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE GENERAL MOTORS PAVILION.")
        gm_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE WISCONSIN PAVILION.")
        wisconsin_pav()
    else:
        print("I didn't understand that.\n")
        miss1()

#(89) Morocco Pavilion
def mor_pav():    
#    time = 45      
    print("While inside you walk around the exhibit 'Land of the Bazaar'.\nWhere you see craftsmen and women in traditional dress\nweave carpets and make brassware and leather goods.")
    print("Where would you like to go to next?")
    print("Do you head left to THE AFRICAN PAVILION\nor right to THE GREECE PAVILION?")
    mor1()
def mor1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE AFRICAN PAVILION.")
        african_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE GREECE PAVILION.")
        greece_pav()
    else:
        print("I didn't understand that.\n")
        mor1()

# Robert Moses
def moses():
#    time = 10
    choice = input("Do you go to see who he is?\nyes or no?\n ") 
    if choice == "yes":
        randint = random.randint(0,2)
        if randint == 1: 
            print("\nYou ask a kid who looks your age who the man is in the middle\nof the crowd and he tells you that he was trying to figure it out, as well.\n")
            print("After your attempt to learn a little about the important person\nin the white suit you decide where to go next.")
            fairs1() 
        elif randint == 2:
            print("\nYou ask a white man who the figure in the middle of the crowd is\nand he says that he is Robert Moses, president of the fair\nand one of the most important men living today\ndue to the number of parks, highways and bridges\nhe was instrumental in creating throughout New York.\n")
            print("After you learn a little about the fair's president you decide where to go next.")
            fairs1()
        elif randint == 3:
            print("\nYou ask a black woman who the man in the middle of the crowd is\nand she says that he is Robert Moses, president of the fair\nand one of the most dispicable human beings due to the mistreatment\nof minority groups while he was the city's parks commisioner and as the president of the public housing* in New York.\n")
            print("After you learn a little about the fair's president you decide where to go next.")
            fairs1() 
    elif choice == "no":
        print("Alright, let's go to the next pavilion.\n")
        fairs1()
    else:
        print("I didn't understand that.\n")
        moses()

#(92) New Jersey
def nj_pav(): 
#    time = 30     
    print("While walking about the pavilion you find out the state\nis celebrating its tercentenary this year.")   
    print("As you make your way towards the center of the pavilion\nyou view local choral groups, bands, symphony orchastras and folk dances.")
    print("Where would you like to go to next?")
    print("To the left is THE NEW YORK CITY PAVILION\nand to the right THE UNISPHERE.")
    nj1()
def nj1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE NEW YORK CITY PAVILION.")
        unisphere()
    elif choice == "right":
        print("\nYOU ARE AT THE UNISPHERE.")
        nyca_pav()
    else:
        print("I didn't understand that.\n")
        nj1()

#(94) New York City Pavilion and Ice Theater A
def nyca_pav():    
#    time = 60
    print("While in the pavilion you observe the incredibly\ndetailed model of the city, which is 180 by 100 feet\nand includes every one of New York's 835,000 buildings\nand all of its streets, ferries, docks, bridges and airports.")   
    print("After you find your neighborhood on the model\nyou decide where to go to next?")
    print("To the left is THE GENERAL MOTORS PAVILION\nand to the right is THE TRANSPORTATION AND TRAVEL PAVILION.")
    nyca1()
def nyca1():   
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE GENERAL MOTORS PAVILION.")
        gm_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE TRANSPORTATION AND TRAVEL PAVILION.")
        tat_pav()
    else:
        print("I didn't understand that.\n")
        nyca1()

#(94) New York City Pavilion and Ice Theater B
def nycb_pav(): 
#    time = 60  
    print("You enjoy a model of NYC as it is today\nand how it was in 1664. Additionaly, you look over an exhibit of art,\n sculpture, artifacts and photographs from 34 of the city's\nmost important museums, libraries, zoos and botanical gardens.")   
    print("After walking around the pavilion you decide where to go to next?")
    print("To the left is THE GENERAL MOTORS PAVILION\nand to the right is THE TRANSPORTATION AND TRAVEL PAVILION.")
    nycb2()
def nycb2():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE GENERAL MOTORS PAVILION.")
        gm_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE TRANSPORTATION AND TRAVEL PAVILION.")
        tat_pav()
    else:
        print("I’m sorry, I didn’t catch that.\n")
        nycb2()

#(95) New York State Pavilion A
def nysa_pav():
#    time = 30 
    print("You take the 'Sky-Streak', a speedy elevator capsule,\nup the side of the fair's tallest towers.")
    print("From atop the tower you are able to see the whole fairgrounds!")
    print("You can also see the NYC Skyline, New Jersey, Connecticut,\nThe Atlantic Ocean and most of Long Island.")
    print("After you take in all the sights and sounds of the Fair\nyou consider where to go to next?")
    print("To the left is THE ALASKA PAVILION\nand to the right is THE MISSOURI PAVILION.")
    nysa1()
def nysa1():
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE ALASKA PAVILION.")
        alaska_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE MISSOURI PAVILION.")
        missouri_pav()
    else:
        print("I didn't understand that.\n")
        nysa1()

#(95) New York State Pavilion B
def nysb_pav():
#    time = 30     
    print("While at the pavilion you decide to check out the 'Tent of Tomorrow'.\nWhile you walk into the Tent you enjoy the sights above and below you.\nAbove you are wonderfully colored translucent fiberglass panels that creates a stained glass effect.\nBelow your feet is a humongous map of the state of New York.\nIn the distance you hear a school choir.")
    print("As you get closer you hear what they are singing, the song is titled 'Everything's Coming up Moses'.")
    nysb1()
def nysb1():    
    choice = input("Interested to know the lyrics to 'Everything's Coming up Moses'?\nyes or no\n ")
    if choice == "yes":
        print("\nYou'll be swell, You'll be great,")
        print("Gonna have the whole world on a plate.")
        print("Starting here, starting now")
        print("It's a small world after all")
        print("Honey, everything's coming up Moses!")
        print("")
        print("Clear the decks, Clear the tracks")
        print("You've got nothing to do but relax.")
        print("Blow a kiss, take a bow,")
        print("It's a small, small world")
        print("Honey, everything's coming up Moses!")
        print("")
        print("Now's our inning,")
        print("Stand the world on its ear!")
        print("Set it spinning,")
        print("It's a small world after all")
        print("That'll be just the beginning!")
        print("")
        print("Curtain up, light the lights")
        print("You got nothing to hit but the heights")
        print("You'll be swell, you'll be great")
        print("I can tell, Just you wait,")
        print("That lucky star I talk about is due..")
        print("Honey everything coming up Moses for me and for you!\n")
        print("After enjoying the song by a middle shool choir from Long Island\nyou decide where to head to next.")
        print("To the left is THE ALASKA PAVILION\nand to the right is THE MISSOURI PAVILION.")
        nysb2()
    elif choice == "no":
        print("\nOf course, as you please. Let's move on to the next pavilion.")
        print("To the left is THE ALASKA PAVILION\nand to the right is THE MISSOURI PAVILION.")
        nysb2()
    else:
        print("I didn't understand that.\n")
        nysb1()

    nysb2()
def nysb2():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE ALASKA PAVILION.")
        alaska_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE MISSOURI PAVILION.")
        missouri_pav()
    else:
        print("I didn't understand that.\n")
        nysb2()

#(95) New York State Pavilion C
def nysc_pav():
#    time = 30     
    print("As you walk around the Theaterama you enjoy the artwork on the outside of the theatre\nby Pop artists such as John Chamberlain, Robert Indiana, Roy Lichtenstein and James Rosenquist.")
    nysc1()
def nysc1():
    choice = input("Would you like to know more about one of the artworks?\nyes or no\n ")
    if choice == "yes":
        randint = random.randint(0,2)
        if randint == 1: 
            print("Roy\n")
            nysc2() 
        elif randint == 2:
            print("Ben\n")
            nysc2() 
        elif randint == 3:
            print("Robert\n")
            nysc2() 
    elif choice == "no":
        print("Of course, let's move on.\n")
        nysc2()
    else:
        print("I didn't understand that.\n")
        nysc1()

    nysc2()
def nysc2():
    print("After you take in the rest of the art around the building\nyou consider where would you like to go to next?")
    print("To the left is THE ALASKA PAVILION\nand to the right is THE MISSOURI PAVILION.")
    nysc3()
def nysc3():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE ALASKA PAVILION.")
        alaska_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE MISSOURI PAVILION.")
        missouri_pav()
    else:
        print("I didn't understand that.\n")
        nysc3()

#(98) Pakistan Pavilion
def pakistan_pav():
#    time = 30 
    print("While walking through the pavilion you learn about the country's history\nthrough relics dating back thousands of years.")
    print("After taking your time to take in all the sights and sounds of the pavilion\nyou consider your next destination.")
    print("To the left is THE NEW YORK STATE PAVILION and to the right is THE NEW JERSEY PAVILION.")
    pak1()
def pak1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE NEW YORK STATE PAVILION.")
        nysb_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE NEW JERSEY PAVILION.")
        nj_pav()
    else:
        print("I’m sorry, I didn’t catch that.\n")
        pak1()

#(99)Pan American Highway Gardens
def panam_pav():
#    time = 10
    print("While you take some time to relax from all the excitement,\nyou enjoy the sights and smells of tropical plants and look over\nthe photomurals that depict the Pan American Highway.")
    print("After taking in the plants and imagery you consider where to head to next.")
    print("To the left is THE EASTMAN KODAK PAVILION\nand to the right is THE SERMONS OF SCIENCE PAVILION.")
    pan1()
def pan1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
       print("\nYOU ARE AT THE EASTMAN KODAK PAVILION.")
       eastman_pav()
    elif choice == "right":
       print("\nYOU ARE AT SERMONS OF SCIENCE PAVILION.")
       sfs_pav()
    else:
       print("I didn't understand that.\n")
       pan1()

#(102) Pepsi-Cola Pavilion
def pepsi_pav():
#    time = 25 
    global gold
    print("As you come up to the entrance of the 'Girdling the Globe' inside the pavilion\nyou are asked to pay 60 cents.")
    pepa()
def pepa():
    choice = input("Do you pay to enter the pavilion?\nyes or no?\n ")
    if choice == "yes":
        gold - 0.60  
        print("You have",gold)
        print("")
        print("\nWhile in the pavilion you take a boat ride called 'It's a Small World'.\nYou see scenes such as the Eiffel Tower,\na Dutch Windmill and India's Taj Mahal\nas anmimated figures dance and sing 'It's a Small World'.")
        pep1()
    elif choice == "no":
        print("That's fine. Let's go to the pavilion next door then.\n")
        time.sleep(3)
        print("You are at THE EASTMAN KODAK PAVILION.")
        eastman_pav()
    else:
        print("I didn't understand that.\n")
        pepa()

def pep1():    
    choice = input("While walking around the rest of the pavilion\nyou catch yourself humming the theme song from the boat ride.\nInterested to know the lyrics to 'It's a Small World'?\nyes or no\n ")
    if choice == "yes":
        print("\nIt's a world of laughter, a world of tears")
        print("It's a world of hopes and a world of fears")
        print("There's so much that we share, that it's time we're aware")
        print("It's a small world after all")
        print("")
        print("It's a small world after all")
        print("It's a small world after all")
        print("It's a small world after all")
        print("It's a small, small world")
        print("")
        print("There is just one moon and one golden sun")
        print("And a smile means friendship to everyone")
        print("Though the mountains divide, and the oceans are wide")
        print("It's a small world after all")
        print("")
        print("It's a small world after all")
        print("It's a small world after all")
        print("It's a small world after all")
        print("It's a small, small world\n")
        pep2()
    elif choice == "no":
        print("\nOf course, as you please.")
        pep2()
    else:
        print("I didn't understand that.\n")
        pep1()

def pep2():
    print("After enjoying the rest of the pavilion\nyou decide where to head to next.")
    print("To the left is THE EASTMAN KODAK PAVILION.")
    print("and to the right is THE SCHAEFER BREWING PAVILION.")
    pep3()
def pep3():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE EASTMAN KODAK PAVILION.")
        eastman_pav()
    elif choice == "right":
        print("\nYOU AT THE SCHAEFER BREWING PAVILION.")
        schaef_pav()
    else:
        print("I didn't understand that.\n")
        pep3()

#(103) Philippines Republic Pavilion
def phil_pav():    
#    time = 25     
    print("While in the pavilion you enjoy twelve large hand-carved wood murals.\nWhich depict the story of the island's history.")
    phil1()
def phil1():
    choice = input("Do you want to know more about one of the works of art from the pavilion guide description?\nyes or no?\n ") 
    if choice == "yes":
        randint = random.randint(0,2)
        if randint == 1: 
            print("The First Panel depicts")
            print("'Malakas at Maganda'") 
            print("In the beginning of Time, there was only the blue sky above,\nand the green sea below dotted here and there by islands filled with lush vegetation ... \nand flying about was a magnificent, black bird called the tigmamanukin.\n")
            print("While resting on a bamboo thicket one day, the great bird heard\nan unusual noise coming from within a large bamboo stalk.\nIn curious concern, the bird pecked on the stalk, the bamboo split in two,\nand lo! from one hollow side emerged a handsome and powerfully-built brown man,\nand from the other side a beautiful brown maiden.")
            print("The man addressed the woman as Maganda (Tagalog word for 'beautiful')\nand she, in turn, called him Malakas (meaning 'strong'),\nand this is how they came to be known.")
            print("Shortly thereafter and with the approval and blessing of Bathala,\nthe god-creator of all, Malakas took Maganda for his wife\nand their children and grand-children and other generations\nthat followed peopled the country now known as the Republic of the Philippines.\n")
            phil2() 
        elif randint == 2:
            print("The Second Panel depicts")
            print("'The Malay Migrations'") 
            print("The Malays were not the first people in the Philippines.\nAetas, and a scattering of pygmy tribes now almost extinct,\nalready inhabited the country when the Malay migrations began.")
            print("Recorded history tells of a fleet of fast-sailing binidays (outriggers)\ncomprising well-organized barangays (village communities)\nof some ten brave datus (tribal chieftans) from neighboring Borneo who,\nin the 13th century, fled their native land to escape the tyranny of Mukatunaw, their sultan.\nThey landed in Panay, westernmost island in the Visayan region that comprises the central area\nof the archipelago, where they settled. Shortly thereafter,\nother migratory waves from Borneo followed which accounts for the Malay\nracial stock of present-day Filipinos who now number well over 30 million.\n")
            phil2() 
        elif randint == 3:
            print("The Third Panel depicts")
            print("Code of Kalantiaw") 
            print("Unknown and unpublicized is the fact that, long before Europe\nmade its first contact in the Philippines, the country and its people enjoyed\na fairly advanced civilization of its own.")
            print("One of the wisest and most beloved rulers during the 13th century was Kalantiaw,\nwho instituted a code of laws for the members of his barangay in the island of Panay.") 
            print("Generally conceded as more humane than the Code of Hamurabi,\nthe Code of Kalantiaw provided penalties for such unlawful acts as\nkilling, stealing, sacrilege, and disrespect for the aged and persons of authority.\n")
            phil2() 
    elif choice == "no":
        print("That's fine. Where would you like to go next?")
        phil2()
    else:
        print("I didn't understand that.\n")
        phil1()
    
def phil2():
    print("Do you head left to THE GREECE PAVILION\nor right to THE UNISPHERE?")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE GREECE PAVILION.")
        greece_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE UNISPHERE.")
        unisphere()
    else:
        print("I didn't understand that.\n")
        phil2()

# Fountain of the Planets
def planets_foun(): 
#    time = 10
    print("")   



    print("Where would you like to go from here?")
    print("To the left is THE TOWER OF LIGHT PAVILION\nand to the right is THE FOUNTAIN OF THE FAIRS.")
    plan1()
def plan1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE TOWER OF LIGHT PAVILION.")
        tol_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE FOUNTAIN OF THE FAIRS.")
        fairs_foun()
    else:
        print("I didn't understand that.\n")
        plan1()

# Rocket Thrower Scuplture
def rocket():
#    time = 10
    print("")   



    print("Where would you like to go from here?")
    print("To the left is THE  PAVILION\nand to the right is THE  PAVILION.")
    rock1()
def rock1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE UNITED ARAB REPUBLIC PAVILION   ")
        uar_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE LEBANON PAVILION.")
        lebanon_pav()
    else:
        print("I didn't understand that.\n")
        rock1()

#(114) Schaefer Brewing Pavilion
def schaef_pav():
#    time = 10
    print("As you walk around the pavilion you check out the gallery of outstanding\nsports photography in addition to the brewing industry history in Germany.")
    print("While walking through the exhibit you notice some commotion coming from the ")
    print("")
    shaef1()
def shaef1():    
    choice = input("Do you go to see what is going on?\nyes or no?\n ") 
    if choice == "yes":
        print("\n . . . ")





        shaef2()
    elif choice == "no":
        print("Of course, let's move on.\n")
        shaef2()
    else:
        print("I didn't understand that.\n")
        shaef1()

def shaef2():
    print("Where would you like to go next?")
    print("To the left is THE PAN AMERICAN HIGHWAY GARDENS\nand to the right is THE GENERAL ELECTRIC PAVILION")
    shaef3()
def shaef3():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE PAN AMERICAN HIGHWAY GARDENS.")
        panam_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE GENERAL ELECTRIC PAVILION.")
        ge_pav()
    else:
        print("I didn't understand that.\n")
        shaef3()

#(116) Sermons from Science Pavilion
def sfs_pav():
#    time = 30
    print("As you walk into the pavilion you enter a 500 seat auditorium.\nYou immediately see a man take off his shoes and stand on a transmitter while holding a pine board.")
    sfs1()
def sfs1():
    choice = input("Do you stay to see what happens next?\nyes or no?\n ") 
    if choice == "yes":
        print("The man on the stage yells, 'Lights!',\nand the auditorium darkens followed by the command 'On!'\nYou then see sparks come from the board of wood as it then bursts into flames.\nSeemingly unharming the presenter, wow!\nAfter watching a couple more demonstrations you consider where to head to next.")
        print("Where would you like to go?")
        print("To the left is THE PAN AMERICAN HIGHWAY GARDEN\nand to the right is THE GUINEA PAVILION.")
        sfs2()
    elif choice == "no":
        print("That's fine. Where would you like to go next?")
        print("To the left is THE PAN AMERICAN HIGHWAY GARDEN\nand to the right is THE GUINEA PAVILION.")
        sfs2()
    else:
        print("I didn't understand that.\n")
        sfs1()

def sfs2():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE PAN AMERICAN HIGHWAY GARDENS.")
        americanisrael_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE GUINEA PAVILION.")
        guinea_pav()
    else:
        print("I didn't understand that.\n")
        sfs2()

#(119) Sierra Leone Pavilion
def sierra_pav():
#    time = 30 
    global gold
    print("As you come up to the entrance of the pavilion\nyou are asked to pay 10 cents.")
    seia()
def seia():
    choice = input("Do you pay to enter the pavilion?\nyes or no?\n ")
    if choice == "yes":
        gold - 0.10  
        print("You have",gold)
        print("")
        seib()
    elif choice == "no":
        print("Alright, let's go to THE MALAYSIA PAVILION.")
        malaysia_pav()
    else:
        print("I didn't understand that.\n")
        seia()

def seib():
    print("Walking up to the pavilion you notice a raised stage with people dancing.")
    print("As you get closer you watch two troupes perform intricate dances.")



    print("Where would you like to go next?")
    print("To the left is THE MALAYSIA PAVILION\nand to the right is THE AFRICAN PAVILION")
    sie1()
def sie1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE MALAYSIA PAVILION.")
        malaysia_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE AFRICAN PAVILION.")
        african_pav()
    else:
        print("I didn't understand that.\n")
        sie1()

#(121) Sinclair Pavilion
def sinclair_pav():
#    time = 10     
    print("Within the open-air pavilion you enjoy the sights of nine fiberglas dinosaurs.")
    sin1()
def sin1():
    choice = input("Would you like to know more about one of the dinosaurs\nbased from the Dinoland Guidebook 'The Exciting World of Dinosaurs'?\nyes or no\n ")
    if choice == "yes":
        randint = random.randint(0,8)
        if randint == 1: 
            print("Brontosaurus\n(Bront-o-sawr-us)")
            print("One of the largest and best-known dinosaurs. Called 'Thunder Lizard' because the ground supposedly shook when they walked. This dinosaur was 70 to 80 feet in length and weighed about 20 tons. They had a very long neck which probably enabled them to feed on underwater plants in marshes and streams. They lived in North America, during the Jurassic Period some 135- to 180-million years ago.")
            sin2() 
        elif randint == 2:
            print("STRUTHIOMIMUS\n(Stru-thi-o-mi-mus)")
            print("Struthiomimus looked like an ostrich, with long hind limbs and small, hard beak. The name means 'ostrich mimic.' They were approximately 14 feet long, seven or eight feet high. Their front legs had clasping fingers and curved claws. They had large eyes and a slender neck. They probably ate fruits and vegetation and perhaps the eggs of other dinosaurs. Struthiomimus lived in the Cretaceous Period in North America some 63- to 135-million years ago.")
            sin2() 
        elif randint == 3:
            print("TRACHODON\n(Trak-o-don)")
            print("Trachodon was a plant-eater. They could walk either on their hind legs or on all fours. The name means 'rough tooth.' Some trachodons had 1,500 teeth, so arranged that, as one row wore out, another row replaced it. But these many teeth were useless as weapons against flesh-eating dinosaurs. Trachodon was a duck-billed, web-footed dinosaur, about 32 feet long and 14 feet high. They lived in North America in the late Cretaceous Period.")
            sin2() 
        elif randint == 4:
            print("TYRANNOSAURUS\n(Tye-ran-o-sawr-us)")
            print("Largest and most terrifying flesh-eater that ever lived. Their teeth were six inches long, like daggers with sharp, serrated cutting edges. They measured 50 feet from tip to tip, and their head rose 18 to 20 feet above the ground. Known as 'Tyrant Lizard,' this ferocious giant spelled death and destruction to most other creatures. They existed in Montana in the late Cretaceous Period. Tyrannosaurus reigned supreme for many millions of years.")
            sin2() 
        elif randint == 5:
            print("TRICERATOPS\n(Tri-ser-a-tops)")
            print("Triceratops was a giant horned dinosaur. The name means 'three horns on the face.' This tough-looking fellow resembled a rhinoceros. They were 20 to 30 feet in length, with a skull 7 feet long. Their best defense against meat-eating enemies was an active offense, employing the long brow horns. They were a vegetable-feeder with a beak like a parrot's and sharp teeth for chopping up plant food. Triceratops lived in Montana and Wyoming in Cretaceous times.")
            sin2()
        elif randint == 6:
            print("ANKYLOSAURUS\n(An-kyle-o-sawr-us)")
            print("Ankylosaurus was a walking fortress. The name means 'curved lizard.' They were completely covered with bony armor which protected them from bigger and stronger dinosaurs. They were about 20 feet long and 6 feet wide. Their skull was large, with an extra layer of bony plates. The huge bony club at the end of their tail was mighty useful as a weapon. Ankylosaurus was a plant-eater. They lived in Western United States and Canada during the Cretaceous Period.")
            sin2() 
        elif randint == 7:
            print("CORYTHOSAURUS\n(Kor-ith-o-sawr-us)")
            print("Although this duck-billed dinosaur averaged 30 feet in length, he was no match for the flesh-eating dinosaurs of his time. He lived in the water, may have eaten water plants, perhaps shellfish, too. Corythosaurus means 'helmet lizard' because of the large crest on his skull, which resembled a Corinthian helmet. He lived in North America during the late Cretaceous times. The duckbills were the most abundant of the dinosaurs.")
            sin2() 
        elif randint == 8:
            print("ORNITHOLESTES\n(Or-nith-o-les-tes)")
            print("Orintholestes weighted little more than a turkey. They were lightly built, had many hollow bones. They lived in the last part of the Jurassic Period in Wyoming. From such small, primitive reptiles came the giant, flesh-eating dinosaurs of later times. Alert and fast-moving, they probably fed on lizards and other small ground animals. This skull was comparatively small. Ornitholestes was about 6 feet in length, had a long tail, bird-like feet and sharp claws.")
            sin2() 
        elif randint == 9:
            print("STEGOSAURUS\n(Steg-o-sawr-us)")
            print("The double row of bony plates on this dinosaurs back made them one of the oddest-looking of all dinosaurs. Apparently, they fought with their back to their enemies, defending themselves with the four long spikes on their tail. The front of their jaws formed a sort of beak. They ranged from 18 to 25 feet long, weighed about four tons. This slow-moving armored dinosaur fed on soft vegetation, lived in Western United States during the Jurassic Period.")
            sin2()
    elif choice == "no":
        print("Of course, let's move on.\n")
        sin2()
    else:
        print("I didn't understand that.\n")
        sin1
    
def sin2():
    print("After you check out some of the dinasours you decide it is time to go home.")
    print("I hope you enjoyed the 1964-1965 World's Fair. Goodbye.")
    time.sleep(5)
    exit()

#(123) SKF Industries Pavilion
def skf_pav():
#    time = 15 
    print("You walk around the 'Matter in Motion' exhibit which displays objects that use bearings\nsuch as a kitchen mixer to a truck axle, cut away to disclose their mechanical interiors.")    
    print("After you walk around the pavilion you decide it is time to go home.")
    print("I hope you enjoyed the 1964-1965 World's Fair. Goodbye.")
    time.sleep(5)
    exit()

#() Solar Fountain
def solar_foun():    
#    time = 10 
    print("")
    print("Do you head left to THE AFRICAN PAVILION\nor right to THE GREECE PAVILION?")
    sol1()
def sol1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE GUINEA PAVILION.")
        guinea_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE AUSTRIA PAVILION.")
        austria_pav()
    else:
        print("I didn't understand that.\n")
        sol1()

#(127) Sweden Pavilion
def sweden_pav():
#    time = 30     
    print("Within the pavilion you enjoy a number of exhibits\nshowing fascinating mechanical or electrical devices.")
    print("On display for the first time is a large model of Sweden's\nsupersecret new fighter plane, the 'Viggen', or Thunderbolt.")
    print("Where would you like to go to next?")
    print("To the left is THE NEW YORK STATE PAVILION\nand to the right is THE PAKISTAN PAVILION.")
    swed1()
def swed1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE NEW YORK STATE PAVILION.")
        nysc_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE PAKISTAN PAVILION.")
        pakistan_pav()
    else:
        print("I’m sorry, I didn’t catch that.\n")
        swed1()

#(129) Switzerland Pavilion
def switzerland_pav():
#    time = 45     
    print("While in the pavilion you check out the 'Time Center' near the entrance.\nAt the front of the exhibit are the dials and indicators of a large 'Master Clock'.")
    print("The 'Master Clock' is so accurate that it can measure irregularities in the earth's rotation.")
    print("After you take time to enjoy the rest of the exhibits you decide where to head to next.")
    print("To the left is THE INTERNATIONAL PAVILION\nand to the right is THE SIERRA LEONE PAVILION.")
    switz1()
def switz1():
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE INTERNATIONAL PLAZA")
        international_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE SIERRA LEONE PAVILION.")
        sierra_pav()
    else:
        print("I didn't understand that.\n")
        switz1()

#(132) Tower of Light Pavilion
def tol_pav():
#    time = 30   
    print("You are taken into the building by a moving ramp that goes over a reflecting pool.\nThe ramp then deposits you inside a show where three-dimensional\nanimated figures illustrate the wonders of electric power and light.\nAfter you enjoy the show and check out the rest of the pavilion you consider where to go next.")
    print("To the left is THE GENERAL CIGAR PAVILION\nand to the right is THE JOHNSON WAX PAVILION.")
    tol1()
def tol1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE GENERAL CIGAR PAVILION.")
        gc_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE JOHNSON WAX PAVILION.")
        jw_pav()
    else:
        print("I didn't understand that.\n")
        tol1()

#(133) Transportation and Travel Pavilion
def tat_pav():
#    time = 60     
    print("You take a moment to look over the roof of the pavilion.\nWhich is a dome that is an accurate relief map of the moon.\nWhile inside you watch a movie titled 'Around the World with the Navy'.\nWhich shows an atomic submarine cruising under Arctic ice, jets operating from an aircraft carrier\nand aerial acrobatics performed by the Navy's Blue Angels precision flying team.")
    print("After you walk around more of the pavilion you consider where to go next.")
    print("To the left is THE SKF INDUSTRIES PAVILION\nand to the right is THE UNITED STATES RUBBER PAVILION.")
    tat1()
def tat1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE SKF INDUSTRIES PAVILION.")
        skf_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE UNITED STATES RUBBER PAVILION.")
        usr_pav()
    else:
        print("I didn't understand that.\n")
        tat1()

#(136) United Arab Republic Pavilion
def uar_pav():    
#    time = 60       
    print("While inside, you enjoy some of the wonders of Egypt.\nSuch as a model of the Suez Canal, Egyptian cotton, and Handicrafts from around Egypt.")
    print("After you look around the rest of the pavilion, you consider where to go next.")
    print("Do you head left to THE JORDAN PAVILION\nor right to THE LEBANON PAVILION?")
    uar1()
def uar1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE JORDAN PAVILION.")
        jordan_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE LEBANON PAVILION.")
        lebanon_pav()
    else:
        print("I didn't understand that.\n")
        uar1()

#(138) United States Rubber
def usr_pav(): 
#    time = 10 
    global gold
    print("As you come up to the entrance of the tire shaped ferris wheel\nyou are asked to pay 25 cents.")
    usra()
def usra():
    choice = input("Do you pay to take the ride?\nleft or right?\n ")
    if choice == "yes":
        gold - 0.25  
        print("You have",gold)
        print("")
        usrb()
    elif choice == "no":
        print("That's fine. Let's go to THE CHRYSLER PAVILION.")
        chrysler_pav()
    else:
        print("I didn't understand that.\n")
        usra()    

def usrb():
    print("Wow you are able to see all the Transportation section,\nas well as most fair, in addition to the city skyline.")
    print("After you enjoy the ride you decide where would you like to go to next.")
    print("To the left is THE SKF INDUSTRIES PAVILION\nand to the right is THE CHRYSLER PAVILION.")
    usr1()
def usr1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE SKF INDUSTRIES PAVILION.")
        skf_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE CHRYSLER PAVILION.")
        chrysler_pav()
    else:
        print("I’m sorry, I didn’t catch that.\n")
        usr1()

#(140) Unisphere
def unisphere():
#    time = 15     
    print("While you try to get a better look at the fair's symbol,\nyou are stopped from getting closer due to a protest.")





#    choice = input("Would you like to know more about the protest?\nyes or no\n")
#    if choice == "yes":
#        print("")
#        print("")
#    elif choice == "no":
#        print("Of course, as you please.")
#    else:
#        print("I didn't understand that.\n")

    uni1()
def uni1():
    print("Where do you decide to go to next?")
    print("To the left is THE WISCONSIN PAVILION\nand to the right is THE NEW YORK CITY PAVILION.")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE WISCONSIN PAVILION")
        international_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE NEW YORK CITY PAVILION.")
        sierra_pav()
    else:
        print("I didn't understand that.\n")
        uni1()

#(141) Vatican Pavilion
def vatican_pav():
#    time = 45     
    print("As you enter the pavilion you walk along the Long Gallery.\nAfter you walk through the Gallery you are brisked away along a moving platform\nwhere you look in awe at the 'Pietà' by Michelangelo.")
    print("After you walk through various other parts of the pavilion\nyou consider where to go to next?")
    print("To the left is THE MINNESOTA PAVILION\nand to the right is THE ASTRAL FOUNTAIN.")
    vat1()
def vat1():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE MINNESOTA PAVILION.")
        minnesota_pav()
    elif choice == "right":
        print("YOU ARE AT THE ASTRAL FOUNTAIN.")
        astral_foun()
    else:   
        print("I didn't understand that.\n")
        vat1()

#(143) Walter's International Wax Museum
def walters_pav():
#    time = 25
    global gold
    print("As you come up to the entrance of the building\nyou are asked to pay 50 cents.")
    walta()
def walta():
    choice = input("Do you pay to enter the museum?\nyes or no?\n ")
    if choice == "yes":
        gold - 0.50  
        print("You have",gold)
        print("")
        print("While in the exhibit you look over some 160 lifelike figures.\nThe figures are taken from art, history, mythology, movies and television.\nThe largest scene is a 20-by-30 foot copy of Leonardo da Vinci's 'The Last Supper'.")
        print("When you think you have seen all the figures in the museum you head for the exit.")
        waltb()
    elif choice == "no":
        print("Of course, let's move on.")
        waltb()
    else:
        print("I didn't understand that.\n")
        walta()  
    
def waltb():    
    print("After you walk around the Lake Amusement Area to take in some of the sights\nyou decide it is time to go on home.")
    print("I hope you enjoyed the 1964-1965 World's Fair. Goodbye.")
    time.sleep(5)
    exit()  

#(145) Westinghouse Pavilion
def westinghouse_pav():
#    time = 15    
    print("Within the pavilion you enjoy the copies of items buried\nin the Time Capsule from 1938.\nYou learn that they were buried in the 1939-1940 World's Fair\nwhich also took place at this park.")
    west1()
def west1():    
    choice = input("Interested to know about some of the items from the Time Capsule?\nyes or no\n ")
    if choice == "yes":
        randint = random.randint(0,5)
        if randint == 1: 
            print("Alarm clock, can opener, nail file, tooth brush,\nset of alphabet blocks, baseball, deck of cards, and poker chips.") 
            westa()
        elif randint == 2:
            print("Rubber fabrics, aluminum, carbon steel, copper, silicon,\nstainless steel, glass wool and raw rubber") 
            westa()
        elif randint == 3:
            print("Money of the United States, a message from Albert Einstein\nand the Holy Bible.") 
            westa()
        elif randint == 4:
            print("Microfilm of 'Guernica' by Pablo Picasso,\nphotograph of string quartet,\nand a typical poker scene.") 
            westa()
        elif randint == 5:
            print("Newsreel of President Franklin D. Roosevelt\nspeaking at Gettysburg, Pennsylvania, July 3, 1938,\nJesse Owens winning 100 meter dash in 1936 Olympic games,\nand Collegiate football: Harvard-Yale, November 1936 at 'Yale Bowl,'\nNew Haven, Conn. Yale wins 14-13.") 
            westa()
    elif choice == "no":
        print("Of course, let's move on.\n")
        westa()
    else:
        print("I didn't understand that.\n")
        west1()

def westa():
    print("After you enjoy the Time Capsule you consider\nthe next pavilion you would like to visit.")
    print("To the left is THE ALASKA PAVILION\nand to the right is THE NEW YORK STATE PAVILION.")
    west2()
def west2():
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE ALASKA PAVILION.")
        alaska_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE NEW YORK STATE PAVILION.")
        nysa_pav()
    else:
        print("I didn't understand that.\n")
        west2()

#(147) Wisconsin Pavilion
def wisconsin_pav(): 
#    time = 20
    print("You walk into a modern teepee that is representative of the states Indian hertiage.\nOnce inside you enjoy displays of the state's\nfarms, industries and great outdoors.")   
    print("Before leaving the Pavilion you notice a large yellow block on a van.\nAs you get closer you find out it is actually a block of cheese\nwhich is said to be 17 tons and possibly the world's largest.")
    wisc1()
def wisc1():
    choice = input("Would you like to know more about the block of cheese?\nyes or no\n ")
    if choice == "yes":
        print("The cheese was made for the Wisconsin Cheese Foundation\nand took 43 1/2 hours to make.\nThe size of the cheese is 6 1/2 feet wide, 5 1/2 feet high and 14 1/2 feet long.\nThe approximate weight of the cheese is 17 1/4 tons or 34,591 pounds.") 
        wisca()
    elif choice == "no":
        print("Of course, let's move on.\n")
        wisca()
    else:
        print("I didn't understand that.\n")
        wisc1()

def wisca():    
    print("On your way out, and a little more hungrier than before you entered the pavilion,\nyou decide where you would like to head to next.")
    print("To the left is THE GENERAL MOTORS PAVILION and to the right is THE TRANSPORTATION AND TRAVEL PAVILION.")
    wisc2()
def wisc2():    
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE AT THE GENERAL MOTORS PAVILION")
        gm_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE TRANSPORTATION AND TRAVEL PAVILION.")
        tat_pav()
    else:
        print("I didn't understand that.\n")
        wisc2()

# First decision
def first(): 
    choice = input("Which way do you go?\nleft or right?\n ")    
    if choice == "left":
        print("\nYOU ARE AT THE EASTMAN KODAK PAVILION")
        eastman_pav()
    elif choice == "right":
        print("\nYOU ARE AT THE PEPSI-COLA PAVILION")
        pepsi_pav()
    else:
        print("I didn't understand that.")
        first()

# Second decision
def second():    
    choice = input("Would you like to know more about the areas of the fair before you proceed?\nyes or no\n ")
    if choice == "yes":
        print("\nThe areas of the fair are: Industrial, International,\nFederal and State, Transportation, Lake Amusement, and Flushing Bay.\n")
        print("The Industrial Area has 45 pavilions that showcases America's industry.\nThe International Area is represented by 80 nations in 37 pavilions.")
        print("The Federal and State Area represents 19 states.\nThe Transportation Area shows off the many forms of transportation.")
        print("The Lake Amusement Area is the smallest section, but with the most variety.\nThe Flushing Bay Area is a place for seafarers and sports fans.\n")            
        print("The site of people as well as strange and colorful buildings\nare in all directions near and as far as the eye can see.")
        print("What do you want to see first?")
        print("To your left you see THE EASTMAN KODAK PAVILION.")
        print("and to your right is THE PEPSI-COLA PAVILION.") 
        first() 
    if choice == "no":    
        print("Of course, as you please.")
        print("\nThe sight of thousands of people as well as dozens of strange and colorful buildings\nare in all directions near and as far as the eye can see.")
        print("What do you want to see first?")
        print("tO your left is THE EASTMAN KODAK PAVILION.")
        print("and to your right is THE PEPSI-COLA PAVILION.") 
        first()  
    else: 
        print("I didn't understand that.") 
        second() 

# Start
def start():
# ascii art font 3D Diagonal 
# from http://www.patorjk.com/software/taag/#p=display&f=3D%20Diagonal&t=FW%2064                                 
    print("                                                     ,--, ") 
    print("    ,---,.            .---.                        ,--.'| ")
    print("  ,'  .' |           /. ./|          ,---.      ,--,  | : ")
    print(",---.'   |       .--'.  ' ;         /     \  ,---.'|  : ' ")
    print("|   |   .'      /__./ \ : |        /    / '  ;   : |  | ; ")
    print(":   :  :     .--'.  '   \' .      .     ' /   |   | : _' | ")
    print(":   |  |-, /___/ \ |    ' '      '    / ;    :   : |.'  | ")
    print("|   :  ;/| ;   \  \;      :      |   :  \    |   ' '  ; : ")
    print("|   |   .'  \   ;  `      |      ;   |   ``. \   \  .'. | ")
    print("'   :  '     .   \    .\  ;      '   ;      \ `---`:  | ' ")
    print("|   |  |      \   \   ' \ |      '   |  .\  |      '  ; | ")
    print("|   :  \       :   '  |--'       |   :  ';  :      |  : ; ")
    print("|   | ,'        \   \ ;           \   \    /       '  ,/  ")
    print("`----'           '---'             `---`--`        '--'   ")                         
    time.sleep(3)

    name()
def name():
    name = input("\nWhat is your name, fairgoer?\n ")
    print("")
    print("Hello, " + name + "!")
# how to store name to recall later?
    print("After riding your bike around the neighborhood")
    print("you decide to see what all the excitement was about at the park\nand now you find yourself at a fence near the fairgrounds.")
    print("It looks like you are able to jump over it.\n")
    intro()
def intro():
    choice = input("Do you decide to sneak into the 1964-1965 World's Fair?\nyes or no\n ")
    if choice == "yes":
        print("")
        print("     ----------------------------------------")
        print("      WELCOME TO THE 1964-1965 WORLD'S FAIR!!")
        print("     ----------------------------------------") 
        print("")       
        print("You are now within the fair at the Court of the Five Boroughs.\nTo the left is the International Area and to the right is the Industrial Area.")
        choice = input("Would you like to know more about the areas of the fair before you proceed?\nyes or no\n ")
        if choice == "yes":
            print("\nThe areas of the fair are: Industrial, International,\nFederal and State, Transportation, Lake Amusement, and Flushing Bay.\n")
            print("The Industrial Area has 45 pavilions that showcases America's industry.\nThe International Area is represented by 80 nations in 37 pavilions.")
            print("The Federal and State Area represents 19 states.\nThe Transportation Area shows off the many forms of transportation.")
            print("The Lake Amusement Area is the smallest section, but with the most variety.\nThe Flushing Bay Area is a place for seafarers and sports fans.\n")            
            print("The site of people as well as strange and colorful\nbuildings are in all directions near and as far as the eye can see.")
            print("What do you want to see first?")
            print("To the left is THE EASTMAN KODAK PAVILION.")
            print("and to your right is THE PEPSI-COLA PAVILION.")  
            first()
        if choice == "no":    
            print("\nThe sight of thousands of people as well as dozens of strange and colorful buildings\nare in all directions near and as far as the eye can see.")
            print("What do you want to see first?")
            print("To the left is THE EASTMAN KODAK PAVILION.")
            print("and to your right is THE PEPSI-COLA PAVILION.")
            first()   
        else: 
            print("I didn't understand that.") 
            second() 
    elif choice == "no":
        print("\nLooks like you are not ready for this year's World's Fair. Goodbye.")
        time.sleep(5)
        exit()
    else: 
        print("I didn't understand that.")
        intro()

# The start of the game 
start()