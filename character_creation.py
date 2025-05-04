from character_classes import Wizard, Barbarian, Ranger, Rogue
import random

class CharacterCreate():

  def __init__(self):
    pass

  def choose_class(self):
    print('What character class would you like to be? \n1. Barbarian \n2. Wizard \n3. Ranger \n4. Rogue')
    character_class = input('Insert the number of your chosen class: ')
    return int(character_class)
  
  def choose_name(self):
    character_name = input('\nWhat is your characters name?\n')
    return character_name
  
  def roll_for_stats(self):
    print(input('\nHit enter to roll your Stength stat'))
    str_roll = random.randint(40, 60)
    print(f'Your Strength is {str_roll}')

    print(input('\nHit enter to roll your Defense stat'))
    def_roll = random.randint(20, 40)
    print(f'Your Defence is {def_roll}')

    print(input('\nHit enter to roll your Dexterity stat'))
    dex_roll = random.randint(10, 20)    
    print(f'Your Dexterity is {dex_roll}')

    print(input('\nHit enter to roll your Speed stat'))
    speed_roll = random.randint(10, 20)
    print(f'Your Speed is {speed_roll}')
    print('\n')
    return {'strength': str_roll, 'defence': def_roll, 'dexterity': dex_roll, 'speed': speed_roll}
  
  def create_character(self):
    class_num = self.choose_class()
    char_name = self.choose_name()
    rolls = self.roll_for_stats()

    if class_num == 1:
      player_character = Barbarian(char_name, rolls['strength'], rolls['defence'], rolls['dexterity'], rolls['speed'])
    elif class_num == 2:
      player_character = Wizard(char_name, rolls['strength'], rolls['defence'], rolls['dexterity'], rolls['speed'])
    elif class_num == 3:
      player_character = Ranger(char_name, rolls['strength'], rolls['defence'], rolls['dexterity'], rolls['speed'])
    else:
      player_character = Rogue(char_name, rolls['strength'], rolls['defence'], rolls['dexterity'], rolls['speed'])
    
    return player_character
