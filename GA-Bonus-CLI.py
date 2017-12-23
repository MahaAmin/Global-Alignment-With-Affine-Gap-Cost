import math
import sys

BLOSUM80 = {
    'A': {'A': 5, 'R': -2, 'N': -2, 'D': -2, 'C': -1, 'Q': -1, 'E': -1, 'G': 0, 'H': -2, 'I': -2, 'L': -2, 'K': -1,
          'M': -1, 'F': -3, 'P': -1, 'S': 1, 'T': 0, 'W': -3, 'Y': -2, 'V': 0, 'B': -2, 'J': -2, 'Z': -1, 'X': -1,
          '*': -6},
    'R': {'A': -2, 'R': 6, 'N': -1, 'D': -2, 'C': -4, 'Q': 1, 'E': -1, 'G': -3, 'H': 0, 'I': -3, 'L': -3, 'K': 2,
          'M': -2, 'F': -4, 'P': -2, 'S': -1, 'T': -1, 'W': -4, 'Y': -3, 'V': -3, 'B': -1, 'J': -3, 'Z': 0, 'X': -1,
          '*': -6},
    'N': {'A': -2, 'R': -1, 'N': 6, 'D': 1, 'C': -3, 'Q': 0, 'E': -1, 'G': -1, 'H': 0, 'I': -4, 'L': -4, 'K': 0,
          'M': -3, 'F': -4, 'P': -3, 'S': 0, 'T': 0, 'W': -4, 'Y': -3, 'V': -4, 'B': 5, 'J': -4, 'Z': 0, 'X': -1,
          '*': -6},
    'D': {'A': -2, 'R': -2, 'N': 1, 'D': 6, 'C': -4, 'Q': -1, 'E': 1, 'G': -2, 'H': -2, 'I': -4, 'L': -5, 'K': -1,
          'M': -4, 'F': -4, 'P': -2, 'S': -1, 'T': -1, 'W': -6, 'Y': -4, 'V': -4, 'B': 5, 'J': -5, 'Z': 1, 'X': -1,
          '*': -6},
    'C': {'A': -1, 'R': -4, 'N': -3, 'D': -4, 'C': 9, 'Q': -4, 'E': -5, 'G': -4, 'H': -4, 'I': -2, 'L': -2, 'K': -4,
          'M': -2, 'F': -3, 'P': -4, 'S': -2, 'T': -1, 'W': -3, 'Y': -3, 'V': -1, 'B': -4, 'J': -2, 'Z': -4, 'X': -1,
          '*': -6},
    'Q': {'A': -1, 'R': 1, 'N': 0, 'D': -1, 'C': -4, 'Q': 6, 'E': 2, 'G': -2, 'H': 1, 'I': -3, 'L': -3, 'K': 1, 'M': 0,
          'F': -4, 'P': -2, 'S': 0, 'T': -1, 'W': -3, 'Y': -2, 'V': -3, 'B': 0, 'J': -3, 'Z': 4, 'X': -1, '*': -6},
    'E': {'A': -1, 'R': -1, 'N': -1, 'D': 1, 'C': -5, 'Q': 2, 'E': 6, 'G': -3, 'H': 0, 'I': -4, 'L': -4, 'K': 1,
          'M': -2, 'F': -4, 'P': -2, 'S': 0, 'T': -1, 'W': -4, 'Y': -3, 'V': -3, 'B': 1, 'J': -4, 'Z': 5, 'X': -1,
          '*': -6},
    'G': {'A': 0, 'R': -3, 'N': -1, 'D': -2, 'C': -4, 'Q': -2, 'E': -3, 'G': 6, 'H': -3, 'I': -5, 'L': -4, 'K': -2,
          'M': -4, 'F': -4, 'P': -3, 'S': -1, 'T': -2, 'W': -4, 'Y': -4, 'V': -4, 'B': -1, 'J': -5, 'Z': -3, 'X': -1,
          '*': -6},
    'H': {'A': -2, 'R': 0, 'N': 0, 'D': -2, 'C': -4, 'Q': 1, 'E': 0, 'G': -3, 'H': 8, 'I': -4, 'L': -3, 'K': -1,
          'M': -2, 'F': -2, 'P': -3, 'S': -1, 'T': -2, 'W': -3, 'Y': 2, 'V': -4, 'B': -1, 'J': -4, 'Z': 0, 'X': -1,
          '*': -6},
    'I': {'A': -2, 'R': -3, 'N': -4, 'D': -4, 'C': -2, 'Q': -3, 'E': -4, 'G': -5, 'H': -4, 'I': 5, 'L': 1, 'K': -3,
          'M': 1, 'F': -1, 'P': -4, 'S': -3, 'T': -1, 'W': -3, 'Y': -2, 'V': 3, 'B': -4, 'J': 3, 'Z': -4, 'X': -1,
          '*': -6},
    'L': {'A': -2, 'R': -3, 'N': -4, 'D': -5, 'C': -2, 'Q': -3, 'E': -4, 'G': -4, 'H': -3, 'I': 1, 'L': 4, 'K': -3,
          'M': 2, 'F': 0, 'P': -3, 'S': -3, 'T': -2, 'W': -2, 'Y': -2, 'V': 1, 'B': -4, 'J': 3, 'Z': -3, 'X': -1,
          '*': -6},
    'K': {'A': -1, 'R': 2, 'N': 0, 'D': -1, 'C': -4, 'Q': 1, 'E': 1, 'G': -2, 'H': -1, 'I': -3, 'L': -3, 'K': 5,
          'M': -2, 'F': -4, 'P': -1, 'S': -1, 'T': -1, 'W': -4, 'Y': -3, 'V': -3, 'B': -1, 'J': -3, 'Z': 1, 'X': -1,
          '*': -6},
    'M': {'A': -1, 'R': -2, 'N': -3, 'D': -4, 'C': -2, 'Q': 0, 'E': -2, 'G': -4, 'H': -2, 'I': 1, 'L': 2, 'K': -2,
          'M': 6, 'F': 0, 'P': -3, 'S': -2, 'T': -1, 'W': -2, 'Y': -2, 'V': 1, 'B': -3, 'J': 2, 'Z': -1, 'X': -1,
          '*': -6},
    'F': {'A': -3, 'R': -4, 'N': -4, 'D': -4, 'C': -3, 'Q': -4, 'E': -4, 'G': -4, 'H': -2, 'I': -1, 'L': 0, 'K': -4,
          'M': 0, 'F': 6, 'P': -4, 'S': -3, 'T': -2, 'W': 0, 'Y': 3, 'V': -1, 'B': -4, 'J': 0, 'Z': -4, 'X': -1,
          '*': -6},
    'P': {'A': -1, 'R': -2, 'N': -3, 'D': -2, 'C': -4, 'Q': -2, 'E': -2, 'G': -3, 'H': -3, 'I': -4, 'L': -3, 'K': -1,
          'M': -3, 'F': -4, 'P': 8, 'S': -1, 'T': -2, 'W': -5, 'Y': -4, 'V': -3, 'B': -2, 'J': -4, 'Z': -2, 'X': -1,
          '*': -6},
    'S': {'A': 1, 'R': -1, 'N': 0, 'D': -1, 'C': -2, 'Q': 0, 'E': 0, 'G': -1, 'H': -1, 'I': -3, 'L': -3, 'K': -1,
          'M': -2, 'F': -3, 'P': -1, 'S': 5, 'T': 1, 'W': -4, 'Y': -2, 'V': -2, 'B': 0, 'J': -3, 'Z': 0, 'X': -1,
          '*': -6},
    'T': {'A': 0, 'R': -1, 'N': 0, 'D': -1, 'C': -1, 'Q': -1, 'E': -1, 'G': -2, 'H': -2, 'I': -1, 'L': -2, 'K': -1,
          'M': -1, 'F': -2, 'P': -2, 'S': 1, 'T': 5, 'W': -4, 'Y': -2, 'V': 0, 'B': -1, 'J': -1, 'Z': -1, 'X': -1,
          '*': -6},
    'W': {'A': -3, 'R': -4, 'N': -4, 'D': -6, 'C': -3, 'Q': -3, 'E': -4, 'G': -4, 'H': -3, 'I': -3, 'L': -2, 'K': -4,
          'M': -2, 'F': 0, 'P': -5, 'S': -4, 'T': -4, 'W': 11, 'Y': 2, 'V': -3, 'B': -5, 'J': -3, 'Z': -3, 'X': -1,
          '*': -6},
    'Y': {'A': -2, 'R': -3, 'N': -3, 'D': -4, 'C': -3, 'Q': -2, 'E': -3, 'G': -4, 'H': 2, 'I': -2, 'L': -2, 'K': -3,
          'M': -2, 'F': 3, 'P': -4, 'S': -2, 'T': -2, 'W': 2, 'Y': 7, 'V': -2, 'B': -3, 'J': -2, 'Z': -3, 'X': -1,
          '*': -6},
    'V': {'A': 0, 'R': -3, 'N': -4, 'D': -4, 'C': -1, 'Q': -3, 'E': -3, 'G': -4, 'H': -4, 'I': 3, 'L': 1, 'K': -3,
          'M': 1, 'F': -1, 'P': -3, 'S': -2, 'T': 0, 'W': -3, 'Y': -2, 'V': 4, 'B': -4, 'J': 2, 'Z': -3, 'X': -1,
          '*': -6},
    'B': {'A': -2, 'R': -1, 'N': 5, 'D': 5, 'C': -4, 'Q': 0, 'E': 1, 'G': -1, 'H': -1, 'I': -4, 'L': -4, 'K': -1,
          'M': -3, 'F': -4, 'P': -2, 'S': 0, 'T': -1, 'W': -5, 'Y': -3, 'V': -4, 'B': 5, 'J': -4, 'Z': 0, 'X': -1,
          '*': -6},
    'J': {'A': -2, 'R': -3, 'N': -4, 'D': -5, 'C': -2, 'Q': -3, 'E': -4, 'G': -5, 'H': -4, 'I': 3, 'L': 3, 'K': -3,
          'M': 2, 'F': 0, 'P': -4, 'S': -3, 'T': -1, 'W': -3, 'Y': -2, 'V': 2, 'B': -4, 'J': 3, 'Z': -3, 'X': -1,
          '*': -6},
    'Z': {'A': -1, 'R': 0, 'N': 0, 'D': 1, 'C': -4, 'Q': 4, 'E': 5, 'G': -3, 'H': 0, 'I': -4, 'L': -3, 'K': 1, 'M': -1,
          'F': -4, 'P': -2, 'S': 0, 'T': -1, 'W': -3, 'Y': -3, 'V': -3, 'B': 0, 'J': -3, 'Z': 5, 'X': -1, '*': -6},
    'X': {'A': -1, 'R': -1, 'N': -1, 'D': -1, 'C': -1, 'Q': -1, 'E': -1, 'G': -1, 'H': -1, 'I': -1, 'L': -1, 'K': -1,
          'M': -1, 'F': -1, 'P': -1, 'S': -1, 'T': -1, 'W': -1, 'Y': -1, 'V': -1, 'B': -1, 'J': -1, 'Z': -1, 'X': -1,
          '*': -6},
    '*': {'A': -6, 'R': -6, 'N': -6, 'D': -6, 'C': -6, 'Q': -6, 'E': -6, 'G': -6, 'H': -6, 'I': -6, 'L': -6, 'K': -6,
          'M': -6, 'F': -6, 'P': -6, 'S': -6, 'T': -6, 'W': -6, 'Y': -6, 'V': -6, 'B': -6, 'J': -6, 'Z': -6, 'X': -6,
          '*': 1},
}


def initializeMatchMatrix(matrix, row, col):
    matrix[0][0] = 0
    for i in range(1, row):
        matrix_match[i][0] = - math.inf
    for j in range(1, col):
        matrix_match[0][j] = - math.inf


def initializeStringMatrix(matrix, row, col, open_penalty, extend_penalty, director):
    if director == "IX":
        for i in range(row):
            matrix[i][0] = open_penalty + (extend_penalty * i)
        for j in range(1, col):
            matrix[0][j] = - math.inf
    elif director == "IY":
        for j in range(col):
            matrix[0][j] = open_penalty + (extend_penalty * j)
        for i in range(1, row):
            matrix[i][0] = - math.inf


def fillingMatrixDNA(match_matrix, IX_matrix, IY_matrix, open_penalty, extend_penalty, s1, s2, row, col):
    for i in range(1, row):
        for j in range(1, col):
            if s1[j - 1] == s2[i - 1]:
                score = 2
            else:
                score = -1
            match_matrix[i][j] = max(match_matrix[i - 1][j - 1] + score, IX_matrix[i - 1][j - 1] + score,
                                     IY_matrix[i - 1][j - 1] + score)
            IX_matrix[i][j] = max(match_matrix[i - 1][j] + open_penalty + extend_penalty,
                                  IX_matrix[i - 1][j] + extend_penalty)
            IY_matrix[i][j] = max(match_matrix[i][j - 1] + open_penalty + extend_penalty,
                                  IY_matrix[i][j - 1] + extend_penalty)


def fillingMatrixProtein(match_matrix, IX_matrix, IY_matrix, open_penalty, extend_penalty, s1, s2, row, col):
    for i in range(1, row):
        for j in range(1, col):
            match_matrix[i][j] = max(match_matrix[i - 1][j - 1] + BLOSUM80[s1[j - 1]][s2[i - 1]],
                                     IX_matrix[i - 1][j - 1] + BLOSUM80[s1[j - 1]][s2[i - 1]],
                                     IY_matrix[i - 1][j - 1] + BLOSUM80[s1[j - 1]][s2[i - 1]])
            IX_matrix[i][j] = max(match_matrix[i - 1][j] + open_penalty + extend_penalty,
                                  IX_matrix[i - 1][j] + extend_penalty)
            IY_matrix[i][j] = max(match_matrix[i][j - 1] + open_penalty + extend_penalty,
                                  IY_matrix[i][j - 1] + extend_penalty)


def traceback(match_matrix, IX_matrix, IY_matrix, open_penalty, extend_penalty, s1, s2, row, col, material):
    GAFirst = ""
    GASecond = ""
    GAMatch = ""
    i = row - 1
    j = col - 1
    if match_matrix[i][j] > IX_matrix[i][j] and match_matrix[i][j] > IY_matrix[i][j]:
        current_matrix = 'm'
        optimalScore = match_matrix[i][j]
        print("Optimal Score = " + str(optimalScore))

    elif IX_matrix[i][j] > match_matrix[i][j] and IX_matrix[i][j] > IY_matrix[i][j]:
        current_matrix = 'x'
        optimalScore = IX_matrix[i][j]
        print("Optimal Score = " + str(optimalScore))

    else:
        current_matrix = 'y'
        optimalScore = IY_matrix[i][j]
        print("Optimal Score = " + str(optimalScore))

    while i > 0 or j > 0:
        if current_matrix == 'm':

            GAFirst += s1[j - 1]
            GASecond += s2[i - 1]
            if s1[j - 1] == s2[i - 1]:
                GAMatch += "|"
            else:
                GAMatch += " "

            if s2[i - 1] == s1[j - 1]:
                if material == 'd':
                    penalty = 2
                elif material == 'p':
                    penalty = BLOSUM80[s1[j - 1]][s2[i - 1]]
            else:
                if material == 'd':
                    penalty = -1
                elif material == 'p':
                    penalty = BLOSUM80[s1[j - 1]][s2[i - 1]]

            if match_matrix[i - 1][j - 1] + penalty == match_matrix[i][j]:
                i -= 1
                j -= 1
                current_matrix = 'm'
            elif IX_matrix[i - 1][j - 1] + penalty == match_matrix[i][j]:
                i -= 1
                j -= 1
                current_matrix = 'x'
            elif IY_matrix[i - 1][j - 1] + penalty == match_matrix[i][j]:
                i -= 1
                j -= 1
                current_matrix = 'y'

        elif current_matrix == 'x':
            GAFirst += "-"
            GASecond += s2[i - 1]
            GAMatch += " "

            if IX_matrix[i - 1][j] + extend_penalty == IX_matrix[i][j]:
                i -= 1
                current_matrix = 'x'
            elif match_matrix[i - 1][j] + open_penalty + extend_penalty == IX_matrix[i][j]:
                i -= 1
                current_matrix = 'm'

        elif current_matrix == 'y':
            GAFirst += s1[j - 1]
            GASecond += "-"
            GAMatch += " "

            if IY_matrix[i][j - 1] + extend_penalty == IY_matrix[i][j]:
                j -= 1
                current_matrix = 'y'
            elif match_matrix[i][j - 1] + open_penalty + extend_penalty == IY_matrix[i][j]:
                j -= 1
                current_matrix = 'm'
    GAFirst = GAFirst[::-1]
    GAMatch = GAMatch[::-1]
    GASecond = GASecond[::-1]

    print("Optimal Alignment:")
    print(GAFirst)
    print(GAMatch)
    print(GASecond)

    # =============================================

    GAFirst1 = ""
    GASecond1 = ""
    GAMatch1 = ""
    i = row - 1
    j = col - 1

    if IX_matrix[i][j] > match_matrix[i][j] and IX_matrix[i][j] > IY_matrix[i][j]:
        current_matrix = 'x'
        optimalScore = IX_matrix[i][j]
        # print("Optimal Score = " + str(optimalScore))

    elif match_matrix[i][j] > IX_matrix[i][j] and match_matrix[i][j] > IY_matrix[i][j]:
        current_matrix = 'm'
        optimalScore = match_matrix[i][j]
        # print("Optimal Score = " + str(optimalScore))

    else:
        current_matrix = 'y'
        optimalScore = IY_matrix[i][j]
        # print("Optimal Score = " + str(optimalScore))

    while i > 0 or j > 0:
        if current_matrix == 'm':

            GAFirst1 += s1[j - 1]
            GASecond1 += s2[i - 1]
            if s1[j - 1] == s2[i - 1]:
                GAMatch1 += "|"
            else:
                GAMatch1 += " "

            if s2[i - 1] == s1[j - 1]:
                if material == 'd':
                    penalty = 2
                elif material == 'p':
                    penalty = BLOSUM80[s1[j - 1]][s2[i - 1]]
            else:
                if material == 'd':
                    penalty = -1
                elif material == 'p':
                    penalty = BLOSUM80[s1[j - 1]][s2[i - 1]]

            if IX_matrix[i - 1][j - 1] + penalty == match_matrix[i][j]:
                i -= 1
                j -= 1
                current_matrix = 'x'

            elif match_matrix[i - 1][j - 1] + penalty == match_matrix[i][j]:
                i -= 1
                j -= 1
                current_matrix = 'm'

            elif IY_matrix[i - 1][j - 1] + penalty == match_matrix[i][j]:
                i -= 1
                j -= 1
                current_matrix = 'y'

        elif current_matrix == 'x':
            GAFirst1 += "-"
            GASecond1 += s2[i - 1]
            GAMatch1 += " "

            if match_matrix[i - 1][j] + open_penalty + extend_penalty == IX_matrix[i][j]:
                i -= 1
                current_matrix = 'm'

            elif IX_matrix[i - 1][j] + extend_penalty == IX_matrix[i][j]:
                i -= 1
                current_matrix = 'x'


        elif current_matrix == 'y':
            GAFirst1 += s1[j - 1]
            GASecond1 += "-"
            GAMatch1 += " "

            if match_matrix[i][j - 1] + open_penalty + extend_penalty == IY_matrix[i][j]:
                j -= 1
                current_matrix = 'm'

            elif IY_matrix[i][j - 1] + extend_penalty == IY_matrix[i][j]:
                j -= 1
                current_matrix = 'y'

    GAFirst1 = GAFirst1[::-1]
    GAMatch1 = GAMatch1[::-1]
    GASecond1 = GASecond1[::-1]

    # print("Optimal Alignment:")
    # print(GAFirst1)
    # print(GAMatch1)
    # print(GASecond1)
    # ---------------------------------------------------------------
    GAFirst2 = ""
    GASecond2 = ""
    GAMatch2 = ""
    i = row - 1
    j = col - 1

    if IY_matrix[i][j] > match_matrix[i][j] and IY_matrix[i][j] > IX_matrix[i][j]:
        current_matrix = 'y'
        optimalScore = IY_matrix[i][j]
        # print("Optimal Score = " + str(optimalScore))

    elif IX_matrix[i][j] > match_matrix[i][j] and IX_matrix[i][j] > IY_matrix[i][j]:
        current_matrix = 'x'
        optimalScore = IX_matrix[i][j]
        # print("Optimal Score = " + str(optimalScore))

    elif match_matrix[i][j] > IX_matrix[i][j] and match_matrix[i][j] > IY_matrix[i][j]:
        current_matrix = 'm'
        optimalScore = match_matrix[i][j]
        # print("Optimal Score = " + str(optimalScore))

    while i > 0 or j > 0:
        if current_matrix == 'm':

            GAFirst2 += s1[j - 1]
            GASecond2 += s2[i - 1]
            if s1[j - 1] == s2[i - 1]:
                GAMatch2 += "|"
            else:
                GAMatch2 += " "

            if s2[i - 1] == s1[j - 1]:
                if material == 'd':
                    penalty = 2
                elif material == 'p':
                    penalty = BLOSUM80[s1[j - 1]][s2[i - 1]]
            else:
                if material == 'd':
                    penalty = -1
                elif material == 'p':
                    penalty = BLOSUM80[s1[j - 1]][s2[i - 1]]

            if IY_matrix[i - 1][j - 1] + penalty == match_matrix[i][j]:
                i -= 1
                j -= 1
                current_matrix = 'y'

            elif IX_matrix[i - 1][j - 1] + penalty == match_matrix[i][j]:
                i -= 1
                j -= 1
                current_matrix = 'x'

            elif match_matrix[i - 1][j - 1] + penalty == match_matrix[i][j]:
                i -= 1
                j -= 1
                current_matrix = 'm'



        elif current_matrix == 'x':
            GAFirst2 += "-"
            GASecond2 += s2[i - 1]
            GAMatch2 += " "

            if IX_matrix[i - 1][j] + extend_penalty == IX_matrix[i][j]:
                i -= 1
                current_matrix = 'x'

            elif match_matrix[i - 1][j] + open_penalty + extend_penalty == IX_matrix[i][j]:
                i -= 1
                current_matrix = 'm'




        elif current_matrix == 'y':
            GAFirst2 += s1[j - 1]
            GASecond2 += "-"
            GAMatch2 += " "

            if IY_matrix[i][j - 1] + extend_penalty == IY_matrix[i][j]:
                j -= 1
                current_matrix = 'y'

            elif match_matrix[i][j - 1] + open_penalty + extend_penalty == IY_matrix[i][j]:
                j -= 1
                current_matrix = 'm'

    GAFirst2 = GAFirst2[::-1]
    GAMatch2 = GAMatch2[::-1]
    GASecond2 = GASecond2[::-1]

    # print("Optimal Alignment:")
    # print(GAFirst2)
    # print(GAMatch2)
    # print(GASecond2)
    file = open("OUTPUT", "w")
    file.write("Optimal Score = " + str(optimalScore) + "\n")
    file.write("Optimal Alignment: " + "\n")
    file.write(GAFirst + "\n")
    file.write(GAMatch + "\n")
    file.write(GASecond + "\n")

    if GAFirst != GAFirst1 or GASecond != GASecond1:
        print("Optimal Alignment:")
        print(GAFirst1)
        print(GAMatch1)
        print(GASecond1)
        file.write("Optimal Alignment: " + "\n")
        file.write(GAFirst1 + "\n")
        file.write(GAMatch1 + "\n")
        file.write(GASecond1 + "\n")
        file.close()

    if (GAFirst != GAFirst2 and GAFirst1 != GAFirst2) or (GASecond != GASecond2 and GASecond1 != GASecond2):
        print("Optimal Alignment:")
        print(GAFirst2)
        print(GAMatch2)
        print(GASecond2)

        file.write(GAFirst2 + "\n")
        file.write(GAMatch2 + "\n")
        file.write(GASecond2 + "\n")
    file.close()


# --------------------------------------------------------------------------
print("----------------------Global Alignment With Affine Gap Cost----------------------")
sys.stdout.write("Choose type of sequence Protein/DNA (p/d): ")
material = input()
print("Enter 1st sequence: ")
str1 = input()

print("Enter 2nd sequence: ")
str2 = input()

print("Enter Open-Gap penalty: ")
open_gap_penalty = int(input())

print("Enter Extend-Gap penalty: ")
extend_gap_penalty = int(input())

# rows --> str2 ex:AAT
# cols --> str1 ex:ACACT

row = len(str2) + 1
col = len(str1) + 1

matrix_match = [[0 for x in range(col)] for y in range(row)]
IX_matrix = [[0 for x in range(col)] for y in range(row)]
IY_matrix = [[0 for x in range(col)] for y in range(row)]

initializeMatchMatrix(matrix_match, row, col)
initializeStringMatrix(IX_matrix, row, col, open_gap_penalty, extend_gap_penalty, "IX")
initializeStringMatrix(IY_matrix, row, col, open_gap_penalty, extend_gap_penalty, "IY")

if material == 'p':
    fillingMatrixProtein(matrix_match, IX_matrix, IY_matrix, open_gap_penalty, extend_gap_penalty, str1, str2, row, col)
elif material == 'd':
    fillingMatrixDNA(matrix_match, IX_matrix, IY_matrix, open_gap_penalty, extend_gap_penalty, str1, str2, row, col)

traceback(matrix_match, IX_matrix, IY_matrix, open_gap_penalty, extend_gap_penalty, str1, str2, row, col, material)