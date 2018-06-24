# from restaurant import Restaurant
# from user import User
# from privileges import Privileges,Admin
from collections import OrderedDict
from die import Die
userDic = OrderedDict()
userDic["name"] = "zzp"
userDic["age"] = 28

for k,v in userDic.items():
	print(k,v)

die6 = Die(6)
die6.roll_die(10)

die6 = Die(10)
die6.roll_die(10)

die6 = Die(20)
die6.roll_die(10)

# class IceCreamStand(Restaurant):
#     """docstring for IceCreamStand"""

#     def __init__(self, restaurant_name, cuisine_type):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = ["草莓", "香草", "巧克力"]

#     def show_Flavors(self):
#         for x in self.flavors:
#             print(x)


# ics = IceCreamStand("DQ", "冰淇淋")
# ics.show_Flavors()

# restaurant = Restaurant("KFC", "快餐")
# print(restaurant.number_served)
# restaurant.number_served = 10
# print(restaurant.number_served)

# restaurant.set_number_served(20)
# print(restaurant.number_served)


# myRestaurant = Restaurant("柚子", "日料")
# print(myRestaurant.restaurant_name, myRestaurant.cuisine_type)
# myRestaurant.describe_restaurant()
# myRestaurant.open_restaurant()

# xiangtianxia = Restaurant("四川香天下火锅", "火锅")
# wangpin = Restaurant("王品牛排", "牛排")
# meishan = Restaurant("梅山铁板烧", "铁板烧")

# xiangtianxia.describe_restaurant()
# wangpin.describe_restaurant()
# meishan.describe_restaurant()



# azzp = Admin("张", "忠鹏", 性别="男")
# azzp.privileges.showPrivileges()
# azzp.privileges.addPrivileges("Judgment")
# azzp.privileges.showPrivileges()


# zzp = User("张", "忠鹏", 性别="男", 籍贯="山东", 年龄=28)
# zzp.increment_login_attempts()
# zzp.increment_login_attempts()
# zzp.increment_login_attempts()
# zzp.increment_login_attempts()
# zzp.increment_login_attempts()
# print(zzp.login_attempts)
# zzp.reset_login_attempts()
# print(zzp.login_attempts)
# zzp.greet_user()
# zzp.describe_user()

# szy = User("沈", "樟烨", 性别="女", 籍贯="江苏", 年龄=28)
# szy.greet_user()
# szy.describe_user()

# zhm = User("张", "贺铭", 性别="男", 籍贯="山东", 年龄=3)
# zhm.greet_user()
# zhm.describe_user()
