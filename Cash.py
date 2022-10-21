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

# print(nickels_divition)
print(total_count)



# Same thing but in C

# #include <cs50.h>
# #include <math.h>
# #include <stdio.h>
# #include <stdlib.h>


# int main(void)
# {
#     int quarter = 25;
#     int dimes = 10;
#     int nickels = 5;
#     int pennies = 1;

#     int count = 0;
#     float cents;

#     do
#     {
#         cents = get_float("Change owed: ");
#     }

#     while (cents < 0);
#     {
#         div_t quarter_division;
#         quarter_division = div(cents, quarter);
#         count = quarter_division.quot;

#         div_t dimes_division;
#         dimes_division = div(quarter_division.rem, dimes);
#         count += dimes_division.quot;

#         div_t nickels_division;
#         nickels_division = div(dimes_division.rem, nickels);
#         count += nickels_division.quot;

#         div_t pennies_division;
#         pennies_division = div(nickels_division.rem, pennies);
#         count += pennies_division.quot;

#         printf("%i\n", count);
#     }
# }
