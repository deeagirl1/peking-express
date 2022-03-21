# a class to define the path of the player
class Player:
    path = []
    spent = 0

    # Declare player's start location
    def __init__(self, start_location):
        self.path = [start_location]
