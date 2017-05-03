def solution(A, k):
    result = []
    for i in range(len(A)):
        idx = ((len(A) - k) + i) % len(A)
        result.append(A[idx])
    return result

def test(A, K, E):
    R = solution(A, K)
    status = 'FAILED'
    if R == E:
        status = 'OK'
    print('Input:\t\t{0} >> {1} \nOutput:\t\t{2}\nExpected:\t{3}\n{4}\n'
            .format(A, K, R, E, status))

A = [3, 8, 9, 7, 6]
E = [6, 3, 8, 9, 7]
test(A, 1, E)

A = [3, 8, 9, 7, 6]
E = [9, 7, 6, 3, 8]
test(A, 3, E)

