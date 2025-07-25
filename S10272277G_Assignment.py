from random import randint

player = {}
game_map = []
fog = []

MAP_WIDTH = 0
MAP_HEIGHT = 0

TURNS_PER_DAY = 20
WIN_GP = 500

minerals = ['copper', 'silver', 'gold']
mineral_names = {'C': 'copper', 'S': 'silver', 'G': 'gold'}
pickaxe_price = [50, 150]

prices = {}
prices['copper'] = (1, 3)
prices['silver'] = (5, 8)
prices['gold'] = (10, 18)

# This function loads a map structure (a nested list) from a file
# It also updates MAP_WIDTH and MAP_HEIGHT
def load_map(filename, map_struct):
    with open(filename, 'r') as map_file:
        for line in map_file:
            map_struct.append(list(line.strip()))
    
    global MAP_WIDTH
    global MAP_HEIGHT
    
    # TODO: Add your map loading code here
    
    MAP_WIDTH = len(map_struct[0])
    MAP_HEIGHT = len(map_struct)

    map_file.close()

# This function clears the fog of war at the 3x3 square around the player
def clear_fog(fog, player):
    for y in range(player['y'] - 1, player['y'] + 2):
        for x in range(player['x'] - 1, player['x'] + 2):
            if 0 <= x < MAP_WIDTH and 0 <= y < MAP_HEIGHT:
                fog[y][x] = False
    return

def initialize_game(game_map, fog, player):
    # initialize map
    load_map("level1.txt", game_map)

    game_map[0][0] = 'M'

    fog.clear() #clear old fog data 
    for something in range(MAP_HEIGHT):
        fog.append([True] * MAP_WIDTH)#makes everything foggy
    
    # TODO: initialize player
    #   You will probably add other entries into the player dictionary
    player['x'] = 0
    player['y'] = 0
    player['copper'] = 0
    player['silver'] = 0
    player['gold'] = 0
    player['GP'] = 0
    player['day'] = 1
    player['steps'] = 0
    player['turns'] = TURNS_PER_DAY

    clear_fog(fog, player)
    
# This function draws the entire map, covered by the fof
def draw_map(game_map, fog, player):
    
    print("+" + "-" * 26 + "+")
    
    for y in range(MAP_HEIGHT):
        row = "|"
        for x in range(MAP_WIDTH):
            if fog[y][x]:#hides the square if theres fog
                row += "?"
            else:
                if game_map[y][x] == "M":#miner position
                    row += "M"
                else:
                    row += f"{game_map[y][x]}" #shows map square if theres no fog
        row += "|"
        print(row)
    print("+" + "-" * 26 + "+")

# This function draws the 3x3 viewport
def draw_view(game_map, fog, player):
    start_x = max(0, player['x'] - 1)
    end_x = min(MAP_WIDTH, player['x'] + 2)
    start_y = max(0, player['y'] - 1)
    end_y = min(MAP_HEIGHT, player['y'] + 2)

    print("+---+")

    for y in range(start_y, end_y + 1):
        row = "|"
        for x in range(start_x, end_x + 1):
            if not(0 <= x < MAP_WIDTH and 0 <= y < MAP_HEIGHT):
                row += "#"
            else:
                if player['x'] == x and player ['y'] == y:
                    row += "M"
                elif fog[y][x]:
                    row += "?"
                else:
                    row += f"{game_map[y][x]}"
                  
        row += "|"
        print(row)
    print("+---+")
    

# This function shows the information for the player
def show_information(player):
    print("----- Player Information -----")
    print(f"Name: {player['Name']}")
    print(f"Portal Position: ({player['x']}, {player['y']})")
    print(f"Pickaxe Level: ")
    print("------------------------------")
    print(f"Load: {player['copper'] + player['silver'] + player['gold']}/{backpackload}")
    print("------------------------------")
    print(f"GP: {player["GP"]}")
    print(f"Steps Taken: {player['steps']}")
    print("------------------------------")


# This function saves the game
def save_game(game_map, fog, player):
    # save map
    # save fog
    # save player
    return
        
# This function loads the game
def load_game(game_map, fog, player):
    # load map
    # load fog
    # load player
    return

def show_main_menu():
    print()
    print("--- Main Menu ----")
    print("(N)ew game")
    print("(L)oad saved game")
#    print("(H)igh scores")
    print("(Q)uit")
    print("------------------")
    mainmenuchoice = input("Your choice? ").lower()
    return mainmenuchoice
    
def show_town_menu():
    print()
    print(f"Day {daynum}")
    print("----- Sundrop Town -----")
    print("(B)uy stuff")
    print("See Player (I)nformation")
    print("See Mine (M)ap")
    print("(E)nter mine")
    print("Sa(V)e game")
    print("(Q)uit to main menu")
    print("------------------------")
    playerchoice = input("Your choice? ").lower()
    return playerchoice
            
def player_info():
    print("----- Player Information -----")
    print(f"Name: {player['Name']}")
    print("Portal Position: ")
    print("Pickaxe Level: ")
    print("------------------------------")
    print("Load: ")
    print("------------------------------")
    print(f"GP: {gp}")
    print("Steps Taken: ")
    
def shop_menu():
    print("---------------- Shop Menu ----------------")
    print("(B)ackpack upgrade to carry 12 items for 20 GP")
    print('(L)eave Shop')
    print("-------------------------------------------")    
    print(f"GP: {gp}")
    print("-------------------------------------------")

#--------------------------- MAIN GAME ---------------------------
game_state = 'main'
print("---------------- Welcome to Sundrop Caves! ----------------")
print("You spent all your money to get the deed to a mine, a small")
print("  backpack, a simple pickaxe and a magical portal stone.")
print()
print("How quickly can you get the 1000 GP you need to retire")
print("  and live happily ever after?")
print("-----------------------------------------------------------")

# TO-DO: The game!

backpackload = 10
gp = 0
daynum = 1
steps = 0
portal = {}
portal['x'] = 0
portal['y'] = 0
load = 0
copperload = 0
silverload = 0
goldload = 0
copperprice = 0
silverprice = 0
goldprice = 0

initialize_game(game_map, fog, player)
mainmenuchoice = show_main_menu()

#NEW GAME

if mainmenuchoice == "q": 
        print("See you, Miner!")
elif mainmenuchoice == "l":
    print("Loading game...")

if mainmenuchoice == "n":
    while True:
        username = input("Greetings, miner! What is your name? ")
        player['Name'] = username
        print(f"Pleased to meet you, {username}. Welcome to Sundrop Town!")
        
        while True: 
            playerchoice = show_town_menu()
            if playerchoice.lower() == "i":
                show_information(player)
                continue

            if playerchoice.lower() == "b":
                shop_menu()
                choice = input("Your choice? ")
                if choice.lower() == "l":
                    continue
                elif choice.lower() == "b":
                    if gp - 20 < 0:
                        print("Insufficient GP.")
                    else:
                        gp -= 20
                        backpackload = 12
                        print("Congratulations! You can now carry 12 items!") #Patch, use .format to change "12"
                        continue
        
            if playerchoice.lower() == "m":
                draw_map(game_map, fog, player)
                continue

            if playerchoice.lower() == "q":
                show_main_menu()

            if playerchoice.lower() == "e":
                print("-----------------------------------------------------------")
                print("                           Day 1                           ")
                print("-----------------------------------------------------------")
                while True:
                    draw_view(game_map, fog, player)
                    print(f"Turns left: {TURNS_PER_DAY - steps}", end=("  "))
                    print(f"Load: {load}/12", end=("   "))
                    print(f"Steps: {steps}")
                    print("(WASD) to move.")
                    print("(M)ap, (I)nformation, (P)ortal, (Q)uit to main menu")
                    useraction = input("Action? ").lower()
                    print("-------------------------------------------------------")
                    if useraction == "q":
                        show_main_menu()
                    if useraction == "i":
                        show_information(player)
                    if useraction == "m":
                        draw_map(game_map, fog, player)
                    
                    #Mining
                    currentnode =  game_map[player['x']][player['y']]
                    if currentnode == 'C':
                        copperload = randint(1, 5)
                        player['copper'] += copperload
                        load += copperload
                    elif currentnode == 'S':
                        silverload = randint(1, 3)
                        player['silver'] += silverload
                        load += silverload
                    elif currentnode == "G":
                        goldload = randint(1, 2)
                        player['gold'] = goldload
                        load += goldload

                    if load == backpackload:
                        print("You cant carry anymore, so you cant go that way.")
                        print("You are exhuasted.")
                        portal['x'] = player['x']
                        portal['y'] = player['y']
                        player['x'] = 0
                        player['y'] = 0
                        daynum += 1
                        print("You place your portal stone here and zap back to town.")
                        copperprice = randint(1, 3)
                        silverprice = randint(5, 8)
                        goldprice = randint(10, 18)
                        total = (copperload * copperprice) + (silverload * silverprice) + (goldload * goldprice)
                        print(f"You sell {copperload} copper ore, {silverload} silver ore, and {goldload} gold ore for {total} GP.")
                        gp += total
                        print(f"You now have {gp} GP!")
                        copperload, silverload, goldload = 0

                    if steps == "20":
                        print("You have ran out of steps.")
                        break
                    elif useraction == 'w':
                        player['y'] += 1
                        steps += 1
                        player['steps'] = steps
                    elif useraction == "a":
                        player['x'] -= 1
                        steps += 1
                        player['steps'] = steps
                    elif useraction == "s":
                        player['y'] -= 1
                        steps += 1
                        player['steps'] = steps
                    elif useraction == "d":
                        player['x'] += 1
                        steps += 1
                        player['steps'] = steps

                    if useraction == 'p':
                        portal['x'] = player['x']
                        portal['y'] = player['y']
                        player['x'] = 0
                        player['y'] = 0
                        print("You place your portal stone here and zap back to town.")
                        copperprice = randint(1, 3)
                        silverprice = randint(5, 8)
                        goldprice = randint(10, 18)
                        daynum += 1
                        total = (copperload * copperprice) + (silverload * silverprice) + (goldload * goldprice)
                        print(f"You sell {copperload} copper ore, {silverload} silver ore, and {goldload} gold ore for {total} GP.")
                        gp += total
                        print(f"You now have {gp} GP!")
                        copperload, silverload, goldload = 0

                    if gp >= 500:
                        print("-----------------------------------------------------------")
                        print(f"Woo-Hoo! Well done, {player['name]']}, you have {gp} GP!")
                        print("You now have enough to retire and play video games every day.")
                        print(f"And it only took you {daynum} days and {steps} steps! You WIN!")
                        print("-----------------------------------------------------------")
                        break