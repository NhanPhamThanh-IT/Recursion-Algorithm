# Helper function to remove adjacent duplicates
def remove_util(s, n):
  
    # Index to store the result string
    k = 0

    # Iterate over the string to remove adjacent duplicates
    i = 0
    while i < n:
      
        # Check if the current character is the same as the next one
        if i < n - 1 and s[i] == s[i + 1]:
          
            # Skip all the adjacent duplicates
            while i < n - 1 and s[i] == s[i + 1]:
                i += 1
        else:
            # If not a duplicate, store the character
            s[k] = s[i]
            k += 1
        i += 1

    # Remove the remaining characters from the original string
    s = s[:k]

    # If any adjacent duplicates were removed, recursively check for more
    if k != n:
        s = remove_util(list(s), k)
    
    return s

# Function to initiate the removal of adjacent duplicates
def rremove(s):
    # Convert the string to a list to allow modification
    s = list(s)
    
    # Call the helper function
    return ''.join(remove_util(s, len(s)))

# Example usage
s = "geeksforgeek"
print(rremove(s))