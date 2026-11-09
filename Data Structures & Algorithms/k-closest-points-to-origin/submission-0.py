class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        res = []

        points = [(math.sqrt(coor[0] ** 2 + coor[1] ** 2), coor) for coor in points]

        heapq.heapify(points)

        while k != 0:

            res.append(heapq.heappop(points)[1])
            k -= 1

        return res

        