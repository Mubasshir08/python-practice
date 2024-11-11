import random

def roll_dice(amount : int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError
    
    rolls : list[int] = []
    for i in range(amount):
        random_rolls = random.randint(1,6)
        rolls.append(random_rolls)
    return rolls
    
while True:
        sum = 0
        try:
             user_input : str = input("Dice Number : ")
             
             if user_input.lower() == 'exit':
                  print('Thanks For Playing')
                  break
             
             final_result = roll_dice(int(user_input))
             print(*final_result, sep=", ")
             
             for i in range(len(final_result)): 
                sum += final_result[i]

             print(f'Total Sum Is {sum}')
             
        except ValueError:
             print('Print A Valid Number')

             

        
    

