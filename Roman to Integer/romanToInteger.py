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
    four='iv'
    nine='ix'
    # new_list = [letters for letters in roman_num]
    # new_list[i] = new_list[i].capitalize()
    # print(new_list)
    # return (new_list)    
    if four in roman_num:
        num_with_four=roman_num.replace('iv','iiii')
        list_with_four = [letters for letters in num_with_four]
        for i in range(len(list_with_four)):
            if list_with_four[i] == 'i':
                list_with_four[i] = 1
            elif list_with_four[i] == 'v':
                list_with_four[i] = 5    
            elif list_with_four[i] == 'x':
                list_with_four[i] = 10
            elif list_with_four[i] == 'l':
                list_with_four[i] = 50
            elif list_with_four[i] == 'c':
                list_with_four[i] = 100
            elif list_with_four[i] == 'd':
                list_with_four[i] = 500
            elif list_with_four[i] == 'm':
                list_with_four[i] = 1000                         
        
        print(sum(list_with_four))
    elif nine in roman_num:
        num_with_nine=roman_num.replace('ix','viiii')
        print(int(num_with_nine))
        
    else:
        print('Is this your roman numeral? ',roman_num)    

romanToInt()        