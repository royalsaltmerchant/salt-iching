import json
from random import randrange

#get iching data
with open('../../assets/data.json') as d:
  data = json.load(d)

def get_hexagram_by_number(number:int):
  if number > 64 or number < 1:
    print('number must be between 1-64')

  else:
    hexagram_by_number_dict = {}

    for hexagram in data['hexagrams']:
      if number == hexagram['number']:
        for i in hexagram:
          hexagram_by_number_dict[i] = hexagram[i] 
  
    print(hexagram_by_number_dict)
    return hexagram_by_number_dict

# get_hexagram_by_number(7)

def get_hexagram_by_lines(lines):
  hexagram_by_lines_dict = {}

  for hexagram in data['hexagrams']:
    if lines == hexagram['lines']:
      for i in hexagram:
        hexagram_by_lines_dict[i] = hexagram[i] 
  
  print(hexagram_by_lines_dict)

# lines = [0, 1, 0, 0, 0 ,0]
# get_hexagram_by_lines(lines)
  return hexagram_by_lines_dict


# def get_lines():

def get_random_hexagram():
  number = randrange(1, 64)
  hexagram = get_hexagram_by_number(number)
  # print(hexagram)
  return hexagram

# get_random_hexagram()



