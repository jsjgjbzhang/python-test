# filename = "about.txt"
# fileLines = []
# with open(filename, encoding="utf-8") as file_object:
#     # contents = file_object.read()
#     # print(contents.replace("Python","C"))
#
#     # contents = file_object.readlines()
#     # for line in contents:
#     # 	print(line.rstrip())
#
#     contents = file_object.readlines()
#     for line in contents:
#         fileLines.append(line)
#
# for x in fileLines:
#     print(x.rstrip().replace("Python", "C"))

# userName = input("请输入你的名字")
# with open("guest.txt","w",encoding="utf-8") as f:
#     f.write(userName)
# while True:
#     userName = input("请输入你的名字：")
#     print("Hi," + userName)
#     with open("guest_book.txt", "a", encoding="utf-8") as f:
#         f.write(userName + "\n")
#     quit = input("输入quit结束录入")
#     if quit == "quit":
#         break

# while True:
#     reason = input("请问你喜欢编程的原因是：")
#     if reason == "quit":
#         break
#     with open("guest_book.txt", "a", encoding="utf-8") as f:
#         f.write(reason + "\n")

# msg = input("请输入参与运算的数字(使用空格隔开):")
# try:
#     listNum = list(map(int, msg.split()))
#     value = 0
#     for x in listNum:
#         value += x
#     print(value)
# except ValueError:
#     print("请输入正确的数字")


# inputTimes = 0
# addValue = 0
# while inputTimes < 2:
#     msg = input("请输入一个数字:")
#     try:
#         msg = int(msg)
#         inputTimes += 1
#     except ValueError:
#         pass
#     else:
#         addValue += msg

# print(addValue)


# fileNames = ["cats.txt", "dogs.txt"]

# for filename in fileNames:
#     try:
#         with open(filename, "r", encoding="utf-8") as f:
#             contents = f.read()
#             print(contents.rstrip())
#     except FileNotFoundError:
#         # print(filename + " 文件未找到！")
#         pass

# try:
#     with open("绿茶婊.txt", "r", encoding="utf-8") as f:
#         contents = f.read()
#         count = contents.count("婊")
#         print(count)
# except FileNotFoundError:
#     pass
import json

fileName = "favoriteNumber.json"
favValue = ""

try:
    with open(fileName, "r", encoding="utf-8") as f:
        favValue = json.load(f)
except FileNotFoundError:
    with open(fileName, "w", encoding="utf-8") as f:
        favValue = input("请输入你最喜欢的数字:")
        json.dump(favValue, f)
        print(favValue + "已存储")
else:
    print("你喜欢的数字是", favValue)
