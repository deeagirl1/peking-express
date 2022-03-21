class Player:
    path = []  # path player has to follow
    spent = 0  # variable used to check if we exceed the budget or not

    # Declare player's start location
    def __init__(self, start_location):
        self.path = [start_location]
