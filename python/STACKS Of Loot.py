import random
class LootStack:
    def __init__(self):
        self.loot = []
        self.kindsOfLoot = {
            "PENUTS":"Food",
            "Banana":"Food",
            "Among us banana":"Anomaly",
            "Milk":"Food",
            "Sword":"Weapon",
            "A pencil":"Weapon",
            "floating point error":"Anomaly",
            "A Python":"Creature",
            "Potion Of Thickness":"Consumable",
            "Cai":"Anomaly",
            "Nyan cat":"Anomaly",
            "Poptart":"Food",
            "A comma":"Creature",
            "You":"Creature",
            "The Amazing World Of Gumball Vol 17":"Weapon",
            "Mia's Ultimate Origami":"Weapon",
            "Blackmail":"Weapon",
            "worldLoot":"Anomaly",
            "This assignment":"Consumable",
            "Wheatley":"Creature",
            "A coding error":"Anomaly",
            "A Minceraft splash text":"Anomaly",
            "!!!":"Anomaly",
            "The Big One":"Weapon",
            "Dr. Coomer":"Creature",
            "Super Mik":"Consumable",
            "Your hand":"Weapon",
            "The Pharaoh's Curse":"Anomaly",
            "Luna":"Creature",
            "An Iterator":"Creature",
            "Sandy Hair":"Anomaly",
            "Mario's full lore":"Anomaly",
            "A Rabbit":"Creature",
            "A ribbit":"Creature",
            "A donk":"Anomaly",
            "nothing!":"Anomaly"
        }
    def is_empty(self):
        return len(self.loot) == 0
    
    def is_full(self):
        return len(self.loot) >= 10
    
    def push_loot(self, item):
        print(f"Acquired {item}!")
        self.loot.append(item)

    def push_loot_random(self):
        worldLoot = ("PENUTS","Banana","Among us banana","Milk","Sword","A pencil","floating point error","A Python","Potion Of Thickness","Cai","Nyan cat","Poptart","A comma!","You","The Amazing World Of Gumball Vol 17","Mia's Ultimate Origami","Blackmail","worldLoot","This assignment","Wheatley","A coding error","A Minceraft splash text","!!!","The Big One","Dr. Coomer","Super Mik","Your hand","The Pharaoh's Curse","Luna","An Iterator","Sandy Hair","Mario's full lore","A Rabbit","A ribbit","A donk","nothing!")
        item = random.choice(worldLoot)
        print(f"Acquired {item}!")
        self.loot.append(item)

    def pop_loot(self):
        if not self.is_empty():
            removed_item = self.loot.pop()
            print(f"Threw away {removed_item}.")
            return removed_item
        else:
            print("Your loot bag is empty.")
    def use_loot(self):
        if not self.is_empty():
            removed_item = self.loot.pop()
            print(f"Used {removed_item}.")
            result = "nothing happened."
            anomalyResults = ("the item explodes!","you got obsessed with it and absorbed it into your being.","you ignored it and played video games.","it begins glowing and phases into the next dimension.","it flies away from you.","it stops existing.","it gives you a pizza.","it takes your soul.","not me.")
            foodResults = ("it tastes good.","it tastes great!","it tastes not to terrible.","you wish you had another.","you throw up.")
            weaponResults = ("it breaks.","it deals damage to... nothing.","you prepping your weapon.")
            creatureResults = ("it looks at you.","it crawls all over you.","it leaves you.","it purrs.","it looks hungry.","it looks full.","it goes on your head.")
            consumeResults = ("all your stats have been boosted.","you fumble the item and break it.","your senses have gone radical.","you melt into a new form.")
            kind = self.kindsOfLoot[removed_item]
            if kind == "Anomaly":
                result = random.choice(anomalyResults)
            elif kind == "Food":
                result = random.choice(foodResults)
            elif kind == "Weapon":
                result = random.choice(weaponResults)
            elif kind == "Creature":
                result = random.choice(creatureResults)
            elif kind == "Consumable":
                result = random.choice(consumeResults)
            print("The Result is", result)
            return result
        else:
            print("Your loot bag is empty!")
    def peek_loot(self):
        if not self.is_empty():
            return self.loot[-1]
        else:
            print("Your loot bag is empty!")

class QuestStack:
    def __init__(self):
        self.quests = []
    def is_empty(self):
        return len(self.quests) == 0
    def is_big(self):
        return len(self.quests) >= 10
    def push_quest(self, item):
        print(f"Recieved quest {item}!")
        self.quests.append(item)
    
    def push_quest_random(self):
            preset_quests = ("Recieve Spamton's CD","Retrieve the Nyan Cat","Fight nothing","Get 10000 copper coins","Do work","Drink enough milk","Get rubber ducks","Learn German","Finish this code for me","Activate the ancient psychic tandem war elephant","Make a wish","Don't give up","Have a good day","Avoid spam emails","Play Minecraft")
            item = random.choice(preset_quests)
            print(f"Recieved quest {item}!")
            self.quests.append(item)

    def pop_quest(self):
        if not self.is_empty():
            removed_item = self.quests.pop()
            print(f"Completed quest {removed_item}.")
            return removed_item
        else:
            print("Your quest book is empty!")
    
    def peek_quest(self):
        if not self.is_empty():
            return self.quests[-1]
        else:
            print("Your quest book is empty!")
# Initialize LootStack object
player_loot = LootStack()
player_quest_basket = QuestStack()
# Simple game loop for interaction
while True:
    print("\n=== Loot Bag And Quest Menu ===\n1: Acquire random loot\n2: Throw away loot\n3: Check top loot item\n4: Use Loot\n5: Acquire random quest\n6: Write down quest\n7: Check top quest in book\n8: Declare top quest complete\n9: Exit")
    choice = input("What would you like to do? ")

    if choice == '1':
        if player_loot.is_full():
            print("Your loot bag is full and cannot contain any more loot")
        else:
            player_loot.push_loot_random()
    elif choice == '2':
        player_loot.pop_loot()
    elif choice == '3':
        top_loot = player_loot.peek_loot()
        if top_loot:
            print(f"The top loot item is: {top_loot}")
    elif choice == '4':
        player_loot.use_loot()
    elif choice == '5':
        if player_quest_basket.is_big():
            print("Your quest book contains 10 or more quests, you should consider completing some of them.")
        player_quest_basket.push_quest_random()
    elif choice == '6':
        if player_quest_basket.is_big():
            print("Your quest book contains 10 or more quests, you should consider completing some of them.")
        new_quest = input("Enter the name of the quest you acquired: ")
        player_quest_basket.push_quest(new_quest)
    elif choice == '7':
        top_quest = player_quest_basket.peek_quest()
        if top_quest:
            print(f"The top loot item is: {top_quest}")
    elif choice == '8':
        player_quest_basket.pop_quest()
    elif choice == '9':
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")