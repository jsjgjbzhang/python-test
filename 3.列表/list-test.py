names = ["zzp","szy","zhm"]
print(names[0],names[1],names[2])

for x in names:
	print("Hi,"+x)
treemo = ["kaiche","ditie","gongjiao","qiche"]
print(treemo)
for z in treemo:
	print("i would like "+z)

guests = ["zzp","zhm","szy"]
for x in guests:
	print("qing "+x+" can jia wan can")
print(guests[2]+"wu fa can jia")
guests[2] = "xhl"
for x in guests:
	print("qing "+x+" can jia wan can")

print("zhao dao xin can zhuo")
guests.insert(0, "bmw")
guests.insert(1, "audi")
guests.append("benz")

for x in guests:
	print("qing "+x+" can jia wan can")

print("zhi neng yao qing 2 wei")

while len(guests) > 2:
	guest = guests.pop()
	print(guest+" sorry!")
for x in guests:
	print("qing "+x+" can jia wan can")
del guests[0]
del guests[0]
print(guests)

city = ["shanghai","beijing","guangzhou","sanya","yantai"]
print(city)

print(sorted(city))

print(sorted(city,reverse=True))
print(city)
city.reverse()
print(city)
city.reverse()
print(city)
city.sort()
print(city)
city.sort(reverse=True)
print(city)



