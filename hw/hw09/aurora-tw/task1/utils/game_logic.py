from random import randint

GUESS_ATTEMPTS = 10

def generate_number():
    return randint(0,100)


def gt_or_less(answer_num,curr_num):
    return "greater" if curr_num > answer_num else "less"

def check_answer(answer_num, guessed_num):
    return True if answer_num == guessed_num else False

