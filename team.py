from .player import Player
from . import MATCH_DF, FIFA_DF, TEAM_NAMES

class Team:

    # Populate roster, append player's event probs to lists, and calculate goals mean & SD
    def __init__(self, club_id, side):
        self.club_id = club_id
        self.club_name = TEAM_NAMES[club_id]
        self.side = side
        self.roster = []
        self.starting_XI = {}
        self.team_probs = {'scoring_probs': [], 'foul_probs': []}
        self.populate_roster()
        self.append_probs()
        self.calc_goals()


    # Create new dataframe for specific team; Drop subs, reserves, and GKs
    # Add position-based multipliers – need more disparity in scoring probabilities
    def populate_roster(self):
        df = FIFA_DF.loc[FIFA_DF['club_id'] == self.club_id, ['short_name', 'team_position', 'nationality', 'overall', 'attacking_finishing', 'mentality_aggression']]
        df = df[~df['team_position'].isin(['SUB','RES'])].reset_index(drop=True)
        for i in range(len(df)):
            player = Player(df.iloc[i,0], self.club_name, df.iloc[i,1], df.iloc[i,2], df.iloc[i,3], df.iloc[i,4], df.iloc[i,5])
            if player.position in ('ST','RS','LS','CF','LF','RF'):
                player.goal_prob = (player.goal_prob*2.8) + player.overall
            elif player.position in ('RW','LW','RM','LM','CAM'):
                player.goal_prob = (player.goal_prob*2) + player.overall
            elif player.position in ('CB','RCB','LCB','LB','RB','CDM','RDM','LDM'):
                player.foul_prob *= 3
            self.starting_XI[i+1] = player.get_attributes()
            # Roster (used in event assignment/probabilities) should not have GK - they get picked too often
            if player.position != 'GK':
                self.roster.append(player)


    # --- Append finishing / aggression ratings to probabilities lists (used to assign match events)
    def append_probs(self):
        for player in self.roster:
            self.team_probs['scoring_probs'].append(player.goal_prob)
            self.team_probs['foul_probs'].append(player.foul_prob)


    # --- Calculate means and SD's of goals for & against
    def calc_goals(self):
        if self.side == 'home':
            df = MATCH_DF[MATCH_DF['HomeID'] == self.club_id]
            self.mean_GF = df.FTHG.mean()
            self.std_GF = df.FTHG.std()
            self.mean_GA = df.FTAG.mean()
            self.std_GA = df.FTAG.std()
        elif self.side == 'away':
            df = MATCH_DF[MATCH_DF['AwayID'] == self.club_id]
            self.mean_GF = df.FTAG.mean()
            self.std_GF = df.FTAG.std()
            self.mean_GA = df.FTHG.mean()
            self.std_GA = df.FTHG.std()