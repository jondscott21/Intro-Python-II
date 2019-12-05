# Implement a class to hold room information. This should have name and
# description attributes
class Room:
    def __init__(self, name, description, loot):
        self.name = name
        self.description = description
        self.loot = list(loot)

    def __str__(self):
        return f'\n{self.name}:\n{self.description}. {self.print_loot()}\n'

    # formatting for printing loot in a room
    def print_loot(self):
        if len(self.loot) == 0:
            return ''
        returned = 'You see'
        if len(self.loot) == 1:
            return f'{returned} a {self.loot[0].name}'
        elif len(self.loot) > 1:
            for i in range(len(self.loot)):
                if i == (len(self.loot) - 1):
                    returned = f"{returned} and a {self.loot[i].name} "
                else:
                    returned = f"{returned} a {self.loot[i].name},"
            return returned

    def get_loot(self):
        return self.loot

    def set_loot(self, item):
        self.loot.append(item)
        
    def add_all_loot(self, items):
        self.loot.extend(items)

    def remove_loot(self, item):
        if item == 'all':
            self.loot.clear()
        else:
            try:
                for key in self.loot:
                    if key.name == item:
                        self.loot.remove(key)
            except:
                print(f"\nNo item named '{item}'\n")