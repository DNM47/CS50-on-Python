quarter = 25
dimes = 10
nickels = 5
pennies = 1

total_count = 0

while True:
    cents = int(input('Change owed: '))
    if cents >= 0:
        break

quarter_divition = divmod(cents, quarter)
total_count = quarter_divition[0]

dimes_divition = divmod(quarter_divition[1], dimes)
total_count += dimes_divition[0]

nickels_divition = divmod(dimes_divition[1], nickels)
total_count += nickels_divition[0]

pennies_divition = divmod(nickels_divition[1], pennies)
total_count += pennies_divition[0]


print(total_count)
