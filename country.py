import numpy as np
from country_types import CountryType
from constants import Constant

class Country:
    def __init__(self, representation, type = CountryType.INIT):
        self.colonies = []
        self.type = type
        self.representation = representation
        self.cost = self.calculateCost()

    def calculateCost(self):
        return np.sum(np.multiply(np.array(Constant.ETC).T, self.representation))

    @property
    def is_colony(self):
        return self.type == CountryType.COLONY

    @property
    def isImperialist(self):
        return self.type == CountryType.IMPERIALIST

    def getCost(self):
        return self.cost

    # def getImperialist



