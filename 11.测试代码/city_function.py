def showCityAndCountry(city, country, population=0):
    cityAndCountry = city.title() + ", " + country.title()
    if population:
        cityAndCountry = cityAndCountry + " - population " + str(population)
    return cityAndCountry
