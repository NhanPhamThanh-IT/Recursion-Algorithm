#include <bits/stdc++.h>
using namespace std;

// Returns true if dictionary d contains the given word
bool isInDict(const string &word, unordered_set<string> &d){
    return d.find(word) != d.end();
}

bool wordBreak(const string &s, unordered_set<string> &d)
{
    int n = s.size();
    if (n == 0)
        return true;

    vector<bool> dp(n + 1, 0);
    dp[0] = true;

    // matched_len stores lengths of
    // prefixes for which we have got
    // the result as true. 
    vector<int> matched_len;
    matched_len.push_back(0);

    for (int i = 1; i <= n; i++)
    {
        int msize = matched_len.size();

        // Consider all already matched lengths
        // and check only for remaining strings
        // after these already matched
        for (int j = msize - 1; j >= 0; j--)
        {
            int len = matched_len[j];
           
            // rem is substring starting from
            // matched_len[j] and of length 
            // i - matched_len[j]
            string rem = s.substr(len, i - len);

            // If the remaining substring is 
            // also a word
            if (isInDict(rem, d))
            {
                dp[i] = 1;
                matched_len.push_back(i);
                break;
            }
        }
    }
    return dp[n];
}

int main()
{
    vector<string> words = {"mobile", "samsung", "sam", "sung", "man", "mango", "icecream",
                            "and",    "go",      "i",   "like", "ice", "cream"};

    unordered_set<string> d(words.begin(), words.end());

    cout << (wordBreak("ilikesamsung", d) ? "Yes\n" : "No\n");
    cout << (wordBreak("iiiiiiii", d) ? "Yes\n" : "No\n");
    cout << (wordBreak("", d) ? "Yes\n" : "No\n");
    cout << (wordBreak("ilikelikeimangoiii", d) ? "Yes\n" : "No\n");
    cout << (wordBreak("samsungandmango", d) ? "Yes\n" : "No\n");
    cout << (wordBreak("samsungandmangok", d) ? "Yes\n" : "No\n");

    return 0;
}