from random import randint

lower_number , higher_number = 1,10
guessed_number : int = randint(lower_number, higher_number)

# print(guessed_number)

while True:
    try:
        user_input : int = int(input('Guess A Number Please Between 1 - 10 : '))
    except ValueError as e:
        print('Please Write A Valid Integer Number')
        continue
    if user_input > guessed_number:
        print('The Number Is Lower')
    elif user_input < guessed_number:
        print('The Number Is Higher')
    else:
        print('You Guessed The Right')
        break
