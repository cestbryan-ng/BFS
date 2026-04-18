from utils import QueueFrontier, Node


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
                # Target found, path built, the first node is not included in the path remember to add it.
                if neighbor.state == target:
                    while neighbor.parent is not None:
                        path.append((neighbor.action, neighbor.state))
                        neighbor = neighbor.parent
                    return path[::-1]
                queue.add(neighbor)
                visited.add(neighbor)
    return None
