from character_classes import Character
import random

class EnemyCreate():

  def __init__(self):
    self.enemy_type = ['Orc', 'Dragon', 'Troll', 'Bandit', 'Wolf', 'Bear']

  def roll_enemy_stats(self):
    print(input('\nHit enter to roll your enemies Stength stat'))
    str_roll = random.randint(40, 60)
    print(f'Your enemies Strength is {str_roll}')

    print(input('\nHit enter to roll your enemies Defense stat'))
    def_roll = random.randint(20, 40)
    print(f'Your enemies Defence is {def_roll}')

    print(input('\nHit enter to roll your enemies Dexterity stat'))
    dex_roll = random.randint(10, 20)    
    print(f'Your enemies Dexterity is {dex_roll}')

    print(input('\nHit enter to roll your enemies Speed stat'))
    speed_roll = random.randint(10, 20)
    print(f'Your enemies Speed is {speed_roll}')
    print('\n')
    return {'strength': str_roll, 'defence': def_roll, 'dexterity': dex_roll, 'speed': speed_roll}

  def create_enemy(self):
    enemy_type = random.choice(self.enemy_type)
    rolls = self.roll_enemy_stats()
    enemy = Character(enemy_type, rolls['strength'], rolls['defence'], rolls['dexterity'], rolls['speed'])
    return enemy
