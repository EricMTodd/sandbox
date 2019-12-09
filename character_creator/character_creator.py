archetypes_list = ["Wizard", "Ranger", "Rogue", "Fighter", "Cleric"]


def assign_archetype():
    for i in archetypes_list:
        print(i)
    archetype = input("Please choose an archetype: ")
    archetype = archetype[0].upper() + archetype[1:].lower()

    if archetype not in archetypes_list:
        assign_archetype()
    else:
        print(archetype)


assign_archetype()
