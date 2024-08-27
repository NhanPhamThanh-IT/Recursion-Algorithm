#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Function to check if the given string can be broken down into words from the word list
bool WordBreak(const string& str, const vector<string>& d)
{
    // If the string is empty, it can be broken down into an empty list of words
    if (str.empty())
        return true;

    int n = str.length();

    // Try every prefix of length i 
    for (int i = 1; i <= n; ++i) {
        
        // if the prefix of length i is a dictionary word and rest of the string can also be broken into valid words, return true
        string prefix = str.substr(0, i);
        if (find(d.begin(), d.end(), prefix) != d.end() && 
            WordBreak(str.substr(i), d)) {
            return true;
        }
    }

    return false;
}

int main()
{
    vector<string> d = { "mobile", "samsung",  "sam",  "sung", "man",
                         "mango",  "icecream", "and",  "go",   "i",
                         "like",   "ice",      "cream" };
    
    cout << (WordBreak("ilikesamsung", d) ? "Yes\n" : "No\n");
    cout << (WordBreak("iiiiiiii", d) ? "Yes\n" : "No\n");
    cout << (WordBreak("", d) ? "Yes\n" : "No\n");
    cout << (WordBreak("ilikelikeimangoiii", d) ? "Yes\n" : "No\n");
    cout << (WordBreak("samsungandmango", d) ? "Yes\n" : "No\n");
    cout << (WordBreak("samsungandmangok", d) ? "Yes\n" : "No\n");

    return 0;
}