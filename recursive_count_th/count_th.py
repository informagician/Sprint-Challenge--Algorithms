'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    count = 0

    if word == "":
        count = 0
    elif word[0:2] == 'th':
        count += 1
        word = word[1:]
        countf = count_th(word)
        count += countf
    else:
        word = word[1:]
        countf = count_th(word)
        count += countf
        
    return count


# if word[0:2] == "th":
#         count += 1
#         word = word[1:]
#         count = count_th(word)
#         print(count,word)
#         count += count
#     else:
#         word = word[1:]
#         count = count_th(word)
#         print(count,word)
#         count += count