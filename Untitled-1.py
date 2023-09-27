
from heapq import heappush, heappop
from copy import deepcopy

INITIAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, None]]
GOAL_STATE = [[1, 2, 3], [8, None, 4], [7, 6, 5]]

def h(state):
    misplaced = sum([1 for i in range(3) for j in range(3) if state[i][j] != GOAL_STATE[i][j]])
    return misplaced

def solve(initial_state):
    open_set = [(h(initial_state), initial_state)]
    closed_set = set()
    path = {tuple(map(tuple, initial_state)): None}

    while open_set:
        _, current_state = heappop(open_set)

        if current_state == GOAL_STATE:
            moves = []
            while current_state:
                moves.append(current_state)
                current_state = path.get(tuple(map(tuple, current_state)))
            return moves[::-1]

        i, j = next((i, j) for i in range(3) for j in range(3) if current_state[i][j] is None)
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < 3 and 0 <= nj < 3:
                successor_state = deepcopy(current_state)
                successor_state[i][j], successor_state[ni][nj] = successor_state[ni][nj], successor_state[i][j]
                if tuple(map(tuple, successor_state)) not in closed_set:
                    g_score = len(path)
                    f_score = g_score + h(successor_state)
                    heappush(open_set, (f_score, successor_state))
                    path[tuple(map(tuple, successor_state))] = current_state

        closed_set.add(tuple(map(tuple, current_state)))

    return None

moves = solve(INITIAL_STATE)

if moves:
    for i, move in enumerate(moves):
        print(f"Move {i}:")
        for row in move:
            print(row)
        print()
else:
    print("No solution found.")
