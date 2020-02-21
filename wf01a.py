# wf01a.py
from sys import exit
import time

# choices: [yes, no], [left, right, forward]


#() African Pavilion
def african_pav():
    print("")
    print("Where would you like to go to now?")
    print("To the left is . . . . and to the right is . . . . ")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE IN THE    PAVILION.")
        westinghouse_pav()
    elif choice == "right":
        print("\nYOU ARE IN THE    PAVILION.")
        minnesota_pav()
    else:
        print("I didn't understand that.\n")

#(3) Alaska Pavilion
def alaska_pav():
    print("While in the igloo shaped pavilion you observe\nthe 32-square-foot topographical model of Alaska.")
    print("Where would you like to go to next?")
    print("To the left is the . . . .  and to the right . . . ")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ENTER THE MISSOURI PAVILION.")
        missouri_pav()
    elif choice == "right":
        print("\nYOU ENTER THE   PAVILION.")
        sierra_pav()
    else:
        print("I didn't understand that.\n")

# Astral Fountain
def astral_pav(): 
    print("")   
    print("")
    print("To the left is THE WESTINGHOUSE PAVILION\nand to the right is THE NEW YORK STATE PAVILION.")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ENTER THE WESTINGHOUSE PAVILION   ")
        westinghouse_pav()
    elif choice == "right":
        print("\nYOU ENTER THE NEW YORK STATE PAVILION.")
        nys_pav()
    else:
        print("I didn't understand that.\n")

#(8) American-Israel Pavilion
def americanisrael_pav():
    print("After enjoying scenes and artifacts portraying 4,000 years of Jewish history\nyou consider which Pavilion to head to next.")
    choice = input("Which way do you go?\nleft or right?\n ")    
    if choice == "left":
        print("\nYOU ENTER THE CHRISTIAN SCIENCE PAVILION")
        christianscience_pav()   
    elif choice == "right":
        print("\nYOU ENTER THE SWITZERLAND PAVILION")
        switzerland_pav()
    else:
        print("I didn't understand that.\n")

#(14) Belguim Pavilion
def belguim_pav():
    print("As you walk through the pavilion you enjoy the sight of Gille Dancers.")
    print("Clowns with wooden shoes, ostrich-feather headdresses and bells\ndance through the streets to the sound of drums and brass instruments.")
    print("You learn that the Gilles hark back to 1540, when Belguim was ruled by Spain,\nand the conquistidors' triumph over Peruvian Indians was celebrated at Mardi Gras.")
    print("To your left you see THE LOUISIANNA PAVILION,\nand to the right you see THE VATICAN PAVILION?")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ENTER THE LOUISIANNA PAVILION")
        louisiana_pav()
    elif choice == "right":
        print("\nYOU ENTER THE VATICAN PAVILION")
        vatican_pav()
    else:
        print("I didn't understand that.\n")

#(24) Christian Science Pavilion
def christianscience_pav():
    print("The Pavilion is in a star-shaped\nand their is descriptions of the faith\nwith displays and recorded testimponials.")
    print("To the left is THE HALL OF FREE ENTERPRISE")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ENTER THE HALL OF FREE ENTERPRISE")
        hall_pav()
    elif choice == "right":
        print("\nYOU ENTER THE SWITZERLAND PAVILION")
        switzerland_pav()
    else:
        print("I didn't understand that.\n")

#(37) Eastman Kodak Pavilion
def eastman_pav():
    print("Atop this pavilion are five color photographs, each 30 by 36 feet in size.")
    print("Where do you decide to go to next?")
    print("To the left you see THE GARDEN OF MEDITATION\nand to the right is THE AMERICAN ISRAEL PAVILION.")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ENTER THE GARDEN OF MEDITATION")
        garden_pav()
    elif choice == "right":
        print("\nYOU ENTER THE AMERICAN ISRAEL PAVILION")
        americanisrael_pav()
    else:       
        print("I didn't understand that.\n")

#(40) First National City Bank Pavilion
def fncb_pav():
    print("Which is the Fair's only bank. Intersting . . . . ") 
    print("After contemplating what you would do with a few extra bucks\nyou consider which pavilion to head to next.")
    print("Do you go left to THE GARDEN OF MEDITATION,\nor right to THE HALL OF FREE ENTERPRISE?")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ENTER THE GARDEN OF MEDITATION.")
        garden_pav()   
    elif choice == "right":
        print("\nYOU ENTER THE CHRISTIAN SCIENCE CENTER.")
        christianscience_pav()
    else:
        print("I didn't understand that.\n")

#(44) France Pavilion
def france_pav():
    print("Within the pavilion there are small fashionable shops in aisles named for Paris streets.")
    print("Where would you like to go to next?")
    print("To the left is the . . . .  and to the right . . . ")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ENTER THE    ")
        international_pav()
    elif choice == "right":
        print("\nYOU ENTER THE   PAVILION.")
        sierra_pav()
    else:
        print("I didn't understand that.\n")

#(45) Garden of Meditation
def garden_pav():
    print("After you relax in the Garden,\nyou contemplate where to head to next.")
    print("Do you head left to THE BELGUIM PAVILION,\nor right to THE CHRISTIAN SCIENCE PAVILION?")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ENTER THE BELGUIM PAVILION.")
        belguim_pav()
    elif choice == "right":
        print("\nYOU ENTER THE CHRISTIAN SCIENCE PAVILION.")
        christianscience_pav()
    else:           
        print("I didn't understand that.\n")

#(48) General Motors
def gm_pav(): 
    print("")   
    print("")
    print("To the left is the . . . .  and to the right . . . ")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ENTER THE    ")
        international_pav()
    elif choice == "right":
        print("\nYOU ENTER THE   PAVILION.")
        sierra_pav()
    else:
        print("I didn't understand that.\n")

#(53) Hall of Free Enterprise Pavilion
def hall_pav():
    print("There is someone talking on an oval stage,\nbut you see a device called the Answer Machine that catches your eye.")
#    choice = input("Do you play with the Answer Machine?\nyes or no\n ")
#    if choice == "yes":
#        print("")  
#    elif choice == "no":
#        print("")
#    else: 
#        print("I didn't understand that.\n")
    print("After playing with the Answer Machine you decide where to go next.")
    print("")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ENTER THE  PAVILION.")
        belguim_pav()
    elif choice == "right":
        print("\nYOU ENTER THE  PAVILION.")
        christianscience_pav()
    else:
        print("I didn't understand that.\n")

#(64) International Plaza
def international_pav():
    print("")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ENTER THE FRANCE PAVILION.")
        france_pav()
    elif choice == "right":
        print("\nYOU ENTER THE SWEDEN PAVILION.")
        sweden_pav()
    else:
        print("I didn't understand that.\n")

#(76) Louisiana Pavilion
def louisiana_pav():
    print("While in the pavilion you dance to jazz in the big Teen-Age Dance Center.\nAfter dancing you consider the next pavilion to go to.")
    print("Do you head left to THE WESTINGHOUSE PAVILION\nor right to THE MINNESOTA PAVILION.")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ENTER THE WESTINGHOUSE PAVILION.")
        westinghouse_pav()
    elif choice == "right":
        print("\nYOU ENTER THE MINNESOTA PAVILION.")
        minnesota_pav()
    else:
        print("I didn't understand that.\n")

#(83) Malaysia Pavilion
def malaysia_pav():
    print("")
    print("Where would you like to go to now?")
    print("To the left is . . . . and to the right is . . . . ")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE IN THE    PAVILION.")
        westinghouse_pav()
    elif choice == "right":
        print("\nYOU ARE IN THE    PAVILION.")
        minnesota_pav()
    else:
        print("I didn't understand that.\n")

#(83) Minnesota Pavilion
def minnesota_pav():
    print("While walking around the pavilion you learn about Minnesota's instrustrial production.")
    print("Where would you like to go to now?")
    print("To the left is THE LOUISIANNA\nand to the right is THE NEW YORK STATE PAVILION.")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE IN THE LOUISIANA PAVILION.")
        louisiana_pav()
    elif choice == "right":
        print("\nYOU ARE IN THE NEW YORK STATE PAVILION.")
        nys_pav()
    else:
        print("I didn't understand that.\n")

#(83) Missouri Pavilion
def missouri_pav():
    print("")
    print("To the left is THE GENERAL MOTORS PAVILION\nand to the right is THE WISCONSIN PAVILION.")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE IN THE GENERAL MOTORS PAVILION.")
        gm_pav()
    elif choice == "right":
        print("\nYOU ARE IN THE WISCONSIN PAVILION.")
        wisconsin_pav()
    else:
        print("I didn't understand that.\n")

#(92) New Jersey
def nj_pav(): 
    print("")   
    print("")
    print("To the left is THE WISCONSIN PAVILION and to the right THE GENERAL MOTORS PAVILION.")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ENTER THE WISCONSIN PAVILION.")
        wisconsin_pav()
    elif choice == "right":
        print("\nYOU ENTER THE GENERAL MOTORS PAVILION.")
        gm_pav()
    else:
        print("I didn't understand that.\n")

#(94) New York City Pavilion and Ice Theater
def nyc_pav(): 
    print("While in the pavilion you observe the incredibly\ndetailed model of the city, which is 180 by 100 feet.")   
    print("After you find your neighborhood on the model\nyou decide where to go to next?")
    print("To the left is the . . . .  and to the right . . . ")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ENTER THE    ")
        international_pav()
    elif choice == "right":
        print("\nYOU ENTER THE   PAVILION.")
        sierra_pav()
    else:
        print("I didn't understand that.\n")

#(95) New York State Pavilion
def nys_pav():
    print("You take the 'Sky-Streak', a speedy elevator capsule,\nup the side of the fair's tallest towers.")
    print("From the tower you are able to see the whole fairgrounds!")
    print("You can also see the NYC Skyline, New Jersey, Connecticut,\nThe Atlantic Ocean and most of Long Island.")
    print("Where would you like to go to next?")
    print("To the left is the  . . . . . and to the right is . . . ")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ENTER THE NEW YORK CITY PAVILION.")
        nyc_pav()
    elif choice == "right":
        print("\nYOU ENTER THE   PAVILION.")
        sierra_pav()
    else:
        print("I didn't understand that.\n")

#() Pakistan Pavilion
def pakistan_pav():
    print("")
    print("")
    print("To the left is . . . . and to the right is . . . . ")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE IN THE    PAVILION.")
        westinghouse_pav()
    elif choice == "right":
        print("\nYOU ARE IN THE    PAVILION.")
        minnesota_pav()
    else:
        print("I didn't understand that.\n")

#() SKF Pavilion
def skf_pav():
    print("")
    print("Where would you like to go to now?")
    print("To the left is . . . . and to the right is . . . . ")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE IN THE    PAVILION.")
        westinghouse_pav()
    elif choice == "right":
        print("\nYOU ARE IN THE    PAVILION.")
        minnesota_pav()
    else:
        print("I didn't understand that.\n")

#(119) Sierra Leone Pavilion
def sierra_pav():
    print("Walking up to the pavilion you notice a raised stage with people dancing.")
    print("As you get closer you watch two troupes perform intricate dances.")
    print("Where would you like to go next?")
    print("To the left is the . . . .  and to the right . . . ")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ENTER THE    ")
        international_pav()
    elif choice == "right":
        print("\nYOU ENTER THE   PAVILION.")
        sierra_pav()
    else:
        print("I didn't understand that.\n")

#() Sinclair Pavilion
def sinclair_pav():
    print("")
    print("Where would you like to go to now?")
    print("To the left is . . . . and to the right is . . . . ")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE IN THE    PAVILION.")
        westinghouse_pav()
    elif choice == "right":
        print("\nYOU ARE IN THE    PAVILION.")
        minnesota_pav()
    else:
        print("I didn't understand that.\n")

#(127) Sweden Pavilion
def sweden_pav():
    print("Within the pavilion you enjoy a number of exhibits\nshowing fascinating mechanical or electrical devices.")
    print("On display for the first time is a large model of Sweden's\nsupersecret new fighter plane, the 'Viggen', or Thunderbolt.")
    print("To the left is the . . . .  and to the right . . . ")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ENTER THE    ")
        international_pav()
    elif choice == "right":
        print("\nYOU ENTER THE   PAVILION.")
        sierra_pav()
    else:
        print("I didn't understand that.\n")

#(129) Switzerland Pavilion
def switzerland_pav():
    print("While in the pavilion you check out the 'Time Center' near the entrance.\nAt the front of the exhibit are the dials and indicators of a large 'Master Clock'.")
    print("The 'Master Clock' is so accurate that it can measure irregularities in the earth's rotation.")
    print("After you take time to enjoy the rest of the exhibits you decide where to head to next.")
    print("To the left is THE INTERNATIONAL PAVILION\nand to the right is THE SIERRA LEONE PAVILION.")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ENTER THE INTERNATIONAL PLAZA")
        international_pav()
    elif choice == "right":
        print("\nYOU ENTER THE SIERRA LEONE PAVILION.")
        sierra_pav()
    else:
        print("I didn't understand that.\n")

#() Transportation and Travel Pavilion
def tat_pav():
    print("")
    print("Where would you like to go to now?")
    print("To the left is . . . . and to the right is . . . . ")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE IN THE    PAVILION.")
        westinghouse_pav()
    elif choice == "right":
        print("\nYOU ARE IN THE    PAVILION.")
        minnesota_pav()
    else:
        print("I didn't understand that.\n")

#() United States Rubber
def usr_pav():
    print("")
    print("Where would you like to go to now?")
    print("To the left is . . . . and to the right is . . . . ")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ARE IN THE    PAVILION.")
        westinghouse_pav()
    elif choice == "right":
        print("\nYOU ARE IN THE    PAVILION.")
        minnesota_pav()
    else:
        print("I didn't understand that.\n")

#(140) Unisphere
def unisphere_pav():
    print("While you try to get a better look at the fair's symbol,\nyou are stopped from getting closer due to a protest.")
#    choice = input("Would you like to know more about the protest?\nyes or no\n")
#    if choice == "yes":
#        print("")
#        print("")
#    elif choice == "no":
#        print("Of course, as you please.")
#    else:
#        print("I didn't understand that.\n")
    print("Where do you decide to go to next?")
    print("To the left is the . . . .  and to the right . . . ")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ENTER THE    ")
        international_pav()
    elif choice == "right":
        print("\nYOU ENTER THE   PAVILION.")
        sierra_pav()
    else:
        print("I didn't understand that.\n")

#(141) Vatican Pavilion
def vatican_pav():
    print("While brisked away along a moving platform you look in awe at the 'Pietà'.")
    print("Where would you like to go to next?")
    print("To the left is THE MINNESOTA PAVILION and to the right is THE ASTRAL FOUNTAIN.")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ENTER THE MINNESOTA PAVILION.")
        minnesota_pav()
    elif choice == "right":
        print("YOU ENJOY THE ASTRAL FOUNTAIN.")
        astral_pav()
    else:   
        print("I didn't understand that.\n")


#(102) Pepsi-Cola Pavilion
def pepsi_pav():
    print("While in the pavilion you take a boat ride, called 'It's a Small World'\nyou see scenes such as the Eiffel Tower,\na Dutch Windmill and India's Taj Mahal\nanmimated figures dance and sing 'Its a Small World'.")
#    choice = input("Interested to know the lyrics to 'It's a Small World'?\nyes or no\n")
#    if choice == "yes":
#        print("It's a world of laughter, a world of tears.")
#        print("It's a world of hopes and a world of fears.")
#        print("There's so much that we share, that it's time we're aware.")
#        print("It's a small world after all.")
#        print("")
#        print("It's a small world after all.")
#        print("It's a small world after all.")
#        print("It's a small world after all.")
#        print("It's a small, small world.")
#        print("")
#        print("There is just one moon and one golden sun.")
#        print("And a smile means friendship to everyone.")
#        print("Though the mountains divide, and the oceans are wide.")
#        print("It's a small world after all.")
#        print("")
#        print("It's a small world after all.")
#        print("It's a small world after all.")
#        print("It's a small world after all.")
#        print("It's a small, small world.")
#    elif choice == "no":
#        print("Of course, as you please.")
#    else:
#        print("I didn't understand that.\n")
    print("After you enjoy 'It's a Small World' you decide where to head to next.")
    print("To the left is the First National City Bank.")
    print("and to the right is the Eastman Kodak Pavilion.")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ENTER THE FIRST NATIONAL CITY BANK.")
        fncb_pav()
    elif choice == "right":
        print("\nYOU ENTER THE EASTMAN KODAK PAVILION.")
        eastman_pav()
    else:
        print("I didn't understand that.\n")

#(145) Westinghouse Pavilion
def westinghouse_pav():
    print("You enjoy the copies of articles buried in the Time Capsule from 1938.")
#    print("Interested to know about an item from the Time Capsule?\nyes or no\n")
#    if choice == "yes":
#        print("") 
#    elif choice == "no":
#        print(""")
#    else:
#        print("I didn't understand that.\n")
    print("After you enjoy the Time Capsule you consider the next pavilion")
    print("Do you head left to the Alaska Pavilion?")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ENTER THE ALASKA PAVILION.")
        alaska_pav()
    elif choice == "right":
        print("\nYOU ENTER THE NEW YORK STATE PAVILION.")
        nys_pav()
    else:
        print("I didn't understand that.\n")

#() Wisconsin Pavilion
def wisconsin_pav(): 
    print("")   
    print("")
    print("To the left is the . . . .  and to the right . . . ")
    choice = input("Which way do you go?\nleft or right?\n ") 
    if choice == "left":
        print("\nYOU ENTER THE    ")
        international_pav()
    elif choice == "right":
        print("\nYOU ENTER THE   PAVILION.")
        sierra_pav()
    else:
        print("I didn't understand that.\n")


# Start
def start():

# Introduction
    name = input("What is your name, fairgoer?\n ")
    print("")
    print("Hello, " + name + "!")
    print("After riding your bike around your neighborhood")
    print("you decided to see what all the excitement was about at the park\nand now you find yourself at a fence near the fairgrounds.")
    print("It looks like you are able to jump over it.\n")

# Start of game
    choice = input("Do you decide to sneak into the 1964-1965 World's Fair?\nyes or no\n ")
    if choice == "yes":
        print("")
        print("     ----------------------------------------")
        print("      WELCOME TO THE 1964-1965 WORLD'S FAIR!!")
        print("     ----------------------------------------") 
        print("")       
        print("You are now within the fair at the Court of the Five Boroughs\nto the left is the International Area and to the right is the Industrial Area.")
        choice = input("Would you like to know more about the areas of the fair before you proceed?\nyes or no\n ")
        if choice == "yes":
            print("\nThere are five areas of the fair: Industrial, International,\nFederal and State, Transportation, Lake Amusement, and Flushing Bay.\n")
            print("The Industrial Area has 45 pavilions that showcases America's industry.\nThe International Area is represented by 80 nations in 37 pavilions.")
            print("The Federal and State Area represents 19 states.\nThe Transportation Area shows off the many forms of transportation.")
            print("The Lake Amusement Area is the smallest section, but with the most variety.\nThe Flushing Bay Area is a place for seafarers and sports fans.\n")            
            print("The site of people as well as strange and colorful buildings\nare in all directions near and as far as the eye can see.")
            print("What do you want to see first?")
            print("To your left you see THE FIRST NATIONAL CITY BANK.")
            print("Forward is THE EASTMAN KODAK PAVILION.")
            print("and to your right is THE PEPSI-COLA PAVILION.")  
        if choice == "no":    
            print("\nThe site of thousands of people as well as dozens of strange and colorful buildings\nare in all directions near and as far as the eye can see.")
            print("What do you want to see first?")
            print("To your left you see THE FIRST NATIONAL CITY BANK.")
            print("Forward is THE EASTMAN KODAK PAVILION.")
            print("and to your right is THE PEPSI-COLA PAVILION.")    
    elif choice == "no":
        print("\nLooks like you are not ready for this year's World's Fair. Goodbye, " + name + ".")
        time.sleep(5)
        exit()
    else: 
        print("I didn't understand that.\n")

# First direction choice
    choice = input("Which way do you go?\nleft, right or forward?\n ")    
    
    if choice == "left":
        print("\nYOU ENTER THE FIRST NATIONAL CITY BANK PAVILION.")
        fncb_pav()
    elif choice == "forward":
        print("\nYOU ENTER THE EASTMAN KODAK PAVILION")
        eastman_pav()
    elif choice == "right":
        print("\nYOU ENTER THE PEPSI-COLA PAVILION")
        pepsi_pav()
    else:
        print("I didn't understand that.\n")

# The start of the game 
start()