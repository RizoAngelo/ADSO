def seven_segment_display(digit):
    if digit >= 0:
        digit = str(digit)
        digit_list = list(digit)
        new_digit = ''
        for i in range(len(digit_list)):
            if digit_list[i] == '0':
                new_digit += zero
            elif digit_list[i] == '1':
                new_digit += one
            if digit_list[i] == '2':
                new_digit += two
            if digit_list[i] == '3':
                new_digit += three
            if digit_list[i] == '4':
                new_digit += four
            if digit_list[i] == '5':
                new_digit += five
            if digit_list[i] == '6':
                new_digit += six
            if digit_list[i] == '7':
                new_digit += seven
            if digit_list[i] == '8':
                new_digit += eight
            if digit_list[i] == '9':
                new_digit += nine
        return ((new_digit))
zero = '###\n# #\n# #\n# #\n###\n\n'
one = '#\n#\n#\n#\n#\n\n'
two = '###\n  #\n###\n#  \n###\n\n'
three = '###\n  #\n###\n  #\n###\n\n'
four = '# #\n# #\n###\n  #\n  #\n\n'
five = '###\n#  \n###\n  #\n###\n\n'
six = '###\n#  \n###\n# #\n###\n\n'
seven = '###\n  #\n  #\n  #\n  #\n\n'
eight = '###\n# #\n###\n# #\n###\n\n'
nine = '###\n# #\n###\n  #\n###\n\n'
print(seven_segment_display(123))


