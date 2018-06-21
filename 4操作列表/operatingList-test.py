zaocan = ["baozi","youtiao","doufunao"]
for x in zaocan:
	print("wo xi huan chi "+x)
print("zao can zhen hao chi")

for x in range(1,21):
	print(x)
numbers = list(range(1,1000001))

print(min(numbers),max(numbers),sum(numbers))

jishu = list(range(1,21,2))
for x in jishu:
	print(x)
rd3 = list(range(3,31,3))
for x in rd3:
	print(x)
for x in range(1,11):
	print(x ** 3)
nummm = [x ** 3 for x in range(1,11)]
print(nummm)

print("The first three items in the list are:")
print(nummm[:3])
print("Three items forom the middle of the list are:")
print(nummm[3:6])
print("The last three items in the list are:")
print(nummm[-3:])

friend_zaocan = zaocan[:]
zaocan.append("jianbing")
friend_zaocan.append("jidan")

print("wo de zaocan:")
for x in zaocan:
	print(x)
print("my friend de zaocan:")
for x in friend_zaocan:
	print(x)

zizhu = ("niupai","yangpai","sanwenyu","shala","shanbei")
for x in zizhu:
	print(x)
zizhu = ("niupai","yangpai","sanwenyu","xiejiao","haishen")
for x in zizhu:
	print(x)



