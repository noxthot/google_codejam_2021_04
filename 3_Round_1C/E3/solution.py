DEBUG = True

def transformString(s, e):
    DEBUG and print(f"Trying to transform {s} to {e}")

    def negateNumber(x, removeTrailing=True):
        notAsList = []
        leadingZero = removeTrailing

        ret = ''

        for c in x:
            if leadingZero and c == '1':
                continue

            if c == '0':
                notAsList += '1'
                leadingZero = False
            else:
                notAsList += '0'

            ret = ''.join(notAsList)

        ret = '0' if ret == '' else ret

        return ret

    def doubleNumber(x):
        ret = x + '0'

        return ret

    def findCommonPattern(s, e):
        subE = e
        lenSubE = len(subE)
        ret = 0

        while lenSubE > 0:
            if len(s) >= lenSubE:
                if (s[-lenSubE:] == subE):
                    ret = lenSubE
                    break

            subE = subE[:-1]
            lenSubE = len(subE)

        return ret

    possible = True
    cntOps = 0
    s_rem = s

    # find parts of s that can be used further
    while possible:
        if e == s_rem:
            DEBUG and print("GOT IT")
            break

        nrCommonChars = findCommonPattern(s_rem, e)
        nrCommonCharsNeg = findCommonPattern(negateNumber(s_rem), e)
        #DEBUG and print(f"Common: {s_rem} and {e} -> {nrCommonChars}")
        #DEBUG and print(f"Common: {negateNumber(s_rem)} and {e} -> {nrCommonCharsNeg}")
        s_rem_prev = s_rem

        if nrCommonChars == len(e):
            s_rem = negateNumber(negateNumber(s_rem))
            cntOps += 2
            DEBUG and print(f"DNEG {s_rem_prev} -> {s_rem}; {cntOps}")
        elif nrCommonCharsNeg == len(e):
            s_rem = negateNumber(s_rem)
            cntOps += 1
            DEBUG and print(f"NEG1 {s_rem_prev} -> {s_rem}; {cntOps}")
        elif len(s_rem) < len(e) and s_rem != '0' and len(e) >= 2 and e[nrCommonChars - 1] == e[nrCommonChars] and s_rem[-1] == '0':
            s_rem = doubleNumber(s_rem)
            cntOps += 1
            DEBUG and print(f"DOUB1 {s_rem_prev} -> {s_rem}; {cntOps}")
        elif len(s_rem) < len(e) and s_rem != '0' and len(e) >= 2 and e[nrCommonChars - 1] == e[nrCommonChars] and s_rem[-1] == '0':
            s_rem = doubleNumber(s_rem)
            cntOps += 1
            DEBUG and print(f"DOUB2 {s_rem_prev} -> {s_rem}; {cntOps}")
        elif len(s_rem) < len(e) and s_rem != '0' and len(s_rem) < len(e):
            s_rem = doubleNumber(s_rem)
            cntOps += 1
            DEBUG and print(f"DOUB3 {s_rem_prev} -> {s_rem}; {cntOps}")
        else:
            s_rem = negateNumber(s_rem)
            cntOps += 1
            DEBUG and print(f"NEG2 {s_rem_prev} -> {s_rem}; {cntOps}")

        if cntOps > 20:
            possible = False

    DEBUG and print(f"POSSIBLE? {possible} / {cntOps}")

    return possible, cntOps

# Read input
T = int(input())  # nr Testcases

S = [None] * T  # Start strings
E = [None] * T  # End strings

for i in range(T):
    S[i], E[i] = input().split(" ")

# Solve problem and output
for i in range(T):
    possible, nrOps = transformString(S[i], E[i])

    if possible:
        print("Case #{}: {}".format(i + 1, nrOps))
    else:
        print("Case #{}: IMPOSSIBLE".format(i + 1))
