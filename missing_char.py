#Missing Char

#Given a non-empty string and an int n, return a new string where the character at index n has been removed. The value of n will be a valid index of a character in the original string


def missing_char (word, n):
    
    return(lambda word, n : ((word[0:n])+ "" + (word[n+1:len(word)])) if n < len(word)-1 else print('enter a number less than', len(word)))(word, n)


Test	
print(missing_char('kitchen', 1)) Result ==> ktchen
print(missing_char('kitchen', 0)) Result ==> itchen
print(missing_char('kitchen', 4)) Result ==> kitcen
