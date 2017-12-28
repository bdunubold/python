class Solution(object):
    def is_unique(self, string):
        return self.is_unique_sub(string, 0, len(string))

    # def is_unique_sub(self, string, i, j):
    #
    #     if len(string) == 1:
    #         return True
    #     mid = len(string) / 2

    def is_permutations(self, s1, s2):

        m1 = {}

        for i in s1:
            if i in m1:
                m1[i] += 1
            else:
                m1[i] = 1

        for i in s1:
            if i in m1:
                m1[i] += 1
            else:
                m1[i] = 1

    # here i am
    def urlify(self, s, l):

        i = l - 1
        j = len(s) - 1

        while i > 0:
            if s[i] == ' ':
                s[j] = '0'
                s[j - 1] = '2'
                s[j - 2] = '%'
                j -= 3
            else:
                s[j] = s[i]
                j -= 1
            i -= 1
        return s

    def palindrom_permutation(self, string):

        result = 0
        for i in string.lower():
            if i == ' ':
                continue
            result ^= (1 << ord(i) - 97)

        count = 0
        while result:
            count += result & 1
            result >>= 1
            if count > 1:
                return False
        return True

    def one_away(self, s1, s2):

        if abs(len(s1) - len(s2)) > 1:
            return False
        l, s = (s1, s2) if len(s1) > len(s2) else (s2, s1)
        i = 0
        j = 0
        rep = False
        while i < len(l) and j < len(s):
            if l[i] != s[j]:
                if rep:
                    return False
                rep = True
                if len(l) == len(s):
                    j += 1
            else:
                j += 1
            i += 1
        return True

    def string_compression(self, string):

        new_string = ""
        i = 0
        while i < len(string):
            j = i
            count = 0
            while j < len(string) and string[i] == string[j]:
                count += 1
                j += 1
            new_string += string[i] + str(count)
            i = j

        return new_string if len(new_string) < len(string) else string


    def zero_matrix(self, matrix):
        col = set()
        row = set()
        for j in range(len(matrix)):
            for k in range(len(matrix[j])):
                if matrix[j][k] == 0:
                    row.add(j)
                    col.add(k)
        for r in row:
            matrix[r] = [0] * len(matrix[r])
        for c in col:
            for m in matrix:
                m[c] = 0

        return matrix

    def stringRotation(self, s1, s2):

        if len(s1) != len(s2):
            return False

        return self.is_substring(s2, s1 + s1)

    def is_substring(self, s1, s2):
        if s1 in s2:
            return True
        return False


matrix = [
    [0, 1, 0],
    [2, 1, 2],
    [3, 3, 3]
]


s = Solution()
u = s.stringRotation("waterbottle", "erbottlewat")

print(u)
