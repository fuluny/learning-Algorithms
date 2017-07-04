# greedy algorithm, change machine example

# number to calculate and array to use to analyze
def greedy(n,A):
#   sort = O(nlogn)
#    A.sort()
#   reverse = O(n)
#    A.reverse()
    if (n<0):
        print("Can't take negative values")
        return -1
    elif (n==0):
        print("No change required")
        return 0
    counter = [0]*len(A)
    if A.index(max(A)) > A.index(min(A)):
        for i in range(len(A)-1,-1,-1):
    #    for i in range(len(A)):
            counter[i] = n/A[i]
            n %= A[i]
    else:
        for i in range(len(A)):
            counter[i]= n/A[i]
            n %= A[i]
    return counter
