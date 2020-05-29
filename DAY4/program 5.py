#program 5 of DAY 4

size = int(input("Enter number of votes: "))
votes = []

for i in range(size):
    votes.append(input("\nEnter name of the candidate: "))

vote2 = []

for name in votes:
    vote2.append([name, votes.count(name)])  #Creates 2D Array: 1st Part stores name & 2nd Part stores its occurrence
    
vote2.sort(key = lambda x : x[0])  #Sorts on the basis of name, lexicographically: Ascending Order
vote2.sort(key = lambda x : x[1], reverse=True)  #Sorts on the basis of vote: Descending order 
print("\nCandidate who won the election:", vote2[0][0])  #Selects name which occurred the most and is the smallest lexicographically
