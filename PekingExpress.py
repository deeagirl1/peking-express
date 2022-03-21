from Player import Player
from Graph import Graph



class PekingExpress:
    budget = 0
    occupiedLocations = []
    currentTurn = 1
    player = None

    # Read the input map, which is provided in Json format.
    def __init__(self, json_map):
        self.source = json_map['Connections']['source']
        self.startLocation = json_map['StartLocation']
        self.pekingMap = initializeGame(json_map, self.source)
        self.player = Player(self.startLocation)
        self.budget = json_map['Budget']
        self.occupiedLocations = json_map['OccupiedLocationsAfterEachTurn']

    # After each move, we update the currently occupied locations, by adding the player's move.
    def update_occupied_locations(self):
        if len(self.occupiedLocations) > self.currentTurn:
            self.occupiedLocations[self.currentTurn] += [self.player.path[-1]]
        else:
            self.occupiedLocations += [[self.player.path[-1]]]

    # Compute player's next move
    def next_move(self):

        # Calculate all paths to destination from current location.
        solution = self.calculate_best_solution((None, None), self.currentTurn, [self.player.path[-1]],
                                                self.player.spent)

        # Price for each vertex is added to "spent"
        if solution[1] is not None and solution[1][0] != solution[1][1]:
            self.player.spent += self.pekingMap.get_vertex(solution[1][0]).weight(solution[1][1])

        # Return next point in shortest path to location.
        if solution[1] is not None:
            return solution[1][1]

        return None

    def calculate_best_solution(self, solution, turn, path, spent) -> tuple:

        # If destination reached, add path and amount spent to solutions.
        if path[-1] == 88 and spent <= self.budget:
            # Check if the solution is better, if yes, then update the solution.
            if solution[1] is None or len(path) < len(solution[1]) or (
                    len(solution[1]) == len(path) and solution[0] > spent):
                solution = (spent, path)
        # Else "spent" is below the budget.
        elif spent < self.budget and (solution[1] is None or len(path) < len(solution[1])):
            # Get adjacent vertices.
            options = self.pekingMap.get_vertex(path[-1]).get_neighbours()
            # Player can stay on the same location if any of the next options are occupied and vital.
            if turn <= len(self.occupiedLocations):
                for option in options:
                    if option in self.occupiedLocations[turn - 1] and self.pekingMap.get_vertex(option).critical:
                        options = options + [path[-1]]
                        break
            # If it's not occupied and vital continue path.
            for option in options:
                if turn > len(self.occupiedLocations) or (
                        not (self.pekingMap.get_vertex(option).critical and option in self.occupiedLocations[turn - 1])):
                    price = self.pekingMap.get_vertex(path[-1]).weight(option) if option != path[-1] else 0
                    solution = self.calculate_best_solution(solution, turn + 1, path + [option], spent + price)
        return solution

    #  While trying to reach 88, we calculate a next move.
    def solve(self):
        if self.startLocation not in self.source:
            return None
        while self.player.path[-1] != 88:
            n = self.next_move()
            if n is None:
                self.player.path += ['Could not find full path.']
                break
            self.player.path += [n]
            self.update_occupied_locations()
            self.currentTurn += 1

    def get_path(self):
        return self.player.path

    def get_path_weight(self):
        return sum([self.pekingMap.get_vertex(i).weight(i + 1) for i in range(len(self.get_path()))])


def initializeGame(json_map, source):
    target = json_map['Connections']['target']
    price = json_map['Connections']['price']
    critical = json_map['Locations']['critical']
    n = len(source)

    peking_map = Graph()

    # Fill in the graph with values.
    for i in range(n):
        peking_map.add_edge(source[i], target[i], price[i])

    for i in critical:
        peking_map.update_critical(i)

    return peking_map
