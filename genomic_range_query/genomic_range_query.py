import unittest


def profile(fn):
    import cProfile
    p = cProfile.Profile()
    p.enable()
    res = fn()
    p.disable()
    p.print_stats()
    return res


def solution_bruteforce(S, P, Q):
    impacts = dict(A=1, C=2, G=3, T=4)
    results = []
    for q in range(len(Q)):
        first = P[q]
        last = Q[q] + 1
        strain = S[first:last]
        lowest = impacts[strain[0]]
        for nucleotide in strain:
            lowest = min(lowest, impacts[nucleotide])
            if lowest == 1:
                break
        results.append(lowest)
    return results


def solution(S, P, Q):
    def frequencies(S):
        a = [0] * (len(S) + 1)
        c = [0] * (len(S) + 1)
        g = [0] * (len(S) + 1)
        t = [0] * (len(S) + 1)
        nucleotides = {
                'A': a,
                'C': c,
                'G': g,
                'T': t,
                }
        for index, nucleotide in enumerate(S):
            a[index + 1] = a[index]
            c[index + 1] = c[index]
            g[index + 1] = g[index]
            t[index + 1] = t[index]
            nucleotides[nucleotide][index + 1] += 1
        return [a, c, g, t]

    def queries(freqs, S, P, Q):
        results = []
        impacts = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
        for q in range(len(Q)):
            first = P[q]
            last = Q[q] + 1
            if first == last:
                results.append(impacts[S[first]])
                continue
            for nucleotide in range(4):
                if freqs[nucleotide][first] < freqs[nucleotide][last]:
                    results.append(nucleotide + 1)
                    break
        return results

    freqs = frequencies(S)
    results = queries(freqs, S, P, Q)
    return results


class Playground(unittest.TestCase):
    def test_example(self):
        S = 'CAGCCTA'
        P = [2, 5, 0]
        Q = [4, 5, 6]
        R = [2, 4, 1]
        self.assertEqual(solution(S, P, Q), R)

    def test_one_element(self):
        S = 'CAGCCTA'
        P = [2]
        Q = [2]
        R = [3]
        self.assertEqual(solution(S, P, Q), R)

    def test_small(self):
        S = 'CT'
        P = [0, 0, 1]
        Q = [0, 1, 1]
        R = [2, 2, 4]
        self.assertEqual(solution(S, P, Q), R)

    def test_single(self):
        S = 'T'
        P = [0]
        Q = [0]
        R = [4]
        self.assertEqual(solution(S, P, Q), R)

    def test_huge(self):
        S = ('A' * 1000000)
        P = [0]
        Q = [len(S) - 1]
        R = [1]
        self.assertEqual(solution(S, P, Q), R)

    def test_huge_last(self):
        S = ('T' * 1000000) + 'A'
        P = [0]
        Q = [len(S) - 1]
        R = [1]
        self.assertEqual(solution(S, P, Q), R)


if __name__ == '__main__':
    unittest.main()
