#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

// Returns true if dictionary d contains the given word
bool isInDict(const string &word, unordered_set<string>& d) {
    return d.find(word) != d.end();
}

// Returns true of a given string can be broken into dictionary d words, else false
bool wordBreak(const string &str, unordered_set<string>& d) {
    
    int n = str.size();
    
    // dp[i] is gping to be true if the prefix of length i can be broken into words.
    vector<bool> dp(n + 1, false);
    dp[0] = true; // Answe is true for an empty string
 
    for (int i = 1; i <= n; i++) {
        
        // Check for smaller strings and if we find a j such that a prefix of length j can be broken and str[j..i-1] is also a valid word
        for (int j = 0; j < i; j++) {
            if (dp[j] && isInDict(str.substr(j, i - j), d)) {
                dp[i] = true;
                break;
            }
        }
    }
    return dp[n];
}

int main() {
    vector<string> words = {"mobile", "samsung", "sam", 
          "sung", "man", "mango", "icecream", "and", "go", 
          "i", "like", "ice", "cream"};

    unordered_set<string> d(words.begin(), words.end());

    cout << (wordBreak("ilikesamsung", d) ? "Yes\n" : "No\n");
    cout << (wordBreak("iiiiiiii", d) ? "Yes\n" : "No\n");
    cout << (wordBreak("", d) ? "Yes\n" : "No\n");
    cout << (wordBreak("ilikelikeimangoiii", d) ? "Yes\n" : "No\n");
    cout << (wordBreak("samsungandmango", d) ? "Yes\n" : "No\n");
    cout << (wordBreak("samsungandmangok", d) ? "Yes\n" : "No\n");

    return 0;
}