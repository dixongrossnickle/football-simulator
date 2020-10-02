class Player:

    def __init__(self, name, club_name, position, nationality, overall, finishing, aggression):
        self.name = str(name)
        self.club_name = str(club_name)
        self.position = str(position)
        self.nationality = str(nationality)
        self.overall = int(overall)
        self.finishing = int(finishing)
        self.aggression = int(aggression)
        # goal_prob & foul_prob are multiplied based on position for more accurate probabilities
        self.goal_prob = int(finishing)
        self.foul_prob = int(aggression)
        self.match_stats = {}

    def get_attributes(self):
        return {
            'name': self.name,
            'clubName': self.club_name,
            'position': self.position,
            'nationality': self.nationality,
            'overall': self.overall,
            'finishing': self.finishing,
            'aggression': self.aggression,
        }
