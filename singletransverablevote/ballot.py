from typing import Dict

class Ballot:
    """Ballot"""
    def __init__(self, rankings):
        self.rankings : Dict[str,int] = rankings
        self.voteValue : int = 1

    def apply_surplus_factor(self, surplus_factor):
      self.voteValue = self.voteValue * surplus_factor