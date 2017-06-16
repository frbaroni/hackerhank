import unittest


def profile(fn):
    import cProfile
    p = cProfile.Profile()
    p.enable()
    res = fn()
    p.disable()
    p.print_stats()
    return res


def solution(A):
    min_avg = 100000
    min_pos = 0
    for idx in range(1, len(A)):
        avg = (A[idx - 1] + A[idx]) / 2.0
        if avg < min_avg:
            min_avg = avg
            min_pos = idx - 1
        if idx > 1:
            avg = (A[idx - 2] + A[idx - 1] + A[idx]) / 3.0
            if avg < min_avg:
                min_avg = avg
                min_pos = idx - 2
    return min_pos


class Playground(unittest.TestCase):
    def test_example(self):
        A = [4, 2, 2, 5, 1, 5, 8]
        R = 1
        self.assertEqual(solution(A), R)

    def test_last(self):
        A = [5, 5, 5, 1, 1]
        R = 3
        self.assertEqual(solution(A), R)

    def test_first(self):
        A = [1, 1, 5, 5, 5]
        R = 0
        self.assertEqual(solution(A), R)

    def test_negative(self):
        A = [-3, -5, -8, -4, -10]
        R = 2
        self.assertEqual(solution(A), R)

    def test_first_three(self):
        A = [1, 2, 1, 5, 5, 5]
        R = 0
        self.assertEqual(solution(A), R)

    def test_big_1_minus_1(self):
        A = [(n % 3) - 1 for n in range(100000)]
        R = 0
        self.assertEqual(solution(A), R)

    def test_all_max(self):
        A = [100000] * 100000
        R = 0
        self.assertEqual(solution(A), R)

    def test_increasing(self):
        A = [n * 2 for n in range(1000)]
        R = 0
        self.assertEqual(solution(A), R)


if __name__ == '__main__':
    unittest.main()
