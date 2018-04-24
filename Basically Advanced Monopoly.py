try:
    print("""
       ===================================
    Basically Advanced Monopoly: Euro Edition
       ===================================
    """)
    # --------------------------------------------------SETUP----------------------------------------------------------#

    from random import *

    # money1 = 1
    # money5 = 5
    # money10 = 10
    # money20 = 20
    # money50 = 50
    # money100 = 100
    # money500 = 500


    # -------------------------------------------------OBJECTS---------------------------------------------------------#

    class Player:  # Creating the class of 'Player'
        pos = 0  # An attribute storing the current position of the player
        playerName = ""  # An attribute storing the player's name
        playerPiece = ""  # An attribute storing the player's piece

        def __init__(self, name, piece):  # The constructor method which sets up the class
            self.playerName = name
            self.playerPiece = piece
            # self.eenPlayerMoney1Quant = 5
            # self.eenPlayerMoney5Quant = 1
            # self.eenPlayerMoney10Quant = 2
            # self.eenPlayerMoney20Quant = 1
            # self.eenPlayerMoney50Quant = 1
            # self.eenPlayerMoney100Quant = 4
            # self.eenPlayerMoney500Quant = 2
            self.totalCash = 1500

        def roll(self):  # A method which rolls the dice
            self.eindie = randint(1, 6)
            self.zweidie = randint(1, 6)
            self.posMove = self.eindie + self.zweidie
            self.pos += self.posMove

        def returnName(self):  # A method which returns the name of the player
            playerName = nameEntry
            return self.playerName


    class Tile:  # A parent class
        def __init__(self, name, pos):
            self.tileName = name
            self.tilePos = pos

        def returnName(self):
            return self.tileName


    class City:  # A child class
        def __init__(self, name, price, pos):
            self.tileName = name
            self.tilePrice = price
            self.tileOwner = ""
            self.tilePos = pos

        def returnName(self):
            return self.tileName


    # ----------------------------------------------TILE CREATION------------------------------------------------------#

    tile0 = Tile("Start", 0)
    tile1 = City("Sofia", 100, 1)
    tile2 = City("Brussels", 150, 2)
    tile3 = City("Vatican City", 150, 3)
    tile4 = City("Moscow", 150, 4)
    tile5 = City("Oslo", 200, 5)
    tile6 = City("Luxembourg", 200, 6)
    tile7 = Tile("Jail", 7)
    tile8 = City("Tallin", 250, 8)
    tile9 = City("Vilnius", 250, 9)
    tile10 = City("Dublin", 250, 10)
    tile11 = City("Copenhagen", 300, 11)
    tile12 = City("Riga", 300, 12)
    tile13 = Tile("Border Control", 13)  # Miss a Turn #Roll, if player rolls double 6, go to jail
    tile14 = City("Athens", 350, 14)
    tile15 = City("Stockholm", 350, 15)
    tile16 = City("Vienna", 350, 16)
    tile17 = City("Bucharest", 400, 17)
    tile18 = City("Warsaw", 400, 18)
    tile19 = City("Lisbon", 400, 19)
    tile20 = Tile("Go to Jail", 20)
    tile21 = City("Madrid", 450, 21)
    tile22 = City("Amsterdam", 450, 22)
    tile23 = City("Paris", 500, 23)
    tile24 = City("Berlin", 500, 24)
    tile25 = City("London", 500, 25)
    tileList = [tile0, tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8, tile9, tile10, tile11, tile12, tile13,
                tile14, tile15, tile16, tile17, tile18, tile19, tile20, tile21, tile22, tile23, tile24, tile25]

    # ---------------------------------------------PLAYER CREATION-----------------------------------------------------#

    nameEntry = input("What is Player One's Name? ")
    pieceEntry = input("What Character is " + nameEntry + "? ")
    eenPlayer = Player(nameEntry, pieceEntry)  # The instantiation of a player
    nameEntry2 = input("What is Player Two's Name? ")
    pieceEntry2 = input("What Character is " + nameEntry2 + "? ")
    tweePlayer = Player(nameEntry2, pieceEntry2)
    playerList = [eenPlayer, tweePlayer]

    # --------------------------------------------------GAME-----------------------------------------------------------#

    currentPlayerNo = 0
    miss = 0
    while True:
        # Pre-Round Checks
        currentPlayer = playerList[currentPlayerNo]
        print (currentPlayer.playerName+"'s Turn!")
        if miss == 0:
            if len(playerList) == 1:
                print(playerList[0].playerName, "has won!")
                break
            if currentPlayer.totalCash <= 0:
                playerList.remove(currentPlayer)

            # Player Turn
            currentPlayer.roll()
            if currentPlayer.pos > 25:
                currentPlayer.pos = currentPlayer.pos - 26
                print("You have passed Start, collect 200")
                currentPlayer.totalCash += 200
            print(currentPlayer.returnName(), "is on position", currentPlayer.pos)
            for i in tileList:
                if i.tilePos == currentPlayer.pos:
                    print("Position", currentPlayer.pos, "is", i.tileName)
                    if i.tileName == "Border Control":
                        miss = 1

                    elif i.tileOwner == eenPlayer.playerName or tweePlayer.playerName:
                        if i.tileOwner == "":
                            yayornay = input("Do you wish to buy this tile? ")
                            yayornay = yayornay.upper()
                            lmn = ("ON")
                            while lmn == "ON":
                                if yayornay == "YES":
                                    if currentPlayer.totalCash < i.tilePrice:
                                        print ("Unable to purchase, insufficient funds.")
                                    else:
                                        i.tileOwner = currentPlayer.playerName
                                        currentPlayer.totalCash = (currentPlayer.totalCash - i.tilePrice)
                                        lmn = ("OFF")
                                elif yayornay == "NO":
                                    print("Ok, moving on...")
                                    lmn = ("OFF")
                                else:
                                    print("Please State Yes or No")
                        elif i.tileOwner == currentPlayer.playerName:
                            pass

                        else:
                            currentPlayer.totalCash = (currentPlayer.totalCash-(i.tilePrice/2))
                            i.tileOwner.totalCash = (i.tileOwner.totalCash + (i.tilePrice/2))


                    else:
                        print ("Nothing to do here...")


        elif miss == 1:
            print(currentPlayer.playerName + "'s turn has been passed.")
            miss = 0

        # Turn Over
        print ("NEEEEEEEEEEEXXT TURN!")
        print("\n")
        if currentPlayerNo == 0:
            currentPlayerNo += 1
        else:
            currentPlayerNo = 1

except:
    print ("Oh poops, there's been an error :(")