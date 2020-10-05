#Program: WordShuffle
#Written by: Lee Friend
#Date: 05/10/2020

#import the library to randomise the list
import random

listword = []
userword = (input('Enter word to be shuffled: '))

while True:
    #convert string input to a list
    listword = list(userword)
    #shuffle the list
    random.shuffle(listword)
    #convert list back to a string for displaying
    finalstring = ''.join(listword)
    print("\n", finalstring)
    userkey = input("\nShuffle again? y/n followed by <return>")
    if userkey == 'n':
        break
    