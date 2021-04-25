import numpy as np

DEBUG = False

def whoCheats(cs):
    def sigm(skill, difficulty):
        return 1 / (1 + np.exp(-(skill - difficulty)))

    def rightAnswerRatioSim(difficulty, participants):
        return np.sum(np.round(sigm(participants, difficulty))) / np.size(participants)

    def rightAnswerRatio(answers):
        return np.sum(answers) / np.size(answers)

    def findDifficulty(realAnswers, simulatedAnswerRatios, difficulties):
        idxDiff = np.argmin(np.abs(rightAnswerRatio(realAnswers) - simulatedAnswerRatios))

        return difficulties[idxDiff]

    difficulties = np.linspace(-3, 3, 1000)
    simParticipants = np.random.uniform(-3, 3, 5000)

    simulatedAnswerRatios = np.array([rightAnswerRatioSim(d, simParticipants) for d in difficulties])
    caseDifficulties = np.array([findDifficulty(cs[:, i], simulatedAnswerRatios, difficulties) for i in range(cs.shape[1])])

    costPart = np.array([np.sum(np.abs(((caseDifficulties / 6) + 0.5) - cs[i, :].T)) for i in range(cs.shape[0])])

    cheater = np.argmax(costPart)

    print(costPart)
    print(costPart[cheater])

    return cheater + 1


# Read input
T = int(input())  # nr Testcases
P = int(input()) # percentage that should be answered correctly

C = [None] * T  # Cases (100 lines each)

for i in range(T):
    C[i] = []

    for _ in range(100):
        C[i].append([int(char) for char in input()])

    C[i] = np.array(C[i])

# Solve problem and output
for i in range(T):
    cheater = whoCheats(C[i])
    print("Case #{}: {}".format(i + 1, cheater))