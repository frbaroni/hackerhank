def solution(N):
    binary = bin(N)[2:]
    current = 0
    best = 0
    for b in binary:
        if b == '1':
            best = max(current, best)
            current = 0
        else:
            current += 1
    return max(best, current)


print(solution(9))
print(solution(1041))
