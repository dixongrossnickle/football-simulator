import random as rnd

class MatchUp:

    def __init__(self, Team1, Team2):
        self.Team1 = Team1
        self.Team2 = Team2
        self.events = {}
        self.results = {}

    # Simulate single game
    #   - Get average of 2 random values from Gaussian distributions of a team's goals for & goals conceded
    def sim(self):
        events_list = []
        home_team_goals = int(round((rnd.gauss(self.Team1.mean_GF,self.Team1.std_GF) + rnd.gauss(self.Team2.mean_GA,self.Team2.std_GA)) / 2))
        away_team_goals = int(round((rnd.gauss(self.Team2.mean_GF,self.Team2.std_GF) + rnd.gauss(self.Team1.mean_GA,self.Team1.std_GA)) / 2))
        events_list.append(home_team_goals) #[0]
        events_list.append(away_team_goals) #[1]
        # Weighted selection for red cards (prob's remain the same each time) -- this is a rough estimation arrived at through testing
        home_red_cards = rnd.choices((0,1), weights=[0.97, 0.03], k=1)[0]
        away_red_cards = rnd.choices((0,1), weights=[0.97, 0.03], k=1)[0]
        events_list.append(home_red_cards) #[2]
        events_list.append(away_red_cards) #[3]
        # Set neg. number to 0 (may occur due to avg. of goals scored + goals against)
        for i in range(4):
            if events_list[i] < 0:
                events_list[i] = 0
        # Determine match result
        if events_list[0] > events_list[1]:
            result = 'home win'
        elif events_list[0] < events_list[1]:
            result = 'away win'
        else:
            result = 'draw'
        # Update match results dictionary
        self.results.update({
            'result': result,
            'homeTeamGoals': events_list[0],
            'awayTeamGoals': events_list[1]
        })
        # Assign players to events using finishing & aggression as probabilities
        poss_mins = list(range(2,95))
        self.assign_events(self.Team1, events_list[0], events_list[2], poss_mins)
        self.assign_events(self.Team2, events_list[1], events_list[3], poss_mins)


    # --- Choose weighted random choice from roster to determine match events
    def assign_events(self, Team, goals, reds, poss_mins):
        for _ in range(goals):
            player = rnd.choices(Team.roster, weights=Team.team_probs['scoring_probs'], k=1)[0]
            minute = rnd.choice(poss_mins)
            while minute-1 in self.events or minute+1 in self.events:
                minute = rnd.choice(poss_mins)
            poss_mins.remove(minute)
            player.match_stats[minute] = 'goal'
            self.events[minute] = {
                'event': 'goal',
                'team': Team.club_name,
                'player': player.name
            }
        for _ in range(reds):
            player = rnd.choices(Team.roster, weights=Team.team_probs['foul_probs'], k=1)[0]
            minute = rnd.choice(poss_mins)
            # Cannot get red card before another event - assign a new minute
            if len(player.match_stats) > 0:
                #   Can't get a second red card - choose a different player
                #   Currently disabled – can only get 0 or 1 red cards
                # ---------------------------------------------------------------
                # while 'Red Card' in player.match_stats.values():
                #     player = rnd.choices(Team.roster, weights=Team.team_probs['foul_probs'], k=1)[0]
                # ---------------------------------------------------------------
                most_recent_event = max(player.match_stats.keys())
                i = 0
                while minute <= most_recent_event:
                    minute = rnd.choice(poss_mins)
                    # Failsafe — prevent looping too long if player scored in last minutes
                    i += 1
                    if i > 50:
                        minute = 96
                        poss_mins.append(96)
            poss_mins.remove(minute)
            player.match_stats[minute] = 'red card'
            self.events[minute] = {
                'event': 'red card',
                'team': Team.club_name,
                'player': player.name
            }
