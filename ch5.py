song = """When an eel grabs your arm,
And it causes great harm,
 That's - a moray!"""

song = song.replace('moray', 'Moray')

print(song)

questions = ["We don't serve strings around here. Are you a string?",
             "What is said on Father's Day in the forest?",
             "What makes the sound 'Sis! Boom! Bah!'?"
             ]

answers = ["An exploding sheep.",
           "No, I'm a frayed knot.",
           "'Pop!' goes the weasel."
           ]

answers = [answers[1], answers[2], answers[0]]

for q, a in zip(questions, answers):
    print('Q: {} \nA: {} \n'.format(q, a))

ham = 'ham'
roast_beef = 'roast beef'
head = 'head'
clam = 'clam'

cat_poem = """My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he's a %s.""" %(roast_beef, ham, head, clam)

print(cat_poem)
letter_dict = {
    'salutation': 'Ms.',
    'name':'Bolen',
    'product':'toothbrush',
    'verbed':'exploded',
    'room':'bathroom',
    'animals':'puffins',
    'amount':'1.99',
    'percent':'3',
    'spokesman':'Bob Vance',
    'job_title': 'Job Haver'
}

form_letter = """Dear {0[salutation]} {0[name]},

Thank you for your letter. We are sorry that our {0[product]}
{0[verbed]} in your {0[room]}. Please note that it should never
be used in a {0[room]}, especially near any {0[animals]}.

Send us your receipt and {0[amount]} for shipping and handling.
We will send you another {0[product]} that, in our tests,
is {0[percent]}% less likely to have {0[verbed]}.

Thank you for your support.

Sincerely,
{0[spokesman]}
{0[job_title]}"""

print(form_letter.format(letter_dict))

def mcface(name):
    print('{}y Mc{}face'.format(name.capitalize(), name.capitalize()))

mcface('duck')
mcface('gourd')
mcface('spitz')