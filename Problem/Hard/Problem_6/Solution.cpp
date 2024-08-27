#include <bits/stdc++.h>
using namespace std;

class NhanPham {
public:
    vector<vector<string> > ans;

    // Checks whether a Partition of string is palindrome or
    // not.
    bool checkPalindrome(vector<string> currPartition)
    {
        for (auto s : currPartition) {
            int n = s.size();
            int i = 0, j = n - 1;
            while (i < j) {
                if (s[i] != s[j])
                    return false;
                i++;
                j--;
            }
        }
        return true;
    }

    // Generates partition of a string according to
    // bitString.
    void generatePartition(string& s, string& bitString)
    {
        vector<string> currPartition;
        string subString;
        subString.push_back(s[0]);
        for (int i = 0; i < bitString.size(); i++) {

            // If current character of bitString is '0' no
            // cut will be made and next character will be
            // included in the current subString
            if (bitString[i] == '0') {
                // no cut is made so next character is added
                // to substring
                subString.push_back(s[i + 1]);
            }

            // If current character of bitString is '1' then
            // a cut will be made and current subString will
            // be appended in current Partition and new
            // subString will start from next position.
            else {
                // subString is added to current Partition.
                currPartition.push_back(subString);

                subString.clear();

                // New substring is created starting from
                // next position of string s.
                subString.push_back(s[i + 1]);
            }
        }
        currPartition.push_back(subString);
        if (checkPalindrome(currPartition)) {
            ans.push_back(currPartition);
        }
    }

    // Recursive function to generate all the bitStrings
    // which will denote the positions in which string will
    // be cut.
    void bitManipulation(string& s, string& bitString)
    {
        // When a bitString is generated generatePartition()
        // will be called to partition the string
        // accordingly.
        if (bitString.size() == s.size() - 1) {
            generatePartition(s, bitString);
            return;
        }
        bitString.push_back('1');
        bitManipulation(s, bitString);
        bitString.pop_back();
        bitString.push_back('0');
        bitManipulation(s, bitString);
        bitString.pop_back();
    }
    // Return all the palindromic partition of string s.
    vector<vector<string> > Partition(string s)
    {
        string bitString;
        bitManipulation(s, bitString);
        return ans;
    }
};

int main()
{
    NhanPham ob;
    // Stores all the partition
    vector<vector<string> > ans;
    string s = "geeks";
    ans = ob.Partition(s);
    for (auto& v : ans) {
        for (auto& it : v) {
            cout << it << " ";
        }
        cout << "\n";
    }
    return 0;
}