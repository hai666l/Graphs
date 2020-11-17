from collections import deque # This may come in handy

class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        # v = visited, q = queue, c = current node
        v = set()
        q = deque()
        q.append(starting_vertex)
        while len(q) > 0:
            c = q.popleft()

            if c not in v:
                print(c)
                v.add(c)
                for edge in self.vertices[c]:
                    q.append(edge)

    def dft(self, starting_vertex):
        # v = visited, s = stack, c = current node
        v = set()
        s = deque()
        s.append(starting_vertex)
        while len(s) > 0:
            c = s.pop()

            if c not in v:
                print(c)
                v.add(c)
                for edge in self.vertices[c]:
                    s.append(edge)

    def dft_recursive(self, starting_vertex):
        v = set()
        self.dft_recursive_helper(starting_vertex, v)

    def dft_recursive_helper(self, curr_vertex, v):
        print(curr_vertex)
        v.add(curr_vertex)

        for edge in self.vertices[curr_vertex]:

            if edge not in v:
                self.dft_recursive_helper(edge, v)

    def bfs(self, starting_vertex, destination_vertex):
        v = set()
        q = deque()
        q.append([starting_vertex])

        while len(q) > 0:
            cPath = q.popleft()
            cNode = cPath[-1]

            if cNode == destination_vertex:
                return cPath

            if cNode not in v:
                v.add(cNode)

                for edge in self.vertices[cNode]:
                    newPath = list(cPath)
                    newPath.append(edge)
                    q.append(newPath)
        return []

    def dfs(self, starting_vertex, destination_vertex):
        s = deque()
        s.append([starting_vertex])
        v = set()

        while len(s) > 0:
            cPath = s.pop()
            cNode = cPath[-1]

            if cNode == destination_vertex:
                return cPath

            if cNode not in v:
                v.add(cNode)

                for edge in self.vertices[cNode]:
                    newPath = list(cPath)
                    newPath.append(edge)
                    s.append(newPath)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        v = set()
        return self.dfs_recursive_helper([starting_vertex], destination_vertex, v)

    def dfs_recursive_helper(self, cPath, destination_vertex, v):
        cVertex = cPath[-1]
        if cVertex == destination_vertex:
            return cPath

        v.add(cVertex)

        for edge in self.vertices[cVertex]:
            if edge not in v:
                newPath = list(cPath)
                newPath.append(edge)
                res = self.dfs_recursive_helper(newPath, destination_vertex, v)
                if len(res) > 0:
                    return res
        return []
