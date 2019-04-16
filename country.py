import numpy as np
from country_types import CountryType
from constants import Constant
import string
import random

class Country:
    def __init__(self, representation, type = CountryType.INIT):
        self.colonies = []
        self.type = type
        self.representation = representation
        self.cost = self.calculateCost()
        self.name = ''.join(random.choices(string.ascii_lowercase, k=3))

    def calculateCost(self):
        return np.sum(np.multiply(np.array(Constant.ETC).T, self.representation))

    @property
    def isColony(self):
        return self.type == CountryType.COLONY

    @property
    def isImperialist(self):
        return self.type == CountryType.IMPERIALIST

    def getCost(self):
        return self.cost

    def getRepresentation(self):
        return self.representation

    def setRepresentation(self, representation):
        self.representation = representation
        self.cost = self.calculateCost()



