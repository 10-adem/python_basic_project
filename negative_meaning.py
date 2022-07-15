#Negative Meaning 

#Define a function to take a word and return negative meaning.
#Given a word, return a new word where "not " has been added to the front. However, if the word already begins with "not", return the string unchanged.

def not_string(word):
    return ((lambda word : ("not"+ " " + word) if (not word.startswith("not")) else word)(word))

Test
print(not_string('sugar')) result ==> not sugar
print(not_string('x')) result ==> not x
print(not_string('not bad')) result ==> not bad
