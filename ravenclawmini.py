def prBlue(skk): print("\u001b[34m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))

def main():
    print("You enter the second room and see a grid and instructions carved into a wall.")
    magic_square = []

    numbers = input("Input 9 muggle numbers with spaces in between. Each group of three starts a new row, and every row and column adds up to 15: ")
    for i in numbers:
        if i.isdigit():
            magic_square.append(int(i))
    print("Your hand cramps as you use the green key to carve your guess into the stone.")

    print(magic_square)

    print(str(magic_square[0]) + " " + str(magic_square[1]) + " " + str(magic_square[2]))    
    print(str(magic_square[3]) + " " + str(magic_square[4]) + " " + str(magic_square[5])) 
    print(str(magic_square[6]) + " " + str(magic_square[7]) + " " + str(magic_square[8])) 

    ismagicsquare = True

    #row sum
    if magic_square[0] + magic_square[1] + magic_square[2] != 15:
        ismagicsquare = False

    if magic_square[3] + magic_square[4] + magic_square[5] != 15:
        ismagicsquare = False

    if magic_square[6] + magic_square[7] + magic_square[8] != 15:
        ismagicsquare = False

    # column sum 
    if (magic_square[0] + magic_square[3] + magic_square[6]) != 15:
        ismagicsquare = False

    if (magic_square[1] + magic_square[4] + magic_square[7]) != 15:
        ismagicsquare = False
        
    if (magic_square[2] + magic_square[5] + magic_square[8]) != 15:
        ismagicsquare = False
    
        #diagonal sum 
    if (magic_square[0] + magic_square[4] + magic_square[8]) != 15:
        ismagicsquare = False
    if (magic_square[2] + magic_square[4] + magic_square[6]) != 15:
        ismagicsquare = False

    #print(ismagicsquare)
    if ismagicsquare == True:
         print("\nYour numbers glow and fade back into the wall, taking the old writing with it. A stone suddenly rumbles and", end='')
         prLightGray("drops out of the wall.")
         print("You peek into the hole it left and see a", end='')
         prBlue("dusty blue key.")
         print("Grabbing the key, you move through the door to the third room.")
         

    if ismagicsquare == False:
        print("Your numbers fade, but the grid stays in place. It seems you have not come up with the right solution.")
        main()
        
 

if __name__ == "__main__":
    main()