# counting sort O(logn)
# usu. don't use this unless less than 10^9
# use python's sort() O(nlogn)

def counting_sort(A):
    A_count=[0]*(max(A)+1)
    A_sorted=[0]*len(A)
    count = 0
    # bin numbers
    for i in range(len(A)):
        A_count[A[i]]+=1
    # translate counts to ordered array
    for i in range(len(A_count)):
        for j in range(A_count[i]):
            A_sorted[count]=i
            count+=1
    return A_sorted
