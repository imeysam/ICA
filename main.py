from constants import Constant
from ICA import Ica


if __name__ == "__main__":

    ica = Ica()

    countries = ica.createCountries(count = Constant.COUNTRY_COUNT)

    ica.createEmpires(countries = countries)

    ica.absorb()

    ica.competition()

    empire = ica.empires[0]

    print(empire.getColoniesCount())