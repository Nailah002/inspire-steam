#Name: Nailah Wanjiku
#Date: 19/2/2026
#ASSIGNMENT


class FighterCharacter:

    def __init__ (self, role, health, damage, speed):
        self.character_role = role
        self.character_health = health
        self.character_damage = damage
        self.character_speed = speed
    
    def run(self, direction):
        print(f"Game log: {self.character_role} runs {direction} at speed {self.character_speed}")
    
    def report_status(self):
        print(f"\nCharacter Log: \n Role: {self.character_role} \n Health: {self.character_health} \n Damage: {self.character_damage} \n Speed: {self.character_speed}\n ___ \n")
    
    def kick(self, opponent):

        character_damage = self.character_damage
        opponent.character_health = opponent.character_health / character_damage
        print(f"Game Log: {self.character_role} deals a damage of {character_damage} to the {opponent.character_role}.")
    
    def takle(self, opponent):
        # implement this so that the opponent's charater_speed is reduced by the damager dealt by the fighter
        # For instance, if the ninja's speed is 120, a takle from the warrior should reduce their speed to 80
        # Remember to remove the pass below before running your trial
        pass
        


ninja_character = FighterCharacter("Ninja", health=100, damage=40, speed=120)
warrior_character = FighterCharacter("warrior", health=160, damage=80, speed=80)


ninja_character.report_status()
warrior_character.report_status()

ninja_character.run("Up")
ninja_character.kick(warrior_character)

ninja_character.report_status()
warrior_character.report_status()

Copy the assignment from the three quotes on the top to the end. 
See if you can spot the first logical error. 

Run the code again to see if the warrior's health is as expected.

The second challenge is to the adventurous. Use inspiration from the kick(self, opponent) function to implement a takle(Self, opponent) function. 

Add these lines to the end to see if the attempts at the takle function is well made:

warrior_character.takle(ninja_character)
ninja_character.report_status()
warrior_character.report_status()