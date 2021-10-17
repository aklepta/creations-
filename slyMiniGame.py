import random
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


def riddles():
    correctCounter = 0
    while correctCounter < 3:
        randoRiddle123 = random.randint(1,3)
        randoRiddle456 = random.randint(4,6)
        randoRiddle789 = random.randint(7,9)
        if (correctCounter == 0 and randoRiddle123 == 1):
            Riddle_1 = input("\nBeasts I love and kind I am. Who am I?: ")
            if Riddle_1.lower() == "hagrid":
                correctCounter += 1
                print("As you twist the last letter into place, the box clicks open. Riddles Correct: ", correctCounter)
            else: 
                print("The lock doesn't budge as you move the last letter. The engraving that holds the riddle starts to change in front of your eyes. Riddles left to go:", (3-correctCounter)) 

        if (correctCounter == 0 and randoRiddle123 == 2):
            Riddle_2 = input("\nThis is a type of high-flying game, you win if you catch the Golden Snitch: ")
            if Riddle_2.lower() == "quidditch":
                correctCounter += 1
                print("As you twist the last letter into place, the box clicks open. Riddles Correct: ", correctCounter)
            else: 
                print("The lock doesn't budge as you move the last letter. The engraving that holds the riddle starts to change in front of your eyes. Riddles left to go:", (3-correctCounter))

        if (correctCounter == 0 and randoRiddle123 == 3):
            Riddle_3 = input("\nRefers to himself only in the third, a kind soul who always keeps his word: ")
            if Riddle_3.lower() == "dobby":
                correctCounter += 1
                print("As you twist the last letter into place, the box clicks open. Riddles Correct: ", correctCounter)          
            else: 
                print("The lock doesn't budge as you move the last letter. The engraving that holds the riddle starts to change in front of your eyes. Riddles left to go:", (3-correctCounter))

        if (correctCounter == 1 and randoRiddle456 == 4):
            Riddle_4 = input("\nThis place has many rooms, including the Great Hall. In 1994 it hosted the Yule Ball: ")
            if Riddle_4.lower() == "hogwarts":
                correctCounter += 1
                print("As you twist the last letter into place, the box clicks open. Riddles Correct: ", correctCounter)
            else: 
                print("The lock doesn't budge as you move the last letter. The engraving that holds the riddle starts to change in front of your eyes. Riddles left to go:", (3-correctCounter))

        if (correctCounter == 1 and randoRiddle456 == 5):
            Riddle_5 = input("\nThis place you wouldn't want to appear, it's guarded by Dementors and Sirius Black escaped from here: ")
            if Riddle_5.lower() == "azkaban":
                correctCounter += 1
                print("As you twist the last letter into place, the box clicks open. Riddles Correct: ", correctCounter)
            else: 
                print("The lock doesn't budge as you move the last letter. The engraving that holds the riddle starts to change in front of your eyes. Riddles left to go:", (3-correctCounter))

        if (correctCounter == 1 and randoRiddle456 == 6):
            Riddle_6 = input("\nA feature Harry shared with his mother, made Snape think of no other: ")
            if Riddle_6.lower() == "eyes":
                correctCounter += 1
                print("As you twist the last letter into place, the box clicks open. Riddles Correct: ", correctCounter)
            else: 
                print("The lock doesn't budge as you move the last letter. The engraving that holds the riddle starts to change in front of your eyes. Riddles left to go:", (3-correctCounter)) 
        if (correctCounter == 2 and randoRiddle789 == 7):
            Riddle_7 = input("\nIn one of his five senses he is lacking, he probably supports fracking: ")
            if Riddle_7.lower() == "voldemort":
                correctCounter += 1
                print("As you twist the last letter into place, the box clicks open. Riddles Correct: ", correctCounter)
            else: 
                print("The lock doesn't budge as you move the last letter. The engraving that holds the riddle starts to change in front of your eyes. Riddles left to go:", (3-correctCounter))

        if (correctCounter == 2 and randoRiddle789 == 8):
            Riddle_8 = input("\nA greedy boy who wants more gifts, in the air he saw his aunt lift: ")
            if Riddle_8.lower() == "dudley":
                correctCounter += 1
                print("As you twist the last letter into place, the box clicks open. Riddles Correct: ", correctCounter)
            else: 
                print("The lock doesn't budge as you move the last letter. The engraving that holds the riddle starts to change in front of your eyes. Riddles left to go:", (3-correctCounter))

        if (correctCounter == 2 and randoRiddle789 == 9):
            Riddle_9 = input("\nA spell to light your way, you could have used it on your stay: ")
            if Riddle_9.lower() == "lumos":
                correctCounter += 1
                print("As you twist the last letter into place, the box clicks open. Riddles Correct: ", correctCounter)
            else: 
                print("The lock doesn't budge as you move the last letter. The engraving that holds the riddle starts to change in front of your eyes. Riddles left to go:", (3-correctCounter)) 
        

def main():
    print("\nYou enter the first room. Your eyes adjust to the darkness and focus on a table holding three boxes and a note. You pick up the note, reading: \n\"Here you will answer three riddles to open the boxes' wordlock combinations and collect your first key. Good luck...\"")
    riddles()
    print("The last box clicks open, and inside lies a",end='')
    prGreen("small green key.")
    print("You grab it and head on to the next room. ")
             
if __name__ == "__main__":
    main()