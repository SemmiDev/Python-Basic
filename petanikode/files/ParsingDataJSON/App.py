import json

file_json = open('details.json')
data = json.loads(file_json.read())
print("Name        -> {}".format(data['name']))
print("Age         -> {}".format(data['age']))
print("Specialist  -> {}".format(data['specialist']))
print("Programming -> {}".format(data['programming']))
print("Media       => ")
for media in data['media']:
    print("\t", media, "-> ",data['media'][media])