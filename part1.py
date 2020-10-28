class Matrix:
    def __init__(self, list_1, list_2, out_list):
        self.matrix = [list_1, list_2]
        self.list_1 = list_1
        self.list_2 = list_2
        self.out_list = out_list

    def __add__(self):
        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                self.out_list[i][j] = self.list_1[i][j] + self.list_2[i][j]

    #               print(f"{self.out_list[i][j]} = {self.list_1[i][j]} + {self.list_2[i][j]}")

    def __str__(self):
        a = '[' + str('], ['.join([', '.join([str(j) for j in i]) for i in self.out_list])) + ']'
        return a


my_matrix = Matrix([[5, 18, 11],
                    [6, 17, 23],
                    [41, 50, 9]],
                   [[45, 8, 2],
                    [6, 7, 93],
                    [24, 5, 97]],
                   [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]])

my_matrix.__add__()
print(my_matrix.__str__())
