# class Solution(object):
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#        
  
# roman_num=input('Enter a number to convert: ')
# if roman_num == "I":
#     print('1')

    #contains
    # 
    # The first thing that I am working on is taking an input and separating the letters into individual items in a list  
from re import X


def romanToInt():
    user_roman_num = input('Enter a roman numeral to convert: ').upper()
    if len(user_roman_num) >= 1 and len(user_roman_num) <= 15:
        roman_num=user_roman_num.replace('IV','IIII').replace('IX','VIIII').replace('XL','XXXX').replace('XC','LXXXX').replace('CD','CCCC').replace('CM','DCCCC')    
    
        list_of_roman_nums=[letters for letters in roman_num]
        
        for i in range(len(list_of_roman_nums)):
            if list_of_roman_nums [i] == 'I':
                list_of_roman_nums [i] = 1
            elif list_of_roman_nums [i] == 'V':
                list_of_roman_nums [i] = 5    
            elif list_of_roman_nums [i] == 'X':
                list_of_roman_nums [i] = 10
            elif list_of_roman_nums [i] == 'L':
                list_of_roman_nums [i] = 50
            elif list_of_roman_nums [i] == 'C':
                list_of_roman_nums [i] = 100
            elif list_of_roman_nums [i] == 'D':
                list_of_roman_nums [i] = 500
            elif list_of_roman_nums [i] == 'M':
                list_of_roman_nums [i] = 1000 
        
        sum_list = (sum(list_of_roman_nums))
        if sum_list >=1 and sum_list <=3999:
            print(sum_list)
        else:    
            print('That number is too high.')

    else:
        print('Please enter a number less than 15 characters.')  
          
    # for i in range(len(list_of_roman_nums)):
    #     if list_of_roman_nums [i] == 'I':
    #         list_of_roman_nums [i] = 1l
    #     elif list_of_roman_nums [i] == 'V':
    #         list_of_roman_nums [i] = 5    
    #     elif list_of_roman_nums [i] == 'X':
    #         list_of_roman_nums [i] = 10
    #     elif list_of_roman_nums [i] == 'L':
    #         list_of_roman_nums [i] = 50
    #     elif list_of_roman_nums [i] == 'C':
    #         list_of_roman_nums [i] = 100
    #     elif list_of_roman_nums [i] == 'D':
    #         list_of_roman_nums [i] = 500
    #     elif list_of_roman_nums [i] == 'M':
    #         list_of_roman_nums [i] = 1000 
    #     print(sum(list_of_roman_nums))
    

romanToInt()        