from queue import Queue

class PuzzleNode:
    def __init__(self, state, parent, action, cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

def bfs_puzzle(initial_state, goal_state):
    explored = set()
    frontier = Queue()
    initial_node = PuzzleNode(initial_state, None, None, 0)
    frontier.put(initial_node)

    while not frontier.empty():
        current_node = frontier.get()
        current_state = current_node.state
        explored.add(tuple(current_state))

        if current_state == goal_state:
            return build_path(current_node)

        zero_pos = current_state.index(0)
        row, col = zero_pos // 3, zero_pos % 3

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_zero_pos = 3 * new_row + new_col
                new_state = current_state[:]
                new_state[zero_pos], new_state[new_zero_pos] = new_state[new_zero_pos], new_state[zero_pos]

                if tuple(new_state) not in explored:
                    new_node = PuzzleNode(new_state, current_node, (dr, dc), current_node.cost + 1)
                    frontier.put(new_node)

    return None

def build_path(node):
    path = []
    while node.parent is not None:
        path.append(node.action)
        node = node.parent
    path.reverse()
    return path

if __name__ == "__main__":
    initial_state = [2, 5, 3, 1, 8, 6, 7, 0, 4]
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    solution = bfs_puzzle(initial_state, goal_state)

    if solution:
        print("Solução encontrada. Passos:")
        for step in solution:
            print(step)
        print(f"Custo total: {len(solution)}")
    else:
        print("Não foi encontrada uma solução.")
