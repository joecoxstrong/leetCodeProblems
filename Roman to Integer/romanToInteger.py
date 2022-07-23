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
def romanToInt():
    roman_num = input('Enter a roman numeral to convert: ')
    new_list = [letters for letters in roman_num]
    print(new_list)
    return (new_list)    

romanToInt()        