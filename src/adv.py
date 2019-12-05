import random
from room import Room
from player import Player
from item import Item

# Declare all the rooms

item = {
    'knife': Item('knife', 'old and rusty'),
    'key': Item('key', 'a shiny silver key'),
    'shield': Item('shield', 'a copper shield with a burnished patina'),
    'gold bar': Item('gold bar', 'this looks heavy'),
    'ruby': Item('ruby', "one of the biggest ruby's you've seen'"),
    'cloak': Item('cloak', "this tattered cloak was blue at one point, now it's a weathered grey"),
    'crown': Item('crown', 'simple gold crown with a modest saphire embedded in the front'),
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item['gold bar'], item['crown'], item['cloak']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Bob', room['outside'])
# print(player)
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
def player_inputs(cmd_input):
    if cmd_input[0] == 'n' or cmd_input[0] == 'e' or cmd_input[0] == 'w' or cmd_input[0] == 's':
           player.set_room(cmd_input[0])
    elif cmd_input[0] == 'l':
        player.current_room.print_loot()
    elif cmd_input[0] == 'h':
        print("\nCommands: (n)orth, (e)ast, (s)outh, (w)est, (get) 'all' or choose an item listed, (d)rop, (h)elp, (q)uit")
    elif cmd_input[0] == 'get':
        try:
            player.set_inventory(cmd_input[1])
            player.current_room.remove_loot(cmd_input[1])
        except:
            print("\nplease type 'get' plus an item name, or choose 'get all'\n")
    elif cmd_input[0] == 'drop':
        try:
            player.drop_item(cmd_input[1])
        except:
            print("\nplease type 'drop' plus an item name, or choose 'drop all'\n")
    elif cmd_input[0] == 'i':
        player.print_inventory()
    elif cmd_input[0] == 'q':
        print('Goodbye!')
        exit()
    else:
        print("\nPlease enter a valid command: (n)orth, (e)ast, (s)outh, (w)est, (get) 'all' or choose an item listed, (d)rop, (h)elp, (q)uit\n")

while True:
    print(player.print_current())
    cmd = input("-> ").split(' ')
    player_inputs(cmd)