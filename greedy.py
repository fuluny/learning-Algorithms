# greedy algorithm, with change machine example.
# Assuming array provided is sorted
# either in descending or ascending order
# A = [1,5,10,25] cent, nickel, dime, quarter for example

# number to calculate and array to use to analyze
def greedy(n,A):
    # check if calculation can be possible or is required
    if (n<0):
        print("Can't take negative values")
        return -1
    elif (n==0):
        print("No change required")
        return 0
    # answer will be number of coins required for change
    # given elements in array A, answer corresponds to A's order
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
