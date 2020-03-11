import pprint

Item = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def countInventory(item):
    print('Inventory:')
    total = 0
    for i, j in item.items():
        total += j
        print(str(j),str(i))
    print('total: ' + str(total))


def addInvebtory(item, Inventory):
    for i in item:
        if i not in Inventory:
            Inventory.setdefault(i, 0)
        Inventory[i] += 1

print('before::')
countInventory(Item)

addInvebtory(dragonLoot, Item)

print('after::')
countInventory(Item)
