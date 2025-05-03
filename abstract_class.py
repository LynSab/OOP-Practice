from abc import ABC, abstractmethod

class Entity(ABC):
  
  def __init__(self, name):
    self.name = name
  
  @abstractmethod
  def __str__(self):
    pass