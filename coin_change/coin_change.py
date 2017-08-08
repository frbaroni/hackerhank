def R(change, coins, M):
    if change == 0:
        return 1
    if change < 0:
        return 0
    if not coins:
        return 0
    key = '{}_{}'.format(change, coins)
    if key in M:
        return M[key]
    ways = 0
    amount = 0
    while amount <= change:
        ways += R(change - amount, coins[1:], M)
        amount += coins[0]
    M[key] = ways
    return ways


def coinChange(change, coins):
    return R(change, list(reversed(sorted(coins))), {})


n, m = map(int, input().split(' '))
coins = list(map(int, input().split(' ')))
print(coinChange(n, coins))
