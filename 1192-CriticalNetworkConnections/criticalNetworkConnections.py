class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        # Initialize the 'discovery time' and 'low time' arrays to keep track of the earliest
        # visited vertex (ancestor) that can be reached from a vertex.
        discovery_time = [0] * n
        low_time = [0] * n
        # The current time count used for both discovery_time and low_time values.
        current_time = 0
        # This array will hold the result: a list of critical connections.
        critical_connections = []

        def tarjan_dfs(vertex: int, parent: int):
            ''' Utility function to perform the Tarjan's DFS algorithm.
                Arguments:
                    vertex : the current vertex being explored.
                    parent : the predecessor vertex of the current vertex in the DFS tree.
            '''
            # We have access to the outer scope's "current_time" variable.
            nonlocal current_time
            # Increment the current discovery time.
            current_time += 1
            # Initialize the discovery time and low value for the current vertex.
            discovery_time[vertex] = low_time[vertex] = current_time
            # Iterate through all the connected vertices of the current vertex.
            for neighbor in graph[vertex]:
                # Skip the exploration of the edge leading back to the parent vertex.
                if neighbor == parent:
                    continue
                if not discovery_time[neighbor]:
                    # The neighbor has not been visited, so we run tarjan_dfs on it.
                    tarjan_dfs(neighbor, vertex)
                    # Update the low_time for the current vertex with the value from the neighbor if it's smaller.
                    low_time[vertex] = min(low_time[vertex], low_time[neighbor])
                    # If the low time value of the neighbor is greater than the discovery time of the current vertex,
                    # it means that no back edge exists and hence, it is a critical connection.
                    if low_time[neighbor] > discovery_time[vertex]:
                        critical_connections.append([vertex, neighbor])
                else:
                    # If the neighbor was already visited, update the low_time of the current vertex.
                    low_time[vertex] = min(low_time[vertex], discovery_time[neighbor])
        # Construct the graph as an adjacency list from the list of connections.
        graph = [[] for _ in range(n)]
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
        # Perform Tarjan's algorithm starting from the first vertex.
        tarjan_dfs(0, -1)
        return critical_connections


def main():
    solution = Solution()
    print(solution.criticalConnections([[0, 1], [1, 2], [2, 0], [1, 3]]))
    print(solution.criticalConnections([[0, 1]]))


if __name__ == "__main__":
    main()
