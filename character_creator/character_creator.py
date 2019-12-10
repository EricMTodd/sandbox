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
    archetype = archetype[0].upper() + archetype[1:].lower()

    if archetype not in archetypes_list:
        assign_archetype()
    else:
        print(archetype)


def assign_name():
    global name
    name = input("Please enter the name of your new character: ")


def assign_race():
    global race
    for i in races_list:
        print(i)
    race = input("Please choose a race: ")
    race = race[0].upper() + race[1:].lower()

    if race not in races_list:
        assign_race()
    else:
        print(race)


# assign_race()
# assign_archetype()
# assign_name()


# print(name, race, archetype)

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
print(ability_scores_rolls)


def assign_ability_scores():
    strength = input(
        "Please assign your strength from your ability scores rolls: ")
    print(strength)
    if strength not in ability_scores_rolls:
        assign_ability_scores()
    else:
        for i in ability_scores_rolls:
            if i == strength:
                ability_scores["strength"] = strength
                del ability_scores_rolls[i]
    print(ability_scores_rolls)

    for key, value in ability_scores.items():
        print(key, value)


assign_ability_scores()
