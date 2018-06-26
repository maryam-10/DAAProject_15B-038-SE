import math

class Print_Neatly(object):

    def print_neatly(self, words, n, M):
 # words = array of words
 # M = maximun length of the line
 # n = number of words
        minpenalty = [float('inf')]*(n+1)
        break_points = [None]*(n+1)

        minpenalty[0] = 0

        def compute_line_cost(extra_space, j, n):
#three cases are described
            if extra_space < 0:
                return float('inf')
            elif j == n and extra_space >= 0:
                return 0
            else:
                return extra_space**3

        for j in range(1, n+1):
            extra_space = M + 1
            for i in range(j, int(max(1, j + 1 - math.ceil(M/2)))-1, -1):
                extra_space = extra_space - len(words[i]) - 1
                cur_penalty = minpenalty[i-1] + compute_line_cost(extra_space, j, n)
                if minpenalty[j] > cur_penalty:
                    minpenalty[j] = cur_penalty
                    break_points[j] = i

        return minpenalty, break_points

    def print_neatly_non_optimized(self, words, n, M):

        extraspace = linecost = [[None for i in range(n+1)] for j in range(n+1)]
        minpenalty = [float('inf')]*(n+1)
        pointer_list = [None]*(n+1)

        minpenalty[0] = 0

  #computing extra spaces for the words
        for i in range(1, n+1):
            extraspace[i][i] = M - len(words[i])
            for j in range(i+1, n+1):

                extraspace[i][j] = extraspace[i][j-1] - len(words[j]) - 1

  #computing the line cost
        for i in range(1, n+1):
            for j in range(1, n+1):
                if extraspace[i][j] < 0:
                    linecost[i][j] = float('inf')
                elif j == n and extraspace[i][j] >= 0:
                    linecost[i][j] = 0
                else:
                    linecost[i][j] = (extraspace[i][j])**3

  #computing the minimum cost of each line
        for j in range(1, n+1):
            for i in range(1, j+1):
                cur_penalty = minpenalty[i-1] + linecost[i][j]
                if minpenalty[j] > cur_penalty:
                    minpenalty[j] = cur_penalty
                    pointer_list[j] = i

        return minpenalty, pointer_list

    def reconstruct_lines(self, text, j, break_points):
        i = break_points[j]
        line_num = 1
        if i != 1:
            line_num = self.reconstruct_lines(text, i-1, break_points) + 1
        print ' '.join(text[i:(j+1)])
        return line_num


if __name__ == '__main__':
    text = "Dynamic programming applies when the sub problems overlap that is, when sub problems share sub problems. In this context, a divide-and-conquer algorithm does more work than necessary, repeatedly solving the common sub problems. A dynamic-programming algorithm solves each sub problem just once and then saves its answer in a table, thereby avoiding the work of recomputing the answer every time it solves each sub problem. We typically apply dynamic programming to optimization problems. Such problems can have many possible solutions. Each solution has a value, and we wish to find a solution with the optimal (minimum or maximum) value. We call such a solution an optimal solution to the problem, as opposed to the optimal solution, since there may be several solutions that achieve the optimal value."
    tests = [text]
    print_neat = Print_Neatly()

    for test in tests:
        test = ['BLANK'] + test.split(' ')
        n = len(test)-1
        M = 40
        min_p, p_list = print_neat.print_neatly(test, n, M)
        min_p2, p_list2 = print_neat.print_neatly_non_optimized(test, n, M)
        print_neat.reconstruct_lines(test, n, p_list)
        print_neat.reconstruct_lines(test, n, p_list2)
        print min_p[-1], min_p2[-1]
