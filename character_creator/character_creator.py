class Character:
    def __init__(self, archetype, name, race):
        self.archetype = archetype
        self.name = name
        self.race = race


archetype = input("""Please choose an archetype: 
Wizard
Ranger
Rogue
Fighter
Cleric
""")
