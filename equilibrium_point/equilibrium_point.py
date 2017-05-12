def equilibrium_point(A):
    best_dist = float('inf')
    left = 0
    right = sum(A)
    best = (0, left, right)
    for index in range(len(A) - 1):
        left += A[index]
        right -= A[index]

        dist = abs(left - right)
        if dist < best_dist:
            best_dist = dist
            best = (index, left, right)
    return best

def solution(A):
    index, left, right = equilibrium_point(A)
    return abs(left - right)

def test(A, R, E):
    status = 'FAILED'
    if R == E:
        status = 'OK'
    print('Input:\t\t{0}\nOutput:\t\t{1}\nExpected:\t{2}\n{3}\n'
            .format(A, R, E, status))

A = [3, 1, 2, 4, 3]
E = 1
test(A, solution(A), E)


A = [6000, 8000]
E = 2000
test(A, solution(A), E)

A = [-1000, 1000]
E = 2000
test(A, solution(A), E)
