from collections import deque
from heapq import heappop, heappush
from math import inf
import GUICode
from PyQt5 import QtWidgets

class Graph:
    def __init__(self, directed=True):
        self.edges = {}
        self.huristics = {}
        self.directed = directed

    def add_edge(self, node1, node2, __reversed=False):
        try: neighbors = self.edges[node1]
        except KeyError: neighbors = set()
        neighbors.add(node2)
        self.edges[node1] = neighbors
        if not self.directed and not __reversed: self.add_edge(node2, node1, True)

    def add_edge_g_A(self, node1, node2, cost=1, __reversed=False):
        try:
            neighbors = self.edges[node1]
        except KeyError:
            neighbors = {}
        neighbors[node2] = cost
        self.edges[node1] = neighbors
        if not self.directed and not __reversed: self.add_edge_g_A(node2, node1, cost, True)

    def set_huristics(self, huristics={}):
        self.huristics = huristics

    def add_edge_ucs(self, node1, node2, cost=1, __reversed=False):
        try:
            neighbors = self.edges[node1]
        except KeyError:
            neighbors = {}
        neighbors[node2] = cost
        self.edges[node1] = neighbors
        if not self.directed and not __reversed: self.add_edge_ucs(node2, node1, cost, True)

    def cost_ucs(self, node1, node2):
        try:
            return self.edges[node1][node2]
        except:
            return inf

    def neighbors(self, node):
        try: return self.edges[node]
        except KeyError: return []

    def cost(self, node1, node2):
        try:
            return self.edges[node1][node2]
        except:
            return inf

    def deapth_first_search(self, start, setOfGoal):
        found, fringe, visited, came_from = False, deque([start]), set([start]), {start: None}
        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------')
        print('{:11s} | {}'.format('-', start))
        while not found and len(fringe):
            current = fringe.pop()
            print('{:11s}'.format(current), end=' | ')
            if current in setOfGoal:
                found = True
                goal = current;
                break
            for node in self.neighbors(current):
                if node not in visited: visited.add(node); fringe.append(node); came_from[node] = current
            print(', '.join(fringe))
        if found:
            print(); return came_from,goal,visited
        else:
            print('No path from {} to {}'.format(start, goal))


    def breadth_first_search(self, start, setOfGoals):
        found, fringe, visited, came_from = False, deque([start]), set([start]), {start: None}
        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------')
        print('{:11s} | {}'.format('-', start))
        while not found and len(fringe):
            current = fringe.pop()
            print('{:11s}'.format(current), end=' | ')
            if current in setOfGoals:
                found = True
                goal = current;
                break
            for node in self.neighbors(current):
                if node not in visited: visited.add(node); fringe.appendleft(node); came_from[node] = current
            print(', '.join(fringe))
        if found:
            print(); return came_from, goal,visited
        else:
            print('No path from {} to {}'.format(start, goal))

    def uniform_cost_search(self, start, setOfGoals=None):
        found, fringe, visited, came_from, cost_so_far = False, [(0, start)], set([start]), {start: None}, {start: 0}
        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------')
        print('{:11s} | {}'.format('-', str((0, start))))
        while not found and len(fringe):
            _, current = heappop(fringe)
            print('{:11s}'.format(current), end=' | ')
            if current in setOfGoals:
                found = True
                goal=current; break
            for node in self.neighbors(current):
                new_cost = cost_so_far[current] + self.cost(current, node)
                if node not in visited or cost_so_far[node] > new_cost:
                    visited.add(node); came_from[node] = current; cost_so_far[node] = new_cost
                    heappush(fringe, (new_cost, node))
            print(', '.join([str(n) for n in fringe]))
        if found: print(); return came_from, cost_so_far[goal],goal,visited
        else: print('No path from {} to {}'.format(start, goal)); return None, inf

    def depth_limited_search(self, start, setOfGoals=None, limit=-1):
     print('Depth limit =', limit)
     found, fringe, visited, came_from = False, deque([(0, start)]), set([start]), {start: None}
     print('{:11s} | {}'.format('Expand Node', 'Fringe'))
     print('--------------------')
     print('{:11s} | {}'.format('-', start))
     while (not (found)) and len(fringe):
        depth, current = fringe.pop()
        print('{:11s}'.format(current), depth,end=' | ')
        if current in setOfGoals:
            found = True
            goal = current
            break
        if limit == -1 or depth < limit:
            for node in self.neighbors(current):
                if node not in visited:
                    visited.add(node)
                    fringe.append((depth + 1, node))
                    came_from[node] = current
        print(', '.join([n for _, n in fringe]))
        print(len(fringe))
     if found:
        print(); return came_from, visited
     else:
        print('No path from {} to {}'.format(start, setOfGoals))
        return None, visited

    def iterative_deepening_dfs(self, start, setOfGoals=None):
        prev_iter_visited, depth,traced_path = [], 0,{start: None}
        while True:
            traced_path, visited = self.depth_limited_search(start, setOfGoals, depth)
            if traced_path or len(visited) == len(prev_iter_visited):
                goal=list(traced_path.keys())[-1]
                return traced_path,goal,visited
            else:
                prev_iter_visited = visited
                depth += 1

    def aStarSearch(self, start, setOfGoals):
        found, fringe, visited, came_from, cost_so_far = False, [(self.huristics[start], start)], set([start]), {
            start: None}, {start: 0}
        goal = 0
        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------')
        print('{:11s} | {}'.format('-', str(fringe[0])))
        while not found and len(fringe):
            _, current = heappop(fringe)
            print('{:11s}'.format(current), end=' | ')
            if current in setOfGoals:
                found = True
                goal = current;
                break
            for node in self.neighbors(current):
                new_cost = cost_so_far[current] + self.cost(current, node)
                if node not in visited or cost_so_far[node] > new_cost:
                    visited.add(node);
                    came_from[node] = current;
                    cost_so_far[node] = new_cost
                    heappush(fringe, (new_cost + self.huristics[node], node))
            print(', '.join([str(n) for n in fringe]))
        if found:
            print(); return came_from, cost_so_far[goal], goal,visited
        else:
            print('No path from {} to {}'.format(start, goal)); return None, inf

    def greedy_search(self, start, setOfGoals):
        found, fringe, visited, came_from, cost_so_far = False, [(self.huristics[start], start)], set([start]), {
            start: None}, {start: 0}
        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------')
        print('{:11s} | {}'.format('-', str(fringe[0])))
        while not found and len(fringe):
            _, current = heappop(fringe)
            print('{:11s}'.format(current), end=' | ')
            if current in setOfGoals:
                found = True
                goal = current
                break
            for node in self.neighbors(current):
                new_cost = cost_so_far[current] + self.cost(current, node)
                if node not in visited or cost_so_far[node] > new_cost:
                    visited.add(node)
                    came_from[node] = current
                    cost_so_far[node] = new_cost
                    heappush(fringe, (self.huristics[node], node))
            print(', '.join([str(n) for n in fringe]))
        if found:
            print()
            return came_from, cost_so_far[goal], goal,visited
        else:
            print('No path from {} to {}'.format(start, goal));
            return None, inf


    @staticmethod
    def print_path(came_from, goal):
        parent = came_from[goal]
        if parent:
            Graph.print_path(came_from, parent)
        else: print(goal, end='');return
        print(' =>', goal, end='')


    def __str__(self):
        return str(self.edges)