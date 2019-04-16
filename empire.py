from constants import Constant
import string
import random
import numpy as np

class Empire:
    def __init__(self, imperialist):
        self.imperialist = imperialist
        self.colonies = []
        self.cost = self.calculateCost()
        self.name = ''.join(random.choices(string.ascii_uppercase, k=2))

    def calculateCost(self):
        colony_count = 1
        if len(self.colonies) > 0: colony_count = len(self.colonies)
        return (self.imperialist.getCost() + (np.sum([colony.getCost() for colony in self.colonies]) * Constant.EMPIRE_COST_RATE)) / colony_count


    def deleteColony(self, index):
        del self.colonies[index]
        self.cost = self.calculateCost()

    def getCost(self):
        return self.cost

    def addColony(self, colony):
        self.colonies.insert(len(self.colonies), colony)
        self.cost = self.calculateCost()

    def getColonies(self):
        return self.colonies

    def getColoniesCount(self):
        return len(self.getColonies())


    def getColony(self, index):
        return self.colonies[index]

    def getImperialist(self):
        return self.imperialist
