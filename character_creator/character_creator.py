from random import randint

archetypes_list = ["Wizard", "Ranger", "Rogue", "Fighter", "Cleric"]
races_list = ["Human", "Dwarf", "Half-Orc", "Eladrin", "Dragonborn"]
ability_scores_rolls = []

archetype = ""
name = ""
race = ""
ability_scores = {
    "strength": 0,
    "dexterity": 0,
    "intelligence": 0,
    "constitution": 0,
    "wisdom": 0,
    "charisma": 0
}


def assign_archetype():
    global archetype
    for i in archetypes_list:
        print(i)
    archetype = input("Please choose an archetype: ")
    print()
    archetype = archetype[0].upper() + archetype[1:].lower()

    if archetype not in archetypes_list:
        assign_archetype()


def assign_name():
    global name
    name = input("Please enter the name of your new character: ")
    print()


def assign_race():
    global race
    for i in races_list:
        print(i)
    race = input("Please choose a race: ")
    print()
    race = race[0].upper() + race[1:].lower()

    if race not in races_list:
        assign_race()


assign_race()
assign_archetype()
assign_name()


def ability_score_generator():
    global ability_scores_rolls
    dice = 0
    ability_rolls = []
    while dice < 4:
        roll = randint(1, 6)
        ability_rolls.append(roll)
        dice += 1

    ability_rolls.remove(min(ability_rolls))
    ability_scores_rolls.append(sum(ability_rolls))


[ability_score_generator() for _ in range(6)]
for i in ability_scores:
    print(i)
print(f"Your ability score rolls: {ability_scores_rolls}")


def assign_ability_scores():
    while len(ability_scores_rolls) > 0:
        i = ability_scores_rolls[0]
        attribute = input(f"Which attribute would you like to apply {i} to? ")
        attribute = attribute.lower()
        if attribute not in ability_scores or ability_scores[attribute] != 0:
            print("try again")
            print()
            print(ability_scores)
            assign_ability_scores()
        else:
            ability_scores[attribute] = i
            print(ability_scores)
            print()
            del ability_scores_rolls[0]
            print(
                f"Your remaining ability score rolls: {ability_scores_rolls}")


assign_ability_scores()
print()
print(f"{name} is a {race} {archetype}")
print()
print(f"{name}'s ability scores: ")
for i in ability_scores:
    print(f"{i}: {ability_scores[i]}")
