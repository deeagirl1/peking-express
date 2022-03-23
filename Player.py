class Player:

    # Declare player's start location
    def __init__(self, start_location):
        self.path = [start_location]  # path player has to follow
        self.spent = 0  # variable used to check if we exceed the budget or not
