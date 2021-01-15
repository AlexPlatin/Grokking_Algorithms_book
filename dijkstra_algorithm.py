class AlgorithmDijkstra:
    def __init__(self):
        self.graph = {}
        self.costs = {}
        self.parents = {}
        self.closed_nodes = list()

    def set_graph(self) -> None:
        """
        Set up graph
        :return:
        """
        self.graph["start"] = {}
        self.graph["start"]["B"] = 2
        self.graph["start"]["A"] = 6
        self.graph["B"] = {}
        self.graph["B"]["A"] = 3
        self.graph["B"]["fin"] = 5
        self.graph["A"] = {}
        self.graph["A"]["fin"] = 1
        self.graph["fin"] = {}

    def set_costs_table(self) -> None:
        """
        Set up cost table with costs from start node
        :return:
        """
        self.costs["B"] = 2
        self.costs["A"] = 6
        self.costs["fin"] = float("inf")

    def set_parents_table(self) -> None:
        """
        Set up parents table with parents from start node
        :return:
        """
        self.parents["A"] = "start"
        self.parents["B"] = "start"
        self.parents["fin"] = None

    def _find_lowest_cost_node(self) -> str:
        """
        Find node with lowest way cost
        :return:
        """
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in self.costs:
            cost = self.costs[node]
            if cost < lowest_cost and node not in self.closed_nodes:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    def calculate_best_way(self) -> int:
        """
        Find best wat from start node to fin node
        :return:
        """
        node = self._find_lowest_cost_node()
        while node:
            cost = self.costs[node]
            neighbors = self.graph[node]
            for neighbor in neighbors.keys():
                node_cost = cost + neighbors[neighbor]
                if self.costs[neighbor] > node_cost:
                    self.costs[neighbor] = node_cost
                    self.parents[neighbor] = node
            self.closed_nodes.append(node)
            node = self._find_lowest_cost_node()

        return self.costs["fin"]

    def best_way(self):
        way_list = list()
        node = "fin"
        way_list.append(node)
        try:
            while True:
                node = self.parents[node]
                way_list.append(node)
        except KeyError:
            print("Minimum cost - " + str(self.costs["fin"]) + ", path nodes: " + ", ".join(way_list))


if __name__ == '__main__':
    dijkstra = AlgorithmDijkstra()
    dijkstra.set_graph()
    dijkstra.set_parents_table()
    dijkstra.set_costs_table()
    dijkstra.calculate_best_way()
    dijkstra.best_way()
