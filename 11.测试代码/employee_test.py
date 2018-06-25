import unittest


class Employee():
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, value=5000):
        self.annual_salary += value
        return self.annual_salary


class EmployeeTest(unittest.TestCase):
    """docstring for EmployeeTest"""

    def setUp(self):
        self.employee = Employee("张", "忠鹏", 30000)

    def test_give_default_raise(self):
        tDefaultRaise = self.employee.give_raise()
        self.assertEqual(tDefaultRaise, 35000)

    def test_give_custom_raise(self):
        tCustomRaise = self.employee.give_raise(6000)
        self.assertEqual(tCustomRaise, 36000)


unittest.main()
