import json

#get iching data
with open('../../assets/data.json') as d:
  data = json.load(d)

def get_hexagram_by_number(number:int):
  for hexagram in data['hexagrams']:
    if number == hexagram['number']:
      for i in hexagram:
        # print(i, hexagram[i])
        hexagram_by_number_dict = {i: hexagram[i]}
        print(hexagram_by_number_dict)

get_hexagram_by_number(7)


