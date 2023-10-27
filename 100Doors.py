import random

def door_picker(doors):
    winner = random.randrange(1, doors + 1)
    return winner

def monty_hall(door_count, enable_auto, total_games, always_switch):
    wins = 0
    games = 0
    switch = "0"
    keep_playing = "y"
    
    while keep_playing == "y":
        choice = "0"
        if enable_auto == "y":
            choice = str(random.randrange(1, door_count + 1))
        print("There are " + str(door_count) + " doors in front of you.\nOne contains a prize.\n")
        
        if enable_auto == "n":
            while not (choice.isdigit() and 0 < int(choice) < door_count + 1):
                choice = input("Pick one: ")
        
        winner = door_picker(door_count)
        choice, switch = door_opener(int(choice), winner, switch, enable_auto, door_count)
        wins += show_winner(int(choice), winner, switch)
        games += 1
        show_rate(wins, games)
        
        if enable_auto == "n":
            keep_playing = None
            while not (keep_playing == "y" or keep_playing == "n"):
                keep_playing = input("Would you like to keep playing? (y/n): ").lower()
        elif int(total_games) == games:
            keep_playing = "n"

def prisoners_simulation(total_games, number_loops):
    wins = 0
    for _ in range(total_games):
        # Simulate 100 Prisoners problem
        boxes = [i for i in range(1, 101)]
        random.shuffle(boxes)
        success = False

        for _ in range(number_loops):
            chosen_box = random.choice(boxes)
            if chosen_box == 1:
                success = True
                break

        if success:
            wins += 1

    return wins

def door_opener(choice, winner, switch, enable_auto, door_count):
    # Modify this function to work with different problem scenarios
    if enable_auto == "n":
        switch = None
    
    if choice == winner:
        closed_door = random.randrange(1, door_count + 1)
        while closed_door == winner:
            closed_door = random.randrange(1, door_count + 1)
    else:
        closed_door = choice
    
    print("I have opened all but doors " + str(closed_door) + " and " + str(winner))
    
    if enable_auto == "n":
        while not (switch == "y" or switch == "n"):
            switch = input("Would you like to switch? (y/n): ").lower()
    
    if switch == "y":
        if choice == winner:
            choice = closed_door
        else:
            choice = winner
    
    return choice, switch

def show_winner(choice, winner, switch):
    if switch == "n":
        print("You did not switch and you ", end="")
    else:
        print("You switched and you ", end="")
    
    if choice == winner:
        print("won!")
        return 1
    else:
        print("lost.")
        return 0

def show_rate(wins, games):
    rate = wins / games
    print("\n" + str(wins) + " wins of " + str(games) + " games")
    print("You are winning " + str(rate * 100) + "% of the time.\n\n")

def main():
    doors = "0"
    total_games = "0"
    enable_auto = None
    keep_playing = "y"
    
    print("Choose a problem to play:")
    print("1. Monty Hall Problem")
    print("2. 100 Prisoners Problem")
    choice = input("Enter the number of the problem you want to play: ")
    
    if choice == "1":
        while not (doors.isdigit() and 2 < int(doors)):
            doors = input("How many doors would you like to play with? ")
        doors = int(doors)
        while not (enable_auto == "y" or enable_auto == "n"):
            enable_auto = input("Would you like to see autoplay? (y/n): ").lower()
        if enable_auto == "y":
            while not (total_games.isdigit() and 0 < int(total_games)):
                total_games = input("How many games? ")
        
        monty_hall(doors, enable_auto, total_games, always_switch="n")
    
    elif choice == "2":
        total_games = int(input("How many 100 Prisoners games to simulate: "))
        number_loops = int(input("Enter the number of loops (e.g., 50): "))
        prisoners_wins = prisoners_simulation(total_games, number_loops)
        show_rate(prisoners_wins, total_games)
    
    else:
        print("Invalid choice. Please select a valid problem to play.")
        return

if __name__ == '__main__':
    main()
