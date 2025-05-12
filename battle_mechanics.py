from character_classes import Wizard, Barbarian, Ranger, Rogue

class Battles():
  
  def __init__(self):
    pass

  def battle(self, player_char, enemy):
    
    while player_char.hp > 0 and enemy.hp > 0:
      if isinstance(player_char, Wizard):
        type_of_attack = int(input('How would you like to attack? \n1. Spell attack \n2. Regular attack \nEnter the number of your chosen attack type: '))
        if type_of_attack == 1:
          print('Which spell would you like to choose?')
          spell_list = [spell for spell in player_char.spells.keys()]
          for i, spell in enumerate(spell_list):
            print(i+1, '. ', spell)
          spell_choice = int(input('Enter the number of your chosen spell: '))
          print(player_char.spell_attack(enemy,spell_list[spell_choice-1]))
        else:
          print(player_char.attack(enemy))
      
      elif isinstance(player_char, Barbarian):
        print(player_char.attack(enemy))
      
      elif isinstance(player_char, Ranger):
        type_of_attack = int(input('How would you like to attack? \n1. Ranged attack \n2. Regular attack \n Enter the number of your chosen attack type: '))
        if type_of_attack == 1:
          print(player_char.ranged_attack(enemy))
        else:
          print(player_char.attack(enemy))
      
      elif isinstance(player_char, Rogue):
        type_of_attack = int(input('How would you like to attack? \n1. Sneak attack \n2. Regular attack \n Enter the number of your chosen attack type: '))
        if type_of_attack == 1:
          print(player_char.sneak_attack(enemy))
        else:
          print(player_char.attack(enemy))
      
      print(enemy.attack(player_char))

      if player_char.hp > 0 and enemy.hp > 0:
        print(f'Your HP is {player_char.hp} \nYour Enemies HP is {enemy.hp}')

    if player_char.hp <= 0:
      print('You lose, better luck next time')
    elif enemy.hp <= 0:
      print(f'Well done you have defeated the {enemy.name}')
