from collections import deque

class Graph:
    def __init__(self):
        self.serach_queue = deque()
        self.searched = []

    def make_graf(self):
        self.graph = dict()
        self.graph["I"] = ["Vanya", "Alina"]
        self.graph["Alina"] = ["Vasya", "Larisa"]
        self.graph["Vasya"] = []
        self.graph["Larisa"] = []
        self.graph["Vanya"] = ["Yulia", "Dima"]
        self.graph["Yulia"] = ["Maksim"]
        self.graph["Maksim"] = []
        self.graph["Dima"] = ["Fedya", "Natasha"]
        self.graph["Fedya"] = []
        self.graph["Natasha"] = []

    def make_deque(self):
        self.serach_queue += self.graph["I"]

    def _know_english(self, person):
        if person[-2] == "h":
            return True

    def search(self):
        while self.serach_queue:
            person = self.serach_queue.popleft()
            if person not in self.searched:
                if self._know_english(person):
                    print("Person is {}".format(person))
                    return person
                self.serach_queue += self.graph[person]
                self.searched.append(person)
        return None

if __name__ == '__main__':
    grapg = Graph()
    grapg.make_graf()
    grapg.make_deque()
    grapg.search()