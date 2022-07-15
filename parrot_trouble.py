#Parrot_Trouble

#Define a function taking two parameters (talking and hour) to return True if we are in trouble. The argument to  talking parameter can only be True or False whether it is talking or not. The argument to hour parameter should be the current hour time in the range of 0 to 23.

def parrot_trouble (talking, hour):
    return ((lambda talking, hour : True if talking is True and hour > 21 or hour < 6 else False)(talking, hour))

print(parrot_trouble(True, 5)) ==> True
print(parrot_trouble(True, 8)) ==> False
print(parrot_trouble(False, 22)) ==> False
