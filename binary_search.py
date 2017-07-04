# array A and number n
def binary_search(A,n):
    m = n/2
    count = m
    # continue searching within range of array
    while (m>=0 and m<=n):
        # if number found return location and value
        if (n==A[m]):
            return True, m
        # search left half of the array
        elif (n<A[m]):
        # if counter reached zero, the number is not in array
            if ( count ==0):
                return False
            else:
                # if counter is greater than zero, 
                # decrease counter size by half
                # and search the left half of the array
                count/=2
                m-=count
        #  search right half of the array
        elif (n > A[m]):
            if (count==0):
                return False
            else:
                count/=2
                m+=count
    return False
