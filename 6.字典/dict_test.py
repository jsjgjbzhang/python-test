#人
mywife = {
	"first_name":"沈",
	"last_name":"樟烨",
	"age":"28",
	"city":"上海",
	}
print(mywife["first_name"],mywife["last_name"],mywife["age"],mywife["city"])
#喜欢的数字
friends = {
	"szy":15,
	"zhm":23,
	"zzp":32,
}
print(friends["szy"],friends["zhm"],friends["zzp"])
#词汇表
Glossary = {
	"for":"循环",
	"if":"条件判断",
	"print":"输出",
	"list":"列表",
}
print("for\n\t" + Glossary["for"])
print("if\n\t" + Glossary["if"])
print("print\n\t" + Glossary["print"])
print("list\n\t" + Glossary["list"])

for k,v in Glossary.items():
	print(k + ": " + v)
#河流
rivers = {
	"长江":"南通",
	"黄河":"济南",
	"黄浦江":"上海",
	}
for k,v in rivers.items():
	print(k + "流经" + v)
for k in rivers.keys():
	print(k)
for v in rivers.values():
	print(v)

#调查
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
surveyUserList = ["zzp","sarah","szy","phil"]
for user in surveyUserList:
	if user in favorite_languages.keys():
		print("感谢" + user + "接受调查")
	else:
		print("你好，" + user + "能参与调查么？")

#人
person1 = {
	"first_name":"沈",
	"last_name":"樟烨",
	"age":"28",
	"city":"上海",
	}
person2 = {
	"first_name":"张",
	"last_name":"忠鹏",
	"age":"28",
	"city":"山东",
	}
person3 = {
	"first_name":"张",
	"last_name":"贺铭",
	"age":"3",
	"city":"江苏",
	}
lPerson = [person1, person2, person3]
for person in lPerson:
	for k,v in person.items():
		print(k + ":" + v)
#宠物
xiaohua = {
	"type":"dog",
	"master":"张忠鹏",
}
miaomiao = {
	"type":"cat",
	"master":"沈樟烨",
}

pets = [xiaohua,miaomiao]
for pet in pets:
	for k,v in pet.items():
		print(k + ":" + v)
#喜欢的地方
favorite_places = {
	"张忠鹏":["度假村","海边"],
	"张贺铭":["游乐园","恐龙乐园","动物园"],
	"沈樟烨":["大润发","健身房"],
}

for k,v in favorite_places.items():
	sPlace = "、".join(v)
	print(k + "喜欢的地方是:" + sPlace)

#喜欢的数字
friends = {
	"szy":[3,45,6,7,8,423],
	"zhm":[12,3,4,5,22],
	"zzp":[666,777,888],
}

for k,v in friends.items():
	sNum = "、".join("%s" %id for id in v)
	print(k + "喜欢的数字是:" + sNum)
#城市
cities = {
	"上海":{
		"国家":"中国",
		"人口":"3000万",
		"标签":"魔幻之都",
	},
	"纽约":{
		"国家":"美国",
		"人口":"2000万",
		"标签":"自由之都",
	},
	"东京":{
		"国家":"日本",
		"人口":"1000万",
		"标签":"樱花之都",
	},
}

del cities["上海"]

cities["巴黎"] = {
	"国家":"法国",
	"人口":"500万",
	"标签":"浪漫之都",
}

for city,cityInfo in cities.items():
	print(city + "的信息是:")
	for k,v in cityInfo.items():
		print("\t" + k + ":" + v)
	

