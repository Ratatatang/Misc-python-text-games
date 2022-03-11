
from math import *
from random import *

sponsorTypes = ['Normal', 'Frugal', 'Rich',]
temperments = ['Mad', 'Scared', 'Friendly']

""""
def Murder():
    randomNumber = randrange(10)
    if(randomNumber == 1):
    "{} kills {} with a {}"
    "{} gets the jump on {} and uses their {} to finish the job"
    "{} attempts to kill {}, but {} get the upper hand and kills {} with their {}"
    "{} kills {} with a trap they set"
    "{} hunts down {} as revenge for killing {}"
    """

class Tribute:
    
    def __init__(self, name, pers, rpClass, number, numberClass):
        self.Kills = []
        self.Name = name
        self.Number = number+1
        self.Personality = pers.capitalize()
        self.Class = numberClass
        self.DisplayClass = rpClass.capitalize()
        self.Items = []
        self.Aim = randrange(10)
        self.Perception = randrange(10)
        self.MaxHealth = randrange(50)+100
        self.Attack = randrange(10)
        self.CurrentHealth = self.MaxHealth
        self.Food = 100
        self.Water = 100
        self.Stamina = 100
        self.SponsorType = ''

    def statIncrease(self, statID, Increase):
        if(statID == 1):
            self.Aim += Increase
            
        if(statID == 2):
            self.Perception += Increase
            
        if(statID == 3):
            self.CurrentHealth += Increase
            
        if(statID == 4):
            self.Attack += Increase
            
        if(statID == 5):
            self.Food +=  Increase
            
        if(statID == 6):
            self.Water += Increase

        if(statID == 7):
            self.Stamina += Increase

        

        
        
