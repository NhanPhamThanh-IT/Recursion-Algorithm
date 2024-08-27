# Python implementation
class NhanPham:

    def checkPalindrome(self, s):
        n = len(s)
        i, j = 0, n - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def partition(self, res, s, ind, curr):
        if ind == len(s):
            res.append(list(curr))
            return

        temp = ""
        for i in range(ind, len(s)):
            temp += s[i]
            if self.checkPalindrome(temp):
                curr.append(temp)
                self.partition(res, s, i + 1, curr)
                curr.pop()

    def main(self):
        obj = NhanPham()
        res = []
        s = "geeks"
        ind = 0
        curr = []
        obj.partition(res, s, ind, curr)

        for iter in res:
            print(iter)

# Creating an instance of NhanPham class
NhanPham_obj = NhanPham()
NhanPham_obj.main()