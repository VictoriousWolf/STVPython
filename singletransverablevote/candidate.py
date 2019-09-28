from ballot import Ballot
from typing import List, Dict

class NoCandidatesLeft(Exception):
  pass

CandidateDict = Dict[str, 'Candidate']

class Candidate():
  """Candidates"""
  def __init__(self, name):
      """Initialize candidate."""
      self._name : str= name
      self._ballots : List[Ballot] = []
      self._votes : float = 0.0
      self._eliminated : bool = False
  
  def add_ballot(self, ballot):
      self.ballots.append(ballot)
      self._votes = self.votes + ballot.voteValue

  @property
  def name(self) -> str:
    return self._name

  @property
  def votes(self) -> float:
    return self._votes

  @property
  def ballots(self) -> List[Ballot]:
    return self._ballots

  @property
  def eliminated(self):
    return self._eliminated

  @property
  def not_eliminated(self):
    return not self._eliminated

  def eliminate(self, quota: int, candidates: CandidateDict):
    print(self.name + " is elimiated and to redistribute")
    self._eliminated = True;
    self.redistribute_ballots(quota, candidates)


  def redistribute_ballots(self, quota : int , candidates : CandidateDict):
    self._assign_ballots_to_next_ranked_candidates(quota, candidates)
    # Ballots have been reassigned so must be cleared
    self.ballots.clear()
    self._votes = 0 if self.eliminated else quota

  def _assign_ballots_to_next_ranked_candidates(self,quota: int , candidates : CandidateDict):
    surplus_factor = 1 if self.eliminated else self._calculate_surplus_factor(quota) 
    for ballot in self.ballots:
      ballot.apply_surplus_factor(surplus_factor)
      try:
        next_candidate = self._get_next_not_elimated_candidate(ballot,candidates)
        self._re_assign_ballot(ballot, next_candidate)
      except NoCandidatesLeft:
        print("No candidates left not eliminated to assign ballot to")

  def _calculate_surplus_factor(self, quota : float):
    return (self.votes - quota) /  self.votes

  def _get_next_not_elimated_candidate(self, ballot : Ballot, candidates : CandidateDict):
    next_rank = ballot.rankings[self.name] + 1
    max_rank = len(ballot.rankings)
    valid = False
    while not valid:
      next_candidate = self._get_next_candidate(ballot, next_rank, candidates)
      valid = next_candidate.not_eliminated
      next_rank += 1      
      if (next_rank > max_rank): raise NoCandidatesLeft
    return next_candidate

  def _get_next_candidate(self, ballot : Ballot, next_rank: int, candidates : CandidateDict):
    try:
      return next((candidates[name] 
                  for name, rank in ballot.rankings.items() 
                    if rank == next_rank))
    except StopIteration:
      raise NoCandidatesLeft    

  def _re_assign_ballot(self, ballot : Ballot, next_candidate : 'Candidate'):
      ballot.rankings.pop(self.name)
      next_candidate.add_ballot(ballot)



    