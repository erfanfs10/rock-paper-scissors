from decorators import cal_time, CHOICES
import random


def bot_choice():
    bot = random.choice(CHOICES)
    return bot


def play_one_hand():
    user_point = 0
    bot_point = 0

    while user_point < 3 and bot_point < 3:

        user = input("your choice: ")
        if user not in CHOICES:
            print("invalid choice! must be (r, p, s)")
            continue
        bot = bot_choice()
        print(f"user: {user} | bot: {bot}")
        if user == 'r' and bot == 'p':
            print("bot won!")
            bot_point += 1
        elif user == 'p' and bot == 'r':
            print("user won!")
            user_point += 1
        elif user == 'p' and bot == 's':
            print("bot won!")
            bot_point += 1
        elif user == 's' and bot == 'p':
            print("user won!")
            user_point += 1
        elif user == 's' and bot == 'r':
            print("bot won!")
            bot_point += 1
        elif user == 'r' and bot == 's':
            print("user won!")
            user_point += 1
        elif user == bot:
            print("draw")
        else:
            continue
        print(f"user: {user_point} | bot: {bot_point}")
    if user_point > bot_point:
        print("USER WON!")
    else:
        print("BOT WON!")
    ask = input("do you want play more? (y/n)")
    if ask == 'y':
        play_one_hand()


@cal_time
def play():
    play_one_hand()


play()
