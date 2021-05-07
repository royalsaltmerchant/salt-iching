import json

#get iching data
with open('../../assets/data.json') as d:
  data = json.load(d)

def get_hexagram(number:int):
  for hexagram in data['hexagrams']:
    if number == hexagram['number']:
      print(hexagram['chineseName'])

get_hexagram(3)


