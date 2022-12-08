import sys

MAX_CANDIDATES = 100
MAX_VOTER = 9

ar = sys.argv
candidate_count = len(ar) - 1

if len(ar) < 2:
    print("Usage: runoff [candidate ...]")
    exit()
if candidate_count > MAX_CANDIDATES:
    print(f"Maximum number of candidates is {MAX_CANDIDATES}")
    exit()

voters_count = input('Number of votes: ')

if int(voters_count) > MAX_VOTER:
    print(f"Maximum number of voters is {MAX_VOTER}")

for i in range(int(voters_count)):
    for j in range(candidate_count):
        name = input(f'Rank {j + 1}: ')
        if name not in ar:
            print("Invalid vote.")
            exit()
    print('\n')
print(name)