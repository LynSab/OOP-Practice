from abstract_class import Entity

class Character(Entity):

  def __init__(self, name, hp, strength, defense, dexterity, speed):
    super().__init__(name)
    self.hp = hp
    self.strength = strength
    self.defence = defense
    self.dexterity = dexterity
    self.speed = speed

  def attack(self, target):
    damage = self.attack - target.defence
    target.hp -= damage
    return f'{self.name} attacks {target.name} and hits for {damage} damage'
  
  def __str__(self):
    return f'Name: {self.name} \nHP: {self.hp} \nStr: {self.strength} \nDef: {self.defence}'


class Rogue(Character):

  def __init__(self, name, hp, strength, defense, dexterity, speed):
    super().__init__(name, hp, strength, defense, dexterity, speed)
    self.dex_attack_bonus = 10
  
  def sneak_attack(self, target):
    if self.dexterity > target.dexterity:
      damage = (self.attack + self.dex_attack_bonus) - target.defence
      target.hp -= damage
      return f'{self.name} sneak attacks {target.name} and hits for {damage} damage'
    else:
      return 'sneak attack failed'

class Barbarian(Character):

  def __init__(self, name, hp, strength, defense, dexterity, speed):
    super().__init__(name, hp, strength, defense, dexterity, speed)
    self.str_attack_bonus = 10
  
  def attack(self, target):
    damage = (self.attack + self.str_attack_bonus) - target.defence
    target.hp -= damage
    return f'{self.name} attacks {target.name} and hits for {damage} damage'

class Wizard(Character):

  def __init__(self, name, hp, strength, defense, dexterity, speed):
    super().__init__(name, hp, strength, defense, dexterity, speed)
    self.mana = 100
    self.spells = {
      'Fireball': {'str':20, 'cost': 25},
      'Ice Knife': {'str':15, 'cost': 20},
      'Lightning Bolt': {'str':10, 'cost': 10}
    }
  
  def spell_attack(self, target, spell):
    damage = self.spells[spell]['str']
    self.mana -= self.spells[spell]['cost']
    target.hp -= damage
    return f'{self.name} attacks {target.name} with spell {spell} and hits for {damage} damage'