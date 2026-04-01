class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class QueueFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node


def neighbors(state):
    """
    Returns list of pairs
    who starred with a given state.
    """
    raise NotImplementedError


def bfs(source, target):
    """
    Returns the shortest list of pairs
    that connect the source to the target.

    If no possible path, returns None.
    """
    print("start")
    queue = QueueFrontier()
    queue.add(Node(source, None, None))
    visited, path = {Node(source, None, None)}, list()
    while queue.empty:
        parent = queue.remove()
        visited.add(parent)
        for neighbor in neighbors(parent.state):
            neighbor = Node(neighbor[1], parent, neighbor[0])
            if neighbor not in visited:
                # Target found, path built
                if neighbor.state == target:
                    while neighbor.parent is not None:
                        path.append((neighbor.action, neighbor.state))
                        neighbor = neighbor.parent
                    return path
                queue.add(neighbor)
                visited.add(neighbor)
    return None
