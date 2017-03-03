#this algorithm gets the median of two sorted arrays in O(lgn) time bitchesss


#where A and B are sorted arrays and n is the size of the arrays
def median(A, B, n):

#------------------------------------------#
    #declare the midpoint values for both arrays
    #n = n
    mid_a = A[len(A)//2]
    mid_b = B[len(B)//2]
    print("Mid value of A: {midValueA}, Mid value of B: {midValueB}".format(midValueA=mid_a, midValueB=mid_b))
    print("Array A: {}, Array B: {}, Size of Array: {}".format(A, B, n))


#------------------------------------------#
    #Once the arrays are at a length of 2. The max of the first postions and the min
    #of the second position divided by 2 will give us the median

    if(n == 2):
        max_0 = max(A[0], B[0])
        min_1 = min(A[1], B[1])
        return((min_1 + max_0) / 2)

#------------------------------------------#
    #Case 1 where both mids are the same
    elif(mid_a == mid_b):
        return mid_a


#------------------------------------------#
    #Case 2 where mid_a > mid_b.
    elif(mid_a > mid_b):
        pos_a = A.index(mid_a)
        pos_b = B.index(mid_b)
        print("position of mid_a: {}, position of mid_b: {}".format(pos_a,pos_b))
        print("A[:pos_a]: {}, B[pos_b:]: {}, n: {}".format(A[:pos_a+1], B[pos_b:], len(B[pos_b:])))
        return median(A[:pos_a+1], B[pos_b:], len(B[pos_b:]))


#------------------------------------------#
    #Case 3 where mid_b > mid_a.

    else:
        pos_a = A.index(mid_a)
        pos_b = B.index(mid_b)
        print("position of mid_a: {}, position of mid_b: {}".format(pos_a,pos_b))
        print("A[:pos_a]: {}, B[pos_b:]: {}, n: {}".format(A[pos_a:], B[:pos_b], len(A[pos_a:])))
        return median(A[pos_a:], B[:pos_b], len(B[pos_b:]))




A = [5, 10, 20, 30, 40]
B = [1, 2, 4, 5, 8]
if(len(A) == len(B)):
    n = len(A)

print("Sorted array A: {arrayA}, Sorted array B: {arrayB}".format(arrayA=A, arrayB=B))
median_number = median(A, B, n)
print("Median number for the combined array of A and B: {median}".format(median=median_number))
