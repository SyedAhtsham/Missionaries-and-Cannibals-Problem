import numpy as np
import math


class State():
    # Parameterized Constructor of State Class
    def __init__(self, cl, ml, boat, cr, mr):
        self.cl = cl
        self.ml = ml
        self.boat = boat
        self.cr = cr
        self.mr = mr
        self.p = None

    # Function to check whether a state is a goal state or not
    def is_goal(self):
        if self.cl == 0 and self.ml == 0:
            return True
        else:
            return False

    # Function to check whether a state is valid or not if it's invalid then it's avoided as Missionaries would be eaten
    def is_valid(self):
        if self.ml >= 0 and self.mr >= 0 \
                and self.cl >= 0 and self.cr >= 0 \
                and (self.ml == 0 or self.ml >= self.cl) \
                and (self.mr == 0 or self.mr >= self.cr):

            return True
        else:
            return False

    # Function to check whether two states are equal or not
    def __eq__(self, other):
        return self.cl == other.cl and self.ml == other.ml \
               and self.boat == other.boat and self.cr == other.cr \
               and self.mr == other.mr

    def __hash__(self):
        return hash((self.cl, self.ml, self.boat, self.cr, self.mr))


# Function to generate successors/children of a state
def successors(pre):
    c = []
    if pre.boat == 'l':
        post = State(pre.cl, pre.ml - 2, 'r', pre.cr, pre.mr + 2)
        if post.is_valid():
            post.p = pre
            c.append(post)
        post = State(pre.cl - 2, pre.ml, 'r', pre.cr + 2, pre.mr)
        if post.is_valid():
            post.p = pre
            c.append(post)
        post = State(pre.cl - 1, pre.ml - 1, 'r', pre.cr + 1, pre.mr + 1)
        if post.is_valid():
            post.p = pre
            c.append(post)
        post = State(pre.cl, pre.ml - 1, 'r', pre.cr, pre.mr + 1)
        if post.is_valid():
            post.p = pre
            c.append(post)
        post = State(pre.cl - 1, pre.ml, 'r', pre.cr + 1, pre.mr)
        if post.is_valid():
            post.p = pre
            c.append(post)

    else:
        post = State(pre.cl, pre.ml + 2, 'l', pre.cr, pre.mr - 2)

        if post.is_valid():
            post.p = pre
            c.append(post)
        post = State(pre.cl + 2, pre.ml, 'l', pre.cr - 2, pre.mr)
        if post.is_valid():
            post.p = pre
            c.append(post)
        post = State(pre.cl + 1, pre.ml + 1, 'l', pre.cr - 1, pre.mr - 1)
        if post.is_valid():
            post.p = pre
            c.append(post)
        post = State(pre.cl, pre.ml + 1, 'l', pre.cr, pre.mr - 1)
        if post.is_valid():
            post.p = pre
            c.append(post)
        post = State(pre.cl + 1, pre.ml, 'l', pre.cr - 1, pre.mr)
        if post.is_valid():
            post.p = pre
            c.append(post)

    return c


# Breadth First Search function for Missionaries and Cannibles Problem
def bfs():
    initial_state = State(3, 3, 'l', 0, 0)

    if initial_state.is_goal():
        return initial_state, initial_state

    frontier = list()
    explored = set()
    nodes_visited = list()
    frontier.append(initial_state)

    while frontier:
        state = frontier.pop(0)
        if state.is_goal():
            explored.add(state)
            nodes_visited.append(state)
            return state, nodes_visited
        explored.add(state)
        if state not in nodes_visited:
            nodes_visited.append(state)
        c = successors(state)
        for child in c:
            if (child not in explored) or (child not in frontier):
                frontier.append(child)
    return None



# Depth First Search function for Missionaries and Cannibles Problem
def dfs():
    initial_state = State(3, 3, 'l', 0, 0)

    if initial_state.is_goal():
        return initial_state, initial_state

    queue = list()
    explored = set()
    nodes_visited = list()
    queue.append(initial_state)

    while queue:
        state = queue.pop(0)
        if state.is_goal():
            explored.add(state)
            nodes_visited.append(state)
            return state, nodes_visited
        explored.add(state)
        if state not in nodes_visited:
            nodes_visited.append(state)
        c = successors(state)
        for child in c:
            if (child not in explored) and (child not in queue):
                queue.insert(0, child) # inserting a child node on the start of the queue

    return None


# Function to print the complete path followed to get to the goal state
def print_solution(solution):
    path = []
    path.append(solution)
    prev_state = solution.p
    while prev_state:
        path.append(prev_state)
        prev_state = prev_state.p

    for t in range(len(path)):
        state = path[len(path) - t - 1]
        print(str(state.cl) + ", " + str(state.ml) + ", " + state.boat + ", " + str(state.cr) + ", " + str(state.mr))



def print_Nodes_Visisted(visited_path):
    for visited_node in visited_path:
        print(str(visited_node.cl) + ", " + str(visited_node.ml) + ", " + visited_node.boat + ", " + str(visited_node.cr) + ", " + str(visited_node.mr))


# Main function
def main():

    print()

    solution, visited_path = bfs()
    print("Solution Path through BFS: ")
    print_solution(solution)
    print()
    print()
    print("Nodes Visited by BFS: ")
    print_Nodes_Visisted(visited_path)

    print()
    print()
    solution, visited_path = dfs()
    print("Solution Path through DFS: ")
    print_solution(solution)
    print()
    print()
    print("Nodes Visited by DFS: ")
    print_Nodes_Visisted(visited_path)

# main function is called
main()
