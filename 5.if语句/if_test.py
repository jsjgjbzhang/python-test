car = "Audi"
print(car == "audi", car.lower() == "audi")
shengao = 175
xingbie = "malee"
if shengao >= 170 and shengao <= 180:
    print("shengao hai ke yi")
if xingbie == "male" or xingbie == "female":
    print("xingbie is " + xingbie)
    pass
xblist = ["male", "female"]
if xingbie in xblist:
    print("zzzzzzz")
if xingbie not in xblist:
    print("bbbbbbbb")

alien_color = "green"
if alien_color == "green":
    print("u get 5 points")

alien_color = "yello"

if alien_color == "green":
    print("u get 5 points")
elif alien_color == "yello":
    print("u get 10 points")
else:
    print("u get 15 points")

age = 19
if age < 2:
    print("ying er")
elif age < 4:
    print("xue bu")
elif age < 13:
    print("er tong")
elif age < 20:
    print("qing shao nian")
elif age < 65:
    print("cheng nian ren")
else:
    print("lao nian ren")

favorite_fruits = ["apple", "orange", "watermelon", "peach", "banana"]

if "apple" in favorite_fruits:
    print("u really like apple")
if "orange" in favorite_fruits:
    print("u really like orange")
if "watermelon" in favorite_fruits:
    print("u really like watermelon")
if "peach" in favorite_fruits:
    print("u really like peach")
if "banana" in favorite_fruits:
    print("u really like banana")

users = ["zzp", "szy", "zhm", "admin", "bbc"]
# users = []
if users:
    for x in users:
        if x == "admin":
            print("Hello " + x + ", would you like to see a status report?")
        else:
            print("Hello " + x + ", thank you for logging in again")
else:
    print("We need to find some users!")

current_user = ["zzp", "John", "zhm", "admin", "bbc"]
new_user = ["zzp", "JOHN", "bmw", "benz", "Audi"]

bFind = False

for x in new_user:
    for z in current_user:
        if x.lower() == z.lower() or x.upper() == z.upper():
            print(x + " yi zhu ce!")
            bFind = True
            break
        else:
            bFind = False
    if bFind is False:
        print(x + " 可以使用")

listOp = list(range(1, 10))
print(listOp)
for x in listOp:
    if x == 1:
        print(str(x) + "st")
    elif x == 2:
        print(str(x) + "nd")
    elif x == 3:
        print(str(x) + "rd")
    else:
        print(str(x) + "th")











