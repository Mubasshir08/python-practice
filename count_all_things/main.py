given_str = "p@#yn26at^&i5ve"


# the useable methods:
# .isalpha()
# .isdigit()

new_array = []

chars = 0
digits = 0
symbols = 0

for str in given_str:
    if str.isalpha() == True:
        new_array.append(str)
        chars += 1
    elif str.isdigit() == True:
        new_array.append(str)
        digits += 1
    else:
        new_array.append(str)
        symbols += 1
        
print(f'{new_array} \nchars = {chars} \ndigits = {digits} \nsymbols = {symbols}')
