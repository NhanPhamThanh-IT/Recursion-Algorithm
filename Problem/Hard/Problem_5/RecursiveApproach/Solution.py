# Function to check if the given word can be broken down into words from the wordList
def wordBreak(wordList, word):
    # If the word is empty, it can be broken down into an empty list of words
    if not word:
        return True
    
    wordLen = len(word)
    
    # Check if the word can be broken down into words from the wordList
    for i in range(1, wordLen + 1):
        prefix = word[:i]
        
        if prefix in wordList and wordBreak(wordList, word[i:]):
            return True
    
    return False

wordList = ["mobile", "samsung", "sam", "sung", "man",
                "mango", "icecream", "and", "go", "i",
                "like", "ice", "cream"]
    
result = wordBreak(wordList, "ilikesamsung")
    
print(result)