#include <bits/stdc++.h>
using namespace std;

// Helper function to remove adjacent duplicates
void remove_util(string &str, int n) {

     // Get the length of the string
    int len = str.length(); 

     // Index to store the result string
    int k = 0; 

    // Iterate over the string to remove adjacent duplicates
    for (int i = 0; i < n; i++) {

        // Check if the current character is the same as the next one
        if (i < n - 1 && str[i] == str[i + 1]) {
            // Skip all the adjacent duplicates
            while (i < n - 1 && str[i] == str[i + 1]) {
                i++;
            }
        } else {
            // If not a duplicate, store the character
            str[k++] = str[i];
        }
    }

    // Remove the remaining characters from the original string
    str.erase(k);

    // If any adjacent duplicates were removed, recursively check for more
    if (k != n)
        remove_util(str, k);
}

// Function to initiate the removal of adjacent duplicates
string rremove(string s) {

    // Call the helper function
    remove_util(s, s.length());

    // Return the modified string
    return s;  
}

int main() {
    string s = "Code Forces";
    cout << rremove(s) << endl; 
    return 0;
}