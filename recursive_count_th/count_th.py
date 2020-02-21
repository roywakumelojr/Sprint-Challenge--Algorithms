'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC

    # "th" contains 2 letters so this part ensures the length of word is less than 2
    if len(word) < 2:
        return 0

    #checks if the first letter of the word is "t" and the second letter is "h"
    if word[0] == "t" and word[1] == "h":
        return 1 + count_th(word[1:])

    else:
        return count_th(word[1:])
