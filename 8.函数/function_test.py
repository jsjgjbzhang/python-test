

# def display_message():
#     print("Function")


# display_message()


# def make_shirt(size, info="I Love Python"):
#     print(size, info)


# make_shirt(16, "zzp")
# make_shirt(info="zhm", size=16)

# make_shirt(15)
# make_shirt(39)
# make_shirt(99, "yes")


# def describe_city(city, country="China"):
#     print(city + " is in " + country)


# describe_city("shanghai")
# describe_city("beijing")
# describe_city("tokyo", "Japan")


# def make_albm(singer, albmName, songsNum=0):
#     albm = {"singer": singer, "albmName": albmName}
#     if songsNum > 0:
#         albm["songsNum"] = songsNum
#     return albm


# print(make_albm("JAY", "以父之名", 10))
# print(make_albm("Yello", "Coldplay"))
# print(make_albm("小红莓", "Joe"))


# while True:
#     singerName = input("请输入歌手的名字：")
#     albmName = input("请输入新专辑的名字：")
#     songsNum = input("请输入新专辑歌单数目：")
#     albm = make_albm(singerName, albmName, int(songsNum))
#     print("专辑创建完毕！", albm)
#     goon = input("是否继续创建新专辑？yes or no")
#     if goon == "no":
#         break


# mages = ["张忠鹏", "沈樟烨", "张贺铭"]
# newMages = []


# def make_great(mageList):
#     for i, mage in enumerate(mageList):
#         mageList[i] = "伟大的" + mage
#     return mageList


# def show_magicians(mageList):
#     for mage in mageList:
#         print(mage)


# newMages = make_great(mages[:])
# show_magicians(mages)
# show_magicians(newMages)


# def zuojidanbing(*zuoliao):
#     for x in zuoliao:
#         print(x)


# zuojidanbing("加辣", "加鸡蛋", "加火腿", "加番茄酱")
# zuojidanbing("加辣", "加鸡蛋", "加火腿")
# zuojidanbing("加辣", "加鸡蛋")


# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile


# user_profile = build_profile("张", "忠鹏", 性别="男", 籍贯="山东", 年龄=28)
# print(user_profile)


# def make_car(brands, model, **car_info):
#     car = {"品牌": brands, "型号": model}
#     for k, v in car_info.items():
#         car[k] = v
#     return car


# car_profile = make_car('subaru', 'outback', color='blue', tow_package=True)
# print(car_profile)


# import model_test
# model_test.showModelTest("this")


# from model_test import showModelTest
# showModelTest("this")

# from model_test import showModelTest as smt
# smt("this")

# import model_test as mt
# mt.showModelTest("this")

from model_test import *
showModelTest("sdkf")






