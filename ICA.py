from country import Country
from country_types import CountryType
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
