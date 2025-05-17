# x = int(input('Enter number: '))

# if x % 2 == 0 and x % 5 == 0:
    #print('right')
#else:
    #print('wrong')

# ---------------------------------------

ch = input('enter char: ')
if 48 <= ord(ch) <= 57:
    print('number')
elif 65 <= ord(ch) <= 90 or 97 <= ord(ch) <= 122:
    print('letter')
else:
    print('other')

