"""

Created by Avi.Kumar on 6/11/2018
Copyright : Aviral (Avi) Kumar

"""
from random import randint
from time import  time

class QuickSort():
    def __init__(self, array , start, end):
        # self.arr = array
        self.quicksort(array, start, end)
        print array

    def quicksort(self, array, start, end):

        if start < end:
            pivot = self.partition(array, start, end)
            self.quicksort(array, start, pivot - 1)
            self.quicksort(array, pivot + 1 , end)

    def partition(self, array, start, end):
        x = array[end]
        i = start - 1
        for j in range(start, end):
            if array[j] < x:
                i += 1
                array[i], array[j] = array[j], array[i]
            else: continue

        array[i+1], array[end] = array[end], array[i+1]

        return i+1

def main():
    size = 100000
    t1 = time()
    array = [randint(1, 100000000) for i in range(0,size)]
    arr = QuickSort(array, 0, size -1 )
    t2 = time()
    print "It took %s to sort the array!" %str(t2-t1)
if __name__ == "__main__":
    main()
