def solution(X, A):
    filled = set()
    for index in range(len(A)):
        pos = A[index]
        if not (pos in filled):
            filled.add(pos)
            if len(filled) == X:
                return index
    return -1

def test(A, R, E):
    status = 'OK' if R == E else 'FAILED'
    print('Input:\t\t{0}\nOutput:\t\t{1}\nExpected:\t{2}\n{3}\n'
            .format(A, R, E, status))

A = [1, 3, 1, 4,  2, 3, 5, 4]
N = 5
E = 6
test(A, solution(N, A), E)
