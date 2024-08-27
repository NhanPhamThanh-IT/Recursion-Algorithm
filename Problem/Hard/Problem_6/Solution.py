class PalindromePartition:
    def __init__(self):
        self.ans = []

    def check_palindrome(self, curr_partition):
        for s in curr_partition:
            n = len(s)
            i, j = 0, n - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
        return True

    def generate_partition(self, s, bit_string):
        curr_partition = []
        sub_string = s[0]
        for i in range(len(bit_string)):
            # If current character of bitString is '0', no cut will be made,
            # and the next character will be included in the current subString.
            if bit_string[i] == '0':
                # No cut is made, so the next character is added to the substring.
                sub_string += s[i + 1]
            # If the current character of bitString is '1', then a cut will be made,
            # and the current subString will be appended in the current partition,
            # and a new subString will start from the next position.
            else:
                # SubString is added to the current partition.
                curr_partition.append(sub_string)

                # New substring is created starting from the next position of the string s.
                sub_string = s[i + 1]

        curr_partition.append(sub_string)
        if self.check_palindrome(curr_partition):
            self.ans.append(curr_partition)

    def bit_manipulation(self, s, bit_string):
        # When a bitString is generated, generate_partition() will be called
        # to partition the string accordingly.
        if len(bit_string) == len(s) - 1:
            self.generate_partition(s, bit_string)
            return
        bit_string += '1'
        self.bit_manipulation(s, bit_string)
        bit_string = bit_string[:-1]  # Pop the last character
        bit_string += '0'
        self.bit_manipulation(s, bit_string)

    def partition(self, s):
        bit_string = ""
        self.bit_manipulation(s, bit_string)
        return self.ans


if __name__ == "__main__":
    ob = PalindromePartition()
    s = "geeks"
    ans = ob.partition(s)
    for v in ans:
        print(" ".join(v))