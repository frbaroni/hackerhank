import unittest


def solution(A):
    def multi(x):
        return x[0] * x[1] * x[2]
    a = sorted(A)
    pos = multi(a[-3:])
    neg = multi(a[-1:] + a[:2])
    return max(pos, neg)


class Playground(unittest.TestCase):
    def test_example(self):
        A = [-3, 1, 2, -2, 5, 6]
        R = 60
        self.assertEqual(solution(A), R)

    def test_medium_range(self):
        A = [x for x in range(-1000, 1000)]
        R = 998001000
        self.assertEqual(solution(A), R)

    def test_large(self):
        A = [n for n in range(-10, 10) for x in range(1000)] + [-1000, 500, -1]
        R = 5000000
        self.assertEqual(solution(A), R)


if __name__ == '__main__':
    unittest.main()
