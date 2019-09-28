import sys

from typing import List, Dict, Tuple, Set

from ballot import Ballot
from candidate import Candidate, CandidateDict
from csv_parser import CSVParser

NUMBER_OF_SEATS = 3
INPUT_FILE = "test/stvExample.csv"
MAX_ITERATIONS = 1000

def main():
  for x in sys.argv:
    print(x)
    
  ballots , candidate_names = get_ballots_and_names_from(INPUT_FILE)
  for ballot in ballots:
      print(ballot.rankings)

  candidates = assign_ballots_to_candidates(ballots, candidate_names)
  for name, cand in candidates.items():
      print(name + " "+ str(cand.votes))
  print("")

  quota = calculate_droop_quota(ballots, NUMBER_OF_SEATS)
  print(f"Candidates must reach {quota} votes")

  winners = determine_winners(quota,candidates)

  print("Final Winners:")
  for winner in winners:
    print(winner.name)

# Private 
def get_ballots_and_names_from(file_name : str) -> Tuple[List[Ballot],List[str]]:
  parser = CSVParser(file_name)
  return (parser.ballots,parser.candidate_names)

def determine_winners(quota: int, candidates : CandidateDict):
  seats = checkForWinners(set(), candidates, quota)
  iteration = 0
  while (seats_not_filled(seats) and iteration < MAX_ITERATIONS):
      re_distribute_ballots(candidates, quota)
      seats = checkForWinners(seats, candidates, quota)
      iteration += 1
  return seats

def re_distribute_ballots(candidates, quota):
  try:
    surplus_candidate = get_candidiate_with_biggest_surplus(candidates,quota)
    print(surplus_candidate.name + " has surplus to redistribute")
    surplus_candidate.redistribute_ballots(quota, candidates)        
    printVotes(candidates)
  except NoSurplus:
    candidate_to_elimate = get_candidiate_with_least_votes(candidates)
    candidate_to_elimate.eliminate(quota, candidates)
    printVotes(candidates)

def seats_not_filled(seats : Set[Candidate]):
  return len(seats) < NUMBER_OF_SEATS


def calculate_droop_quota(ballots : List[Ballot], number_of_seats: int):
  return (len(ballots)/ (number_of_seats + 1)) + 1    

def assign_ballots_to_candidates(ballots : List[Ballot], 
                                  candidate_names : str) -> Dict[str,Candidate]:
  candidates = { name : Candidate(name) for name in candidate_names}
  for ballot in ballots:
    top_candidate = get_highest_ranked_candidate(ballot)
    candidates[top_candidate].add_ballot(ballot)
  return candidates  

def get_highest_ranked_candidate(ballot : Ballot) -> str:
  highest_rank = sys.maxsize
  top_candidate = "RON"
  for cand , rank in ballot.rankings.items():
      if (rank < highest_rank):
        top_candidate ,highest_rank = cand, rank
  return top_candidate  

def checkForWinners(seats : Set[Candidate], candidates : CandidateDict, quota: float):
    for name, candidate in candidates.items():
        if candidate.votes > quota:
            seats.add(candidate);
    return seats

def there_is_a_surplus_of_votes(candidates : CandidateDict, quota: float):
    for name, candidate in candidates.items():
        if candidate.votes > quota:
            return True;
    else:
      return False;

def get_candidiate_with_biggest_surplus(candidates:CandidateDict, quota: float):
    max = 0;
    for name, candidate in candidates.items():
        if candidate.votes > quota and candidate.votes > max:
            max = candidate.votes
            candidiate_with_biggest_surplus = candidate

    if max == 0:
      raise NoSurplus
    else:
      return candidiate_with_biggest_surplus

def get_candidiate_with_least_votes(candidates: CandidateDict):
    min = sys.maxsize
    for name, candidate in candidates.items():
        if ((candidate.votes < min) and candidate.not_eliminated):
            candidate_to_elimate = candidate
            min = candidate.votes
    return candidate_to_elimate


    
class NoSurplus(Exception):
   pass


def printVotes(candidates):
    #Debug Printing
    for name, cand in candidates.items():
        print(name + " "+ str(cand.votes))
    print("")

if __name__ == "__main__":
  main()
