from ballot import Ballot

from typing import TextIO
from typing import NamedTuple
from typing import List

class CandidateRanking(NamedTuple):
  name: str
  ranking: str

class CSVParser():
  def __init__(self, file_name: str):
    with open(file_name, "r") as self.csv_file:
      first_line = self.csv_file.readline()
      self._candidate_names = self._parse_candidate_names(first_line)
      self._ballots = self._parse_ballots()
    print(len(self._candidate_names))
    print(self.candidate_names)

  @property
  def candidate_names(self) -> List[str]:
    return self._candidate_names

  @property
  def ballots(self) -> List[Ballot]:
    return self._ballots

  def _parse_candidate_names(self, line : str):
    return set(line.strip().split(','))

  def _parse_ballots(self) -> List[Ballot]:
    return [self._parse_ballot(line) 
              for line in self.csv_file 
                if not line.isspace()]

  def _parse_ballot(self, line: str) -> Ballot:
    return self._create_ballot(self._parse_candidate_rankings(line))

  def _parse_candidate_rankings(self, line : str) -> List[CandidateRanking]:
    return [CandidateRanking(*(item.split(':'))) 
            for item in line.strip().split(',')]

  def _create_ballot(self, candidate_rankings:List[CandidateRanking]) -> Ballot:
    rankings = {candidate_ranking.name : int(candidate_ranking.ranking) 
                for candidate_ranking in candidate_rankings
                  if self._is_valid(candidate_ranking)}
    return Ballot(rankings)

  def _is_valid(self, candidate_ranking: CandidateRanking) -> bool:
    x = candidate_ranking.name in self._candidate_names
    y = self._rank_is_valid(candidate_ranking)
    return y and x

  def _rank_is_valid(self, candidate_ranking : CandidateRanking) -> bool:
    """Check rank is valid : not negative and not greater than number of candidates"""
    rank = int(candidate_ranking.ranking)
    return rank >= 0 and rank < len(self._candidate_names)