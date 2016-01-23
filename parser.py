from pymongo import MongoClient
import json

client = MongoClient('mongodb://transitapp:transitapp123@ds045694.mongolab.com:45694/subways')
db = client.get_default_database()


with open('subwayLocations.json') as data_file:
	data = json.load(data_file)

subwayData = data['data']

class SubwayStop:
	def __init__(self, name, location, lines):
		self.name = name
		self.location = location
		self.lines = lines

subwayList = []
for array in subwayData:
	a = SubwayStop(array[8], array[9].split(' '), array[11])
	subwayList.append(a)

for subway in subwayList:
	sub = subway.location
	sub.remove("POINT")
	i = 0
	newList = []
	while i < len(sub):
		new = sub[i].replace("(", "")
		new2 = new.replace(")", "")
		newList.append(new2)
		i += 1
	subway.location = newList

print subwayList[0].name

for subway in subwayList:
	db.locations.insert( {
		"name" : subway.name,
		"location" : {
			"lat" : subway.location[1],
			"lon" : subway.location[0] },
		"lines" : subway.lines.split('-')
		} )
