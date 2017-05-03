def abc_counts(text):
    letters = {'a': 0,
               'b': 0,
               'c': 0}
    for i in range(len(text)):
        letters[text[i]] += 1

    return letters['a'], letters['b'], letters['c']

tests = int(input())
for test in range(tests):
    text = input()
    a, b, c = abc_counts(text)
    l = len(text)
   
    mods2 = (a % 2) + (b % 2) + (c % 2)
    allodds = mods2 == 3
    allevens = mods2 == 0
    
    if a == l or b == l or c == l:
        print(l)
    elif allevens or allodds:
        print(2)
    else:
        print(1)
