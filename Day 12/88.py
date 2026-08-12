game_level = 10
enimies = ["Goblin", "Troll", "Dragon", "Orc", "Vampire"]

def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enimies[0]  
    print(f"A wild {new_enemy} appears!")