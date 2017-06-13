def solution(A, B, K):
    first = A if ((A % K) == 0) else (A + (K - (A % K)))
    if first > B:
        return 0
    return 1 + ((B - first) / K)

def t(A, B, K, E):
    r = solution(A, B, K)
    print('solution({} {} {}) ({}) => {} [{}]\n'.format(A, B, K, E, r, 'OK' if r == E else 'FAIL'))

t(5, 11, 2, 3)    
t(5, 11, 3, 2)
t(5, 11, 6, 1)
t(5, 11, 1, 7)
t(6, 11, 2, 3)
