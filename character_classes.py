from abstract_class import Entity

class Character(Entity):

  def __init__(self, name, strength, defense, dexterity, speed):
    super().__init__(name)
    self.strength = strength
    self.defence = defense
    self.dexterity = dexterity
    self.speed = speed
    self.hp = 100

  def attack(self, target):
    damage = self.strength - target.defence
    if damage > 0:
      target.hp -= damage
    return f'{self.name} attacks {target.name} and hits for {damage} damage'
  
  def __str__(self):
    return f'Name: {self.name} \nHP: {self.hp} \nStr: {self.strength} \nDef: {self.defence} \nDex: {self.dexterity} \nSpeed: {self.speed}'


class Rogue(Character):

  def __init__(self, name, strength, defense, dexterity, speed):
    super().__init__(name, strength, defense, dexterity, speed)
    self.dex_attack_bonus = 10
  
  def sneak_attack(self, target):
    if self.dexterity > target.dexterity:
      damage = (self.strength + self.dex_attack_bonus) - target.defence
      if damage > 0:
        target.hp -= damage
      return f'{self.name} sneak attacks {target.name} and hits for {damage} damage'
    else:
      print('sneak attack failed')
      return self.attack(self, target)

class Barbarian(Character):

  def __init__(self, name, strength, defense, dexterity, speed):
    super().__init__(name, strength, defense, dexterity, speed)
    self.str_attack_bonus = 10
  
  def attack(self, target):
    damage = (self.strength + self.str_attack_bonus) - target.defence
    if damage > 0:
      target.hp -= damage
    return f'{self.name} attacks {target.name} and hits for {damage} damage'

class Wizard(Character):

  def __init__(self, name, strength, defense, dexterity, speed):
    super().__init__(name, strength, defense, dexterity, speed)
    self.mana = 100
    self.spells = {
      'Fireball': {'str':20, 'cost': 25},
      'Ice Knife': {'str':15, 'cost': 20},
      'Lightning Bolt': {'str':10, 'cost': 10}
    }
  
  def spell_attack(self, target, spell):
    if self.mana >self.spells[spell]['cost']:
      damage = self.spells[spell]['str']
      self.mana -= self.spells[spell]['cost']
      target.hp -= damage
      return f'{self.name} attacks {target.name} with spell {spell} and hits for {damage} damage'
    else:
      print('You do not have enough mana, you do a regular attack instead')
      return self.attack(target)

  def __str__(self):
    return super().__str__() + f'\nMana: {self.mana}'
  
class Ranger(Character):

  def __init__(self, name, strength, defense, dexterity, speed):
    super().__init__(name, strength, defense, dexterity, speed)
    self.arrows = 20
    self.ranged_atk_bonus = 10
  
  def ranged_attack(self, target):
    damage = (self.strength + self.ranged_atk_bonus) - target.defence
    if damage > 0:
      target.hp -= damage
    self.arrows -= 1
    return f'{self.name} ranged attacks {target.name} and hits for {damage} damage'
