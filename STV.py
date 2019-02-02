#!/usr/bin/python

import operator
import sys
print("Welcome!")
#candidates = input("Enter candidates:\n")
#print(candidates);
#number_of_votes = input("How many votes?\n")
#number_of_votes = int(number_of_votes);
#print(number_of_votes);
#record_0 = dict.fromkeys(candidates,0)
#records = [record_0]
#for record in range(number_of_votes):
#    records.append(input("Gis us record\n"))



ballots = [
{'lion':1,'tiger':2,'monkey':3,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':2,'monkey':3,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':2,'monkey':3,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':2,'monkey':3,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':3,'monkey':2,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':3,'monkey':2,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':3,'monkey':2,'gorrilla':4,'turtle':5,'bird':6},
{'lion':4,'tiger':1,'monkey':3,'gorrilla':5,'turtle':2,'bird':6},
{'lion':4,'tiger':1,'monkey':3,'gorrilla':5,'turtle':2,'bird':6},
{'lion':3,'tiger':1,'monkey':4,'gorrilla':5,'turtle':2,'bird':6},
{'lion':3,'tiger':1,'monkey':4,'gorrilla':5,'turtle':2,'bird':6},
{'lion':3,'tiger':1,'monkey':4,'gorrilla':5,'turtle':2,'bird':6},
{'lion':2,'tiger':3,'monkey':1,'gorrilla':4,'turtle':5,'bird':6},
{'lion':4,'tiger':5,'monkey':6,'gorrilla':1,'turtle':3,'bird':2},
{'lion':4,'tiger':5,'monkey':6,'gorrilla':1,'turtle':3,'bird':2},
{'lion':4,'tiger':5,'monkey':6,'gorrilla':1,'turtle':3,'bird':2},
{'lion':0,'tiger':0,'monkey':0,'gorrilla':3,'turtle':1,'bird':2},
{'lion':0,'tiger':0,'monkey':0,'gorrilla':3,'turtle':1,'bird':2},
{'lion':0,'tiger':0,'monkey':0,'gorrilla':3,'turtle':1,'bird':2},
{'lion':4,'tiger':5,'monkey':6,'gorrilla':2,'turtle':3,'bird':1},
           
{'lion':1,'tiger':2,'monkey':3,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':2,'monkey':3,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':2,'monkey':3,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':2,'monkey':3,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':3,'monkey':2,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':3,'monkey':2,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':3,'monkey':2,'gorrilla':4,'turtle':5,'bird':6},
{'lion':4,'tiger':1,'monkey':3,'gorrilla':5,'turtle':2,'bird':6},
{'lion':4,'tiger':1,'monkey':3,'gorrilla':5,'turtle':2,'bird':6},
{'lion':3,'tiger':1,'monkey':4,'gorrilla':5,'turtle':2,'bird':6},
{'lion':3,'tiger':1,'monkey':4,'gorrilla':5,'turtle':2,'bird':6},
{'lion':3,'tiger':1,'monkey':4,'gorrilla':5,'turtle':2,'bird':6},
{'lion':2,'tiger':3,'monkey':1,'gorrilla':4,'turtle':5,'bird':6},
{'lion':4,'tiger':5,'monkey':6,'gorrilla':1,'turtle':3,'bird':2},
{'lion':4,'tiger':5,'monkey':6,'gorrilla':1,'turtle':3,'bird':2},
{'lion':4,'tiger':5,'monkey':6,'gorrilla':1,'turtle':3,'bird':2},
{'lion':0,'tiger':0,'monkey':0,'gorrilla':3,'turtle':1,'bird':2},
{'lion':0,'tiger':0,'monkey':0,'gorrilla':3,'turtle':1,'bird':2},
{'lion':0,'tiger':0,'monkey':0,'gorrilla':3,'turtle':1,'bird':2},
{'lion':4,'tiger':5,'monkey':6,'gorrilla':2,'turtle':3,'bird':1},
{'lion':1,'tiger':2,'monkey':3,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':2,'monkey':3,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':2,'monkey':3,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':2,'monkey':3,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':3,'monkey':2,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':3,'monkey':2,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':3,'monkey':2,'gorrilla':4,'turtle':5,'bird':6},
{'lion':4,'tiger':1,'monkey':3,'gorrilla':5,'turtle':2,'bird':6},
{'lion':4,'tiger':1,'monkey':3,'gorrilla':5,'turtle':2,'bird':6},
{'lion':3,'tiger':1,'monkey':4,'gorrilla':5,'turtle':2,'bird':6},
{'lion':3,'tiger':1,'monkey':4,'gorrilla':5,'turtle':2,'bird':6},
{'lion':3,'tiger':1,'monkey':4,'gorrilla':5,'turtle':2,'bird':6},
{'lion':2,'tiger':3,'monkey':1,'gorrilla':4,'turtle':5,'bird':6},
{'lion':4,'tiger':5,'monkey':6,'gorrilla':1,'turtle':3,'bird':2},
{'lion':4,'tiger':5,'monkey':6,'gorrilla':1,'turtle':3,'bird':2},
{'lion':4,'tiger':5,'monkey':6,'gorrilla':1,'turtle':3,'bird':2},
{'lion':0,'tiger':0,'monkey':0,'gorrilla':3,'turtle':1,'bird':2},
{'lion':0,'tiger':0,'monkey':0,'gorrilla':3,'turtle':1,'bird':2},
{'lion':0,'tiger':0,'monkey':0,'gorrilla':3,'turtle':1,'bird':2},
{'lion':4,'tiger':5,'monkey':6,'gorrilla':2,'turtle':3,'bird':1},
{'lion':1,'tiger':2,'monkey':3,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':2,'monkey':3,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':2,'monkey':3,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':2,'monkey':3,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':3,'monkey':2,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':3,'monkey':2,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':3,'monkey':2,'gorrilla':4,'turtle':5,'bird':6},
{'lion':4,'tiger':1,'monkey':3,'gorrilla':5,'turtle':2,'bird':6},
{'lion':4,'tiger':1,'monkey':3,'gorrilla':5,'turtle':2,'bird':6},
{'lion':3,'tiger':1,'monkey':4,'gorrilla':5,'turtle':2,'bird':6},
{'lion':3,'tiger':1,'monkey':4,'gorrilla':5,'turtle':2,'bird':6},
{'lion':3,'tiger':1,'monkey':4,'gorrilla':5,'turtle':2,'bird':6},
{'lion':2,'tiger':3,'monkey':1,'gorrilla':4,'turtle':5,'bird':6},
{'lion':4,'tiger':5,'monkey':6,'gorrilla':1,'turtle':3,'bird':2},
{'lion':4,'tiger':5,'monkey':6,'gorrilla':1,'turtle':3,'bird':2},
{'lion':4,'tiger':5,'monkey':6,'gorrilla':1,'turtle':3,'bird':2},
{'lion':0,'tiger':0,'monkey':0,'gorrilla':3,'turtle':1,'bird':2},
{'lion':0,'tiger':0,'monkey':0,'gorrilla':3,'turtle':1,'bird':2},
{'lion':0,'tiger':0,'monkey':0,'gorrilla':3,'turtle':1,'bird':2},
{'lion':4,'tiger':5,'monkey':6,'gorrilla':2,'turtle':3,'bird':1},
{'lion':1,'tiger':2,'monkey':3,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':2,'monkey':3,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':2,'monkey':3,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':2,'monkey':3,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':3,'monkey':2,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':3,'monkey':2,'gorrilla':4,'turtle':5,'bird':6},
{'lion':1,'tiger':3,'monkey':2,'gorrilla':4,'turtle':5,'bird':6},
{'lion':4,'tiger':1,'monkey':3,'gorrilla':5,'turtle':2,'bird':6},
{'lion':4,'tiger':1,'monkey':3,'gorrilla':5,'turtle':2,'bird':6},
{'lion':3,'tiger':1,'monkey':4,'gorrilla':5,'turtle':2,'bird':6},
{'lion':3,'tiger':1,'monkey':4,'gorrilla':5,'turtle':2,'bird':6},
{'lion':3,'tiger':1,'monkey':4,'gorrilla':5,'turtle':2,'bird':6},
{'lion':2,'tiger':3,'monkey':1,'gorrilla':4,'turtle':5,'bird':6},
{'lion':4,'tiger':5,'monkey':6,'gorrilla':1,'turtle':3,'bird':2},
{'lion':4,'tiger':5,'monkey':6,'gorrilla':1,'turtle':3,'bird':2},
{'lion':4,'tiger':5,'monkey':6,'gorrilla':1,'turtle':3,'bird':2},
{'lion':0,'tiger':0,'monkey':0,'gorrilla':3,'turtle':1,'bird':2},
{'lion':0,'tiger':0,'monkey':0,'gorrilla':3,'turtle':1,'bird':2},
{'lion':0,'tiger':0,'monkey':0,'gorrilla':3,'turtle':1,'bird':2},
{'lion':4,'tiger':5,'monkey':6,'gorrilla':2,'turtle':3,'bird':1},
]

class Ballot:
    """Ballot"""
    def __init__(self, rankings):
        self.rankings = rankings
        self.voteValue = 1

class Candidate():
    """Candidates"""
    def __init__(self, name):
        """Initialize candidate."""
        self.name = name
        self.ballots = []
        self.votes = 0.0
        self.notEliminated = True
    
    def addBallot(self, ballot):
        self.ballots.append(ballot)
        self.votes = self.votes + ballot.voteValue

def checkForWinners(seats):
    for name, candidate in sortedBallots.iteritems():
        if candidate.votes > quota:
            seats.add(candidate);
    return seats

def isThereASurplus():
    for name, candidate in sortedBallots.iteritems():
        if candidate.votes > quota:
            return True;
    return False;

def getCandidiateWithBiggestSurplus():
    max = 0;
    for name, candidate in sortedBallots.iteritems():
        if candidate.votes > quota and candidate.votes > max:
            max = candidate.votes
            candidateWithBiggestSurplus = candidate
    return candidateWithBiggestSurplus

def getCandidiateWithLowestVotes():
    min = sys.maxint
    for name, cand in sortedBallots.iteritems():
        if ((cand.votes < min) and cand.notEliminated):
            candidateToElimate = cand
            min = cand.votes
    return candidateToElimate

def reAssignBallot(ballot,candidateName):
    nextRank = ballot.rankings[candidateName] + 1
    ballot.rankings.pop(candidateName)
    notRedistributed = True
    while (notRedistributed):
        for candName , rank in ballot.rankings.iteritems():
            if (rank == nextRank):
                # Check to see if candidate has been eliminated
                if(sortedBallots[candName].notEliminated):
                    sortedBallots[candName].addBallot(ballot)
                    notRedistributed = False
                    break;
                else:
                    nextRank = nextRank + 1
                    if (nextRank == len(candidateNames)):
                        notRedistributed = False

def printVotes():
    #Debug Printing
    for name, cand in sortedBallots.iteritems():
        print(name + " "+ str(cand.votes))
    print("")

# Scipt Startish #====================================================

candidateNames = ['lion','tiger','monkey','gorrilla','turtle','bird']
numberOfReps = 3.0
#Droop
quota = (len(ballots) / (numberOfReps + 1)) + 1

# Sort into first place preference
sortedBallots = {}
for name in candidateNames:
    sortedBallots[name] = Candidate(name)

for vote in ballots:
    for cand , rank in vote.iteritems():
        if (rank == 1):    
            sortedBallots[cand].addBallot(Ballot(vote))
            break;

for name, cand in sortedBallots.iteritems():
    print(name + " "+ str(cand.votes))

print("")
seats = set()
seats = checkForWinners(seats)
count = 0
while (len(seats) < numberOfReps):
    if (isThereASurplus()):
        surplusCandidate = getCandidiateWithBiggestSurplus()
        print(surplusCandidate.name + " has surplus to redistribute")
        # Redistribute
        surplusFactor = (surplusCandidate.votes - quota) /  surplusCandidate.votes;
        for ballot in surplusCandidate.ballots:
            ballot.voteValue = ballot.voteValue * surplusFactor
            reAssignBallot(ballot,surplusCandidate.name)
    
        # Remove all ballots form surplus candidate as they have been transferred
        surplusCandidate.ballots = []
        surplusCandidate.votes = quota
        
        printVotes()
    # No surplus remaining, Eliminate and transfer votes of lowest candidate
    else:
        candidateToElimate = getCandidiateWithLowestVotes()
        # Redistribute
        for ballot in candidateToElimate.ballots:
            reAssignBallot(ballot,candidateToElimate.name)
        # Elimate candidate
        print(candidateToElimate.name + " is elimiated and to redistribute")
        candidateToElimate.votes = 0;
        candidateToElimate.notEliminated = False;
        candidateToElimate.ballots = [];
        printVotes()


    seats = checkForWinners(seats)
    if (count == 15):
        numberOfReps = 0
    count = count + 1


print ("Final Winners:")
for name, cand in sortedBallots.iteritems():
    if (cand.votes >= quota):
        print(name + " "+ str(cand.votes))



"""candRecords = {}
for c in candidates:
    candRecords[c] = []

for record in recordsDict:
    for cand in record:
        if (record[cand] == 1):
            totalsDic[cand] += 1
            candRecords[cand].append(record)

numberOfSeats = 3;
quota = len(recordsDict) / float(numberOfSeats)
print(quota)
seats = [];

fptp = sorted(totalsDic.items(), key=operator.itemgetter(1),reverse=True)


for t in fptp:
    print(t)
    if (t[1] > quota):
        seats.append(t)

print("seats = " + str(len(seats)))
while (len(seats) < numberOfSeats and len(candRecords) > numberOfSeats):
    print("123 = ")
    #Has anyone reached the quota?
    if (len(seats) > 0):
        supplusCand = 0
        while (supplusCand < len(seats) and len(seats) < numberOfSeats):
            print("456 = ")
            cand = seats[supplusCand][0]
            for record in candRecords[cand]:
                record.pop(cand)
                sortedRecords = sorted(totalsDic.items(), key=operator.itemgetter(1),reverse=True)
                
                for t in lensortedRecords:
                
                
                print(record)
            supplusCand = 5
            numberOfSeats = 0


print(seats)"""


