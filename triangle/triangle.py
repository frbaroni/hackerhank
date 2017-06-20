import unittest


def solution(A):
    a = sorted(A)
    for i in range(len(A) - 2):
        if a[i] + a[i + 1] > a[i + 2]:
            return 1
    return 0


class Playground(unittest.TestCase):
    def test_example(self):
        A = [10, 2, 5, 1, 8, 20]
        R = 1
        self.assertEqual(solution(A), R)

    def test_example_bad(self):
        A = [10, 50, 5, 1]
        R = 0
        self.assertEqual(solution(A), R)


if __name__ == '__main__':
    unittest.main()
