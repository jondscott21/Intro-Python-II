# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = list()
    def __str__(self):
        return f"\nYou are {self.name}. You're standing in {self.current_room}\n"

    def print_current(self):
        return f'{self.current_room}'

    def get_current(self):
        return self.current_room

    def set_room(self, cmd):
        try:
            self.current_room = getattr(self.current_room, f'{cmd}_to')
        except:
            print("\nyou can't go that direction\n")

    def print_inventory(self):
        returned_inv = list()
        for i in self.inventory:
            returned_inv.append(i.name)
        if len(returned_inv) == 0:
            print('\nInventory is empty\n')
        else:
            print(f"\nInventory: {returned_inv}\n")

    def get_inventory(self):
        return self.inventory

    def set_inventory(self, item):
        if(item == 'all'):
            print('\nYou take everything\n')
            self.inventory.extend(self.current_room.get_loot())
        else:
            success = False
            for el in self.current_room.get_loot():
                if el.name == item:
                    self.inventory.append(el)
                    success = True
            if success:
                print(f'\nYou take the {item}')
            else:
                print(f"\nNo item named '{item}'\n")
    
    def drop_item(self, item):
        if item == 'all':
            self.current_room.add_all_loot(self.get_inventory())
            self.inventory.clear()
        for el in self.inventory:
            if el.name == item:
                self.inventory.remove(el)
                self.current_room.set_loot(el)
