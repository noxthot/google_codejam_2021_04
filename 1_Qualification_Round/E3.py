import numpy as np
import random

DEBUG = False
DEBUG_WITH_E1 = False

def invReverseSort(n, c):
    #maxCost = sum(range(1, n + 1)) - 1
    seq = [None] * n

    leftIdx = 0
    rightIdx = n - 1
    currDirLeft = True

    for idx in range(1, n + 1):
        DEBUG and print(f"Finding a place for {idx}")

        nrToCome = n - idx
        currMaxCausedCost = nrToCome + 1

        DEBUG and print(f"We still need to fill {nrToCome} elements and traversing now would cause a cost of {currMaxCausedCost}. We still need to consume a cost of {c}")

        if idx < n:
            if (nrToCome - 1) + currMaxCausedCost <= c:
                currDirLeft = not currDirLeft
                c -= currMaxCausedCost
                DEBUG and print(f"Traversing makes sense. We change direction to {'left' if currDirLeft else 'right'} and the cost to consume reduces to {c}")
            else:
                c -= 1
                DEBUG and print(f"Stay at direction {'left' if currDirLeft else 'right'} and cost to consume reduces to {c}")

        if currDirLeft:
            seq[leftIdx] = idx
            leftIdx += 1
        else:
            seq[rightIdx] = idx
            rightIdx -= 1

    DEBUG and print(f"Current sequence: {seq}")

    possible = (c == 0)

    return possible, " ".join([str(s) for s in seq])


if DEBUG_WITH_E1:
    T = 5
    currT = 0
    print(T)

    while currT < T:
        n = random.randint(2, 100)
        c = random.randint(1, 1000)

        possible, seq = invReverseSort(n, c)

        if True: # possible:
            print(n, c)
            print(possible, seq)
            currT += 1
else:
    # Read input
    T = int(input())  # nr Testcases

    N = [None] * T  # list lengths
    C = [None] * T  # desired costs

    for i in range(T):
        N[i], C[i] = [int(s) for s in input().split(" ")]

    # Solve problem and output
    for i in range(T):
        possible, seq = invReverseSort(N[i], C[i])

        if possible:
            print("Case #{}: {}".format(i + 1, seq))
        else:
            print("Case #{}: IMPOSSIBLE".format(i + 1))