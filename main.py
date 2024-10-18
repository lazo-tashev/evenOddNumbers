# Create a tuple with the given numbers.
numbers = ( 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Initialize counters for odd and even numbers.
even_count = 0
odd_count = 0

# Iterate through the numbers.
for x in numbers:

    # Check if the number is divisible by 2 with no reminder.
    if x % 2 == 0:
        even_count += 1 # if so add the number to even count.

    else:
        odd_count +=1 # else add to the odd count.

print('even numbers', even_count, 'odd numbers', odd_count) # print the numbers.