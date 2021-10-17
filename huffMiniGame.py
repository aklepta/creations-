import random

def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))

def RPSgame():
    input("As you walk alongside tall bookcases, the glint of light reflecting off of an emerald surface catches your eye.\nYou walk over and pick up a black notebook with a silver engraving on the front. (enter)\n")
    print("The engraved letters spell out the name")
    prGreen("Tom Marvolo Riddle.")
    print("\n")
    input("You curiously open the book to find it filled with blank pages... (enter)\n")
    print("Suddenly ink etches across the center of the page you flipped to.")
    print("\n")
    prLightGray("Hello, mudblood. My name is Tom Riddle.\n I understand you require a third key to escape your circumstance.\n If you manage to win three games of Resurrection Stone, Invisibility Cloak, Elder Wand, I will grant you what you seek.")
    print("You flip to the next page and a new line of text appears. You grab a nearby quill and ink.")
    print("\n")

    hasNotWon = True
    while(hasNotWon):
        randomInt = random.randint(1,2)

        RiddleScore = 0
        userScore = 0
        i = 0
        for i in range(3):
                prLightGray("Write your answer if you dare to challenge me.")
                userPlay = input("R for Resurrection Stone, I for Invisibility Cloak, or E for Elder Wand: ")
                if userPlay == 'R':   

                    if randomInt == 1:
                         prLightGray("Riddle wrote Invisibility Cloak🧥. Cloak suffocates Stone. You lose.\n")
                         RiddleScore = RiddleScore + 1
                                    
                    if randomInt == 2:
                         prLightGray("Riddle wrote Elder Wand🪄. Wand zaps Rock to pieces. You win!\n")
                         userScore = userScore + 1
                                
                            
                if userPlay == 'I': 
                     if randomInt == 1:
                         prLightGray("Riddle wrote Resurrection Stone🪨. Cloak suffocates Stone. You win!\n")
                         userScore = userScore + 1
                            
                     if randomInt == 2:
                         prLightGray("Riddle wrote Elder Wand🪄. Wand zaps Rock to pieces. You lose.\n")
                         RiddleScore = RiddleScore + 1
                            
                if userPlay == 'E':
                     if randomInt == 1: 
                         prLightGray("Riddle chose Resurrection Stone🪨. Stone destroys Wand. You lose.\n")
                         RiddleScore = RiddleScore + 1
                            
                     if randomInt == 2:
                          prLightGray("Riddle chose Invisibility Cloak🧥. Wand uses spell to unravel Cloak threads. You win!\n")
                          userScore = userScore + 1
                                   
                if userPlay != 'R' and userPlay != 'I' and userPlay != 'E':
                     prLightGray("That is not allowed! I win this round mudblood.\n")
                     RiddleScore = RiddleScore + 1
                     continue

        print("At the bottom of the page your scores appear.")
        print(" ")
        print("  You ~ ", userScore)
        print("  Riddle ~ ", RiddleScore)
                                

        if userScore > RiddleScore:
            prLightGray("You have beaten me this time! Flip to the back of my diary to find the key you seek.")
            print("You take the golden key and toss the book back back onto the shelf and continue walking.")
            hasNotWon = False
        else:
            prLightGray("You fool I can not be beaten! You are lucky I am willing to give you another chance.\n")
