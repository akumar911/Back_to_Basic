"""

Created by Avi.Kumar on 7/6/2018
Copyright : Aviral (Avi) Kumar

"""

import pandas as pd
import numpy as np

def print_matrix(w):
    '''
    Takes in the weighted graph as an input

    :param w:
    :return:
    '''

    print "The Input Graph looks like : \n"
    print w

    #Just showing how to print element by element. We can just do a print (df) as well.
    for i in range(0, len(w)):
        print "For vertex : %s" % str(i+1)
        for j in range(0, len(w)):
            print w.iloc[i][j]

def floyd(w):
    n = len(w)
    d = w
    p = pd.DataFrame(data = np.zeros(shape = (6,5))).reindex(range(1, n+1))
    p.columns = ['1','2','3','4','5']
    # Now let us populate a matrix that will have the highest index of an intermediate vertex on the shortest path
    # from Vi to Vj, if at least one intermediate vertex exists. 0, if no intermediate vertex exists.
    for k in range(0,n):
        for i in range(0,n):
            for j in range(0, n):
                if (d.iloc[i][k] + d.iloc[k][j] <d.iloc[i][j]):
                    p.iloc[i][j] = k+1
                    d.iloc[i][j] = d.iloc[i][k] + d.iloc[k][j]
    # d.iloc[i][j] = min(d.iloc[i][j], d.iloc[i][k] + d.iloc[k][j])
    print d
    print p




def get_input():
    '''
    Please hardcode the input here. THIS INPUT ONLY SHOWS A 5x5 MATRIX.
    The input is a dictionary with the weights taken in as a list.
    1000 shows that we have no path.

    :return: A dataframe with the Adjacency Matrix
    '''
    input = {1: [0,1,1000,1,5],
             2: [9,0,3,2,1000],
             3 : [1000,1000,0,4,1000],
             4:[1000,1000,2,0,3],
             5:[3,1000,1000,1000,0]
            }

    w = pd.DataFrame(index =input.keys(), data= input.values(), columns = ['1','2','3','4','5'])
    return w


if __name__ == "__main__":
    w = get_input()
    print_matrix(w)
    floyd(w)
