this_list = [n for n in range(3,-1, -1)]

for x in this_list:
    print(x)
# 7.1
years_list = [number for number in range(1979, 1985)]

for x in years_list:
    print(x)
# 7.2
print(years_list[3])

# 7.3
last = years_list[-1:]
print(last)

# 7.4
things = ["mozzerella", "cinderella", "salmonella"]
# 7.5
things[1] = things[1].capitalize()
print(things)
# 7.6
things[0] = things[0].upper()
print(things)
# 7.7
things.remove(things[2])
print(things)
# 7.8
surprise = ["Groucho", "Chico", "Harpo"]
# 7.9
surprise[2] = surprise[2][::-1].lower().capitalize()
print(surprise)
# 7.10
even = [n for n in range(10) if n % 2 == 0]
print(even)
# 7.11
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
    ]
start2 = "Someone better"

start1_str = "! ".join(start1).title() + '! '
for x, y in rhymes:
    print(start1_str + x.capitalize() + '!' + "\n" + start2 + " " + y + ".")

