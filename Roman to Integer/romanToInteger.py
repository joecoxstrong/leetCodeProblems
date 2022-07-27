# class Solution(object):
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """


def romanToInt():
    user_roman_num = input('Enter a roman numeral to convert: ').upper()
    allowed_user_roman_num = "IVXLCDM"
    validated_roman_num = all(ch in allowed_user_roman_num for ch in user_roman_num)
    if validated_roman_num == True:
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
                print('That number is too high. Try again.')
                romanToInt()
        else:
            print('Please enter a number less than 15 characters.')
            romanToInt()  
    else:
        print('That is not a valid Roman Numeral. Try Again')
        romanToInt()      
    
    

romanToInt()        