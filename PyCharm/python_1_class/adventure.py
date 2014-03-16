import random
import sys

probl = [10, 3, 10, 5, 25]
nprobl = []
oao = 0
no = random.randint(1, 5)
places = ('airstrip', 'forest', 'cave', 'meadow')
transitions = {
    'airstrip': ('forest', 'city'),
    'forest': ('airstrip', 'cave'),
    'cave': ('forest', 'meadow'),
    'meadow': ('cave', 'desert'),
    'desert': ('meadow', 'jungle'),
    'jungle': ('city', 'desert'),
    'city': ('jungle', 'airstrip')
}
place = random.choice(places)

while True:
    if oao == 0:
        print('You are at the', place)
        destinations = transitions[place]
        print('From here you can go to the', ' or the '.join(destinations))
        newDest = input('Where would you like to go? ')
        if newDest == 'quit':
            break
        elif newDest in destinations:
            if random.randint(1, probl[0]) == 1:
                print('You were struck by lightning. Game Over.')
                sys.exit()
            place = newDest
            if place == "meadow":
                if random.randint(1, probl[1]) == 1:
                    print('You fell in a hole and you are stuck.')
                    print("There is a door, a big door, and a trapdoor.")
                    ent = input("Which entrance do you go through? ")
                    while True:
                        if ent == "door":
                            if random.randint(1, 4) == 1:
                                print("You find an amazing treasure. You Win!!!")
                                sys.exit()
                            else:
                                print("You get killed by a zombie. Game Over.")
                                sys.exit()
                        elif ent == "trapdoor":
                            print("You fall into a pool with sharks.")
                            dora = input("Do you stay and die or get out of the pool? ")
                            if dora == "stay" or "die" or "stay and die":
                                print("You got eaten by sharks. Game Over")
                            elif dora == "get out of the pool":
                                print("You go into a room.")
                                if random.randint(1, 5) == 1:
                                    print("You find an amazing treasure. You Win!!!")
                                    sys.exit()
                                else:
                                    print("You get murdered by thieves. Game Over.")
                                    sys.exit()
                        elif ent == "big door":
                            print("You step into a human cannon and get blasted out of there.")
                            print("You land in a abandoned pirate ship.")
                            if random.randint(1, 10):
                                print("You find an amazing treasure. You Win!!!")
                                sys.exit()
                            else:
                                print("You get eaten by sharks. Game Over.")
                                sys.exit()
                        else:
                            print("There isn't such of an entrance.")
                elif random.randint(1, 3) == 1:
                    if random.randint(1, 4) == 1:
                        print("You stepped on a beehive and got stung to death.")
                    else:
                        print('You discover an amazing treasure! You Win!!!')
                    sys.exit()
            elif place == "desert":
                if random.randint(1, probl[2]) == no:
                    print("You find an amazing treasure. You Win!!!")
                elif random.randint(1, probl[3]) == no:
                    print("You die of thirst. Game Over.")
                elif random.randint(1, probl[4]) == no:
                    print("You run into a cactus and die. Game Over.")
            elif place == "forest" or place == "jungle":
                if oao == 1:
                    continue
                else:
                    oao = 1
                    if random.randint(1, 4) == 1:
                        wmonm = input("Do you want to use magic? ")
                        if wmonm == "yes":
                            if random.randint(1, 5) == 1:
                                wonw = input("Magic has failed to work. Give the secret ingredient to make it work. ")
                                if wonw == "carrot":
                                    print("Magic obtained.")
                                    for i in probl:
                                        nprobl.append(i + 10)
                                else:
                                    print("Sorry, that's the wrong ingredient. No magic for you.")
                            else:
                                print("You have some magic")
                                for i in probl:
                                    nprobl.append(i + 10)

        else:
            print("You can't go there.")
    else:
        print('You are at the', place)
        destinations = transitions[place]
        print('From here you can go to the', ' or the '.join(destinations))
        newDest = input('Where would you like to go? ')
        if newDest == 'quit':
            break
        elif newDest in destinations:
            wtm = input("Do you want to use magic?")
            if wtm == "yes":
                if random.randint(1, nprobl[0]) == 1:
                    print('You were struck by lightning. Game Over.')
                    sys.exit()
            elif wtm == "no":
                if random.randint(1, probl[0]) == 1:
                    print('You were struck by lightning. Game Over.')
                    sys.exit()
            place = newDest
            if place == "meadow":
                wtm2 = input("Do you want to use magic?")
                if wtm2 == "yes":
                    if random.randint(1, nprobl[1]) == 1:
                        print('You fell in a hole and you are stuck.')
                        print("There is a door, a big door, and a trapdoor.")
                        ent = input("Which entrance do you go through? ")
                        while True:
                            if ent == "door":
                                if random.randint(1, 4) == 1:
                                    print("You find an amazing treasure. You Win!!!")
                                    sys.exit()
                                else:
                                    print("You get killed by a zombie. Game Over.")
                                    sys.exit()
                            elif ent == "trapdoor":
                                print("You fall into a pool with sharks.")
                                dora = input("Do you stay and die or get out of the pool? ")
                                if dora == "stay" or "die" or "stay and die":
                                    print("You got eaten by sharks. Game Over")
                                elif dora == "get out of the pool":
                                    print("You go into a room.")
                                    if random.randint(1, 5) == 1:
                                        print("You find an amazing treasure. You Win!!!")
                                        sys.exit()
                                    else:
                                        print("You get murdered by thieves. Game Over.")
                                        sys.exit()
                            elif ent == "big door":
                                print("You step into a human cannon and get blasted out of there.")
                                print("You land in a abandoned pirate ship.")
                                if random.randint(1, 10):
                                    print("You find an amazing treasure. You Win!!!")
                                    sys.exit()
                                else:
                                    print("You get eaten by sharks. Game Over.")
                                    sys.exit()
                            else:
                                print("There isn't such of an entrance.")
                elif wtm2 == "no":
                    if random.randint(1, probl[1]) == 1:
                        print('You fell in a hole and you are stuck.')
                        print("There is a door, a big door, and a trapdoor.")
                        ent = input("Which entrance do you go through? ")
                        while True:
                            if ent == "door":
                                if random.randint(1, 4) == 1:
                                    print("You find an amazing treasure. You Win!!!")
                                    sys.exit()
                                else:
                                    print("You get killed by a zombie. Game Over.")
                                    sys.exit()
                            elif ent == "trapdoor":
                                print("You fall into a pool with sharks.")
                                dora = input("Do you stay and die or get out of the pool? ")
                                if dora == "stay" or "die" or "stay and die":
                                    print("You got eaten by sharks. Game Over")
                                elif dora == "get out of the pool":
                                    print("You go into a room.")
                                    if random.randint(1, 5) == 1:
                                        print("You find an amazing treasure. You Win!!!")
                                        sys.exit()
                                    else:
                                        print("You get murdered by thieves. Game Over.")
                                        sys.exit()
                            elif ent == "big door":
                                print("You step into a human cannon and get blasted out of there.")
                                print("You land in a abandoned pirate ship.")
                                if random.randint(1, 10):
                                    print("You find an amazing treasure. You Win!!!")
                                    sys.exit()
                                else:
                                    print("You get eaten by sharks. Game Over.")
                                    sys.exit()
                            else:
                                print("There isn't such of an entrance.")
                elif random.randint(1, 3) == 1:
                    if random.randint(1, 4) == 1:
                        print("You stepped on a beehive and got stung to death.")
                    else:
                        print('You discover an amazing treasure! You Win!!!')
                    sys.exit()
            elif place == "desert":
                wtm3 = input("Do you want to use magic?")
                if wtm3 == "yes":
                    if random.randint(1, nprobl[2]) == no:
                        print("You find an amazing treasure. You Win!!!")
                    elif random.randint(1, nprobl[3]) == no:
                        print("You die of thirst. Game Over.")
                    elif random.randint(1, nprobl[4]) == no:
                        print("You run into a cactus and die. Game Over.")
                elif wtm3 == "no":
                    if random.randint(1, probl[2]) == no:
                        print("You find an amazing treasure. You Win!!!")
                    elif random.randint(1, probl[3]) == no:
                        print("You die of thirst. Game Over.")
                    elif random.randint(1, probl[4]) == no:
                        print("You run into a cactus and die. Game Over.")
        else:
            print("You can't go there.")