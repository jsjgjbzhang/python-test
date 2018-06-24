class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name, self.cuisine_type)

    def open_restaurant(self):
        print("营业中")

    def set_number_served(self, value):
        self.number_served = value

    def increment_number_served(self, value):
        self.number_served += value
        return self.number_served