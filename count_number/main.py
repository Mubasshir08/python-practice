# The question is an array will come out with random numbers. Now we have to find out how many times they appears

# given array
array = [1,1,2,3,4,5,8,9,6,2,1,5,8,9,10,11,52,36,17,2,8,4,6,9,52,48,50,50,48,87,96,105,50]

# making new array to store each unique number
new_array=[]

for num in array:
    if num in new_array:
        continue
    else:
        new_array.append(num)

# now matching the new numbers with the existing number, and increasing count value.
for new_num in new_array:
        count = 0
        for prev_num in array:
             if new_num == prev_num:
                  count += 1
             else:
                  continue
        print(f'{new_num} count is {count}')
            
                  



    