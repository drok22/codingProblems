''' Included a readme for this one. we're going to create a zig zag pattern
    from an input string, probably using separate arrays for each numRows passed in.
    then we'll take each char and rearrange them from each array so they will end up
    reading jumbled at the end. PAYPALISHERE with 3 rows would look like:
    P   A   H   N
    A P L S I I G
    Y   I   R
    With final output of: PAHNAPLSIIGYIR
'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = make_matrix(numRows)
        dir = True
        h = 0

        # iter thru input string and place chars
        for i in range(0, len(s)):

            matrix[h].append(s[i])
            if dir:
                h += 1
            else:
                h -= 1
            if h == numRows:
                # catch edge case where numRows is 1 or less
                h = numRows - 2 if numRows > 2 else 0
                dir = False
            elif h < 0:
                # catch edge case where numRows is 1 or less
                h = 1 if numRows > 1 else 0
                dir = True

        return combine_matrix(matrix)


def make_matrix(numRows: int) -> list:
    ''' create a matrix that is as deep as numRows
    '''
    matrix = []
    for h in range(0, numRows):
        matrix.append([])
    return matrix


def combine_matrix(matrix) -> str:
    ''' take all of the chars in the lists and add them together.
    '''
    chars = []

    for letters in matrix:
        chars = chars + letters

    return ''.join(chars)


solution = Solution()
print(solution.convert('ABC', 1))
print(solution.convert('PAYPALISHIRING', 3))
print(solution.convert('PAYPALISHIRING', 4))
print(solution.convert('A', 1))
