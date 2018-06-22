message = input("请问你想买什么品牌的汽车？")
print("我去帮你找" + message)

visiterNum = input("您好，请问几位？")

visiterNum = int(visiterNum)

if visiterNum > 8:
    print("没座")
else:
    print("里边请！")

gusNum = input("请输入一个数字")
gusNum = int(gusNum)
if gusNum % 10 == 0:
    print(str(gusNum) + "是10的整数倍！")

active = True
print("请问你想加什么配料？输入quit结束添加")
while active:
    ngredientsi = input()
    if ngredientsi == "quit":
        # break
        active = False
    else:
        print(ngredientsi + "已添加!")

while True:
    age = input("请输入您孩子的年龄:")
    age = int(age)
    if age < 3:
        print("免费")
    elif age <= 12:
        print("10美元")
    else:
        print("15美元")

sandwich_orders = ["冰镇小龙虾", "蒜香小龙虾", "十三香小龙虾", "麻辣小龙虾"]
finished_sandwiches = []
while sandwich_orders:
    corder = sandwich_orders.pop()
    finished_sandwiches.append(corder)
    print(corder + "已经做好了！")
print("，".join(finished_sandwiches) + "已经全部做好了")

sandwich_orders = ["冰镇小龙虾", "蒜香小龙虾", "十三香小龙虾",
                   "麻辣小龙虾", "十三香小龙虾", "十三香小龙虾", "十三香小龙虾"]
finished_sandwiches = []
print("十三香用光了！")

while "十三香小龙虾" in sandwich_orders:
    sandwich_orders.remove("十三香小龙虾")

while sandwich_orders:
    corder = sandwich_orders.pop()
    finished_sandwiches.append(corder)
    print(corder + "已经做好了！")
print("，".join(finished_sandwiches) + "已经全部做好了")
visitors = {}
while True:
    hi = input("你好，请问能帮我们做个调查么？yes or no")
    if hi == "no":
        print("好的，打扰了！")
        break
    name = input("谢谢，请问你叫什么名字？")
    place = input(name + "，你最想去哪里旅游呢？")
    visitors[name] = place
    print("好的，谢谢你配合我们调查！")

for k, v in visitors.items():
    print(k + "最想去的地方是：" + v)
