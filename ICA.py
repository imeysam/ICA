from country import Country
from helpers import *
from constants import Constant
from empire import Empire
import numpy as np


class Ica:
    def __init__(self):
        self.countries = []
        self.empires = []
        self.colonies = []

    def createCountries(self, **args):
        count = args['count']
        for i in range(count):
            dimensions = generator(Constant.REPRESENTATION[0], Constant.REPRESENTATION[1])
            self.countries.append(Country(dimensions))

        return self.countries

    def createEmpires(self, **args):
        countries = args['countries']

        costs = []
        for i in range(len(countries)):
            costs.append(countries[i].getCost())
        costs = np.array(costs)

        sorted_indicates = np.argsort(costs)

        new_countries = []
        for i in sorted_indicates:
            new_countries.append(self.countries[i])
        new_countries = np.array(new_countries)

        self.countries = new_countries
        empires = self.countries[: Constant.IMPERIALIST_COUNT]
        self.colonies = self.countries[Constant.IMPERIALIST_COUNT:]

        for i in empires:
            self.empires.append(Empire(i))

        empires_costs = np.array([np.sum(empire.getCost()) for empire in self.empires])

        P = np.absolute(np.divide(empires_costs, np.sum(empires_costs)))

        for colony in self.colonies:
            k = randomSelection(P)
            self.empires[k].addColony(colony)

        return self.empires



    def absorb(self):
        for empire in self.empires:
            for colony in empire.getColonies():
                colony_vector = colony.getRepresentation()
                X = (np.random.uniform(0, colony_vector * Constant.BETTA)).astype(int)
                colony.setRepresentation(colony_vector + X)

                imperialist = empire.getImperialist()
                if colony.getCost() < imperialist.getCost():
                    temp = imperialist.getRepresentation()
                    imperialist.setRepresentation(colony.getRepresentation())
                    colony.setRepresentation(temp)




    def competition(self):

        if len(self.empires) == 1:
            return self.empires[0]

        TotalCost = np.array([empire.getCost() for empire in self.empires])

        weakest_empire_index = np.argmax(TotalCost)
        weakest_empire = self.empires[weakest_empire_index]

        P = np.divide(TotalCost, TotalCost.sum())
        P = np.flip(P, 0)

        if weakest_empire.getColoniesCount() > 0:

            weakest_empire_colonies_cost = np.array([colony.getCost() for colony in weakest_empire.getColonies()])

            weakest_colony_index = np.argmax(weakest_empire_colonies_cost)
            weakest_colony = weakest_empire.getColony(weakest_colony_index)

            winning_empire_index = randomSelection(P)
            winning_empire = self.empires[winning_empire_index]

            winning_empire.addColony(weakest_colony)

            weakest_empire.deleteColony(weakest_colony_index)


        if weakest_empire.getColoniesCount() == 0:

            winning_empire_index = randomSelection(P)

            winning_empire = self.empires[winning_empire_index]

            winning_empire.addColony(weakest_empire.getImperialist())

            del self.empires[self.empires.index(weakest_empire)]

        self.competition()




