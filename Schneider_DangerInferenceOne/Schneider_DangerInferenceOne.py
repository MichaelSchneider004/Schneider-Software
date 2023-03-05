import random
while True:
    print("Your nom de guerre:")
    playerName = str(input())
    playerProfessionsList = ["presbyter", "bishop", "weaver", "layman", "yeoman", "drayman", "ironmonger", "butler"]
    playerProfession = random.choice(playerProfessionsList)
    playerHitpoints = random.randint(3,4)
    playerStrength = random.randint(3,4)
    playerWealth = 0
    playerRiskedWealth = 0
    playerTeeth = 32
    print(playerName + " the " + playerProfession + " joins the fight with " + str(playerHitpoints) + " hitpoints and " + str(playerStrength) + " strength!")

    foeList = ["rebel","wizard","duke's guard","general scientist","liquid CO2 technician","agent of the C.W.M.B."]
    foeHitpoints = 0
    foeStrength = 0

    while playerHitpoints > 0 and playerTeeth > 0:
        obstacles = random.randint(0,5)
        foeName = random.choice(foeList)
        foeHitpoints = random.randint(1,6)
        foeStrength = random.randint(1,6)
        print("You have found a terrible foe in the treacherous " + foeName + "!")
        while playerHitpoints > 0 and foeHitpoints > 0:
            if obstacles == 0:
                print("You may escape this " + foeName + " unscathed.")
            print("(A)ttack | (R)etreat")
            command = input()
            if command == "A" or command == "a":
                print("You exchange blows with the enemy.")
                foeHitpoints = foeHitpoints-playerStrength
                playerRiskedWealth = playerRiskedWealth + 1
                playerHitpoints = playerHitpoints-foeStrength                
            elif command == "R" or command == "r":
                 if obstacles == 0:
                     playerWealth = playerWealth + playerRiskedWealth
                     playerRiskedWealth = 0
                     print("You make a daring escape to the ATM and wire your ill-gotten gains into a clandestine Swiss bank account, returning to the fray refreshed.")
                 else:
                     playerHitpoints = playerHitpoints - 1
                     print("You sustain a swift kick while fleeing the enemy.")
                 break
            else: print("Oh behave!")
        print("THE BATTLE IS ENDED.\n")
        playerTeeth = playerTeeth - 1
        print("Pocket: " + str(playerRiskedWealth))
        print("Retirement: " + str(playerWealth))
        if foeHitpoints <= 0 or obstacles == 0:
            playerHitpoints = playerHitpoints + playerStrength + 1
        print("HP: " + str(playerHitpoints))
        print("STR:" + str(playerStrength))
        print(str(foeName) + " STR: " + str(foeStrength))
        print("\n")
    if playerHitpoints <= 0:
            print("Our hero " + playerName + " the mighty " + str(playerProfession) + " fell in mortal combat against a fierce, red-handed " + foeName + ".\nTheir winning sword-arm netted them " + str(playerWealth) + " glittering promises.\n--\n\n")
    elif playerTeeth <= 0:
            print("Ok dude, I think you got 'em. You made some pretty sweet gravy, too. You rest easy on your laurels knowing you've earned " + str(playerWealth+playerRiskedWealth) + " specie.\n--\n\n")
