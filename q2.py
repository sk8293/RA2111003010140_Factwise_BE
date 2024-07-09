def maxScore(cardPoints, k):
    n = len(cardPoints)
    total_sum = sum(cardPoints)
    
   
    if k == n:
        return total_sum

    
    min_sum = float('inf')
    current_sum = 0
    left = 0

    for right in range(n):
        current_sum += cardPoints[right]
        
        
        if right >= n - k:
            min_sum = min(min_sum, current_sum)
            current_sum -= cardPoints[left]
            left += 1

    
    return total_sum - min_sum


print(maxScore([1,2,3,4,5,6,1], 3))  
print(maxScore([2,2,2], 2))           
print(maxScore([9,7,7,9,7,7,9], 7))  
