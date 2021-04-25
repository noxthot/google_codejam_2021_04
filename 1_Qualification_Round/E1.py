import numpy as np

DEBUG = False

def reverseSort(arr, len):
    cost = 0

    for idx in range(len - 1):
        j = idx + np.argmin(arr[idx:])
        arr[idx:j+1] = np.flip(arr[idx:j+1])
        cost += (j + 1) - (idx + 1) + 1
        DEBUG and print(j, idx, cost, arr)

    return arr, cost


# Read input
T = int(input())  # nr Testcases

N = [None] * T  # list lengths
L = [None] * T  # lists

for i in range(T):
    N[i] = int(input())
    L[i] = np.array([int(s) for s in input().split(" ")])

# Solve problem and output
for i in range(T):
    _, cost = reverseSort(L[i], N[i])
    print("Case #{}: {}".format(i + 1, cost))