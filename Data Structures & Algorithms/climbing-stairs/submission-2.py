class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        ref = [0] * (n)

        ref[-1] = 1
        ref[-2] = 2

        for i in range(n - 3, -1, -1):
            ref[i] = ref[i + 1] + ref[i + 2]

        return ref[0]
        