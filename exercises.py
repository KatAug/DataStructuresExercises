# Problem 1 (Sets)

"""
Create a new Set with string values that represent colors
Loop through the Set and print each value
"""

def print_colors(set_of_colors):
    colors = {"blue", "red", "green", "tomato"}
    for color in set_of_colors:
        print(color)

# Problem 2 (Sets)

"""
Take the Set from Problem 1
Take input from the user, asking for their favorite color
Check to see if their favorite color is in the Set
If the color is in the Set, print "We found your favorite color!"
If the color is not in the Set, add that color to the Set
"""

def find_favorite_color(colors):
    user_input = input("What is your favorite color? ")
    if user_input in colors:
        print("We found your favorite color!")
    else:
        colors.add(user_input)
        print(f"We added {user_input} to the list!")

# Problem 3 (Sets)

"""
Take the Set from Problem 1
Display the contents to the user in the terminal
Ask the user what colors they would like to add
Create a NEW Set with colors the user adds
Then utilize the `union` Set method to combine sets
display the new Set
See: https://www.w3schools.com/python/python_sets_join.asp
"""

def add_colors(colors):
    print("Here are some colors:")
    print_colors(colors)
    user_input = input("What other colors would you like to add? ") 
    set_two = {user_input}
    set_three = colors.union(set_two)
    print(set_three)
    
colors = {"blue", "red", "green", "tomato"}

# Recommend having this resource open for Problems 4-6
# https://www.w3schools.com/python/python_tuples.asp

# Problem 4 (Tuples)

"""
Write a Tuple that contains strings that represent coins
There will be three types of coins: "gold", "silver", and "copper"
For example: ("gold", "silver", "copper", "gold")
Note that there are duplicates (imagine coins in a purse)
Next, write a function that displays all coins using a WHILE loop

"""
coins = ("gold", "copper", "silver", "copper", "gold", "silver", "silver")
def display_coins(coins):
    change = 0
    while change < len(coins):
        print(coins[change])
        change = change + 1

# Problem 5 (Tuples)

"""
Take the Tuple from Problem 4 and add a new coin to it
Then, display all of the coins in the Tuple after adding the coin
NOTE: You will need to convert your Tuple to a List, then back to a Tuple in order to do this!
See: https://www.w3schools.com/python/python_tuples_update.asp
"""

coins = ("gold", "copper", "silver", "copper", "gold", "silver", "silver")
def add_coin(coins):
    coin = ("bronze",)
    coins += coin
    print(coins)
    
# Problem 6 (Tuples)

"""
Take the Tuple from Problem 4 and remove all of the duplicates from it
Then, display all of the "coin types" to the user
Example Output: "gold, silver, copper"
NOTE: You will need to convert your Tuple to a Set, then back to a Tuple in order to de-duplicate
"""

coins = ("gold", "copper", "silver", "copper", "gold", "silver", "silver")
coin = list(coins)
def display_coin_types(coins):
    coin.remove("gold")
    coin.remove("silver")
    coin.remove("silver")
    coin.remove("copper")
    coins = tuple(coin)
    print(coins)
    