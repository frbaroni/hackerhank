from collections import Counter

def solution(N, A):
    biggest = 0
    base = 0
    counters = Counter()
    for op in A:
        op -= 1
        if op == N:
            counters = Counter()
            base = biggest
        else:
            counters[op] += 1
            biggest = max(biggest, base + counters[op])
    
    return [(base + counters[c]) for c in range(N)]

def test(A, R, E):
    status = 'FAILED'
    if R == E:
        status = 'OK'
    print('Input:\t\t{0}\nOutput:\t\t{1}\nExpected:\t{2}\n{3}\n'
            .format(A, R, E, status))


A = [3, 4, 4, 6, 1, 4, 4]
N = 5
E = [3, 2, 2, 4, 2]
test(A, solution(N, A), E)
