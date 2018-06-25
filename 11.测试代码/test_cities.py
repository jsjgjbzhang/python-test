import unittest
from city_function import showCityAndCountry


class CityTest(unittest.TestCase):
    """docstring for ClassName"""

    def test_showCityAndCountry(self):
        returnInfo = showCityAndCountry("santiago", "chile")
        self.assertEqual(returnInfo, "Santiago, Chile")

    def test_city_country_population(self):
        returnInfo = showCityAndCountry("santiago", "chile", 999999)
        self.assertEqual(returnInfo, "Santiago, Chile - population 999999")


unittest.main()
