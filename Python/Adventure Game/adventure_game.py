import time
import random


monster_list = ["Moderately Irate Sloth",
                "Slightly Inebriated Moose",
                "Cybernetic Techno-Terror",
                "Cranky Old Lady"]

key_list = ["Gold Key",
            "Hairpin",
            "Skeletal Finger",
            "Lockpick"]

weapon_list = ["Big Frikkin' Gun",
               "Really, REALLY Big Axe",
               "Holy Hand Grenade",
               "Giant Foam Finger"]

armor_list = ["Cool Leather Jacket",
              "Big Bird Costume",
              "Feather Boa of Protection",
              "Jaunty Ten-Gallon Hat"]


class GameItems:
    def __init__(self):
        self.monster = random.choice(monster_list)
        self.key = random.choice(key_list)
        self.weapon = random.choice(weapon_list)
        self.armor = random.choice(armor_list)


class Player:
    def __init__(self, player_name):
        self.name = player_name
        self.has_key = False
        self.has_weapon = False
        self.has_armor = False

    def give_key(self):
        self.has_key = True

    def give_weapon(self):
        self.has_weapon = True

    def give_armor(self):
        self.has_armor = True


def play_game(player_name):
    while True:
        player = Player(player_name)
        items = GameItems()

        intro(player)
        central_chamber(player, items)

        print_slow("Play again?")

        play_again = ["Yes", "No"]

        choice = get_choice(play_again)

        if choice == "No":
            break


def intro(player):
    print_slow(f"Welcome, {player.name}, to the proving grounds!")
    print_slow("You must escape by any means possible.")
    print_slow("Find the items necessary to complete the challenges beyond...")
    print_slow("You begin your adventure in the central chamber!\n")


def central_chamber(player, items):
    doors = ["North", "East", "South", "West"]

    print_slow("There are four doors. Which do you choose?")

    choice = get_choice(doors)

    if choice == 'North':
        north_room(player, items)
    if choice == 'East':
        east_room(player, items)
    if choice == 'South':
        south_room(player, items)
    if choice == 'West':
        west_room(player, items)


def north_room(player, items):
    if player.has_key:
        print_slow("You take a step into the northern room...")
        print_slow(f"Before you stands a {items.monster}\n")
        print_slow("What do you do?")

        options = ["Fight like a boss!", "Run away like a coward!"]

        choice = get_choice(options)

        if choice == "Fight like a boss!":
            fight(player, items)
        else:
            print_slow("You run in terror!")
            print_slow("")
            return_to_center(player, items)
    else:
        no_key(player, items)


def east_room(player, items):
    if player.has_key:
        print_slow("You enter the Eastern room...\n")
        if player.has_armor:
            empty_room(player, items)
        else:
            print_slow("Before you stands the finest armor in all the land!")
            print_slow(f"You put on the {items.armor}!")
            print_slow("This will certainly help you in your battles ahead!")
            print_slow("")
            player.give_armor()
            return_to_center(player, items)
    else:
        no_key(player, items)


def south_room(player, items):
    print_slow("You enter the Southern room...\n")
    if player.has_weapon:
        empty_room(player, items)
    else:
        print_slow("You see a giant chest before you, "
                   "beckoning you to open it.")
        print_slow("You creep forward and lift the lid of the chest...")
        print_slow(f"Inside is the {items.weapon}!")
        print_slow("You quickly grab it and holster it at your side.")
        print_slow("")
        player.give_weapon()
        return_to_center(player, items)


def west_room(player, items):
    print_slow("You enter the Western room...\n")
    if player.has_key:
        empty_room(player, items)
    else:
        print_slow("The room is dark but you see something in the corner.")
        print_slow("As you inch closer, the image becomes clearer...")
        print_slow(f"You found the {items.key}!")
        print_slow("This should unlock any door in here.")
        print_slow("")
        player.give_key()
        return_to_center(player, items)


def no_key(player, items):
    print_slow(f"The door won't budge.")
    print_slow("You'll have to find a way to open it.")
    print_slow(f"Maybe a {items.key} will help?")
    print_slow("")
    return_to_center(player, items)


def empty_room(player, items):
    print_slow("Not a lot has changed since you were here last...")
    return_to_center(player, items)


def return_to_center(player, items):
    print_slow("You return to the central chamber.\n")
    central_chamber(player, items)


def fight(player, items):
    if player.has_weapon and player.has_armor:
        game_over([f"You engage in an epic battle with the {items.monster}!",
                   f"{items.monster} attacks you like a bat out of hell "
                   f"but your {items.armor} protects you from the blow.",
                   f"You attack with your {items.weapon} and deal a "
                   "killing blow!",
                   "You are successful in proving your mettle.",
                   "All the trappings of wealth and fame await!"])
    elif player.has_armor:
        game_over([f"You attempt to fight the {items.monster} with your bare "
                   "fists (how brave!).",
                   "The pugilistic battle wages on for "
                   "hours until finally you're overcome with exhaustion.",
                   f"Should have gotten a {items.weapon} first...!",
                   f"The {items.monster} lets out a haunting laugh just "
                   "before you pass out."])
    elif player.has_weapon:
        game_over([f"You valiantly charge at the {items.monster} screaming "
                   "with bravado!",
                   f"Before you can even use your {items.weapon}, the "
                   f"{items.monster} swipes at you, mortally injuring you.",
                   f"The {items.monster} scoffs at you. Maybe instead of being"
                   f" naked you should have found a {items.armor}."])
    else:
        game_over([f"You attack the monster with the only thing you have:",
                   "... your total insanity...\n",
                   f"The {items.monster} tilts its head to the side in "
                   "confusion for a brief second before opening its mouth "
                   "and eating you whole.",
                   f"Hey {player.name}, next time try finding a weapon like "
                   f"a {items.weapon} and maybe clothe yourself in "
                   f"a {items.armor} instead.",
                   "There's a fine line between between being courageous "
                   "and stupid but I think we know which one you are."])


def game_over(end_msg):
    for line in end_msg:
        print_slow(line)
    print_fast("\n\nGAME OVER\n\n")


def get_choice(options):
    # display options
    index = 1
    for item in options:
        print_fast(f"{index}. {item}")
        index += 1

    # get selection, loop until valid input, return input
    while True:
        choice = str(input("Make your choice:\n")).lower()

        if choice.isdigit():        # if int entered, return value at index - 1
            if 0 < int(choice) <= len(options):
                print()
                return options[int(choice) - 1]
        else:                              # else return option chosen if found
            for option in options:
                if choice in option.lower() or option.lower() in choice:
                    print()
                    return option

        # if good input not received, alert user and loop again for input
        print("That was not a valid option")


def print_fast(prompt):
    print(prompt)
    time.sleep(0.25)


def print_slow(prompt):
    print(prompt)
    time.sleep(2)


if __name__ == "__main__":
    print_slow("Welcome to the Best Adventure Game of Your Life!")
    name = input("Before we get started, what is your name, hero?\n")
    print()
    play_game(name)
