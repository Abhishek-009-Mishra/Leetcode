from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        # Give every litter cell a bit position.
        litter_id = {}
        litter_count = 0
        start_r = start_c = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litter_id[(r, c)] = litter_count
                    litter_count += 1

        full_mask = (1 << litter_count) - 1

        # State: (row, col, mask, remaining_energy)
        q = deque()
        q.append((start_r, start_c, 0, energy))

        # best[(r, c, mask)] = maximum energy seen so far.
        #
        # If we reach the same (r, c, mask) with <= this energy,
        # that state is dominated and need not be explored.
        best = [-1] * (m * n * (1 << litter_count))

        def index(r, c, mask):
            return ((r * n + c) << litter_count) | mask

        best[index(start_r, start_c, 0)] = energy

        moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
        distance = 0

        while q:
            # Process one BFS level.
            for _ in range(len(q)):
                r, c, mask, e = q.popleft()

                if mask == full_mask:
                    return distance

                for dr, dc in moves:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    # Need one unit of energy for the move.
                    if e == 0:
                        continue

                    ne = e - 1
                    nmask = mask

                    cell = classroom[nr][nc]

                    # Collect litter.
                    if cell == 'L':
                        bit = litter_id[(nr, nc)]
                        nmask |= 1 << bit

                    # Reset energy upon reaching R.
                    if cell == 'R':
                        ne = energy

                    idx = index(nr, nc, nmask)

                    # This state is dominated if we've already reached
                    # the same position/mask with at least as much energy.
                    if ne <= best[idx]:
                        continue

                    best[idx] = ne
                    q.append((nr, nc, nmask, ne))

            distance += 1

        return -1