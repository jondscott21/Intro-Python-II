# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = list()
    def __str__(self):
        return f'{self.name}, {self.current_room}'
    def print_current(self):
        return f'{self.current_room}'
    def get_current(self):
        return self.current_room
    def set_room(self, cmd):
        try:
            self.current_room = getattr(self.current_room, f'{cmd}_to')
        except:
            print("you can't go that direction")
    def get_inventory(self):
        print(self.inventory)
    def set_inventory(self, item):
        self.inventory.append(item)
    def drop_item(self, item):
        self.inventory.remove(item)
