import random
import sys
import pandas as pd
import datetime


def print_welcome():
    play_ans = input("type 'y' for yes or 'n' for no")
    play_ans = play_ans.lower()
    if play_ans in ('y', 'yes', 'yeah'):
        print("Of course you'd like to play, you naughty so-and-so ;-)")
    elif play_ans in ('n', 'no', 'nah'):
        print("Oh, I see. You'd rather play with yourself. Bitchtits!!")
        sys.exit()
    else:
        print("Sorry, I didn't understand that. Please type 'y' or 'n'")
        print_welcome()


def get_diff():
    list_of_diff = ["Easy", "Medium", "Hard"]
    selected_diff = input("What difficulty would you like: \
                          1. {0}, 2. {1} or 3. {2}".format(*list_of_diff))
    try:
        selected_diff = int(selected_diff)
    except ValueError:
        selected_diff = selected_diff.capitalize()
    except TypeError:
        print("Sorry there was a problem with understanding your desired"
              "difficulty")
        raise

    if selected_diff in (int(1), list_of_diff[0]):
        selected_diff, upper_num, guesses_start = list_of_diff[0], 15, 6
        print("You've selected {}, AKA 'bitch-level'".format(selected_diff))

    elif selected_diff in (int(2), list_of_diff[1]):
        selected_diff, upper_num, guesses_start = list_of_diff[1], 20, 4
        print("You've selected {}.\
              Gunning for mediocrity!".format(selected_diff))

    elif selected_diff in (int(3), list_of_diff[2]):
        selected_diff, upper_num, guesses_start = list_of_diff[2], 35, 3
        print("{}. Look's like someone's cocky..".format(selected_diff))
    else:
        print("I didn't quite get that...")
    return selected_diff, upper_num, guesses_start


def get_player_name():
    player_name = input("Right then sailor, what should I call you?")
    return player_name


def print_instruct(upper_num):
    print("I've chosen a random integer between 0 and {}.".format(upper_num))
    print("You have {} attempts to guess this number.".format(guesses_start))
    return


def gen_random_number(upper_num):
    jackpot_number = random.randrange(0, upper_num+1)
    print(jackpot_number)
    return jackpot_number


def play_game(guesses_start, jackpot_number, name, diff, upper_num):
    guesses_left = guesses_start
    jackpot_number = jackpot_number
    print("You have {} guesses. Good luck!".format(guesses_left))
    while True:
        this_guess = int(input("Type a number:"))
        guesses_left -= 1
        if this_guess is jackpot_number:
            print("You win")
            guesses_taken = guesses_start - guesses_left
            score = scoring(upper_num, guesses_left)
            record_keeping(name, diff, guesses_taken, score)
            break
        elif guesses_left is not 0:
            if this_guess < jackpot_number:
                print("Too low, mofo. Only {} left!".format(guesses_left))
            if this_guess > jackpot_number:
                print("Too high, my guy. Only {} left!".format(guesses_left))
        else:
            print("You lose")
            break
    return


def scoring(upper_num, guesses):
    score = upper_num * guesses
    print("Not bad, you scored {} points!!!".format(score))
    return score


def record_keeping(name, diff, guesses_taken, score):
    """Round the time, sort the dataframe by score then diff"""
    current_time = datetime.datetime.now()
    cols = ['Time', 'Player', 'Difficulty', 'Guesses taken', 'Score']
    data = [current_time, name, diff, guesses_taken, score]
    current_game_df = pd.DataFrame(data=[data], columns=cols)
    try:
        records_csv = pd.read_csv('records.csv')
        records_csv = pd.concat([records_csv, current_game_df],
                                ignore_index=True)
        records_csv.to_csv('records.csv', index=False)
        print(records_csv, "index is:", records_csv.index)
    except OSError:
        current_game_df.to_csv('records.csv', index=False)
        print(current_game_df)
    except:
        print("Woah, something went wrong with record keeping")
        raise


print("Oh hello there, would you like to play with me?")
print_welcome()
diff, upper_num, guesses_start = get_diff()
name = get_player_name()
jackpot_number = gen_random_number(upper_num)
print_instruct(upper_num)
play_game(guesses_start, jackpot_number, name, diff, upper_num)
sys.exit()
