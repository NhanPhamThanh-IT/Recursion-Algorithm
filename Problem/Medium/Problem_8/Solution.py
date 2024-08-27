# Python3 implementation to find the length of longest palindromic sub-string using Recursion
 
# Function to find maximum of the two variables 
def maxi(x, y) :
    if x > y :
        return x
    else :
        return y
 
# Function to find the longest palindromic substring : Recursion 
def longestPalindromic(strn, i, j, count): 
     
    # Base condition when the start index is greater than end index 
    if i > j : 
        return count 
     
    # Base condition when both the start and end index are equal 
    if i == j : 
        return (count + 1)
         
    # Condition when corner characters are equal in the string 
    if strn[i] == strn[j] : 
         
        # Recursive call to find the longest Palindromic string by excluding the corner characters 
        count = longestPalindromic(strn, i + 1, j - 1, count + 2) 
        return maxi(count, maxi(longestPalindromic(strn, i + 1, j, 0), 
                    longestPalindromic(strn, i, j - 1, 0))) 
     
    # Recursive call to find the longest Palindromic string by including one corner character at a time 
    return maxi( longestPalindromic(strn, i + 1, j, 0), 
                longestPalindromic(strn, i, j - 1, 0)) 
 
# Function to find the longest palindromic sub-string 
def longest_palindromic_substr(strn):
 
    # Utility function call
    k = len(strn) - 1
    return longestPalindromic(strn, 0, k, 0)
 
strn = "aaaabbaa"
 
# Function Call 
print( longest_palindromic_substr(strn) )