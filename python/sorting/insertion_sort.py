'''
Insertion sort:
    取第一个item，组成list，这个list是排好序的
    取下一个item，放入上面的list里，比较最后（也是最大）的item，如果大于它，则放在它的后面
    如果小于它，则和它交换位置，然后比较list里的前一个item，如果大于它，则这个list是排好序了
    继续这个过程。
    not a fast sorting algorithm
    uses nested loops to sort
    useful only for small data sets
    runs in O(n^2)
'''


def insertion_sort(A):
    for i in range(1, len(A)):
        for j in range(i-1, -1, -1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            else:
                break


def insertion_sort_shifting(A):
    for i in range(1, len(A)):
        # this is the one need to be put in the right place
        curNum = A[i]
        k = 0
        for j in range(i-1, -2, -1):
            k = j
            if A[j] > curNum:
                A[j+1] = A[j]
            else:                
                break
        A[k+1] = curNum