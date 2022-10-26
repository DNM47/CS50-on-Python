points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 
        1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

word1 = input('Player 1: ')
word2 = input('Player 2: ')

score1 = 0
score2 = 0

for letter in word1.lower():
    n_letter = int(ord(letter))
    new_l = n_letter - 97
    if new_l in range(0, 27):
        score1 += points[new_l]
    else: score1 += 0

for letter in word2.lower():
    n_letter = int(ord(letter))
    new_l = n_letter - 97
    if new_l in range(0, 27):
        score2 += points[new_l]
    else: score2 += 0

if score1 > score2:
    print('Player 1 wins!')
elif score1 < score2:
    print('Player 2 wins!')
else:
    print('Tie!')