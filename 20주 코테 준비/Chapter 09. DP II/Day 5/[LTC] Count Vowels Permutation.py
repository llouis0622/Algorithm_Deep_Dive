class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        a = e = i = o = u = 1
        for _ in range(n - 1):
            na = (e + i + u) % MOD
            ne = (a + i) % MOD
            ni = (e + o) % MOD
            no = i % MOD
            nu = (i + o) % MOD
            a, e, i, o, u = na, ne, ni, no, nu
        return (a + e + i + o + u) % MOD
