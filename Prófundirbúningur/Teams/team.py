from typing import Any
from player import Player
class Team(Player):
    def __init__(self, team):
        self.team = team
        self.players = []
    
    def add_player(self, players):
        self.players.append(players)
    
    def most_goals_player(self):
        all_goals = sorted(self.players, key=lambda p: p.goals, reverse=True)
        return all_goals[0] if all_goals else None

    def __add__(self, other):
        combined_team = Team(self.team+"+"+other.team)
        combined_team.players = self.players + other.players
        return combined_team

    def __str__(self):
        result = f"{self.team}:"
        
        for player in sorted(self.players, key=lambda p: p.goals, reverse=True):
            result += f"\n\t{player}"

        return result