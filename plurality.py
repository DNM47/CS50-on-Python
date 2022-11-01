import sys

ar = sys.argv
candidates = {ar[1]:0, ar[2]:0}

try:
    if ar[3]:
        candidates[ar[3]] = 0
except:
    pass

votes = input('Number of votes: ')
vote_count = 1

while int(votes) >= vote_count and int(votes) <= 9: 
    candidate = input('vote: ')
    if int(votes) > 9:
        break
    for c in candidates:
        c = candidate
        if c in candidates:
            candidates[c] += 1
    vote_count += 1

winners = [key for key, value in candidates.items()
if value == max(candidates.values())]                   # find the max of multiple values

winner = '\n'.join(winners)
print(winner)