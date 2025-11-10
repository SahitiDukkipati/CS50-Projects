## Part of CS50’s AI project: Degrees
## This section includes my implementation for the logical reasoning setup.
## Only my written logic is shared here, not the full project framework.


# Define the function that removes a node from the frontier and returns it.
def shortest_path(source, target):


    start = Node(state=source, parent=None, action=None)
    frontier = QueueFrontier()
    frontier.add(start)
    explored = set()

    while True:
        if frontier.empty():
            return None

        node = frontier.remove()
        explored.add(node.state)

        for movie_id, person_id in neighbors_for_person(node.state):
            if not frontier.contains_state(person_id) and person_id not in explored:
                child = Node(state=person_id, parent=node, action=movie_id)

                if child.state == target:
                    path = []
                    while child.parent is not None:
                        path.append((child.action, child.state))
                        child = child.parent
                    path.reverse()
                    return path

                frontier.add(child)
