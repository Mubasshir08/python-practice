given_str = "I don't love You"
given_str = given_str.lower()

vowels = 0

for str in given_str:
    if str == 'a' or str == 'e' or str == 'i' or str == 'o' or str == 'u' :
        vowels += 1
print(f'vowels in given string are {vowels}')