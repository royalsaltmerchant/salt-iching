# Salt Iching

## Iching will return a dict of information on a hexagram
---

To start:

`from iching import iching`

--

To get a random hexagram:

`iching.random()`

--

To get a hexagram by number: \
Enter a number between 1-64

`iching.number(3)`

--

To get a hexagram by lines represented in binary inside an array:

(the first "0" here is the bottom line of the hexagram)

`iching.lines([0, 1, 0, 0, 0, 0])`

--

To get all hexagrams:

`iching.get_hexagrams()`

To get all trigrams:

`iching.get_trigrams()`