import itertools

def freqs(letters):
    result = {}
    for ch in letters:
        result[ch] = result.get(ch, 0) + 1
    return result

def number_needed(a, b):
    freqa = freqs(a)
    freqb = freqs(b)
    letters = set(itertools.chain(freqa.keys(), freqb.keys()))

    operations = 0
    for ch in letters:
        ca = freqa.get(ch, 0)
        cb = freqb.get(ch, 0)
        operations += abs(ca - cb)
    return operations
    

a = input().strip()
b = input().strip()

print(number_needed(a, b))
