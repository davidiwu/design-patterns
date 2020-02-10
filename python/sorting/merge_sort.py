'''
Merge sort:
    is recursive, method that calls itself
    divide and conquer alogrithm
    very efficient for large data sets
    runs in O(nlogn)
    log(n) merge steps because each merge step doubles the list size
    n work for each merge step because it must look at every item
'''


def _split(arr):
    arr_length = len(arr)
    idx = arr_length // 2
    return arr[0:idx], arr[idx:arr_length]

def _merge(arr1, arr2):
    idx1=0
    idx2=0
    ret=[]
    for _ in range(len(arr1) + len(arr2)):
        if idx2>=len(arr2) or (idx1 <len(arr1) and arr1[idx1] < arr2[idx2]):
            ret.append(arr1[idx1])
            idx1=idx1+1
        else:
            ret.append(arr2[idx2])
            idx2=idx2+1

    return ret

def merge_sort(arr):

    if len(arr) < 2:
        return arr
    
    left, right = _split(arr)
    merged_left = merge_sort(left)
    merged_right = merge_sort(right)

    merged = _merge(merged_left, merged_right)

    return merged

if __name__ == '__main__':

    a = [1,3,9,12,16]
    b = [3,11,17]
    c = [9,13,22,56]

    print(_merge(a, b))
    print(_merge(b, c))

    d = [34,1,3,67,11,5,9,23,21,17,4,90,43]
    print(merge_sort(d))
