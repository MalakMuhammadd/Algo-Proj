def max_subarray_condition(A, L, R):
    if L > R:
        return float('-inf')
    if L == R:
        return A[L]
    mid = (L + R) // 2
    max1 = max_subarray_condition(A, L, mid)
    max2 = max_subarray_condition(A, mid + 1, R)
    sum1, sum2 = 0, 0
    max3, max4 = float('-inf'), float('-inf')
    for j in range(mid, L , -1):
        sum1 += A[j]
        if sum1 > max3:
            max3 = sum1
    
    for j in range(mid + 1 , R):
        sum2 += A[j]
        if sum2 > max4:
            max4 = sum2
    return max(max1, max2, max3 + max4)

# Example:
A = [3,-5,2,-1,5,-6,1,-2]
result = max_subarray_condition(A, 0, len(A)-1)
print(result)
