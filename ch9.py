# lambda function
stairs = ['thud', 'meow', 'thud', 'hiss']

def edit_story(words, func):
    for word in words:
        print(func(word))

edit_story(stairs, lambda word: word.capitalize() + '!')

# generator functions

def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step
ranger = my_range(1,5)

for x in ranger:
    print(x)

# Generator objects

genobj = (pair for pair in zip(['a', 'b'], ['1','2']))

for x in genobj:
    print(x)


#9.1
def good():
    return ['Harry', 'Ron', 'Hermione']
print(good())

# 9.2
def get_odds(first=0, last=10):
    num = first
    while num < last:
        if num % 2 != 0:
            yield num
        num += 1

getO = get_odds(0,10)

for x in getO:
    print(x)

# 9.3
def test(func):
    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print("end")
        return result
    return wrapper


@test
def dummy():
    print("middle")

dummy()






