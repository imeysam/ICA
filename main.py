from constants import Constant
from ICA import Ica


if __name__ == "__main__":
    ica = Ica()

    countries = ica.createCountries(count = Constant.COUNTRY_COUNT)

    empires = ica.createEmpires(countries=countries)

    ica.absorb()



    # for empire in empires:
    #     print(empire.getNumberOfColonies())
