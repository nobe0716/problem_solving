class Solution(object):
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        if n == 0:
            return True

        visited = [False] * n
        q = [0]
        while len(q) > 0:
            nq = set()
            for e in q:
                visited[e] = True
                for k in rooms[e]:
                    if visited[k]:
                        continue
                    nq.add(k)
            q = list(nq)
        return all(visited)
