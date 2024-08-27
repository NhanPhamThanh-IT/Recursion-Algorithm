# A Dynamic Programming based program to test whether a given String can be segmented into space separated words in dictionary

# A utility function to check whether a word is present in dictionary or not.
# An array of Strings is used for dictionary. Using array of Strings for dictionary is definitely not a good idea. We have used for simplicity of the program
def dictionaryContains(word):
    dictionary = [ "mobile", "samsung", "sam", "sung", "man", "mango", "icecream", "and", "go", "i",
                "like", "ice", "cream" ]
    size = len(dictionary)
    for i in range(size):
        if (dictionary[i]== word):
            return True
    return False

# Returns True if String can be segmented into space separated words, otherwise returns False
def wordBreak(Str):
    size = len(Str)
    if (size == 0):
        return True

        # Create the DP table to store results of subproblems. The value wb[i] will be True if str[0..i-1] can be segmented into dictionary words, otherwise False.
    wb = [False for i in range(size + 1)]

    for i in range(1,size + 1):
        # if wb[i] is False, then check if current prefix can make it True.
        # Current prefix is "str.substring(0, i)"
        if (wb[i] == False and dictionaryContains(Str[0: i])):
            wb[i] = True

        # wb[i] is True, then check for all subStrings starting from (i+1)th character and store their results.
        if (wb[i] == True):
            # If we reached the last prefix
            if (i == size):
                return True

            for j in range(i + 1,size + 1):
                # Update wb[j] if it is False and can be updated
                # Note the parameter passed to dictionaryContains() is subString starting from index 'i' and length 'j-i'
                if (wb[j] == False and dictionaryContains(Str[i: j])):
                    wb[j] = True

                # If we reached the last character
                if (j == size and wb[j] == True):
                    return True
                
            

    # If we have tried all prefixes and none of them worked
    return False

# Driver program to test above functions
    
if (wordBreak("ilikesamsung")):
    print("Yes")
else:
    print("No")
if (wordBreak("iiiiiiii")):
    print("Yes")
else:
    print("No")
if (wordBreak("")):
    print("Yes")
else:
    print("No")
if (wordBreak("ilikelikeimangoiii")):
    print("Yes")
else:
    print("No")
if (wordBreak("samsungandmango")):
    print("Yes")
else:
    print("No")
if (wordBreak("samsungandmangok")):
    print("Yes")
else:
    print("No")