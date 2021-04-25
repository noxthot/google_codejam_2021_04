import numpy as np

DEBUG = False

def fillWithMinCost(x, y, s):
    def tripleScore(prevChar, currChar, nextChar, x, y):
        trip = prevChar + currChar + nextChar
        score = 0

        if 'CJ' in trip:
            score += x

        if 'JC' in trip:
            score += y

        return score

    def tupleScore(char1, char2, x, y):
        tup = char1 + char2

        if tup == 'CJ':
            return x
        elif tup == 'JC':
            return y

        return 0

    def choose_best_char(prevChar, currChar, nextChar, reversed, x, y):
        if currChar != '?':
            best_char = currChar
        else:
            best_char = 'J' if tripleScore(prevChar, 'C', nextChar, x, y) > tripleScore(prevChar, 'J', nextChar, x, y) else 'C'

        tupScore = tupleScore(best_char, nextChar, x, y) if reversed else tupleScore(prevChar, best_char, x, y)

        return best_char, tupScore


    startPos = 0

    for pos in range(len(s)):
        if s[pos] != "?":
            startPos = pos
            break

    fullprice = 0

    # special case: only ? in string s
    for pos in range(startPos, len(s)):
        prevChar = '?' if pos - 1 < 0 else s[pos - 1]
        currChar = s[pos]
        nextChar = '?' if pos + 1 > len(s) - 1 else s[pos + 1]
        bestchar, price = choose_best_char(prevChar, currChar, nextChar, False, x, y)

        s[pos] = bestchar
        fullprice += price

    for pos in reversed(range(startPos)):
        prevChar = '?' if pos - 1 < 0 else s[pos - 1]
        currChar = s[pos]
        nextChar = '?' if pos + 1 > len(s) - 1 else s[pos + 1]
        bestchar, price = choose_best_char(prevChar, currChar, nextChar, True, x, y)

        s[pos] = bestchar
        fullprice += price

    return s, fullprice


# Read input
T = int(input())  # nr Testcases

X = [None] * T  # costs X
Y = [None] * T  # costs Y
S = [None] * T  # strings

for i in range(T):
    X[i], Y[i], S[i] = input().split(" ")
    X[i] = int(X[i])
    Y[i] = int(Y[i])
    S[i] = [char for char in S[i]]

# Solve problem and output
for i in range(T):
    s, fullprice = fillWithMinCost(X[i], Y[i], S[i])
    DEBUG and print("Case #{}: {} {}".format(i + 1, s, fullprice))
    print("Case #{}: {}".format(i + 1, fullprice))