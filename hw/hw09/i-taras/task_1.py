import random



def guess_number(rand_num: int) -> str:
    try_numbe = 0

    while try_numbe <= 9:
        shot = int(input("Guess the number: "))
        if shot != secret_number:
            if shot > secret_number:
                print("The secret number is smaller.")
            else:
                print("The secret number is bigger.")
            try_numbe += 1
        elif shot == secret_number:
            print('Congratulation!!!')
            break
    if try_numbe == 10:
        print("All attempts have been used up!")

secret_number = random.randint(1, 1000)
guess_number(secret_number)