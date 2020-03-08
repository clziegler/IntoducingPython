# 8.1
e2f = {
    'dog':'chien',
    'cat':'chat',
    'walrus':'morse',
}
print(e2f)
# 8.2
print(e2f["walrus"])
# 8.3
f2e = {x:y for y, x in e2f.items()}
print(f2e)
# 8.4
print(f2e["chien"])
#8.5
print(set(e2f))
#8.6

life = {
    'animals': {
        'cats':[
            'Henry',
            'Grumpy',
            'Lucy',
        ],
        'octopi':{},
        'emus':{},
                    },
        'plants': {},
        'others': {},

        }
#8.7
print(life.keys())
# 8.8
print(life['animals'].keys())
# 8.9
print(life['animals'].get('cats'))
# 8.10
squares = {x*x : x for x in range(10)}
print(squares)
# 8.11
odd = { x for x in range(10) if x % 2 != 0}
print(odd)
# 8.12
got = ['Got ' + str(num) for num in range(10)]
for x in got:
    print(x)

# 8.13
keys = ('optimist', 'pessimist', 'troll')
values = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')

combined = {k:v for k, v in zip(keys, values)}
print(combined)

# 8.14
titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane']
plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']

movies = {t:p for t, p in zip(titles, plots)}
print(movies)