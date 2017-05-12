def solution(A):
    found = set(A)
    for i in range(1, len(A) + 2):
        if not (i in found):
            return i
    return 0

def test(A, E):
    R = solution(A)
    status = 'FAILED'
    if R == E:
        status = 'OK'
    print('Input:\t\t{0}\nOutput:\t\t{1}\nExpected:\t{2}\n{3}\n'
            .format(A, R, E, status))

A = [2, 3, 1, 5]
E = 4
test(A, E)

A = []
E = 1
test(A, E)

A = [2, 3]
E = 1
test(A, E)

A = [2, 1]
E = 3
test(A, E)

A = [1]
E = 2
test(A, E)

A = [2]
E = 1
test(A, E)
