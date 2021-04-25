import sys
import numpy as np

DEBUG = False

def addblock(towers, block, B, N):
    sizes = [len(tower) for tower in towers]
    sizesset = set(sizes)

    DEBUG and print("sizesset: ", sizesset)

    if B in sizesset:
        sizesset.remove(B)

    DEBUG and print("sizesset without B: ", sizesset)

    sizesdict = {size: [] for size in sizesset}

    for idx, size in enumerate(sizes):
        if size in sizesset:
            sizesdict[size].append(idx)

    sizesunique = list(sizesset)
    sizesunique.sort()

    DEBUG and print("sizesunique: ", sizesunique)

    towerframewidth = (len(sizesunique) / 10)
    towerframestart = np.floor(block * towerframewidth)
    towerframeend = np.ceil(towerframestart + towerframewidth)

    towerframeIndicesNr = towerframewidth

    bestPick = int(towerframestart + max(min(np.round(towerframeIndicesNr * (block / 9)), towerframeIndicesNr), 1) - 1)

    consideredTowers = sizesdict[sizesunique[bestPick]]

    #for idx in range(int(towerframestart), int(towerframeend)):
    #    consideredTowers.extend(sizesdict[sizesunique[idx]])

    chooseTower = np.random.choice(consideredTowers)

    DEBUG and print("Appending ", block, " to tower ", chooseTower)

    towers[chooseTower].append(block)

    DEBUG and print("New tower ", chooseTower, ": ", towers[chooseTower])

    print(chooseTower + 1)
    sys.stdout.flush()


T, N, B, P = [int(x) for x in input().split(" ")]


for _ in range(T):
    towers = [[] for _ in range(N)]

    for _ in range(N * B):
        block = int(input())

        if block == -1:
            print("ERROR", towers)
            break

        addblock(towers, block, B, N)

    DEBUG and print("towers: ", towers)

_ = input()