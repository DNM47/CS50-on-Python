import sys

MAX = 9
ar = sys.argv

if len(ar) < 2:
    print("Usage: plurality [candidate ...]")
    exit()
elif len(ar) - 1 > MAX:
    print(f"Maximum number of candidates is {MAX}")
    exit()

candidates = {ar[1]:0, ar[2]:0}

try:
    if ar[3]:
        candidates[ar[3]] = 0
except:
    pass

votes = input('Number of votes: ')
vote_count = 1

for n in range(int(votes)): 
    candidate = input('vote: ')
    if candidate not in candidates:
        print("Invalid vote.")
        exit()
    for c in candidates:
        c = candidate
        if c in candidates:
            candidates[c] += 1
    vote_count += 1

winners = [key for key, value in candidates.items()
if value == max(candidates.values())]                   # find the max of multiple values

winner = '\n'.join(winners)
print(winner)